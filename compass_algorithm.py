import numpy as np
from PIL import Image

resim=np.array(Image.open("resim.jpg")).astype(np.uint8)
griResim=np.around(0.299*resim[:,:,0]+
                   0.587*resim[:,:,1]+
                   0.114*resim[:,:,2]).astype(np.uint8)
height,width=griResim.shape

g0=np.array([[-1,-1,-1],[1,-2,1],[1,1,1]])
g45=np.array([[-1,-1,1],[-1,-2,1],[1,1,1]])
g90=np.array([[-1,1,1],[-1,-2,1],[-1,1,1]])
g135=np.array([[1,1,1],[-1,-2,1],[-1,-1,1]])
g180=np.array([[1,1,1],[1,-2,1],[-1,-1,-1]])
g225=np.array([[1,1,1],[1,-2,-1],[1,-1,-1]])
g270=np.array([[1,1,-1],[1,-2,-1],[1,1,-1]])
g315=np.array([[1,-1,-1],[1,-2,-1],[1,1,1]])

yeniResim=np.zeros((height,width))

for i in range(1, height-1):
    for j in range(1, width-1):
        g0Deger =   (g0[0,0] * griResim[i-1,j-1]) + \
                    (g0[0,1] * griResim[i-1,j]) + \
                    (g0[0,2] * griResim[i-1,j+1]) + \
                    (g0[1,0] * griResim[i,j-1]) + \
                    (g0[1,1] * griResim[i,j]) + \
                    (g0[1,2] * griResim[i,j+1]) + \
                    (g0[2,0] * griResim[i+1,j-1]) + \
                    (g0[2,1] * griResim[i+1,j]) + \
                    (g0[2,2] * griResim[i+1,j+1])
        g45Deger =  (g45[0,0] * griResim[i-1,j-1]) + \
                    (g45[0,1] * griResim[i-1,j]) + \
                    (g45[0,2] * griResim[i-1,j+1]) + \
                    (g45[1,0] * griResim[i,j-1]) + \
                    (g45[1,1] * griResim[i,j]) + \
                    (g45[1,2] * griResim[i,j+1]) + \
                    (g45[2,0] * griResim[i+1,j-1]) + \
                    (g45[2,1] * griResim[i+1,j]) + \
                    (g45[2,2] * griResim[i+1,j+1])
        g90Deger =  (g90[0, 0] * griResim[i - 1, j - 1]) + \
                    (g90[0, 1] * griResim[i - 1, j]) + \
                    (g90[0, 2] * griResim[i - 1, j + 1]) + \
                    (g90[1, 0] * griResim[i, j - 1]) + \
                    (g90[1, 1] * griResim[i, j]) + \
                    (g90[1, 2] * griResim[i, j + 1]) + \
                    (g90[2, 0] * griResim[i + 1, j - 1]) + \
                    (g90[2, 1] * griResim[i + 1, j]) + \
                    (g90[2, 2] * griResim[i + 1, j + 1])
        g135Deger = (g135[0, 0] * griResim[i - 1, j - 1]) + \
                    (g135[0, 1] * griResim[i - 1, j]) + \
                    (g135[0, 2] * griResim[i - 1, j + 1]) + \
                    (g135[1, 0] * griResim[i, j - 1]) + \
                    (g135[1, 1] * griResim[i, j]) + \
                    (g135[1, 2] * griResim[i, j + 1]) + \
                    (g135[2, 0] * griResim[i + 1, j - 1]) + \
                    (g135[2, 1] * griResim[i + 1, j]) + \
                    (g135[2, 2] * griResim[i + 1, j + 1])
        g180Deger = (g180[0, 0] * griResim[i - 1, j - 1]) + \
                    (g180[0, 1] * griResim[i - 1, j]) + \
                    (g180[0, 2] * griResim[i - 1, j + 1]) + \
                    (g180[1, 0] * griResim[i, j - 1]) + \
                    (g180[1, 1] * griResim[i, j]) + \
                    (g180[1, 2] * griResim[i, j + 1]) + \
                    (g180[2, 0] * griResim[i + 1, j - 1]) + \
                    (g180[2, 1] * griResim[i + 1, j]) + \
                    (g180[2, 2] * griResim[i + 1, j + 1])
        g225Deger = (g225[0, 0] * griResim[i - 1, j - 1]) + \
                    (g225[0, 1] * griResim[i - 1, j]) + \
                    (g225[0, 2] * griResim[i - 1, j + 1]) + \
                    (g225[1, 0] * griResim[i, j - 1]) + \
                    (g225[1, 1] * griResim[i, j]) + \
                    (g225[1, 2] * griResim[i, j + 1]) + \
                    (g225[2, 0] * griResim[i + 1, j - 1]) + \
                    (g225[2, 1] * griResim[i + 1, j]) + \
                    (g225[2, 2] * griResim[i + 1, j + 1])
        g270Deger = (g270[0, 0] * griResim[i - 1, j - 1]) + \
                    (g270[0, 1] * griResim[i - 1, j]) + \
                    (g270[0, 2] * griResim[i - 1, j + 1]) + \
                    (g270[1, 0] * griResim[i, j - 1]) + \
                    (g270[1, 1] * griResim[i, j]) + \
                    (g270[1, 2] * griResim[i, j + 1]) + \
                    (g270[2, 0] * griResim[i + 1, j - 1]) + \
                    (g270[2, 1] * griResim[i + 1, j]) + \
                    (g270[2, 2] * griResim[i + 1, j + 1])
        g315Deger = (g315[0, 0] * griResim[i - 1, j - 1]) + \
                    (g315[0, 1] * griResim[i - 1, j]) + \
                    (g315[0, 2] * griResim[i - 1, j + 1]) + \
                    (g315[1, 0] * griResim[i, j - 1]) + \
                    (g315[1, 1] * griResim[i, j]) + \
                    (g315[1, 2] * griResim[i, j + 1]) + \
                    (g315[2, 0] * griResim[i + 1, j - 1]) + \
                    (g315[2, 1] * griResim[i + 1, j]) + \
                    (g315[2, 2] * griResim[i + 1, j + 1])
        dizim=[g0Deger,g45Deger,g90Deger,g135Deger,g180Deger,g225Deger,g270Deger,g315Deger]
        buyukluk=0
        for k in range(8):
            if(dizim[k]>buyukluk):
                buyukluk=dizim[k]
                yeniResim[i - 1, j - 1] = buyukluk

Image.fromarray(resim).show()
Image.fromarray(yeniResim).show()

