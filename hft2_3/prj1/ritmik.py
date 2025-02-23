def ritmik_sayma():
    baslangic = int(input("Başlangıç sayısını girin: "))
    bitis = int(input("Bitiş sayısını girin: "))
    artis = int(input("Artış miktarını girin: "))

    if baslangic < bitis:
        for sayi in range(baslangic, bitis + 1, artis):
            print(sayi, end=" ")
    else:
        for sayi in range(baslangic, bitis - 1, -artis):
            print(sayi, end=" ")
    print()

def ritmikmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║             RİTMİK SAYMA               ║")
        print("║                                        ║")
        print("║         1-Ritmik Sayma Yap             ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            ritmik_sayma()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    ritmikmenu()