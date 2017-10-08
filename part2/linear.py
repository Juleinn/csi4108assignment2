# CSI4108 - Assignment #2
# Anton Claes, 2017
# file linear.py
# implements the simplified example of linear cryptanalysis
# given by Heys at : https://www.engr.mun.ca/~howard/PAPERS/ldc_tutorial.pdf
import random

# mapping for all s-boxes
# contains list of outputs in input order
sbox = [0x0e, 0x04, 0x0d, 0x01, 0x02, 0x0f, 0x0b, 0x08, 0x03, 0x0a, 0x06, 0x0c, 0x05, 0x09, 0x00, 0x07]

# permutation list
perm = [e - 1 for e in [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]]

# sbox run backwards
isbox = []
for i in range(len(sbox)):
	isbox.append(sbox.index(i))

#generates a random key of size 16
def genRndKey():
	return bitStringTobitList(bin(random.randint(0, 2**16 - 1))[2:].rjust(16, '0'))

# enter perform substituton through given sbox
def substitute(bitlist, mapping):
	# convert bitlist to int, substitute and convert back
	value = int(reduce(lambda a, b: str(a)+""+str(b), bitlist), 2)
	value = mapping[value]
	value = bin(value)[2:].rjust(4, "0")
	return bitStringTobitList(value)

# permute bits
def permute(bitlist, mapping):
	return [bitlist[mapping[e]] for e in range(len(bitlist))]

#converts a bitstring into a bitlist
def bitStringTobitList(value):
	res = []
	for e in value:
		if e == '0':
			res.append(0)
		else:
			res.append(1)
	return res


# bitwise XoR, bitlist1&2 must have same length
def bitwiseXor(bitlist1, bitlist2):
	return [(bitlist1[e] + bitlist2[e]) % 2 for e in range(len(bitlist1))]	

#cipher the given plaintext (as a list of bits)
def generateCipherText(plaintextBitList):
	U = [e for e in plaintextBitList]
	for i in range(3):	# 3 first rounds
		V = [0 for e in range(len(plaintextBitList))]
		# xor with key for round
		V = bitwiseXor(U, keys[i])
		# substitute (all s-box the same)
		U[0:4] = substitute(V[0:4], sbox)
		U[4:8] = substitute(V[4:8], sbox)
		U[8:12] = substitute(V[8:12], sbox)
		U[12:16] = substitute(V[12:16], sbox)
		# permute
		U = permute(U, perm)

	# round 3 (4th round) no permutation
	V = bitwiseXor(U, keys[3]) 
	# substitute (all s-box the same)
	U[0:4] = substitute(V[0:4], sbox)
	U[4:8] = substitute(V[4:8], sbox)
	U[8:12] = substitute(V[8:12], sbox)
	U[12:16] = substitute(V[12:16], sbox)

	# at the end, XoR with K5
	return bitwiseXor(U, keys[4])

# generate 5 randoms keys 
keys = []
for i in range(5):
	keys.append(genRndKey())

# set the appropriate bits of key five to [7 D] = [0111 1101]
keys[4][4:8] = [0, 1, 1, 1]  	# 0x7
keys[4][12:16] = [1, 1, 0, 1]	# 0xD

#avoid using same plaintext twice
usedPlainText =[]

# deep copy key
k5 = [e for e in keys[4]]

pairs = []

samples = 25000
for i in range(samples):
	# generate a random number in plaintext space (2^16)
	ptStr =  bin(random.randint(0, 2**16 - 1))[2:].rjust(16, '0')
	while ptStr in usedPlainText:
		ptStr = bin(random.randint(0, 2**16 - 1))[2:].rjust(16, '0')
	usedPlainText.append(ptStr)
	plaintext = bitStringTobitList(ptStr)

	# plaintext = bitStringTobitList(bin(i)[2:].rjust(16))
	ciphertext = generateCipherText(plaintext)
	pairs.append((plaintext, ciphertext))

print("Generated pairs. Attacking")

# test for all keys in the given range 
# to make a table like table 5
for key_mod in range(0x6c, 0x87):
	count = 0
	# change keybits accordingly
	k5[4:8] = bitStringTobitList(bin(key_mod)[2:].rjust(8, '0')[0:4])
	k5[12:16] = bitStringTobitList(bin(key_mod)[2:].rjust(8, '0')[4:8])

	# test for the generated keypair if it suits the 
	# probabilities computed for 
	for i in range(len(pairs)):
		# now for the attack
		# take the ciphertext, XoR it with k5
		cipherXoR = bitwiseXor(pairs[i][1], k5)
		# reverse S-box it
		U4 = [0 for e in range(16)]
		U4[0:4] = substitute(cipherXoR[0:4], isbox)
		U4[4:8] = substitute(cipherXoR[4:8], isbox)
		U4[8:12] = substitute(cipherXoR[8:12], isbox)
		U4[12:16] = substitute(cipherXoR[12:16], isbox)

		# check if equation holds true
		if (U4[5] + U4[7] + U4[13] + U4[15] + pairs[i][0][4] + 
			pairs[i][0][6] + pairs[i][0][7]) % 2 == 0:
			count += 1

	biasMagnitude = float(abs(count - (len(pairs)/2))) / float(len(pairs))
	print(hex(key_mod) + " : " + str(biasMagnitude))

