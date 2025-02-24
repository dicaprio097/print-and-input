def bmi_hesapla():
    boy = float(input("Boyunuzu metre cinsinden girin (örneğin 1.75): "))
    kilo = float(input("Kilonuzu kilogram cinsinden girin (örneğin 70): "))

    bmi = kilo / (boy ** 2)
    print(f"Vücut Kitle İndeksiniz (BMI): {bmi:.2f}")

    if bmi < 18.5:
        print("Durum: Zayıf")
    elif 18.5 <= bmi < 24.9:
        print("Durum: Normal kilolu")
    elif 25 <= bmi < 29.9:
        print("Durum: Fazla kilolu")
    elif 30 <= bmi < 34.9:
        print("Durum: Obez (Sınıf 1)")
    elif 35 <= bmi < 39.9:
        print("Durum: Obez (Sınıf 2)")
    else:
        print("Durum: Aşırı obez (Sınıf 3)")

def bmimenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║            BMI HESAPLAMA               ║")
        print("║                                        ║")
        print("║         1-BMI Hesapla                  ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            bmi_hesapla()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    bmimenu()