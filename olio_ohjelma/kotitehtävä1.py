#TEHTÄVÄ 1:Muuta allaolevaa koodia niin, että kaikki samat 
# toiminnot tapahtuvat yhden for-loopin sisällä!
#------------------------------------------------------------------------------------------------
# img1=Image.open('spade_1.png')
# img2=Image.open('spade_2.png')
# img3=Image.open('spade_3.png')
# img4=Image.open('spade_4.png')
# img5=Image.open('spade_5.png')

from PIL import Image

img_paths = ['spade_1.png', 'spade_2.png', 'spade_3.png', 'spade_4.png', 'spade_5.png']
images = []

for path in img_paths:
    img = Image.open(path)
    images.append(img)


