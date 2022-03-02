class Helyek:
    def __init__(self, név ,builddate , nyitás , magasság , hely ):
        self . név  =  név
        self . builddate  =  builddate
        self . nyitás  =  nyitás
        self . magasság  =  magasság
        self . hely  =  hely


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

#adatok összekotrása
adatok = dict()
for i in range(0,len(c_nevek)):
   adatok[i] =  c_nevek[i] .név+': '+c_nevek[i].builddate+' ,'+c_nevek[i].nyitás+' ,'+c_nevek[i].magasság+' ,'+c_nevek[i].hely+'\n'

#adatok fájlba való irása
file = open('celeb_adatok.txt','w')
for i in range(0,len(c_nevek)):
    file.write(adatok[i])
file.close()





