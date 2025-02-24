import random

kelimeler = ["python", "programlama", "bilgisayar", "yazilim", "algoritma"]
secilen_kelime = random.choice(kelimeler)
tahmin_edilen_harfler = []
yanlis_tahmin_sayisi = 0
max_yanlis_tahmin = 6

def kelimeyi_goster():
    gosterilen_kelime = ""
    for harf in secilen_kelime:
        if harf in tahmin_edilen_harfler:
            gosterilen_kelime += harf
        else:
            gosterilen_kelime += "_"
    return gosterilen_kelime

def adamasmaca():
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

    input("Oyunu bitirmek için Enter tuşuna basın.")

def adamasmacamenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║             ADAM ASMACA                ║")
        print("║                                        ║")
        print("║         1-Oyunu Başlat                 ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            adamasmaca()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    adamasmacamenu()