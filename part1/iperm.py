plaintext = "1 0010 1111 1111 0111 0100 1111 0010 0010 1111111 11000111 11111111 11000111"

keymatrix = []

for e in plaintext:
	if e == '0':
		keymatrix.append(0)
	elif e == '1':
		keymatrix.append(1)

print(len(keymatrix))

pc1p1 = [40, 8, 48, 16, 56, 24, 64, 32, 
39, 7, 47, 15, 55, 23, 63, 31, 
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25]

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
