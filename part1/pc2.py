keystr = "11111111111100011000111001011000111111110001111111101001"

keymatrix = []

for e in keystr:
	if e == '0':
		keymatrix.append(0)
	elif e == '1':
		keymatrix.append(1)

print(len(keymatrix))

pc1p1 = [14, 17, 11, 24, 1, 5, 3, 28, 
15, 6, 21, 10, 23, 19, 12, 4, 
26, 8, 16, 7, 27, 20, 13, 2, 
41, 52, 31, 37, 47, 55, 30, 40, 
51, 45, 33, 48, 44, 49, 39, 56, 
34, 53, 46, 42, 50, 36, 29, 32]

pc1 = []
for e in pc1p1:
	pc1.append(e-1)

print(len(pc1))
pc1edk = []

for i in range(0, 48):
	pc1edk.append(keymatrix[pc1[i]])

print(len(pc1edk))

outstr = ""
for i in range(0, 6):
	for e in pc1edk[8*i: 8*i+8]:
		if e == 0:
			outstr += '0'
		else:
			outstr += '1'
	outstr +='\n'

print(outstr)
