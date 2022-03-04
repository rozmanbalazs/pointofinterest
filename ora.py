class Places:
    def __init__(self, name,  builddate, opening, height, place):
        self.name = name
        self.builddate = builddate
        self.opening = opening
        self.height = height
        self.place = place

    def printinfo(self):
        print(f"A(z) {self.name}-(o)t {self.builddate}-ben kezdték el építeni és {self.opening}-ben nyitották meg látogatásra, a {self.height}-magasságú építmény {self.place}-ban megtekinthető.")

eiffel = Places("Eiffel torony", "1887", "1889", "300m", "Párizs")
holly_sign = Places("Hollywood felirat", "1923", "1978", "108m", "Los-Angeles")
kolosszeum = Places("Kolosszeum", "72", "81", "48m", "Róma")
stoneshit = Places("Stonehenge", "Kr.e. 2500", "Kr.e. 2100", "## nincs pontos adat ##", "Anglia")
miakhalifa = Places("Burdzs Kalifa", "2004", "2010", "830m", "Egyesült Arab Emírségek")
piramis = Places("El Castillo", "500", "1988", "30m", "Mexikó")
versailles = Places("Versailles-i kastély", "1631", "1688", "12.5m", "Versailles")
budacastle = Places("Budai vár", "1300", "1400", "40m", "Buda")
freedom = Places("Függetlenség Csarnok", "1753", "1753", "52m", "Philadelphia")
freedomszobor = Places("Szabadság-szobor", "1875", "1886", "93m", "New York")
rejszstick = Places("Reichstag", "1884", "1999", "47m", "Berlin")
obamasheesh = Places("Obama emlékmű", "2009", "2009", "60m", "USA")

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
            eiffel.printinfo()
    
        elif x == "3" or x.upper() == c_nevek[2].upper():
            eiffel.printinfo()
    
        elif x == "4" or x.upper() == c_nevek[3].upper():
            eiffel.printinfo()
    
        elif x == "5" or x.upper() == c_nevek[4].upper():
            eiffel.printinfo()
    
        elif x == "6" or x.upper() == c_nevek[5].upper():
            eiffel.printinfo()
    
        elif x == "7" or x.upper() == c_nevek[6].upper():
            eiffel.printinfo()
    
        elif x == "8" or x.upper() == c_nevek[7].upper():
            eiffel.printinfo()
    
        elif x == "9" or x.upper() == c_nevek[8].upper():
            eiffel.printinfo()
    
        elif x == "10" or x.upper() == c_nevek[9].upper():
            eiffel.printinfo()
    
        elif x == "11" or x.upper() == c_nevek[10].upper():
            eiffel.printinfo()
    
        elif x == "12" or x.upper() == c_nevek[11].upper():
            eiffel.printinfo()
        
        else:
            print("NO DATA FOUND")
        
        calc += 1
        
    except ValueError:
        print("### please answer y or n! ###")
        
