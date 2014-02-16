import Image,ImageDraw,ImageFont


fontpath  = "fonts/data-latin.ttf"
keypath   = "keys/id_rsa"

size = (750, 600)
im = Image.new('RGB', size)
dr = ImageDraw.Draw(im)

clr= (255,255,255)

fontsize =  22

fon = ImageFont.truetype(fontpath , fontsize)

f = open(keypath, 'r')
s = f.read()
f.close()

i=0
for tmp in s.split('\n'):
  dr.text((23,i*fontsize), tmp, font=fon, fill=clr)
  i=i+1



im.save('rsa.jpg', 'JPEG')
