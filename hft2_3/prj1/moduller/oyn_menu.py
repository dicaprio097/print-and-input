import ttrs
import yilan
import adam
import xox
import numara

def oynmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║                OYUNLAR                 ║")
        print("║                                        ║")
        print("║         1-Tetris                       ║")
        print("║                                        ║")
        print("║         2-Yılan Oyunu                  ║")
        print("║                                        ║")
        print("║         3-Adam Asmaca                  ║")
        print("║                                        ║")
        print("║         4-Tic-Tac-Toe(XOX)             ║")
        print("║                                        ║")
        print("║         5-Numara Tahmin Oyunu          ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")
        print("║                                        ║")    
        print("║             Seçiminiz nedir?           ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Hangi oyunu oynamak istersiniz? ")
        if secim == "1":
            ttrs.tetrismenu()
        elif secim == "2":
            yilan.yilanmenu()
        elif secim == "3":
            adam.adamasmacamenu()
        elif secim == "4":
            xox.xoxmenu()
        elif secim == "5":
            numara.numaratamhinmenu()
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    oynmenu()