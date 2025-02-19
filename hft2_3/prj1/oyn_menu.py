import tetris as ttrs
import adamasmaca as adam

def oynmenu():
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


secim = input("Hangi oyunu oynamak istersiniz?") 
if secim == "1" : ttrs.tetrismenu()

if secim == "3" : adam.adamasmacamenu()