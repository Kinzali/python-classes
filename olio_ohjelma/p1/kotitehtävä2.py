
#Resize the image in the given (width, height)
# img1=img1.resize((128,128))
# img2=img2.resize((128,128))
# img3=img3.resize((128,128))
# img4=img4.resize((128,128))
# img5=img5.resize((128,128))

images = [img1, img2, img3, img4, img5]
new_size = (128, 128)

for img in images:
    img = img.resize(new_size)
