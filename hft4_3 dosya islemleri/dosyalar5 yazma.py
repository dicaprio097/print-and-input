ds = open("rehber.txt","a")
ad = input("Adınızı girin:\t")
no = input("Numaranızını girin:\t")

ds.write(f"{ad|{no}}")