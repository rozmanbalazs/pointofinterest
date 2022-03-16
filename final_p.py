import random
import webbrowser

class Places:
    def __init__(self, név,  builddate, nyitás, magasság, hely):
        self.név = név
        self.builddate = builddate
        self.nyitás = nyitás
        self.magasság = magasság
        self.hely = hely

    def printinfo(self):
        print(f"A(z) {self.név}-(o)t {self.builddate}-ban kezdték el építeni és {self.nyitás}-ben nyitották meg látogatásra. A {self.magasság}-magasságú építmény {self.hely}-ban megtekinthető.")

    def printinfo_v2(self):
        print(f"A(z) {self.név}-(o)t {self.builddate}-ben építették eleinte mint reklámfogás, majd {self.nyitás}-ben megújították erősebb fémből stb. A {self.magasság}-magasságú, 107-méter hosszú  építmény {self.hely}-ben megtekinthető.")

    def printinfo_v3(self):
        print(f"A(z) {self.név}-(o)t {self.builddate}-körül építették, majd nyitott meg {self.nyitás}-ben. A {self.magasság}-magasságú építmény {self.hely}-ban megtekinthető.")

    def printinfo_v4(self):
        print(f"A(z) {self.név}-(e)t {self.builddate}-körül kezdték el építeni és {self.nyitás}-ra lett kész. Magasságáról {self.magasság}. {self.hely}-ban megtekinthető.")
    
    def printinfo_vers(self):
        print(f"A(z) {self.név}-(o)t {self.builddate}-körül építették és {self.nyitás} fele bővítették. Magassága: {self.magasság}. {self.hely}-ban megtekinthető.")

    def printinfo_buda(self):
        print(f"A(z) {self.név}-(a)t {self.builddate}-körül építették, majd a  {self.nyitás}-ban átalakították. Magassága kb.: {self.magasság}. {self.hely}-ban megtekinthető.")
    
    def printinfo_freedom(self):
        print(f"A(z) {self.név}-(o)t {self.builddate}-körül építették és {self.nyitás}-ban itt írták alá a függetlenségi nyilatkozatot. Magassága: {self.magasság}. {self.hely}-ban megtekinthető.")

    def printinfo_freedomszob(self):
        print(f"A(z) {self.név}-(o)t {self.builddate}-körül építették Franciaországban és {self.nyitás}-ben adták át az Amerikai Egyesült Államoknak. Magassága: {self.magasság}. {self.hely}-ban megtekinthető.")

    def printinfo_reich(self):
        print(f"A(z) {self.név}-(e)t {self.builddate}-ban kezdték építeni és {self.nyitás}-ben nyílt meg. Magassága: {self.magasság}. {self.hely}-ben megtekinthető.")

    def printinfo_obama(self):
        print(f"A(z) {self.név}-(e)t {self.builddate}-ben építették és {self.nyitás}-ben került adásra :D . Magassága: {self.magasság}. {self.hely}-ban megtekinthető.")

    def printinfo_el(self):
        print(f"A(z) {self.név}-(e)t {self.builddate}-ban kezdték építeni és {self.nyitás}-ben vették fel az UNESCO-ba. Magassága: {self.magasság}. {self.hely}-ben megtekinthető.")
    
    

eiffel = Places("Eiffel torony", "1887", "1889", "300m", "Párizs")
holly_sign = Places("Hollywood felirat", "1923", "1978", "108m", "Los-Angeles")
kolosszeum = Places("Kolosszeum", "72", "81", "48m", "Róma")
stoneshit = Places("Stonehenge", "Kr.e. 2500", "Kr.e. 2100", "## nincs pontos adat ##", "Anglia")
miakhalifa = Places("Burdzs Kalifa", "2004", "2010", "830m", "Egyesült Arab Emírségek")
piramis = Places("Chichen Itza", "500", "1988", "30m", "Mexikó")
versailles = Places("Versailles-i kastély", "1631", "1688", "12.5m", "Versailles")
budacastle = Places("Budai vár", "1300", "19.század", "40m", "Buda")
freedom = Places("Függetlenség Csarnok", "1753", "1776", "52m", "Philadelphia")
freedomszobor = Places("Szabadság-szobor", "1875", "1885", "93m", "New York")
rejszstick = Places("Reichstag", "1884", "1999", "47m", "Berlin")
obamasheesh = Places("Obama emlékmű", "2009", "2009", "60m", "Family Guy")

c_nevek = [eiffel,holly_sign,kolosszeum,stoneshit,miakhalifa,piramis,versailles,budacastle,freedom,freedomszobor,rejszstick,obamasheesh]
p_nevek = ["Eiffel torony","Hollywood felirat","Kolosszeum","Stonehenge","Burdzs Kalifa","El Castillo","Versailles-i kastély","Budai vár","Függetlenség Csarnok","Szabadság-szobor","Reichstag","Obama emlékmű"]
evszamok = [['1887','1889'],['1923','1978'],['72','81'],['2500','2100'],['2004','2010'],['500','1988'],['1631','1688'],['1300','1900'],['1753','1756'],['1875','1885'],['1884','1999'],['2009','2009']] 
onevek = []
calc = 0
adatok = dict()
    
