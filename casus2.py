# --------------------------------------------------------------------------------------------------------
# Gebruiker kiest een categorie: A: Ford Fiesta, B: Ford Focus, C: Ford Puma, D: Ford Kuga
# Prijs per dag A: 55 euro, B: 70 euro, C: 80 euro, D: 90 euro. 
# Prijs per KM gereden: 0,18 euro 20 km gratis. C en D  hebben 50 km gratis.
# Dus cat B 2 dagen en 40 km is: 2*70+(40-20)*0,18.

# All-in pakket met verzekering: A en B + 25 euro per dag, C en D + 40 euro per dag. 
# 	+ 100 km gratis(Voor alle categorieën) in totaal(dus niet per dag)

# De gebruiker simuleert 3 autos: Zet de totaalprijzen in een lijst. Druk ze vervolgens regel per regel af met optie 1,2,3
# Vb Afdruk: Optie 1: x euro in totaal.
# --------------------------------------------------------------------------------------------------------

def wagen(categorie):
    if categorie=="A":
        prijs=55
    elif categorie=="B":
        prijs=70
    elif categorie=="C":
        prijs=80
    else:
        prijs=90
    return prijs


def km(aantal,categorie,all_in):
    if all_in=="N":
        if aantal<=20:
            prijs=0
        elif aantal>20 and (categorie=="A" or categorie=="B"):
            prijs=0.18*(aantal-20)
        elif aantal>50 and (categorie=="C" or categorie=="D"):
            prijs=0.18*(aantal-50)
    elif all_in=="Y":
        if aantal<=100:
            prijs=0
        else:
            prijs=0.18*(aantal-100)


    return prijs

def all_in(keuze,categorie):
    if keuze=="Y" and (categorie=="A" or categorie=="B"):
        prijs=25
    elif keuze=="Y" and (categorie=="C" or categorie=="D"):
        prijs=40
    else:
        prijs=0
    return prijs
     

for i in range(0,3):
    keuze_wagen= input("Kies een wagen: A (Ford Fietsa), B (Ford Focus), C (Ford Puma) of D (Ford Kuga): " )
    aantal_km=int(input("Geef het aantal kilometers: "))
    all_in_pakket=input("Wil je all-in pakket? (Y/N): ")

    prijs_wagen=wagen(keuze_wagen)
    prijs_km=km(aantal_km,keuze_wagen,all_in_pakket)
    prijs_all_in = all_in(all_in_pakket,keuze_wagen)
    print("huurprijs wagen: ",prijs_wagen)
    print("Prijs kilometers: ",prijs_km)
    print("Prijs all-in pakket: ",prijs_all_in)

# --------------------------------------------------------------------------------------------------------

