class celebek:
    def __init__(self,nev,kor,szhely):
        self.nev = nev
        self.kor = kor
        self.szhely = szhely


#celebek
jani = celebek('Szőke János','50','Budapest')
sanyi = celebek('Havas Sándor','35','Székesfehérvár')

#celebek nevei
c_nevek = [jani,sanyi]

#adatok összekotrása
adatok = dict()
for i in range(0,len(c_nevek)):
   adatok[i] =  c_nevek[i] .nev+': '+c_nevek[i].kor+' ,'+c_nevek[i].szhely+'\n'

#adatok fájlba való irása
file = open('celeb_adatok.txt','w')
for i in range(0,len(c_nevek)):
    file.write(adatok[i])
file.close()