def info_box():
    print("írd be a hely nevét vagy számát az ahhoz kapcsolódó információ lekéréséhez!\n")
    for x in range(0, len(p_nevek)):
        print(f"{x+1} - {p_nevek[x]}")

    print("\n")

    while True:
        try:
            if calc >= 1:
                q = input(" # ask again? (y/n) ")
                if q.upper() == "Y":
                    pass

                elif q.upper() == "N":
                    break

                else:
                    raise ValueError

            x = input("select > ")

            if x == "1" or x.upper() == p_nevek[0].upper():
                eiffel.printinfo()
                webbrowser.open("https://www.toureiffel.paris/en")
            
            elif x == "2" or x.upper() == p_nevek[1].upper():
                holly_sign.printinfo_v2()
                webbrowser.open("https://www.hollywoodsign.org/")
        
            elif x == "3" or x.upper() == p_nevek[2].upper():
                kolosszeum.printinfo_v3()
                webbrowser.open("https://parcocolosseo.it/en/visit/opening-times-and-tickets/")
                
            elif x == "4" or x.upper() == p_nevek[3].upper():
                stoneshit.printinfo_v4()
                webbrowser.open("https://www.english-heritage.org.uk/visit/places/stonehenge/")
        
            elif x == "5" or x.upper() == p_nevek[4].upper():
                miakhalifa.printinfo()
                webbrowser.open("https://www.burjkhalifa.ae/en/")
        
            elif x == "6" or x.upper() == p_nevek[5].upper():
                piramis.printinfo_el()
                webbrowser.open("https://www.chichenitza.com/")
        
            elif x == "7" or x.upper() == p_nevek[6].upper():
                versailles.printinfo_vers()
                webbrowser.open("https://en.chateauversailles.fr/")
        
            elif x == "8" or x.upper() == p_nevek[7].upper():
                budacastle.printinfo_buda()
                webbrowser.open("https://www.budavarikapu.hu/index.php/hu/budai-var/latogatas-a-varban")
        
            elif x == "9" or x.upper() == p_nevek[8].upper():
                freedom.printinfo_freedom()
                webbrowser.open("https://www.nps.gov/inde/planyourvisit/independencehall.htm")
        
            elif x == "10" or x.upper() == p_nevek[9].upper():
                freedomszobor.printinfo_freedomszob()
                webbrowser.open("https://www.nps.gov/stli/index.htm")
        
            elif x == "11" or x.upper() == p_nevek[10].upper():
                rejszstick.printinfo_reich()
                webbrowser.open("https://www.bundestag.de/en/visittheBundestag/dome/registration-245686")
        
            elif x == "12" or x.upper() == p_nevek[11].upper():
                obamasheesh.printinfo_obama()
                webbrowser.open("https://youtu.be/U9u3bFfCcXY")
            
            else:
                print("NO DATA FOUND")
            
            calc += 1
            
        except ValueError:
            print("### please answer y or n! ###")

def filewrite():
        for i in range(0,len(c_nevek)):
            adatok[i] =  c_nevek[i].név+': '+c_nevek[i].builddate+' ,'+c_nevek[i].nyitás+' ,'+c_nevek[i].magasság+' ,'+c_nevek[i].hely+'\n'
            
        #adatok fájlba való irása
        with open("celeb_adatok.txt", "w") as file:
            for i in range(0,len(c_nevek)):
                file.write(adatok[i])

def quizgame():
    lista = ['Milyen magas az Obama-emlékmű?','Mikor KEZDTÉK EL építeni a Burdzs Kalifát?','A StoneHenge mikor készült el (Kr.e)?','A Reichstag mikor került megnyitásra?',
                  'A Hollywood Táblának mi volt eredeti célja?','A Versailles-i kastély-t mikor bővítette az akkori uralkodó?','Hol épült eredetileg a Szabadságszobor, ami ma New Yorkban található?']

        #kérdésekre a válszok SORRENDBEN. pl: egyes kérdés?  hez az 1 tartozik
    valasz = ['60m','2004','2100','1999','Reklámfogás','1688','Franciaországban']

        #a while hoz változók
    s = 1
    talalat = 0
    y = None
    jo = 0


        #itt röviden az történik hogy kapsz 5 random kérdést amire válaszolni kell, és eldönti hogy jo e vagy sem.
        #ezentul kiirja a a helyes válaszok után kapott pontszámot a végén
    while True:
        while True:
            y = random.choice(lista)
        

            print('-------------%s. kérdésed-------------  \n-%s'.center(245)%(s,y))
            x = input('A kérdésre a válasz: ')

            for i in range(0,len(lista)):
                if lista[i] == y:
                    talalat = i

            if x.upper() == valasz[talalat].upper():
                    print('✓✓✓✓✓✓✓✓✓✓✓✓✓✓\n'.center(230))
                    jo = jo + 1
            else:
                    print('X X X X X X X X X X X X X X X X X \n'.center(241))

            valasz.remove(valasz[talalat])
            lista.remove(y)
            

        
            s = s +1
            if s == 6:
                    break
        if s == 6:
            print('\n')
            print('****** Helyes találatok száma: %s ******'.center(240)%jo)
            break
        
def datenum():
    y = input('Add meg az évszámot')

    for i in range(0,len(evszamok)):
        for x in range(0,len(evszamok[i])):
            if evszamok[i][x] == y:
                print(p_nevek[i])
                break
def onev():
    y = input('Add meg az évszámot')

    for i in range(0,len(p_nevek)):
        if onevek[i] == y:
            print(evszamok)

            
        
print('Válassz az alábbi opciók közül:\n1.Adatok fájlba való mentése\n2.Tudnivalók a nevezetességekről\n3.Kvíz indítása\n4.Évszám szerinti keresés')

while True:
    try:
        valasztas = int(input('válasz: '))
        
        if valasztas == 1:
            filewrite()
            break

        elif valasztas == 2:
            info_box()
            break

        elif valasztas == 3:
            quizgame()
            break
        elif valasztas == 4:
            datenum()
            break
        elif valasztas == 5:
            onev()
            break

        else:
            raise ValueError
        
    except ValueError:
        print("> hibás érték!")


    
