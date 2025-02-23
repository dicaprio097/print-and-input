def doviz_cevirme():
    kurlar = {
        "USD": 1.0,  # ABD Doları
        "EUR": 0.85,  # Euro
        "TRY": 8.5,  # Türk Lirası
        "GBP": 0.75,  # İngiliz Sterlini
        "JPY": 110.0  # Japon Yeni
    }

    print("Mevcut döviz kurları:")
    for birim, kur in kurlar.items():
        print(f"1 USD = {kur} {birim}")

    miktar = float(input("Çevirmek istediğiniz miktarı girin (USD): "))
    hedef_birim = input("Hangi para birimine çevirmek istiyorsunuz (EUR, TRY, GBP, JPY)? ").upper()

    if hedef_birim in kurlar:
        cevrilen_miktar = miktar * kurlar[hedef_birim]
        print(f"{miktar} USD = {cevrilen_miktar} {hedef_birim}")
    else:
        print("Geçersiz para birimi.")

def dovizmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║             DÖVİZ ÇEVİRME              ║")
        print("║                                        ║")
        print("║         1-Döviz Çevir                  ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            doviz_cevirme()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    dovizmenu()