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
