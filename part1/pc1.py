keystr = "10101010 10101011 10111011 11001100 11001101 11011101 11101110 11101111"

keymatrix = []

for e in keystr:
	if e == '0':
		keymatrix.append(0)
	elif e == '1':
		keymatrix.append(1)

print(len(keymatrix))

pc1p1 = [57, 49, 41, 33, 25, 17, 9, 
		1, 58, 50, 42, 34, 26, 18,
		10, 2, 59, 51, 43, 35, 27,
		19, 11, 3, 60, 52, 44, 36,
		63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
		14, 6, 61, 53, 45, 37, 29,
		21, 13, 5, 28, 20, 12, 4]

pc1 = []
for e in pc1p1:
	pc1.append(e-1)

print(len(pc1))
pc1edk = []

for i in range(0, 56):
	pc1edk.append(keymatrix[pc1[i]])

outstr = ""
for i in range(0, 8):
	for e in pc1edk[7*i: 7*i+7]:
		if e == 0:
			outstr += '0'
		else:
			outstr += '1'
	outstr +='\n'

print(outstr)
