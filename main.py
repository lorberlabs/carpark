from avto import avto

def menu():
    print "1. Dodaj avto"
    print "2. Izpisi avto"
    print "3. Izbrisi avto"
    print "4. Shrani avte"
    print "5. Preberi avte"
    print "6. Izhod"

    return int(raw_input())

def dodaj ():
    from avto import avto

    znamka = raw_input("Znamka: ")
    model = raw_input("Model: ")
    prevozeni_kilometri= raw_input(" Prevozeni kilometri: ")
    zadnji_servis = raw_input("Zadnji servis: ")

    avto = avto(znamka, model, prevozeni_kilometri, zadnji_servis)

    return avto

def izpis_avtov(avti_list):
    i = 0
    for avto in avti_list:
        print str(1) + "."
        avto.izpis()
        i += 1


def shrani (avti_list):
    file = open("avti.txt", " w+")

    for avto in avti_list:
        file.write(avto.model + ";")
        file.write(avto.znamka + ";")
        file.write(str(avto.prevozeni_km) + ";")
        file.write(avto.zadnji_servis + ";")

def preberi_avte():
    file = open("avti.text", "r+")
    temp_avti = []
    for line in file:
        a - line.split(";")
        av = avto(a[0], a[1], int(a[2]), a[3])
        temp_avti.append(av)
    return temp_avti


avti = []

while True:
    x = menu ()

    if x == 1:
        avto = dodaj ()
        avti.append(avto)

    if x == 2:
        for avto in avti:
         avto.izpis()

    if x == 3:
        izpis_avtov(avti)
        st_avta = int(raw_input(" Stevilka avta za izpis: "))
        avti.remove(avti[st_avta])


    if x == 4:
        shrani(avti)



    if x == 5:
       avti = preberi_avte()
       print avti

    if x == 6:
        break






