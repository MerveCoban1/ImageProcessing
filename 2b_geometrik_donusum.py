import numpy as np
from PIL import Image
resim=np.array(Image.open("resim.jpg")).astype(np.uint8)
griResim=np.around(0.299*resim[:,:,0]+
                   0.587*resim[:,:,1]+
                   0.114*resim[:,:,2]).astype(np.uint8)
height,width=griResim.shape
def translationIslemi(tx,ty):
    translation = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    yeniResim = np.zeros((height, width))
    for i in range(1, height-1):
        for j in range(1, width-1):
            coordinate = np.array([i, j, 1])
            a,b,c = translation.dot(coordinate);
            deger=griResim[i,j]
            if(a>0 and b>0 and a<height and b<width):
                yeniResim[a,b]=deger
    return yeniResim
def scalingIslemi(sx,sy):
    scaling=np.array([[sx,0,0],[0,sy,0],[0,0,1]])
    yeniResim = np.zeros((height, width))
    for i in range(1, height-1):
        for j in range(1, width-1):
            coordinate = np.array([i, j, 1])
            a,b,c = scaling.dot(coordinate);
            deger=griResim[i,j]
            if(a>0 and b>0 and a<height and b<width):
                yeniResim[a,b]=deger
    return yeniResim
def rotationIslemi(q):
    rotation=np.array([[np.cos(q),-np.sin(q),0],[np.sin(q),np.cos(q),0],[0,0,1]])
    yeniResim = np.zeros((height, width))
    for i in range(1, height-1):
        for j in range(1, width-1):
            coordinate = np.array([i, j, 1])
            a,b,c = rotation.dot(coordinate);
            deger=griResim[i,j]
            if (a > 0 and b > 0 and a < height and b < width):
                yeniResim[a, b] = deger
    return yeniResim
translationSonuc=translationIslemi(50,20)
scalingSonuc=scalingIslemi(2,1)
rotationSonuc=rotationIslemi(-90)
Image.fromarray(translationSonuc).show()
Image.fromarray(scalingSonuc).show()
Image.fromarray(rotationSonuc).show()
