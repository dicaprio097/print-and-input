def ayarlar_menu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║                AYARLAR                 ║")
        print("║                                        ║")
        print("║         1-Ses Ayarları                 ║")
        print("║         2-Ekran Ayarları               ║")
        print("║         3-Dil Ayarları                 ║")
        print("║         4-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            ses_ayarları()
        elif secim == "2":
            ekran_ayarları()
        elif secim == "3":
            dil_ayarları()
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

def ses_ayarları():
    print("Ses ayarları menüsüne hoş geldiniz.")
    # Ses ayarları ile ilgili işlemler burada yapılabilir
    input("Devam etmek için Enter tuşuna basın.")

def ekran_ayarları():
    print("Ekran ayarları menüsüne hoş geldiniz.")
    # Ekran ayarları ile ilgili işlemler burada yapılabilir
    input("Devam etmek için Enter tuşuna basın.")

def dil_ayarları():
    print("Dil ayarları menüsüne hoş geldiniz.")
    # Dil ayarları ile ilgili işlemler burada yapılabilir
    input("Devam etmek için Enter tuşuna basın.")

if __name__ == "__main__":
    ayarlar_menu()