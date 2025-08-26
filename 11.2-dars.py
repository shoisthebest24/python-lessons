"""yosh=int(input("Yoshingizni kiriting!\n>>>"))
if yosh<=4 or yosh>=65:
    price=0
elif 4<yosh<18:
    price=10000
elif 18<=yosh<65:
    price=20000
print(f"Muzeyga kirish uchun siz"dan {price} so'm "bo'ladi!")"""

"""mahsulotlar = ['olma', 'anor', 'shaftoli', 'nok', 'gilos', 'behi', 'uzum', 'qovun', 'tarvuz']
savat = []
bor = []
yoq = []

for s in range(5):
    savat.append(input(f"Savatga {s+1}-mahsulotni kiriting! -> "))

for sav in savat:
    if sav in mahsulotlar:
        bor.append(sav)
    else:
        yoq.append(sav)
    
print("Do'konimizda yo'q mahsulotlar:")
for y in yoq:
    print(y)"""
    
"""foyda = ["anvar", "laziz", "ali", "vali"]
log = str(input("Loginingizni kiriting -> "))
if log not in foyda:
    print(f"Xush kelibsiz {log}!")
else:
    print("BU login band!")"""

#Istalgan sonni [a:b] orliqda qanday songa qoldiqsiz bolinishi
a=int(input("Oraliqni boshini kiriting"))   
b=int(input("Oraliqni oxiririni kiriting"))   

son = int(input("Istalgan butun son kiriting!"))
for n in range(a,b+1):
    if son%n==0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi!")
