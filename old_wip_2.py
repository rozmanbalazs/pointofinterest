import random

class Helyek:
    def __init__(self, név ,builddate , nyitás , magasság , hely ):
        self . név  =  név
        self . builddate  =  builddate
        self . nyitás  =  nyitás
        self . magasság  =  magasság
        self . hely  =  hely

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
    
        


#helyek
eiffel  =  Helyek ( "Eiffel torony" , "1887" , "1889" , "300m" , "Párizs" )
holly_sign  =  Helyek ( "Hollywood felirat" , "1923" , "1978" , "108m" , "Los-Angeles" )
kolosszeum  =  Helyek ( "Kolosszeum" , "72" , "81" , "48m" , "Róma" )
stoneshit  =  Helyek ( "Stonehenge" , "Kr.e. 2500" , "Kr.e. 2100" , "## nincs pontos adat ##" , "Anglia" )
miakhalifa  =  Helyek ( "Burdzs Kalifa" , "2004" , "2010" , "830m" , "Egyesült Arab Emírségek" )
piramis  =  Helyek ( "El Castillo" , "500" , "1988" , "30m" , "Mexikó" )
versailles  =  Helyek ( "Versailles-i kastély" , "1631" , "1688" , "12.5m" , "Versailles" )
budacastle  =  Helyek( "Budai vár" , "1300" , "1400" , "40m" , "Buda" )
szabadság  =  Helyek ( "Függetlenség Csarnok" , "1753" , "1753" , "52m" , "Philadelphia" )
szabadságszobor  =  Helyek ( "Szabadság-szobor" , "1875" , "1886" , "93m" , "New York" )
rejszstick  =  Helyek ( "Reichstag" , "1884" , "1999" , "47m" , "Berlin" )
obamasheesh  =  Helyek ( "Obama emlékmű" , "2009" , "2009" , "60m" , "USA" )

#helyek nevei
c_nevek = [eiffel,holly_sign,kolosszeum,stoneshit,miakhalifa,piramis,
           versailles,budacastle,szabadság,szabadságszobor,rejszstick,obamasheesh]



print('Válassz az alábbi opciók közül:\n1.Adatok fájlba való mentése\n2.Tudnivalók a nevezetességekről\n3.Kvíz indítása')

valasztas = int(input('válasz: '))

while True:
    
    if valasztas == 1:
        
        #adatok összekotrása
        adatok = dict()
        for i in range(0,len(c_nevek)):
            adatok[i] =  c_nevek[i] .név+': '+c_nevek[i].builddate+' ,'+c_nevek[i].nyitás+' ,'+c_nevek[i].magasság+' ,'+c_nevek[i].hely+'\n'
            
        #adatok fájlba való irása
        file = open('celeb_adatok.txt','w')
        for i in range(0,len(c_nevek)):
            file.write(adatok[i])
        file.close()
        
    if valasztas == 2:
        print("írd be a hely nevét vagy számát az ahhoz kapcsolódó információ lekéréséhez!\n")
        for x in range(0, len(c_nevek)):
            print(f"{x+1} - {c_nevek[x]}")

        print("\n")
    
        calc = 0
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

                if x == "1" or x.upper() == c_nevek[0].upper():
                    eiffel.printinfo()
        
                elif x == "2" or x.upper() == c_nevek[1].upper():
                    holly_sign.printinfo_v2()
    
                elif x == "3" or x.upper() == c_nevek[2].upper():
                    kolosszeum.printinfo_v3()
    
                elif x == "4" or x.upper() == c_nevek[3].upper():
                    stoneshit.printinfo_v4()
    
                elif x == "5" or x.upper() == c_nevek[4].upper():
                    miakhalifa.printinfo()
    
                elif x == "6" or x.upper() == c_nevek[5].upper():
                    piramis.printinfo_el()
    
                elif x == "7" or x.upper() == c_nevek[6].upper():
                    versailles.printinfo_vers()
    
                elif x == "8" or x.upper() == c_nevek[7].upper():
                    budacastle.printinfo_buda()
    
                elif x == "9" or x.upper() == c_nevek[8].upper():
                    freedom.printinfo_freedom()
    
                elif x == "10" or x.upper() == c_nevek[9].upper():
                    freedomszobor.printinfo_freedomszob()
    
                elif x == "11" or x.upper() == c_nevek[10].upper():
                    rejszstick.printinfo_reich()
    
                elif x == "12" or x.upper() == c_nevek[11].upper():
                    obamasheesh.printinfo_obama()
        
                else:
                    print("NO DATA FOUND")
        
                calc += 1
        
            except ValueError:
                print("### please answer y or n! ###")



    if valasztas == 3:
        #kérések listája
        lista = ['egyes kérdés?','kettes kérdés?','hármas kérdés?','négyes kérdés?',
                  'ötös kérdés?','hatos kérdés?','hetes kérdés?','nyolcas kérdés?']

        #kérdésekre a válszok SORRENDBEN. pl: egyes kérdés?  hez az 1 tartozik
        valasz = ['1','2','3','4','5','6','7','8']

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

                if x == valasz[talalat]:
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
    break
