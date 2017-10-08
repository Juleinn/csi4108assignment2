r0 = "11111111110001111111111111000111"

keymatrix = []

for e in r0:
	if e == '0':
		keymatrix.append(0)
	elif e == '1':
		keymatrix.append(1)

print(len(keymatrix))

pc1p1 = [32, 1, 2, 3, 4, 5,
4, 5, 6, 7, 8, 9,
8, 9, 10, 11, 12, 13,
12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21,
20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29,
28, 29, 30, 31, 32, 1]

pc1 = []
for e in pc1p1:
	pc1.append(e-1)

print(len(pc1))
pc1edk = []

for i in range(0, 48):
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
