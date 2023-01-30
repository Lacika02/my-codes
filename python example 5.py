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

# ## Feladat 3 (2.5 pont)

# Olvassátok be a `covid_data.csv` nevű fájl tartalmát!
# A fájl 4 oszlopot tartalmaz.
# Az első a dátumot, a második és harmadik
# a világ covidos megbetegedések és a halálesetek napi számát tartalmazza 1 millió főre vetítve.
# A negyedik az eltelt napok számát a mérés kezdetétől számítva.
# - Olvasd be az adatokat, és mentsd el őket egy `array`-be! <span style="color:red">(0.5 p)</span>
# - Ábrázold két ábrán a dátum függvényében a fertőzés számokat és a haláleseteket is! <span style="color:red">(0.75 p)</span>
# - Illessz [Gauss-görbét](https://en.wikipedia.org/wiki/Gaussian_function) a fertőzési ráta 4 jól kivehető csúcsára, továbbá a nekik megfelelő halálozási csúcsokra is! Ábrázold 2 ábrán a 4-4 illesztett görbét, valamint a hozzájuk tartozó adatsort is!  <span style="color:red">(1 p)</span>
# - Az illesztett paraméterek alapján határozd meg, hogy hány nap telt a fertőzési és halálozási ráta maximumai között! <span style="color:red">(0.25 p)</span>
# 
# A `matplotlib` képes olyan `array`-ket és `list`-eket feldolgozni melyeknek elemei a `python` nyelv beépített dátumok feldolgozásához használt [datetime](https://docs.python.org/3/library/datetime.html) tipusúak. 
# A `datetime` modul [strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime) függvénye segítségedre lehet abban, hogy az adatsor első oszlopának elemit `str` típusból `datetime` típusúra konvertáld.

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import os, os.path
from datetime import datetime


# In[2]:


path='/v/courses/fiznum1.public/data/covid_data.csv' # elmentem a helyét a fáljnak path-ként


# In[3]:


ido=[]
beteg=[] # ezekbe a mapáákba mentem majd az adtaimat
halott=[]
eltelt=[]
with open(path) as f:
    sorok=f.readlines() # soronként nézem
    for i in sorok[0:]:
        beteg.append( float(i.split(",")[1]))  # ,-vel álvalasztva vannak az adataim, szóval aszerint hányadik adat, úgy rakom be mappába
        halott.append( float(i.split(",")[2]))
        eltelt.append( float(i.split(",")[3]))
        ido.append(datetime64((i.split(",")[0]))) # furcsa datetime parancs... amit véletlen sem neten találtam
 # print(halott) csodálkoztam a plotban miért ilyen pici a halott, de hát mert millió főre lett mondva
ido=array(ido)  # array-é aéalítom a listámat, hátha hasznos lesz
beteg=array(beteg)
halott=array(halott)
eltelt=array(eltelt)


# In[4]:


plot(ido,beteg) # plotolok a megadott adatok alapján
xlabel("dátum")
ylabel("esetszám millió főként")


# In[5]:


plot(ido,halott) # itt is
xlabel("dátum")
ylabel("esetszám millió főre")


# In[6]:


csucsido1=eltelt[200:400]
csucsido2=eltelt[385:500] # tippelek nagyjából hol vannak a csúcsok
csucsido3=eltelt[520:640]
csucsido4=eltelt[620:780]
csucsbeteg1=beteg[200:400]
csucsbeteg2=beteg[385:500]
csucsbeteg3=beteg[520:640]
csucsbeteg4=beteg[620:780]
csucshalott1=halott[200:400]
csucshalott2=halott[385:500]
csucshalott3=halott[520:640]
csucshalott4=halott[620:780]


# In[7]:


from scipy.optimize import curve_fit 
def fuggveny(x,a,b,c,d): # gauss képleét leírtam
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt,pcov=curve_fit(fuggveny, csucsido1,csucsbeteg1,p0=[63,350,0.016,31]) #a lentebb lévő plottal tippelgettem menniy legyen a p0
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido1,csucsbeteg1,linestyle='None',marker='o',label='mért adatok') #fittelek
plt.plot(csucsido1,fuggveny(csucsido1,popt[0],popt[1],popt[2],popt[3]),label='Illesztés')   
legend()
def fuggveny2(x,a,b,c,d): # négyszer csinálok mindent
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt12,pcov=curve_fit(fuggveny2, csucsido2,csucsbeteg2,p0=[65,460,0.03,40])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido2,csucsbeteg2,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido2,fuggveny2(csucsido2,popt12[0],popt12[1],popt12[2],popt12[3]),label='Illesztés')   
legend()
def fuggveny3(x,a,b,c,d):
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt13,pcov=curve_fit(fuggveny3, csucsido3,csucsbeteg3,p0=[55,570,0.3,31])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido3,csucsbeteg3,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido3,fuggveny3(csucsido3,popt13[0],popt13[1],popt13[2],popt13[3]),label='Illesztés')   
legend()
def fuggveny4(x,a,b,c,d):
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt14,pcov=curve_fit(fuggveny4, csucsido4,csucsbeteg4,p0=[388,728,0.045,45])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido4,csucsbeteg4,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido4,fuggveny4(csucsido4,popt14[0],popt14[1],popt14[2],popt14[3]),label='Illesztés')   
legend()


