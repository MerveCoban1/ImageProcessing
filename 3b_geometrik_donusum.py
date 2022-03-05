from skimage import io
import numpy as np
image_collectin=io.imread_collection('D:\*.tiff')
image_3d=io.concatenate_images(image_collectin)
zEkseniBoy,yEkseniBoy,xEkseniBoy,renk=image_3d.shape
def translationIslemi(tx,ty,tz):
    translation=np.array([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])
    yeniResim=np.zeros((zEkseniBoy,yEkseniBoy,xEkseniBoy))
    for i in range(0, zEkseniBoy):
        for j in range(0, yEkseniBoy):
            for m in range(0, xEkseniBoy):
                coordinate = np.array([i, j, m, 1])
                x, y, z, w = translation.dot(coordinate);
                deger = image_3d[i, j, m]
                if (x > 0 and y > 0 and z > 0 and x < zEkseniBoy and y < yEkseniBoy and z < xEkseniBoy):
                    yeniResim[x, y, z] = deger
    return yeniResim
def scalingIslemi(sx,sy,sz):
    scaling=np.array([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])
    yeniResim=np.zeros((zEkseniBoy,yEkseniBoy,xEkseniBoy))
    for i in range(0, zEkseniBoy - 1):
        for j in range(0, yEkseniBoy - 1):
            for m in range(0, xEkseniBoy - 1):
                coordinate = np.array([i, j, m, 1])
                x, y, z, w = scaling.dot(coordinate);
                deger = image_3d[i, j, m]
                if (x > 0 and y > 0 and z > 0 and x < zEkseniBoy and y < yEkseniBoy and z < xEkseniBoy):
                    yeniResim[x, y, z] = deger
    return yeniResim
def rotationIslemi(q):
    rotation_x = np.array([[1, 0, 0, 0], [0, np.cos(q), -np.sin(q), 0], [0, np.sin(q), np.cos(q), 0], [0, 0, 0, 1]])
    rotation_y = np.array([[np.cos(q), 0, np.sin(q), 0], [0, 1, 0, 0], [-np.sin(q), 0, np.cos(q), 0], [0, 0, 0, 1]])
    rotation_z = np.array([[np.cos(q), -np.sin(q), 0, 0], [np.sin(q), np.cos(q), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    yeniResim=np.zeros((zEkseniBoy,yEkseniBoy,xEkseniBoy))
    for i in range(0, zEkseniBoy - 1):
        for j in range(0, yEkseniBoy - 1):
            for m in range(0, xEkseniBoy - 1):
                coordinate = np.array([i, j, m, 1])
                x, y, z, w = rotation_x.dot(coordinate);
                deger = image_3d[i, j, m]
                if (x > 0 and y > 0 and z > 0 and x < zEkseniBoy and y < yEkseniBoy and z < xEkseniBoy):
                    yeniResim[x, y, z] = deger
    return yeniResim
translationSonuc=translationIslemi(10,20,10)
scalingSonuc=scalingIslemi(2,1,1)
rotationSonuc=rotationIslemi(-90)
io.imshow_collection(translationSonuc)
io.show()



















