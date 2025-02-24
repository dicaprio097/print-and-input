def toplama():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a + b}")

def cikarma():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a - b}")

def carpma():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a * b}")

def bolme():
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    if b != 0:
        print(f"Sonuç: {a / b}")
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")

def us_alma():
    a = float(input("Taban sayıyı girin: "))
    b = float(input("Üs sayıyı girin: "))
    print(f"Sonuç: {a ** b}")

def karenin_cevresi():
    a = float(input("Karenin bir kenar uzunluğunu girin: "))
    print(f"Karenin çevresi: {4 * a}")

def karenin_alani():
    a = float(input("Karenin bir kenar uzunluğunu girin: "))
    print(f"Karenin alanı: {a * a}")

def mesafe_donusturucu():
    km = float(input("Kilometreyi girin: "))
    print(f"Mil: {km * 0.621371}")

def hmmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║             HESAP MAKİNESİ             ║")
        print("║                                        ║")
        print("║         1-Toplama                      ║")
        print("║                                        ║")
        print("║         2-Çıkarma                      ║")
        print("║                                        ║")
        print("║         3-Çarpma                       ║")
        print("║                                        ║")
        print("║         4-Bölme                        ║")
        print("║                                        ║")
        print("║         5-Üs alma                      ║")
        print("║                                        ║")
        print("║         6-Karenin Çevresini Bulma      ║")
        print("║                                        ║")
        print("║         7-Karenin Alanını Bulma        ║")
        print("║                                        ║")
        print("║         8-Mesafe Dönüştürücü           ║")
        print("║                                        ║")    
        print("║             Seçiminiz nedir?           ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            toplama()
        elif secim == "2":
            cikarma()
        elif secim == "3":
            carpma()
        elif secim == "4":
            bolme()
        elif secim == "5":
            us_alma()
        elif secim == "6":
            karenin_cevresi()
        elif secim == "7":
            karenin_alani()
        elif secim == "8":
            mesafe_donusturucu()
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    hmmenu()