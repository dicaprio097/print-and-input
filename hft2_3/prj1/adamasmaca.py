def adamasmacamenu():
    print("Adam asmaca oyununa hoşgeldiniz...")

import random

kelime_listesi = ["python", "programlama", "bilgisayar", "oyun", "yapayzeka"]
secilen_kelime = random.choice(kelime_listesi)
tahmin_edilen_harfler = []
yanlis_tahmin_sayisi = 0
max_yanlis_tahmin = 6

def kelimeyi_goster():
    gosterilecek_kelime = ""
    for harf in secilen_kelime:
        if harf in tahmin_edilen_harfler:
            gosterilecek_kelime += harf
        else:
            gosterilecek_kelime += "_"
    return gosterilecek_kelime

print("Adam Asmaca Oyununa Hoş Geldiniz!")

while yanlis_tahmin_sayisi < max_yanlis_tahmin:
    print("\n" + kelimeyi_goster())
    tahmin = input("Bir harf tahmin edin: ").lower()

    if tahmin in tahmin_edilen_harfler:
        print("Bu harfi zaten tahmin ettiniz.")
    elif tahmin in secilen_kelime:
        print("Doğru tahmin!")
        tahmin_edilen_harfler.append(tahmin)
        if all(harf in tahmin_edilen_harfler for harf in secilen_kelime):
            print("Tebrikler, kelimeyi buldunuz: " + secilen_kelime)
            break
    else:
        print("Yanlış tahmin.")
        tahmin_edilen_harfler.append(tahmin)
        yanlis_tahmin_sayisi += 1

    print(f"Yanlış tahmin sayısı: {yanlis_tahmin_sayisi}/{max_yanlis_tahmin}")

if yanlis_tahmin_sayisi == max_yanlis_tahmin:
    print("Üzgünüm, kaybettiniz. Kelime: " + secilen_kelime)


