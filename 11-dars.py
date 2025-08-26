
menu = ["manti", "osh", "somsa", "xonim"]
sok = ["olma", "anor", "nok"]
narh=0
taom = str(input("Nima taom buyurtma berasiz?\n>>>"))
non=str(input("Non buyurtma berasizmi?\n>>>"))
salat=str(input("Salat buyurtma berasizmi?\n>>>"))
sharbat=str(input("Qanday sharbat aytasiz?\n>>>"))
if taom.lower() in menu:
    print(f"{taom.title()}: 15000")
    narh=narh+15000
else:
    print("Siz buyurtma bergan taom mavjud emas ekan!")
    print(menu)
    taom=str(input("Nima buyurtma berasiz?\n>>>"))
    if taom.lower() in menu:
        print(f"{taom.title()}: 15000")
        narh=narh+15000
if non.lower()=="ha":
    print("Non: 5000")
    narh=narh+5000
if salat.lower()=="ha":
    print("Salat: 7000")
    narh=narh+7000
if sharbat.lower() in sok:
    print(f"{sharbat.title()} Sharbati: 12000")
    narh=narh+12000
else:
    print("Siz buyurtma bergan sharbat mavjud emas ekan!")
    print(sok)
    sharbat=str(input("Qanday sharbat aytasiz?\n>>>"))
    if sharbat.lower() in sok:
        print(f"{sharbat.title()} sharbati: 12000")
        narh=narh+12000
print(f"Sizdan jami: {narh} so\'m")