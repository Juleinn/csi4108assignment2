plaintext = "1010101010101011101110111100110011001101110111011110111011101111"

keymatrix = []

for e in plaintext:
	if e == '0':
		keymatrix.append(0)
	elif e == '1':
		keymatrix.append(1)

print(len(keymatrix))

pc1p1 = [58, 50, 42, 34, 26, 18, 10, 2, 
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8, 
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7]

pc1 = []
for e in pc1p1:
	pc1.append(e-1)

print(len(pc1))
pc1edk = []

for i in range(0, 64):
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
