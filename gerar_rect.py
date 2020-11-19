import cv2, numpy as np, sys, math
from matplotlib import pyplot as plt
import random

kwargs = dict(arg.split('=') for arg in sys.argv[2:])

#o tamanho padrao e 1024x768
img = np.zeros((768, 1024)).astype(np.uint8)
H, W = img.shape

#se vai utilizar um tamanho fixo
fixedSize = 'size' in kwargs
#se vai utilizar um angulo fixo
fixedTheta = 'angle' in kwargs
#se vai utilizar um numero de quadrados fixo
fixedNumber = 'number' in kwargs

if fixedNumber:
	n = int(kwargs['number'])
else:
	n = random.randint(3, 100)

print(n)
for k in range(n):
	if fixedSize:
		size = int(kwargs['size'])
	else:
		size = random.randint(4, 30)
	#hd: metade da diagonal
	hd = math.sqrt(2)*size/2
	if fixedTheta:
		angle = float(kwargs['angle'])
	else:
		angle = random.random()*math.pi/2
	theta = angle + math.pi/4
	y = random.randint(int(size), H-1-int(size))
	x = random.randint(int(size), W-1-int(size))
	print(str(x) + ' ' + str(y) + ' ' + str(size) + ' ' + str(angle))
	pts = []
	for i in range(4):
		pts.append((x+hd*math.cos(theta+i*math.pi/2), y-hd*math.sin(theta+i*math.pi/2)))
	cv2.fillPoly(img, np.int32([pts]), 255)

cv2.imshow('janela', img.astype(np.uint8))
cv2.imwrite(sys.argv[1], img)
cv2.waitKey(0)
