import cv2
import numpy as np
def histogramOlustur(resim):   #histogram dizisini oluşturduk
    resultArray=np.zeros(256) #256 boyutunda 0lardan oluşan bir dizi ürettik
    for i in range(resim.shape[0]):#shape ile resmin boyutlarını aldık her bir değerini i ve jye attık
        for j in range(resim.shape[1]):
            resultArray[resim[i,j]]+=1#varolan her i noktası için ne kadar j değeri varsa sayısını buluyoruz.
    return resultArray
def histogramEsitle(histogramDizisi,resimBoyutu,L):
    yeniDegerler=np.zeros(len(histogramDizisi))
    yeniDegerler[0]=histogramDizisi[0]
    for i in range(1,len(yeniDegerler),+1):
        yeniDegerler[i]=(int)(histogramDizisi[i])+(int)(yeniDegerler[i-1]) #kümülatif toplam bulundu
    for i in range(yeniDegerler.shape[0]):
        yeniDegerler[i]=round(((yeniDegerler[i]-min(histogramDizisi))/(resimBoyutu-min(histogramDizisi)))*(2**L-1))
    return yeniDegerler
def histogramGerme(histogramDizisi,resim,gerilmisResim):
    A=max(histogramDizisi)
    B=0
    b=max(histogramDizisi)
    a=min(histogramDizisi)
    print(histogramDizisi)
    fark=b-a;
    for i in range(resim.shape[0]):
        for j in range(resim.shape[1]):
            gerilmisResim[i][j]=((A-B)/fark)*(resim[i][j]-a)
    return gerilmisResim
def histogramResimCevir(resim,esitlenmisDegerler):
    sonucResmi=np.zeros((resim.shape[0],resim.shape[1],1), dtype=np.uint8)
    for i in range(sonucResmi.shape[0]):
        for j in range(sonucResmi.shape[1]):
            sonucResmi[i,j]=esitlenmisDegerler[resim[i,j]]
    return sonucResmi

resim=cv2.imread('resim.jpg',0) #resmimizi gri olarak aldık
gerilmisResim=cv2.imread('resim.jpg',0)
histogramDizisi=histogramOlustur(resim) #resim değerlerini içeren bir dizi oluşturduk histogram yani.
esitlenmisDegerler=histogramEsitle(histogramDizisi,resim.shape[0]*resim.shape[1],8) #eşitleme fonksiyonumuz. Dizinin elemanları üzerinde işlem yapılcak
esitlenmisResim=histogramResimCevir(resim,esitlenmisDegerler) #esitlenmiş değerlerimizi resmimize uyguladık.
gerilmisResim=histogramGerme(histogramDizisi,resim,gerilmisResim) #germe fonksiyonumuz. Dizinin elemanları üzerinde işlem yapılcak
cv2.imshow("Normal Resim",resim)
cv2.imshow("Histogram Esitlemesi Yapilmis Resim",esitlenmisResim)
cv2.imshow("Histogram Germe Islemi Yapilmis Resim",gerilmisResim)
cv2.waitKey(0)

# resim.shape[0]=height resim.shape[1]=width