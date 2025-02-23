def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def sicaklikmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║           SICAKLIK ÇEVİRME             ║")
        print("║                                        ║")
        print("║         1-Celsius'tan Fahrenheit'a     ║")
        print("║         2-Fahrenheit'tan Celsius'a     ║")
        print("║         3-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            celsius = float(input("Celsius değerini girin: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C, {fahrenheit}°F'ye eşittir.")
        elif secim == "2":
            fahrenheit = float(input("Fahrenheit değerini girin: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F, {celsius}°C'ye eşittir.")
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    sicaklikmenu()