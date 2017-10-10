# CSI4108 - Assignment #2
# Anton Claes, 2017
# file perm.py
# script that allows permutation of bits in a list of bits
# for semi-automation of DES execution for one round
plaintext = "11100110111001111010100101110010"

keymatrix = []

for e in plaintext:
	if e == '0':
		keymatrix.append(0)
	elif e == '1':
		keymatrix.append(1)

print(len(keymatrix))

pc1p1 = [16, 7, 20, 21, 29, 12, 28, 17,
1, 15, 23, 26, 5, 18, 31, 10,
2, 8, 24, 14, 32, 27, 3, 9,
19, 13, 30, 6, 22, 11, 4, 25]

pc1 = []
for e in pc1p1:
	pc1.append(e-1)

print(len(pc1))
pc1edk = []

for i in range(0, 32):
	pc1edk.append(keymatrix[pc1[i]])

outstr = ""
for i in range(0, 8):
	for e in pc1edk[8*i: 8*i+8]:
		if e == 0:
			outstr += '0'
		else:
			outstr += '1'
	outstr +='\n'

print(outstr)
