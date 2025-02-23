import hm_menu
import oyn_menu
import set_menu
import takvim
import nothesaplama
import sicaklik
import doviz
import ritmik
import sekil
import bmi
# Diğer modülleri de import edin (takvim, nothesaplama, sicaklik, doviz, ritmik, sekil, bmi)

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
    print("║         4-Takvim                       ║")
    print("║                                        ║")
    print("║         5-Not Hesaplama                ║")
    print("║                                        ║")
    print("║         6-Sıcaklık Çevirme             ║")
    print("║                                        ║")
    print("║         7-Döviz Uygulaması             ║")
    print("║                                        ║")
    print("║         8-Ritmik Sayma                 ║")
    print("║                                        ║")
    print("║         9-Şekil Çizdirme               ║")
    print("║                                        ║")
    print("║        10-BMI Hesaplama                ║")
    print("║                                        ║")
    print("║             Surum 1.9.3                ║")
    print("╚════════════════════════════════════════╝")

def main():
    while True:
        vektorelappmenu()
        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            hm_menu.hmmenu()
        elif secim == "2":
            oyn_menu.oynmenu()
        elif secim == "3":
            set_menu.ayarlar_menu()
        elif secim == "4":
            takvim.takvimmenu()
        elif secim == "5":
            nothesaplama.nothesaplamamenu()
        elif secim == "6":
            sicaklik.sicaklikmenu()
        elif secim == "7":
            doviz.dovizmenu()
        elif secim == "8":
            ritmik.ritmikmenu()
        elif secim == "9":
            sekil.sekilmenu()
        elif secim == "10":
            bmi.bmimenu()
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()