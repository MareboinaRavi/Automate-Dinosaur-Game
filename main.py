import pyautogui
from PIL import Image,ImageGrab
import time
# import numpy

# def ts():
# 	img = ImageGrab.grab().convert('L')
# 	return img 
  
def hit(key):
 	pyautogui.keyDown(key)
 
def isCollide(data):
	for i in range(210, 280):
		for j in range(410, 480):
			if data[i, j] < 100:
				hit("up")
				return 

	for i in range(170, 206):
		for j in range(350, 408):
			if data[i, j] < 0:
				hit("down")
				return 
	return 


print("executing program in 3 sec....")
time.sleep(2)
# hit('up')
# image = ts()
while True:
	image = ImageGrab.grab().convert('L')
	data = image.load()
	isCollide(data)
	     # hit("up")
	# else:
	# 	hit("down")
	# print(numpy.asarray(image))
	# draw() 
	# for i in range(230, 415):
	# 	for j in range(430, 500):
	# 		data[i,j]=0
	# image.show()