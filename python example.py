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

# ## Feladat 1 (2.5 pont)

# **A feladat megoldása során ne használjunk `for` ciklust és segédlistákat, hanem kizárólag a `pandas` és `numpy` modulok beépített függvényeit és algoritmusait.**
# 
# 1. Olvassuk be a `pandas` csomag segítségével a `data/country_data.json` fájlt egyetlen sorban.  <span style="color:red">(0.5 p)</span>
# 
# A fájl különböző országokra tartalmazza a várható életkor értékét évben, a teljes populációt, a populáció-sűrűséget ($1/\mathrm{km}^2$ egységben) és az évi átlagos hőmérsékletet °C-ban. A beolvasott adattáblában az országok neve mint a tábla indexe, a többi adat pedig mint oszlopok jelenjenek meg.
# 
# 2. Számoljuk ki az országok területét és tároljuk el az `area_calculated` oszlopban! A megfelelő függvény megírása után használjuk a `pandas` DataFrame objektumok `apply` metódusát!  <span style="color:red">(0.5 p)</span>
# 
# 
# 3. Olvassuk be a `pandas` csomag segítségével a `data/country-by-surface-area.json` fájlt egyetlen sorban. <span style="color:red">(0.25 p)</span>
# 
# 
# A fájl különböző országok esetében tartalmazza az adott ország területét $\mathrm{km}^2$ egységekben.
# 
# 4. Készítsünk egy harmadik adattáblát az előző két tábla összefésülésével: az első adattábla minden sorához írjuk hozzá a második adattábla `area` oszlopában található adatot azzal a feltétellel, hogy az első tábla indexei azonosak legyenek a második adattábla `country` oszlopában található értékekkel. (Az összefésült táblában csak azokra az országokra vonatkozó adatok szerepeljenek, amikre mindkét eredeti táblázatban található adat.)  <span style="color:red">(0.5 p)</span>
# 
# 
# 5. Szűrjük ki a táblából azokat a sorokat, ahol legalább egy oszlopban hiányzik az adat! Hány ország marad a megszűrt adattáblában? <span style="color:red">(0.25 p)</span>
# 
# 
# 6. Ellenőrizzük, hogy jól számoltuk-e fent az országok területeit! Ehhez ábrázoljuk az adattábla `area` és `area_calculated` oszlopait egymás függvényében olyan pontokkal, melyeknek a színét az adott ország populáció-sűrűségének logaritmusával arányosan választjuk egy tetszőleges színskáláról! Rajzoljuk fel az $y=x$ egyenest is az ábrára! Mit tapasztalunk? (Az ábrán szerepeljenek tengelyfeliratok és a színek jelentése is.) <span style="color:red">(0.5 p)</span>
# 

# In[1]:


import pandas as pd
from pandas import DataFrame
get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


fajl1=pd.read_json("/v/courses/fiznum1.public/data/country_data.json") # beolvasom az adatokat


# In[3]:


fajl2=fajl1.T # mefordítom az oszlopokat a sorokkal
fajl2.head()


# In[4]:


fajl2['area_calculated'] =  fajl2.apply(lambda x: x.population/x.population_density if x.population and x.population_density >0 else nan ,axis=1)


# In[5]:


fajl2


# In[6]:


fajl3=pd.read_json("/v/courses/fiznum1.public/data/country-by-surface-area.json") # ezt is beolvasom


# In[7]:


fajl3


# In[8]:


mdf=fajl2.merge(fajl3,how='inner',      # összerakom a képlettel
             left_on=fajl2.index,
             right_on='country')
mdf.head()


# In[9]:


mdf


# In[10]:


mdf2=mdf.dropna() # kiszedem azt ahol valahol nincs adat


# In[15]:


ax=mdf2.plot("area","area_calculated","scatter",title="ország populáció sűrűség", colorbar=True)
xlabel("area")
# valamiért az x tengelyt nem nevezi el?? tudtommal a title után vesszővel odairom, hogy xlabel="area", de nem tetszik neki
# panda nem szereti az x tengelyt confirmed

ax.set_xlabel("Area")
ax.set_ylabel("Area_calculated")

show()


# In[ ]:





# In[ ]:




