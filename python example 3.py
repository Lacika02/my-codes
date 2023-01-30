#!/usr/bin/env python
# coding: utf-8

# # HF 2 (15 pont)
# 
# - Minden feladatot a feladatszámnak megfelelő számú megoldásnotebookban oldj meg. Az első feladatot az feladat01.ipynb notebookban és így tovább.
# - A megoldás tartalmazza a megoldandó feladat szövegét a megoldásnotebook első markdown cellájában!
# - **Kommentekkel**, illetve **markdown cellákkal** magyarázd, hogy éppen mit csinál az adott kódrészlet!
# - Magyarázat nélkül a beküldött feladatok csak fél feladatnak számítanak!
# - Az elkészített ábrák minden esetben rendelkezzenek ábrafeliratokkal (cím, tengelyfeliratok és  −  amennyiben indokolt  −  jelmagyarázat)! Amennyiben a beadott ábrákon nincsenek feliratok, az adott feladat automatikusan csak fél feladatnak számít!
# - A beadott notebookok Kernel -> Restart&Run All hatására a beadott formát reprodukálják! (Próbáld ki!)
# ---
# 

# # Adatfileok
# 
# **Figyelem** minden, a HF megoldásá során feldolgozandó, adatfilet a kurzushoz tartozó publikus mappában, azaz a `/v/courses/fiznum1.public/data` mappában találjátok!

# ## Feladat 2 (2.5 pont)

# Ebben a feladatban a `katyvasz` nevű mappában található, [fa struktúrát](https://hu.wikipedia.org/wiki/Fa_(adatszerkezet) )  fogjátok feldolgozni.
# A `katyvasz` minden mappájában legfeljebb 3 mappa található, és minden mappa neve egy egész szám 1, 2, ..., 32-ig.
# <br>
# 10 levél mappában (azaz olyan mappában amiből már nem nyílnak új mappák) található egy-egy file, mely egy numpy array-t tartalmaz. Ezek nevei szintén egész számok és kiterjesztésük `.npy`, azaz: "0.npy", "1.npy", .."9.npy".
# 
# - Számoljátok le, hogy hány levél mappája van katyvasznak! <span style="color:red">(1 p)</span>
# - Keressétek meg mind a 10 fájlt! <span style="color:red">(0.5 p)</span>
# - A fájlokban található `array`-okat fűzzétek össze egy `array`-é a fájlok neve szerint növekvő sorrendben! <span style="color:red">(0.5 p)</span>
# - Ábrázoljátok az így létrehozott `array`-t az [imshow](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.imshow.html) függvénnyel! Kivételesen ehhez az ábrához a tengelyfelirat elhagyható, ám az ábrát egy markdown cellában diszkutáld! <span style="color:red">(0.5 p)</span>
# 
# 
# A feladat megoldásához használd a `python` beépített [`os`](https://docs.python.org/3/library/os.html) moduljának függvényeit! Kiváltképp segítségedre lehet az [exists](https://docs.python.org/3/library/os.path.html) függvény!
# Az array-ek helyes összefűzésében hasznos lehet a [numpy](https://numpy.org/doc/stable/user/index.html#user) modul [concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html) függvénye.

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import os, os.path


# In[2]:


path= '/v/courses/fiznum1.public/data/katyvasz' # elmentem path náven a katyvasz elérési útvonalát


# In[3]:





# In[4]:


levelmappak=0 # eredetileg 0-nak adom meg
fajlok=[] # mappák, amikben elmentem majd adolgokat
fajlokhelye=[]
for dirpath, dirnames, filenames in os.walk(path): # végigmegyek minden lehetséges uton
    if len(dirnames)==0: # ha már nem tudok továbbmenni, ott egy fájl van, szóval hozzáadok egyet a levélmappához
        levelmappak+=1
    if len(filenames)==1: # hogyha ugye egy fájlnevem van ott, akkor ott van a mappa
        
        fajlokhelye.append(dirpath) # elmentem az útját
        fajlok.append(filenames) # és magát a fájl nevét is
for i in range(len(fajlok)):
    print(fajlokhelye[i],fajlok[i]) # megnézem hogy kell elérni a mappáimat, hogy majd tudjak velük dolgozni
      


    
print(levelmappak) # megnézem mennyi levélmappa van


# In[5]:


sorrend=[]
for j in range(0,len(fajlok)): # megnézem milyen sorrendben vannak a fáljaim
    szam=fajlok[j][0]
    sorrend.append(szam[0][0])
print(sorrend)


# In[6]:


print(fajlokhelye[sorrend.index('0')],"/0.npy") # megnézem a sorrba rakott fáljaim helyét
print(fajlokhelye[sorrend.index('1')],"/1.npy")
print(fajlokhelye[sorrend.index('2')],"/2.npy")
print(fajlokhelye[sorrend.index('3')],"/3.npy")
print(fajlokhelye[sorrend.index('4')],"/4.npy")
print(fajlokhelye[sorrend.index('5')],"/5.npy")
print(fajlokhelye[sorrend.index('6')],"/6.npy")
print(fajlokhelye[sorrend.index('7')],"/7.npy")
print(fajlokhelye[sorrend.index('8')],"/8.npy")
print(fajlokhelye[sorrend.index('9')],"/9.npy")


# In[35]:


egy='/v/courses/fiznum1.public/data/katyvasz/25/17/2/23/27/13/3/32/31/1/0.npy' # egy válotzóba rakom őket
ketto='/v/courses/fiznum1.public/data/katyvasz/25/17/2/19/11/13/3/8/29/12/1.npy'
harom='/v/courses/fiznum1.public/data/katyvasz/25/17/14/24/11/10/15/21/29/12/2.npy'
negy='/v/courses/fiznum1.public/data/katyvasz/6/30/14/19/27/4/26/32/31/1/3.npy'
ot='/v/courses/fiznum1.public/data/katyvasz/5/30/2/23/11/13/26/21/29/12/4.npy'
hat='/v/courses/fiznum1.public/data/katyvasz/6/28/14/19/16/10/26/32/31/1/5.npy'
het='/v/courses/fiznum1.public/data/katyvasz/25/17/20/24/16/13/15/21/31/9/6.npy'
nyolc='/v/courses/fiznum1.public/data/katyvasz/6/28/20/19/16/10/26/21/31/9/7.npy'
kilenc='/v/courses/fiznum1.public/data/katyvasz/6/17/14/19/27/10/26/8/29/1/8.npy'
tiz='/v/courses/fiznum1.public/data/katyvasz/5/30/2/23/27/4/15/21/29/9/9.npy'
file1=load(egy)
file2=load(ketto) # betöltöm az összes arrayt
file3=load(harom)
file4=load(negy)
file5=load(ot)
file6=load(hat)
file7=load(het)
file8=load(nyolc)
file9=load(kilenc)
file10=load(tiz)

osszes=np.concatenate((file1,file2,file3,file4,file5,file6,file7,file8,file9,file10)) # egyberakom a megadott parancsal
imshow(osszes) # megnézem mi lett akép


# never gonna give you up, never gonna let you down

# In[ ]:





# In[ ]:




