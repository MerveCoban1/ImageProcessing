import numpy as np
from PIL import Image

resim=np.array(Image.open("resim.jpg")).astype(np.uint8) #resmimizi açtık numpy dizisi olarak
griResim=np.around(0.299*resim[:,:,0]+  #resmimizi griye çevirdik
                   0.587*resim[:,:,1]+
                   0.114*resim[:,:,2]).astype(np.uint8)
height,width=griResim.shape #863,700 çıkıyor.Resmimizin boyutlarını aldık

yatay=np.array([[-1,0,1],[-1,0,1],[-1,0,1]]) #prewit için filtrelerimizi tanımladık
dikey=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

yeniResim=np.zeros((height,width))  #resmimizin boyutlarında 0'lardan oluşan bir matris tanımladık

for i in range(1, height-1):
    for j in range(1, width-1):
        yatayDeger= (yatay[0,0] * griResim[i-1,j-1]) + \
                    (yatay[0,1] * griResim[i-1,j]) + \
                    (yatay[0,2] * griResim[i-1,j+1]) + \
                    (yatay[1,0] * griResim[i,j-1]) + \
                    (yatay[1,1] * griResim[i,j]) + \
                    (yatay[1,2] * griResim[i,j+1]) + \
                    (yatay[2,0] * griResim[i+1,j-1]) + \
                    (yatay[2,1] * griResim[i+1,j]) + \
                    (yatay[2,2] * griResim[i+1,j+1])
        dikeyDeger = (dikey[0,0] * griResim[i-1,j-1]) + \
                     (dikey[0,1] * griResim[i-1,j]) + \
                     (dikey[0,2] * griResim[i-1,j+1]) + \
                     (dikey[1,0] * griResim[i,j-1]) + \
                     (dikey[1,1] * griResim[i,j]) + \
                     (dikey[1,2] * griResim[i,j+1]) + \
                     (dikey[2,0] * griResim[i+1,j-1]) + \
                     (dikey[2,1] * griResim[i+1,j]) + \
                     (dikey[2,2] * griResim[i+1,j+1])
        buyukluk=np.sqrt(pow(yatayDeger,2.0) + pow(dikeyDeger,2.0))  #formül gereği karelerinin toplamının karekökü sonucu verir.
        yeniResim[i-1,j-1]=buyukluk

Image.fromarray(resim).show()
Image.fromarray(yeniResim).show()#dizi şeklindeki resmi görüntüleme
#numpy sınıfı büyük boyutlu dizi işlemlerinde kullanılır genellikle. Dizilerle,matrislerle çalışmak için kullanılan bir python kütüphanesidir.
#numpy.uint8= unsigned integer(0 to 255)
#0: mavi
#1: yeşil
#2: kırmızı demektir
#resim[:,:,0] resmin mavi bileşeni demektir. ilk 2 boşluk resmin genişlik ve yüksekliği ifade etmekte 3.kısım renk kısmı.
#around() yuvarlama işlemi yapıyor.
#sqrt karekök değerini alıyor.
#pow üs alma işlemi için kullanılır.
