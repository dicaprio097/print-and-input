def kare_ciz():
    kenar = int(input("Karenin kenar uzunluğunu girin: "))
    for i in range(kenar):
        print("* " * kenar)

def dikdortgen_ciz():
    uzunluk = int(input("Dikdörtgenin uzunluğunu girin: "))
    genislik = int(input("Dikdörtgenin genişliğini girin: "))
    for i in range(genislik):
        print("* " * uzunluk)

def ucgen_ciz():
    yukseklik = int(input("Üçgenin yüksekliğini girin: "))
    for i in range(1, yukseklik + 1):
        print("* " * i)

def sekilmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║             ŞEKİL ÇİZDİRME             ║")
        print("║                                        ║")
        print("║         1-Kare Çiz                     ║")
        print("║         2-Dikdörtgen Çiz               ║")
        print("║         3-Üçgen Çiz                    ║")
        print("║         4-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            kare_ciz()
        elif secim == "2":
            dikdortgen_ciz()
        elif secim == "3":
            ucgen_ciz()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    sekilmenu()