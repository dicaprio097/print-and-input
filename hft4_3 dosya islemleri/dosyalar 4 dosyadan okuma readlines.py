d = open("rehber.txt")
okunan = d.readlines()
#print(type(okunan)) #list türü veri döndürücü
for a in okunan:
    #print(a)
    #print(type(a))
    b = a.split("|")
    #print(tpye(b))
    print(f"Adı:\t{b[0]}, \tNumarası:\t{int(b[1])}")