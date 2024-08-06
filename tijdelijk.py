Prijzen = {
"Aardbei" : "3",
"Vanille" : "4",
"Chocolade" : "5",
}
Aanbieding = int("3")* 0.8
Reclame_tekst = (f"Vandaag in de aanbieding: Aardbei-ijs, 1 liter - slechts €{Aanbieding}")
Reclame_tekst2 = Reclame_tekst[:62]
Reclame_tekst3 = (Reclame_tekst2.upper())
Reclame_tekst4 = (Reclame_tekst3.split(" "))
for e1 in Reclame_tekst4:
    if len(e1)<5: print(e1.lower())
    if len(e1)>4: print(e1.upper())
