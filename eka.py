# Se ihan ensimmäinen hei maailma esimerkki

print("Hello World")

print("Ja tämän sovelluksen koodasi jakke Jäynä")

# ESIMERKKEJÄ MUUTTUJIEN KÄYTÖSTÄ
# ===============================

# YKSINKERTAINEN MUUTTUJA
# -----------------------


etunimi = "Jonne"
ika = 16
yhtoaineiden_keskiarvo = 2.5 # Liukuluku floating point number (foalt)
valmistunut = False # Totuusarvo boolean (bool)
print(etunimi, "sai keskiarvoksi YTO-aineista", yhtoaineiden_keskiarvo)
print(etunimi, "on valmistunut", valmistunut)

# RAKENTELLISET MUUTTUJAT
# -----------------------

nimilista = ["jonne", "jasmiina", "Aleksanteri"] # Lista list
print("Listassa ensimmäisenä on", nimilista[0]) # Indeksissä 0 oleva arvo
jasenia = len(nimilista) # Lista jässermäär selviää len-komennolla
print("nimilistassa on", jasenia, "henkilöä")
nimilista.sort() # järjestetään lista aakkosjärjestykseen
print("Aakkostettu lista on", nimilista)

ryhmat = ("Tivi24A", "Tivi23B", "Tivi20oa") # monikko tuple
print("Meidän ryhmä on", ryhmat[2]) 
# ryhmat[2] = "Tivi20ka" # Yksittäistä jäsentä ei voi muuttaa
ryhmat = ("Tivi24A", "Tivi23B", "Tivi20ka") # Koko monikko voi muuttaa
print("Meidän uusi ryhmä on", ryhmat[2])

joukko ={"Tuittu", "Assi", "Calle"} # Joukko set
print("Ja joukkoon kuuluvat", joukko) # Huomaa järjestys
# print(joukko[2]) ei toimi, koska jäseniä ei voi viitata indeksillä

# Sanakirja dictionary (dict)
henkilotiedot = {"etunimi": "Jonne", "sukunimi": "Janttari", "ika": 16} # Sanakirja dictionary

print("Opiskelijan", henkilotiedot["etunimi"],"ikä on", henkilotiedot["ika"])

opiskelija1 = {"etunimi": "Jonne", "sukunimi": "Janttari", "ika": 16}
opiskelija2 = {"etunimi": "Iina", "sukunimi": "Urpo", "ika": 17}
opiskelija3 = {"etunimi": "Tuittu", "sukunimi": "Kiukkunen", "ika": 27}

# Lista sanakirjoista -> Taulukko
opiskelijalista = [opiskelija1, opiskelija2, opiskelija3]
print("Opiskelijalista on", opiskelijalista)

uusi_opiskelija = {"etunimi": "Assi", "sukunimi": "Kalma", "ika": 65}

# Lisätään uusi arvo olevaan listaan
opiskelijalista.append(uusi_opiskelija)

# Tulostetaan opiskelijalistan ensimmäinen ja viimainen jäsen
print("Listassa ensimmäisenä on", opiskelijalista.pop(0))
print("Ja viimeisenä on", opiskelijalista.pop())




