# ----------------------------------------------------------------------------------------------------------
# Kies de vorm van het zwembad: vierkant, rechthoekig, ovaal.
# Kies het Materiaal: Staal of Hout.
# 	Prijs per m²: hout €100, staal €115.
# 	Hoogste standaard: 150 cm, elke centimeter erboven + 2 procent.
# 	Dus zwembad van 200 cm hoogte = basisprijs +50*2 %:
# 	bvb zwembad met 100m² hout van 160 cm hoog
# 		100*100=10000+ (160-150)=10*2% = 20% dus totaalprijs € 12000
# 	Graafwerken € 60 per m³ 10*10*1,6= 160*60 = € 9600
# 	Plaatsingskost:  <= 50 m³= €20 per m³
# 		  <=100m³ = €18 per m³
# 		>100m³ = € 15 per m³
# Druk de kostprijs van het zwembad, de graafkosten en plaatsingskosten en de totaalprijs van het project af. 
# ----------------------------------------------------------------------------------------------------------

import math

def opp(vorm):
    if vorm=="V":
        zijde=int(input("Geef de zijde op in m: "))
        return zijde**2
    elif vorm=="R":
        breedte=int(input("Geef breedte op in m: "))
        hoogte=int(input("Geef hoogte op in m: "))
        return breedte*hoogte
    else:
        straal=int(input("Geef straal op in cm: "))
        return math.pi*straal**2
    


vorm=input("Geef de vorm van het zwembad: V (vierkant, R (rechthoek) of R(rond): )")
materiaal=input("Geef het materiaal: S (staal) of H (hout): ")
hoogte=int(input("Geef de hoogte van het zwembad in cm: "))

oppervlakte=opp(vorm)
if materiaal=="H" and hoogte<=150:
    kostprijs=oppervlakte*100
elif materiaal=="S" and hoogte<=150:
    kostprijs=oppervlakte*115
elif materiaal=="H" and hoogte>150:
    kostprijs=oppervlakte*100 + (hoogte-150)*100*0.02
else:
    kostprijs=oppervlakte*115 + (hoogte-150)*100*0.02   

prijs_graafwerken=oppervlakte*hoogte/100*60


volume=oppervlakte*hoogte/100
prijs_graafwerken=volume*60

if volume<=50:
    plaatsingskost= volume*20
elif volume >=100:
    plaatsingskost= volume*18
else:
    plaatsingskost= volume*15

print("De kostprijs van het zwembad is ", kostprijs)
print("De prijs van het graafwerk is ",prijs_graafwerken)
print("De plaatsingskost is ", plaatsingskost)
print("De totale prijs is ",kostprijs+prijs_graafwerken+plaatsingskost)

# ----------------------------------------------------------------------------------------------------------






