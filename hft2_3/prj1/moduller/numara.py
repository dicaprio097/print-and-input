import random

def numara_tahmin():
    print("Numara Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misiniz?")

    tutulan_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        tahmin = int(input("Tahmininiz nedir? "))
        tahmin_sayisi += 1

        if tahmin < tutulan_sayi:
            print("Daha büyük bir sayı söyleyin.")
        elif tahmin > tutulan_sayi:
            print("Daha küçük bir sayı söyleyin.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} tahminde doğru sayıyı buldunuz: {tutulan_sayi}")
            break

def numaratamhinmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║          NUMARA TAHMİN OYUNU           ║")
        print("║                                        ║")
        print("║         1-Oyunu Başlat                 ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            numara_tahmin()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    numaratamhinmenu()