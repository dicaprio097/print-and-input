import calendar

def ay_takvimi():
    yil = int(input("Yılı girin: "))
    ay = int(input("Ayı girin (1-12): "))
    print(calendar.month(yil, ay))

def yil_takvimi():
    yil = int(input("Yılı girin: "))
    print(calendar.calendar(yil))

def takvimmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║                TAKVİM                  ║")
        print("║                                        ║")
        print("║         1-Ay Takvimi Göster            ║")
        print("║         2-Yıl Takvimi Göster           ║")
        print("║         3-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            ay_takvimi()
        elif secim == "2":
            yil_takvimi()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    takvimmenu()