class avto(object):
    znamka = ""
    model = ""
    prevozeni_km = 0
    zadnji_servis = "1. 1. 2017"

    def __init__(self, znamka, model, prevozeni_km, zadnji_servis):
        self.znamka = znamka
        self.model = model
        self.prevozeni_km = prevozeni_km
        self.zadnji_servis = zadnji_servis


    def izpis(self):
        print "Znamka: %s \n Model: %s \n Prevozeni kilometri: %s \n Zadnji servis: %s" % (self.znamka,self.model,self.prevozeni_km, self.zadnji_servis)

