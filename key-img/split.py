import Image
import os


im = Image.open('rsa.jpg', 'r')
w , h =  im.size

splitspath = "html/splits/"

c = []

for i in range(0, w+1, w/5):
    for j in range(0, h+1, h/4):
        c.append((j, i, j+150 ,i+150 ))


c = c[:20]


k = 0
for i in c:
    a = im.crop(i)
    a.save(splitspath+str(k)+'.jpg', 'jpeg')
    k =  k+1

