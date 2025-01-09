# MUUTTUJAT MERKKIJONOISSA
# ========================

# Sanakirjat
henkilo1 = {"etunimi": "Tiina", "ika": 27}
henkilo2 = {"etunimi": "Jonne", "ika": 44}
henkilo3 = {"etunimi": "Iida", "ika": 7} 

# Perinteinen ratkaisu
print(henkilo1["etunimi"]+"n", "ikä on", henkilo1["ika"], "vuotta vanha")

# Sama muotoiltuna merkkijonona (f-string)

muotoiltu_merkkijono = f"{henkilo1['etunimi']}n ikä on {henkilo1['ika']} vuotta vanha"
print(muotoiltu_merkkijono)

