import os
import imageio

myfiles = os.listdir('myimage')


images = []
for i in range(len(myfiles)):
    image = imageio.imread("myimage/"+ myfiles[i])
    images.append(image)

imageio.mimsave('classgif.gif',images)    