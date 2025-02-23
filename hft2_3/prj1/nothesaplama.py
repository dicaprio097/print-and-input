def not_hesapla():
    isim = input("İsminizi girin: ")
    soyisim = input("Soyisminizi girin: ")

    while True:
        not1 = float(input("Birinci notu girin (0-100): "))
        if 0 <= not1 <= 100:
            break
        else:
            print("Geçersiz not. Lütfen 0 ile 100 arasında bir değer girin.")

    while True:
        not2 = float(input("İkinci notu girin (0-100): "))
        if 0 <= not2 <= 100:
            break
        else:
            print("Geçersiz not. Lütfen 0 ile 100 arasında bir değer girin.")

    ortalama = (not1 + not2) / 2
    print(f"{isim} {soyisim}, ortalamanız: {ortalama:.2f}")

    if ortalama >= 90:
        print("Tebrikler!")
    elif ortalama >= 80:
        print("Mükemmel!")
    elif ortalama >= 70:
        print("İyi!")
    elif ortalama >= 60:
        print("İdare eder!")
    elif ortalama >= 50:
        print("Biraz daha çalışmalısınız!")
    else:
        print("Maalesef kaldınız!")

def nothesaplamamenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║            NOT HESAPLAMA               ║")
        print("║                                        ║")
        print("║         1-Not Hesapla                  ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            not_hesapla()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    nothesaplamamenu()

