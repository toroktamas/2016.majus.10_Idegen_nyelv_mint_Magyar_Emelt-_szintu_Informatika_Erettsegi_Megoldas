#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""2016.majus.10 Idegen nyelv mit magyar emelt szintu erettsegi megoldas python nyelven."""
import random
#print("1. feladat")
"""Be kell olvasni a ajto.txt fajlt.A"mit en egy szotarba csinalnek ami igy nezne ki.
zar={
    "hanyadik":probalkozas
}
"""
zar={}
n=0
with open("ajto.txt", "rt", encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "")
        n+=1
        zar[n] = sor
#print(zar)

print("2. feladat")
"""Be kell kerni a felhasznalotol egy szamsorozatot."""
szamsorozat = str(input("Adja meg, mi nyitja a zarat! "))

print("3. feladat")
"""Meg kell jeleniteni hogy melyik kiserletben hasznaltak ugyanazt a szamot mint a bekert."""
print("A nyito kodok sorai: {}".format(" ".join([str(k) for k,v in zar.items() if v == szamsorozat])))

print("4. feladat")
"""Meg kell adni melyik az a probalkozas ami ismetlodo karaktereket tartalmaz."""
volt=False
for k, v in zar.items():
    n = len(v)
    j = len(set(v))
    if n != j:
        print("Az elso ismetlodest tartalmazo probalkozas sorszama: {}".format(k))
        volt=True
        break
if volt == False:
    print("Nem volt ismatlodo szamjegy.")

print("5. feladat")
"""Elo kell allitani egy velatlenszeru ismetles nelkuli ugyanolyan hosszu kodot mint a bekert."""
kod = []
#a = random.choice("0123456789")
while len(kod) < len(szamsorozat):
    a=random.choice("0123456789")
    kod.append(a)
print("Egy {0} hosszu kodszam: {1}".format(len(kod), "".join(kod)))

#print("6. feladat")
"""Fugveny iras."""
def nyit(jo, proba):
    egyezik = False
    if len(jo) == len(proba):
        egyezik = True
    if egyezik == True:
        elteres=ord(jo[1])-ord(proba[1])
        for i in range(2, len(jo)):
            if elteres-ord(jo[i])-ord(proba[i]) and ord(jo[i])%ord(proba[i])==0:
                egyezik=False        
    
    return egyezik

#print("7. feladat")
"""Meg kell alkotni a siker.txt allomanyt."""
with open("siker.txt", "wt", encoding="utf-8") as g:
    for k,v in zar.items():
        if len(szamsorozat) != len(v):
            g.write("{0} hibas hossz\n".format(v))
        elif v == szamsorozat:
            g.write("{} sikeres\n".format(v))
        elif nyit(szamsorozat, v) == False:
            g.write("{0} hibas kodszam\n".format(v))
        else:
            g.write("{} sikeres\n".format(v))