# labor miatt rengeteget fitteltem már, így lényegében csak kimásoltam onnan a template-met, és átírtam mit kell 

# In[8]:


plot(csucsido1,csucsbeteg1,label='adatok')
popt2=[63,350,0.016,31] #itt tesztelgettem
plot(csucsido1,fuggveny(csucsido1,popt2[0],popt2[1],popt2[2],popt2[3]))


# In[9]:


plot(csucsido2,csucsbeteg2,label='adatok')
popt2=[65,460,0.03,40]
plot(csucsido2,fuggveny(csucsido2,popt2[0],popt2[1],popt2[2],popt2[3]))


# In[23]:


plot(csucsido3,csucsbeteg3,label='adatok')
popt2=[53,570,0.03,31]
plot(csucsido3,fuggveny(csucsido3,popt2[0],popt2[1],popt2[2],popt2[3]))


# In[11]:


plot(csucsido4,csucsbeteg4,label='adatok')
popt2=[388,728,0.045,45]
plot(csucsido4,fuggveny(csucsido4,popt2[0],popt2[1],popt2[2],popt2[3]))


# In[12]:


plt.plot(csucsido1,fuggveny(csucsido1,popt[0],popt[1],popt[2],popt[3]),label='Illesztés',linewidth=10)   
plt.plot(csucsido2,fuggveny2(csucsido2,popt12[0],popt12[1],popt12[2],popt12[3]),label='Illesztés2',linewidth=10) 
plt.plot(csucsido3,fuggveny3(csucsido3,popt13[0],popt13[1],popt13[2],popt13[3]),label='Illesztés3',linewidth=10)   
plt.plot(csucsido4,fuggveny4(csucsido4,popt14[0],popt14[1],popt14[2],popt14[3]),label='Illesztés4',linewidth=10)   
plt.plot(eltelt,beteg,linestyle='None',marker='o',label='mért adatok')
legend()
xlabel('eltelt napok száma') # itt raktam egybe az egészet
ylabel('fertőzések száma')


# tudom hogy borzalmasan néz ki, de olyan jó az illesztésem, hogy annyira rásimul, hogy nem látszik, hogy létezik egyáltalán, ha vékonyabb a vonal. 

# In[13]:


def fuggvenyh(x,a,b,c,d):
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt2,pcov=curve_fit(fuggvenyh, csucsido1,csucshalott1,p0=[1,363,0.025,0.8])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok) # ugyanez, csak más adatra fittelek

plt.figure(figsize=(16,6))
plt.plot(csucsido1,csucshalott1,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido1,fuggvenyh(csucsido1,popt2[0],popt2[1],popt2[2],popt2[3]),label='Illesztés')   
legend()


# In[14]:


plot(csucsido1,csucshalott1,label='adatok')
popt2=[1,363,0.025,0.8]
plot(csucsido1,fuggvenyh(csucsido1,popt2[0],popt2[1],popt2[2],popt2[3]))


# In[15]:


def fuggvenyh2(x,a,b,c,d):
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt22,pcov=curve_fit(fuggvenyh2, csucsido2,csucshalott2,p0=[0.55,460,0.037,1.2])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido2,csucshalott2,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido2,fuggvenyh2(csucsido2,popt22[0],popt22[1],popt22[2],popt22[3]),label='Illesztés')   
legend()


# In[16]:


plot(csucsido2,csucshalott2,label='adatok')
popt22=[0.55,460,0.037,1.2]
plot(csucsido2,fuggvenyh2(csucsido2,popt22[0],popt22[1],popt22[2],popt22[3]))


# In[17]:


def fuggvenyh3(x,a,b,c,d):
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt23,pcov=curve_fit(fuggvenyh3, csucsido3,csucshalott3,p0=[0.3,575,0.06,1])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido3,csucshalott3,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido3,fuggvenyh3(csucsido3,popt23[0],popt23[1],popt23[2],popt23[3]),label='Illesztés')   
legend()


# In[18]:


plot(csucsido3,csucshalott3,label='adatok')
popt23=[0.3,575,0.06,1]
plot(csucsido3,fuggvenyh3(csucsido3,popt23[0],popt23[1],popt23[2],popt23[3]))


# In[19]:


def fuggvenyh4(x,a,b,c,d):
    return a*np.exp(-(((x-b)**2)/2*c**2))+d

popt24,pcov=curve_fit(fuggvenyh4, csucsido4,csucshalott4,p0=[0.44,746,0.06,0.9])
gyok=sqrt(diag(pcov))
print('az illesztés paraméterei:  ',popt,'\Az ilessztés paramétereinek hibái: ', gyok)

plt.figure(figsize=(16,6))
plt.plot(csucsido4,csucshalott4,linestyle='None',marker='o',label='mért adatok')
plt.plot(csucsido4,fuggvenyh4(csucsido4,popt24[0],popt24[1],popt24[2],popt24[3]),label='Illesztés')   
legend()


# In[20]:


plot(csucsido4,csucshalott4,label='adatok')
popt24=[0.44,746,0.06,0.9]
plot(csucsido4,fuggvenyh4(csucsido4,popt24[0],popt24[1],popt24[2],popt24[3]))


# In[21]:


plt.plot(csucsido1,fuggvenyh(csucsido1,popt2[0],popt2[1],popt2[2],popt2[3]),label='Illesztés',linewidth=5)   
plt.plot(csucsido2,fuggvenyh2(csucsido2,popt22[0],popt22[1],popt22[2],popt22[3]),label='Illesztés2',linewidth=10) 
plt.plot(csucsido3,fuggvenyh3(csucsido3,popt23[0],popt23[1],popt23[2],popt23[3]),label='Illesztés3',linewidth=10)   
plt.plot(csucsido4,fuggvenyh4(csucsido4,popt24[0],popt24[1],popt24[2],popt24[3]),label='Illesztés4',linewidth=10)   
plt.plot(eltelt,halott,linestyle='None',marker='o',label='mért adatok')
legend()
xlabel('eltelt napok száma')
ylabel('halálozások száma')


# az illesztés paraméterei:   5.55289468e+01 3.28673224e+02 2.21060377e-02 2.94815298e+01\Az ilessztés paramétereinek hibái:  1.20594580e+00 6.83264377e-01 6.42368233e-04 1.19025376e+00
# az illesztés paraméterei:   5.68478107e+01 4.55518553e+02 4.78366277e-02 4.75538516e+01 \Az ilessztés paramétereinek hibái:  0.62806885 0.19609696 0.00072316 0.5418634 
# az illesztés paraméterei:   3.43945436e+01 5.70591588e+02 4.30125514e-02 5.04048406e+01 \Az ilessztés paramétereinek hibái: 0.56503234 0.27965399 0.00098645 0.55049613
# az illesztés paraméterei:   3.39211492e+02 7.32342504e+02 4.62896596e-02 6.40179212e+01\Az ilessztés paramétereinek hibái:  8.05084849e+00 5.26345884e-01 1.40944687e-03 4.74986365e+00
# 
# 
# az illesztés paraméterei:   1.01468380e+00 3.54253728e+02 2.30293367e-02 6.83080462e-01 \Az ilessztés paramétereinek hibái:  1.91607492e-02 9.50461565e-01 7.21687576e-04 1.56500392e-02
# az illesztés paraméterei:   5.36017409e-01 4.60831142e+02 5.26494263e-02 1.20427505e+00\Az ilessztés paramétereinek hibái:  0.01417477 0.47462767 0.00184699 0.01041327
# az illesztés paraméterei:   4.13172854e-01 5.70677114e+02 3.52501792e-02 8.49823193e-01 \Az ilessztés paramétereinek hibái:  0.01083875 0.34331917 0.0011363  0.01162263
# az illesztés paraméterei:   5.16765050e-01 7.44351196e+02 8.78830640e-02 8.82833858e-01]\Az ilessztés paramétereinek hibái:  0.01566114 0.38499873 0.00324902 0.00554051
# 
# a maximumok azok mindig a második paraméterek voltak. egyes csúcsnál ez 328 és 354 volt, ami 26 nap
# 2-es csúcs 455 és 460, 5 nap
# 3-as 570 , 570. ugyan azon a napon
# 4-es 732,744 12 nap
# 
# Ha nem arra gondolt hogy ugyanazon fertőzéshez mikor volt a  maximum halál, hanem a 4-4 maximukom közötti eltelt nap, akkor:
# 328-455-570-732-> 127 nap,115 nap és 162 nap
# 
# halálozásnál:354,460,570,744->106,110,162
