class Places:
    def __init__(self, name,  builddate, opening, height, place):
        self.name = name
        self.builddate = builddate
        self.opening = opening
        self.height = height
        self.place = place

    def printinfo(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-ban kezdték el építeni és {self.opening}-ben nyitották meg látogatásra. A {self.height}-magasságú építmény {self.place}-ban megtekinthető.")

    def printinfo_v2(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-ben építették eleinte mint reklámfogás, majd {self.opening}-ben megújították erősebb fémből stb. A {self.height}-magasságú, 107-méter hosszú  építmény {self.place}-ben megtekinthető.")

    def printinfo_v3(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-körül építették, majd nyitott meg {self.opening}-ben. A {self.height}-magasságú építmény {self.place}-ban megtekinthető.")

    def printinfo_v4(self):
        print(f"A(z) {self.name}-(e)t {self.builddate}-körül kezdték el építeni és {self.opening}-ra lett kész. Magasságáról {self.height}. {self.place}-ban megtekinthető.")
    
    def printinfo_vers(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-körül építették és {self.opening} fele bővítették. Magassága: {self.height}. {self.place}-ban megtekinthető.")

    def printinfo_buda(self):
        print(f"A(z) {self.name}-(a)t {self.builddate}-körül építették, majd a  {self.opening}-ban átalakították. Magassága kb.: {self.height}. {self.place}-ban megtekinthető.")
    
    def printinfo_freedom(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-körül építették és {self.opening}-ban itt írták alá a függetlenségi nyilatkozatot. Magassága: {self.height}. {self.place}-ban megtekinthető.")

    def printinfo_freedomszob(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-körül építették Franciaországban és {self.opening}-ben adták át az Amerikai Egyesült Államoknak. Magassága: {self.height}. {self.place}-ban megtekinthető.")

    def printinfo_reich(self):
        print(f"A(z) {self.name}-(e)t {self.builddate}-ban kezdték építeni és {self.opening}-ben nyílt meg. Magassága: {self.height}. {self.place}-ben megtekinthető.")

    def printinfo_obama(self):
        print(f"A(z) {self.name}-(e)t {self.builddate}-ben építették és {self.opening}-ben került adásra :D . Magassága: {self.height}. {self.place}-ban megtekinthető.")

    def printinfo_el(self):
        print(f"A(z) {self.name}-(e)t {self.builddate}-ban kezdték építeni és {self.opening}-ben vették fel az UNESCO-ba. Magassága: {self.height}. {self.place}-ben megtekinthető.")
    
    

eiffel = Places("Eiffel torony", "1887", "1889", "300m", "Párizs")
holly_sign = Places("Hollywood felirat", "1923", "1978", "108m", "Los-Angeles")
kolosszeum = Places("Kolosszeum", "72", "81", "48m", "Róma")
stoneshit = Places("Stonehenge", "Kr.e. 2500", "Kr.e. 2100", "## nincs pontos adat ##", "Anglia")
miakhalifa = Places("Burdzs Kalifa", "2004", "2010", "830m", "Egyesült Arab Emírségek")
piramis = Places("El Castillo", "500", "1988", "30m", "Mexikó")
versailles = Places("Versailles-i kastély", "1631", "1688", "12.5m", "Versailles")
budacastle = Places("Budai vár", "1300", "19.század", "40m", "Buda")
freedom = Places("Függetlenség Csarnok", "1753", "1776", "52m", "Philadelphia")
freedomszobor = Places("Szabadság-szobor", "1875", "1885", "93m", "New York")
rejszstick = Places("Reichstag", "1884", "1999", "47m", "Berlin")
obamasheesh = Places("Obama emlékmű", "2009", "2009", "60m", "Family Guy")

c_nevek = ["Eiffel torony","Hollywood felirat","Kolosszeum","Stonehenge","Burdzs Kalifa","El Castillo","Versailles-i kastély","Budai vár","Függetlenség Csarnok","Szabadság-szobor","Reichstag","Obama emlékmű"]


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
        
