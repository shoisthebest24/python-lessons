#cars = ["bmw", "audi", "ferrari", "tesla", "bugatti", "volvo"]
#print(sorted(cars))
#print(len(cars))

"""toq sonlar yigindisi n gacha
n=int(input("Chegarani oxirini kiriting!\n>>>"))
sonlar = list(range(1,n,2))
print("Hamma toq sonlar: " + str(sonlar))
min_q = min(sonlar)
max_q = max(sonlar)
summa = sum(sonlar)
print(min_q)
print(max_q)
print(summa)"""

"""dav = ["Rossiya", "Belgiya", "Portugaliya", "Uzbekistan"]
print(sorted(dav, reverse=True))
dav.reverse()
dav.sort()
print(dav)"""

#sonlar = list(range(120,1202,2))
#print(sonlar)
#print("Royxat uzunligi " + str(len(sonlar)))
#print(max(sonlar)-min(sonlar))
#print("Summa " + str(sum(sonlar)))
#print(sonlar[-20:])

taomlar = []
taomlar.append("manti")
taomlar.append("somsa")
taomlar.append("osh")
taomlar.append("tuxum")
taomlar.append("mastava")

nonushta = taomlar[:]
nonushta.remove("osh")
nonushta.remove("somsa")
nonushta.remove("manti")
nonushta.append("klab")
nonushta.insert(1, "baliq")

print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)
print(type(nonushta))

nonushta = list(nonushta)
nonushta[0]="qaymoq"

