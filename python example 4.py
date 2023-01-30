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

# ## Feladat 2 (2.5 pont)

# - Írj egy python függvényt, ami megvalósítja a következő függvényt (ahol $n$ egy pozitív egész szám, a függvény bemeneti változója): <span style="color:red">(0.5p)</span> $$ f(n) = \begin{cases} \frac{n}{2} & \text{ha} \ n \ \text{páros}\\ 3 n + 1 & \text{ha} \ n \ \text{páratlan}\end{cases}$$
# 
# - Írj egy python függvényt, aminek a bemenete egy pozitív egész szám $a_0$ és a kimenete egy lista, ami tartalmazza a következő sorozatot $a_k = f^k(a_0)$. A függvény addig iteráljon, amíg a sorazat el nem éri az 1-et. Például ha a bemenet $a_0 = 6$, akkor a függvény kimenete [6, 3, 10, 5, 16, 8, 4, 2, 1]. Figyelj arra, hogy a függvény ne léphessen végtelen ciklusba! Adj meg egy nagy számot, például 1000000-et, aminél a függvény nem iterálhat többet. Megjegyzés: $f^k$ az $f$ függvény $k$-szor önmagával vett kompozícióját jelöli. Például: $f^3(a_0) = f(f(f(a_0)))$. <span style="color:red">(0.5p)</span>
# 
# - Futtasd le a fentebb definiált függvényt az $a_0 = 1, 2, 3, \cdots, 10000$ számokra! Mit tapasztalsz? Van-e olyan szám, amire a függvény által generált sorozat nem éri el az 1-et? <span style="color:red">(0.5p)</span>
# 
# - Ábrázold $a_0$ függvényében a megállási időt ($a_0 = 1, 2, 3, \cdots, 10000$)! A megállasi idő $T$, az az egész szám, ahány iteráció szükséges hogy a sorazat elérje az 1-et, azaz $1 = f^T(a_0)$. Ábrázoláskor az adatpontok ne legyenek összekötve! <span style="color:red">(0.5p)</span>
# 
# - Mi volt a leghosszabb megállási idő, és melyik kezdeti értékhez tartozik? <span style="color:red">(0.5p)</span>
# 

# In[1]:


def f(n):   # definiálom a függvényt
    if n%2==0: # megnézem páros-e
        n=n/2 # ha az, akkor osztom 2-vel
    else :
        n=(3*n)+1 # ha nem, akkor megszorzom 3-al majd hozzáadok 1-et
    return(n) # térjen vissza az értékkel


# In[2]:


def ellenörző(n): 
    sorozat=[]  # létrehozok egy üres listát
    sorozat.append(n)  # első elemem legyen az, amit megadok
    for i in range(0,1000000):  # nagyon sokszor megnézem majd *
        if f(sorozat[i])!=1: # ha a megadott számomra hattatom a legelső kódom, és nem egy
            sorozat.append(f(sorozat[i])) # akkor  hozzáadom a sorozatomhoz
            if len(sorozat)==1000000: # * de csak max ennyi darabszor
                return(sorozat)  # ha elértem a limitszámot akkor térjek vissza az eddigi eredményemmel
        else:
            sorozat.append(1)  # amint a hattatásommal elérem az egyet, hozzáadom az 1-es számot
            return(sorozat)  # és vissza is térek a sorozatommal, a returnel megszakítom
        
    


# In[3]:


for d in range(1,10000):# csinálok egy változót ami 1-től 10000-ig fut
    print(ellenörző(d)) # ki is printelem. azt vettem észre, hogy mindig eléri az 1-et


# In[4]:


def T(n): # létrehozok egy változót
    megállási=[] # kell egy lista
    for d in range(1,n+1): #egytől tizezerig akarom csinálni       
        megállási.append(len((ellenörző(d)))) # hozzáadom a listához a d-edig lista karakterhosszát(hány számból érte el)
    return(megállási) # meg is nézetem


# In[5]:


hossz=T(10000) #létrehozok egy változóz, ami a 10000-ig tartalmazza listaként a függvény értékeit
eddigilegmagasabb=1  # egy változó ami az eddigi legmagasabbak tárolja
for i in range(0,10000):
    éppeni=hossz[i]
    if éppeni > eddigilegmagasabb: # ha az új vizsgált szám nagyobb
        eddigilegmagasabb=éppeni # akkor kicserélem arra a legelső változómat
    
print(eddigilegmagasabb-1)  # meg is nézem mi az


# In[6]:


T(d).index(262)+1 # mivel 0-val kezdődik az indexelés, ezért -1,ik szám lesz az, mint amit kiír


# In[ ]:




