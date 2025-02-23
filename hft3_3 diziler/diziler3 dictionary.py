tatil_günleri=("Cumartesi","Pazar")
siniflar = ["9A","10A","11A","11B"]
ogrenci_bilgileri={ #dictionary tanımlama işlemi süslü parantez ile yapılır. 
    "ogrenci_adi" :"Remzi DURAN",
    "ogrenci_no" : "351"
}

print(ogrenci_bilgileri)
# print(ogrenci_bilgileri[1]) #dictioanry de indexleme yapılmaz. Onun yerine key ile value alınır.
print(ogrenci_bilgileri["ogrenci_adi"])