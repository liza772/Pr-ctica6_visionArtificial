#Yasmin Esqueda Muñoz
#Práctica 6

from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils
import numpy as np


fila = 2
columna = 4
fig = plt.figure(figsize=(10,7), constrained_layout=True)
img1 = cv2.imread('challenger.jpg', 1)
img1hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(img1hsv, low_red, high_red)
red = cv2.bitwise_and(img1hsv,img1hsv, mask=red_mask)
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(img1hsv, low_blue, high_blue)
blue = cv2.bitwise_and(img1hsv, img1hsv, mask=blue_mask)
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
green_mask = cv2.inRange(img1hsv, low_green, high_green)
green = cv2.bitwise_and(img1hsv, img1hsv, mask=green_mask)

fig.add_subplot(fila,columna,1)
plt.title("Imagen: Original")
plt.axis('off')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
fig.add_subplot(fila,columna,2)
plt.axis('off')
plt.title("Imagen: HSV")
plt.imshow(img1hsv)

fig.add_subplot(fila,columna,3)
plt.axis('off')
plt.title("Imagen: Filtrado Rojo")
plt.imshow(red_mask)
fig.add_subplot(fila,columna,4)
plt.axis('off')
plt.title("Imagen: Resultado Rojo")
plt.imshow(red)

fig.add_subplot(fila,columna,5)
plt.axis('off')
plt.title("Imagen: Filtrado Verde")
plt.imshow(green_mask)
fig.add_subplot(fila,columna,6)
plt.axis('off')
plt.title("Imagen: Resultado Verde")
plt.imshow(green)

fig.add_subplot(fila,columna,7)
plt.axis('off')
plt.title("Imagen: Filtrado Azul")
plt.imshow(blue_mask)
fig.add_subplot(fila,columna,8)
plt.axis('off')
plt.title("Imagen: Resultado Azul")
plt.imshow(blue)
plt.show()