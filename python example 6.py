#!/usr/bin/env python
# coding: utf-8

# # HF 1 (15 pont)
# 
# - Minden feladatot a feladatszámnak megfelelő számú megoldásnotebookban oldj meg. Az első feladatot az feladat01.ipynb notebookban és így tovább.
# - A megoldás tartalmazza a megoldandó feladat szövegét a megoldásnotebook első markdown cellájában!
# - **Kommentekkel**, illetve **markdown cellákkal** magyarázd, hogy éppen mit csinál az adott kódrészlet!
# - Magyarázat nélkül a beküldött feladatok csak fél feladatnak számítanak!
# - Az elkészített ábrák minden esetben rendelkezzenek ábrafeliratokkal (cím, tengelyfeliratok és  −  amennyiben indokolt  −  jelmagyarázat)! Amennyiben a beadott ábrákon nincsenek feliratok, az adott feladat automatikusan csak fél feladatnak számít!
# - A beadott notebookok Kernel -> Restart&Run All hatására a beadott formát reprodukálják! (Próbáld ki!)
# ---
# 

# ## Feladat 4 (2.5 pont)

# Ebben a feladatban a XX. század derekán népszerű televíziós vetélkedők egyik fajtájának statisztikus tulajdonságait fogjuk vizsgálni.
# A játék során a játékosnak három ajtó közül kell választania. Az egyik ajtó mögött valami fantasztikus nyeremény (például 42 kis piros polietilén pingponglabda) található, a másik két ajtó mögött pedig valami haszontalan tárgy (egy zsák marhatrágya). A játék során, miután a játékos rábökött egy ajtóra, a játékvezető kinyit egyet a három közül, mely egyrészt nem tartalmazza a nyereményt, másrészt nem az az ajtó, amelyiket a játékos kiválasztott. Ezután megkérdi a játékvezető a játékost, hogy meg szeretné-e változtatni a választását. Vajon melyik stratégia (változtat/nem változtat) a nyerő?
# - Írjunk egy python függvényt, mely egyenletes eloszlású véletlen számok segítségével leszimulálja egy vetélkedő menetét! 
# - A függvénynek egy bemenő paramétere legyen, aminek a neve `valtoztat`, ami egy Bool típusú változó. A függvény kimenő paramétere szintén egy Bool típusú változó legyen. <span style="color:red">(0.25p)</span>
# - A függvény kimenete `True` értéket vegyen fel, ha a játékos nyer, és `False` értéket, ha a játékos veszít. <span style="color:red">(0.75p)</span>
# - Az implementált függvény segítségével szimuláljunk le 10000/10000 játékot úgy, hogy a két különböző stratégiát választjuk. <span style="color:red">(1.0p)</span>
# - Készíts egy táblázatot arról, hogy melyik stratégia hány százalékos nyerési esélyt biztosított. <span style="color:red">(0.25p)</span>
# - Saját szavaiddal fogalmazd meg, melyik stratégia teljesít átlagosan jobban. <span style="color:red">(0.25p)</span>
# 
# A feladat megoldására hasznos lehet a `numpy` véletlen választásokat implementáló [rutinja](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html), illetve a python nyelvben natív [halmaz (set)](https://people.ubuntu.com/~kelemeng/.ufp3/native-datatypes.html#sets) változótípusa!
#  

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
def valtoztat(talan):  # létrehozom a fv-t
    ajtok=[1,2,3]    #megszámozom az ajtókat
    x=randint(1,4)  # a választott szám
    y=randint(1,4)  # a nyerő szám
    nemvalasztott=[] # mik a nem választott számok?
    for i in range(1,len(ajtok)+1): # végig megyek a számokon 
        if i!=x  and i!=y :  # ha aszám amit vizsgálok se a nyerő, se a választott szám,
            nemvalasztott.append(i) # akkor berakom a nem választottakba
    if len(nemvalasztott)>1: # ha több mint 1 db ilyenem van
        z=randint(0,len(nemvalasztott)) # akkor random számot generálok ami a lista tagszámával lehet max =
    else: 
        z=0 # de ha csak 1 tagu akkor a 0.-ik indexe kell
    nemvalasztott.pop(z)  # eldobok egy ajtót
    if x!=y: # ha nem a nyerőt választottam, akkor azt is hozzáadom a listához
        nemvalasztott.append(y)
    if len(nemvalasztott)>1: # tudom hogy az esetemben csak 1 tagu lehet a lista
        c=randint(0,len(nemvalasztott)) # de ha több tagu lenne is működjön a kódom
    else:
        c=0
    if talan:   # ha változtattam
        x=nemvalasztott[c]  #akkor az új választott tagot az eddigi nemválasztottból szedjem ki
    else:
        x=x  # ha nem akkor marad
    return(x==y)
            
    


# In[2]:


nyert=0   # csinálok egy változót azzal, hogy mennyiszer nyert
for i in range(0,10000):  # 10000-szer futattom le
    nyerte=valtoztat(True) #ha változtatott
    if nyerte==True:  # és ha nyerte
        nyert+=1 # akkor adjoon hozzá egyet a  nyerthez
print(nyert) # nézzük is meg mennyi lett
nemvaltoztatottnyert=0   # ugyanez a nem változtatotthoz
for i in range(0,10000):
    nyertem=valtoztat(False)
    if nyertem==True:
        nemvaltoztatottnyert+=1
print(nemvaltoztatottnyert)        


# |cserélt és nyert | nem cserélt és nyert|  
# |---|---|
# | kb.66%| kb.33% | 
# 

# ha cserélek ajtót miután egyel kevesebb van, amiről tudok hogy rossz volt, akkor nagyjából kétszer akkora esélyyel nyerek
