import hm_menu as hm
import oyn_menu as oyn


def vektorelappmenu():
    print("╔════════════════════════════════════════╗")
    print("║                                        ║")
    print("║                                        ║")
    print("║                                        ║")
    print("║               VEKTOREL APP             ║")
    print("║                                        ║")
    print("║         1-Hesapmakinesi                ║")
    print("║                                        ║")
    print("║         2-Oyunlar                      ║")
    print("║                                        ║")
    print("║         3-Ayarlar                      ║")
    print("║                                        ║")
    print("║         4-                             ║")
    print("║                                        ║")
    print("║                                        ║")    
    print("║             Surum 1.9.3                ║")
    print("╚════════════════════════════════════════╝")

vektorelappmenu()
secim = input("Seçiminiz nedir?")
if secim == "1" : hm.hmmenu()
if secim == "2" : oyn.oynmenu()