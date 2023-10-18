# ----------------------------------------------------------------------------------------------------
# Looptijden:
# Geef het aantal deelnemers in.
# Geef de looptijd in minuten in.
# Sla alle tijden op in een lijst
# Geef de 3 snelste tijden.
# Geef de gemiddelde tijd.
# ----------------------------------------------------------------------------------------------------

aantal=int(input("Geeft het aantal deelnemers in: "))
lijst=[]
for i in range(0,aantal):
    looptijd=int(input("Geeft de looptijd in minuten: "))
    lijst.append(looptijd)
lijst.sort()
lijst.reverse()

for k in lijst[:3]:
    print(k) 


som_looptijd = 0
gemiddelde = 0
for j in lijst:
    som_looptijd += j
gemiddelde = som_looptijd/aantal
print(gemiddelde)

# ----------------------------------------------------------------------------------------------------