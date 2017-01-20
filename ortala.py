# -*- coding: utf-8 -*-
import os

yeni_Genislik = yeni_Yukseklik = 360
arkaplan_Genislik = arkaplan_Yukseklik = 360

from PIL import Image


def ortala(resim):
    print resim

    im = Image.open(resim)
    im.thumbnail((yeni_Genislik, yeni_Yukseklik), Image.ANTIALIAS)
    im.save('thumb/' + resim[:-4] + '.png', quality=100)

    til = Image.new("RGBA", (arkaplan_Genislik, arkaplan_Yukseklik), '#ffffff')
    imm = Image.open('thumb/' + resim[:-4] + '.png')

    son_Genislik = imm.size[0]
    son_Yukselik = imm.size[1]

    yukaridan = (arkaplan_Yukseklik - son_Yukselik) / 2
    soldan = (arkaplan_Genislik - son_Genislik)  / 2


    til.paste(imm, (soldan, yukaridan))
    til.save('son/' + resim[:-4] + '.png', quality=100)


dosya_klasoru = "/home/muslu/django/falez/ydk/referanslar/"
uzantilar = ['jpg', 'jpeg', 'png']

dosyalar = [fn for fn in os.listdir(dosya_klasoru) if any(fn.endswith(ext) for ext in uzantilar)]

for dosya in dosyalar:
    ortala(dosya)
