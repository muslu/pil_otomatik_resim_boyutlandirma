# -*- coding: utf-8 -*-
import os

yeni_Genislik = yeni_Yukseklik = 360
### İstenilen genişlik ve yüksekliğin maksimum değerleri
### Imajlar 360*360 pikselleri geçmeyecek şekilde orantılı olarak boyutlandırılacak

arkaplan_Genislik = arkaplan_Yukseklik = 360
### Tüm imajların en son alacağı boyutlar


from PIL import Image


def ortala(resim):
    print resim

    im = Image.open(resim)
    ### Görseli aç
    
    im.thumbnail((yeni_Genislik, yeni_Yukseklik), Image.ANTIALIAS)
    ### Görseller 360*360 pikselleri geçmeyecek şekilde orantılı olarak boyutlandırılacak. Bozulmalar önlenecek
    #### 360*360 pikselden küçük olanlar boyutlandırılmaz
    
    im.save('thumb/' + resim[:-4] + '.png', quality=100)
    ### thumb klasörünün altında var olan uzantıları silinip .png olacak şekilde tekrar adlandırılacak
    ### kalitesi en fazla olacak şekilde ayarlanacak
    #### kayıt işlemi opsiyonel
    
    bos = Image.new("RGBA", (arkaplan_Genislik, arkaplan_Yukseklik), '#ffffff')
    ### RGB ve Alpha olacak şekilde arkaplanı beyaz boş bir imaj oluşturuluyor
    
    imth = Image.open('thumb/' + resim[:-4] + '.png')
    ### biraz önce boyutlandırılan resim tekrar yükleniyor.

    
    son_Genislik = imth.size[0]
    son_Yukselik = imth.size[1]
    ### Verilen değerlerden küçük resimler tekrarboyutlandırılmadığı için son genişlik ve yüksekliği alıyoruz.


    ################### boş imaja yükleme yapılmadan önce yukarıdan ve soldan nereye getirileceğini hesaplamamız gerekiyor. #####################
    
    yukaridan = (arkaplan_Yukseklik - son_Yukselik) / 2
    ### boş imajın yüksekliğinde boyutlandırılan (ya da boyutlandırılmayan) imajın yüksekliğinde çıkarıp yarısını alıyoruz
    
    soldan = (arkaplan_Genislik - son_Genislik)  / 2
    ### soldan ortalamak için 

    bos.paste(imth, (soldan, yukaridan))
    ### boş imaja yapıştırma işlemi yaparken hangi imaj ve nerelere bilgilerini veriyoruz
    
    bos.save('son/' + resim[:-4] + '.png', quality=100)
    ### oluşturulan boş sayfa ve üzerine eklenen imajı kayıt ediyoruz


dosya_klasoru = "/home/muslu/resimler/"
istenen_uzantilar = ['jpg', 'jpeg', 'png']
#### sadece bu uzantıları istiyoruz


dosyalar = [fn for fn in os.listdir(dosya_klasoru) if any(fn.endswith(ext) for ext in istenen_uzantilar)]


for dosya in dosyalar:
    ortala(dosya)
