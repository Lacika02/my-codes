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

# ## Feladat 4 (2.5 pont)

# Határozzuk meg a következő alakzatok tömegközéppontjának koordinátáját!
# 
# ![](https://oroszl.web.elte.hu/tmp/egybe.png)
# 
# Az integrálást mindent esetben Descartes-koordinátarendszerben végezzük el, kettős integrálás segítségével. A határok megállapításában segítenek az ábrák! A tömegközéppont definíciója a következő:
# 
# $$\overline{x}=\frac{1}{M}\int \int x\cdot\varrho(x,y)\mathrm{d}x\mathrm{d}y, \qquad\overline{y}=\frac{1}{M}\int \int y\cdot\varrho(x,y)\mathrm{d}x\mathrm{d}y,$$
# ahol $M$ az alakzat tömege: $M=\int\int\varrho(x,y)\mathrm{d}x\mathrm{d}y$
# 
# - a) Egy félkör, melynek a sűrűsége pontról, pontra változik a következő összefüggés szerint: $\varrho(x,y) = xy+x^2$ <span style="color:red">(0.75p)</span>
# 
# - b) Az $y = x$ és az $y = x^2$ görbék által határolt alakzat melynek a sűrűsége a következő: $\varrho(x,y)=x^2+y$! <span style="color:red">(0.75p)</span>
# 
# - c) A 2 sugarú körből az ábrán látható módon kivágott alakzat melynek a sűrűsége a következő: $\varrho(x,y)=x^2+y^2$! <span style="color:red">(0.75p)</span>
# 
# 
# Ábrázoljuk a kijelölt tartományokat és a tömegközéppontokat! <span style="color:red">(0.25p)</span>

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
from scipy.integrate import *
def rho1(y,x): # egyszer kell az M
    return(x*y+x**2) # amit így kapok meg
M1=dblquad(rho1,-1,1,lambda x:0,lambda x:sqrt(1-x**2)) #integrálom is
print(M1)


# In[2]:


def rho1x(y,x): # az x koordináta
    return(x*y**2+x**2*y)
def rho1y(y,x): # y koordináta
    return x*y**2+x**2*y

x11=dblquad(rho1x,-1,1,lambda x:0,lambda x:sqrt(1-x**2)) # integrálom is őket, először, hogy milyen fv-t, első 2 paraméter
y11=dblquad(rho1y,-1,1,lambda x:0,lambda x:sqrt(1-x**2)) # második 2 paramétert az előző fv-ében kell megadnom, így
x12=x11[0]/0.39269908169863055 # megszorzom 1/M-el
y12=y11[0]/0.39269908169863055
print(x12,y12) # megnézem mik ezek


# In[3]:


x=linspace(-1,1,100) # ábrázolom 
y=sqrt(1-x**2) # a megadott adatok alapján
figsize(15,10)
plot(x,y,color='red') # szinezek és plotolok
plot(x12,y12,marker='o',color='blue')
xlabel('X tengely') # el is nevezem a tengelyeket
ylabel('y tengely')
title('A kör súlypontja')


# In[4]:


def rho2(y,x): # ugyanazt megcsinálom, csak másik megadot képlettel
    return x**2+y

def rho2x(y,x):  # az x-em más lesz most
    return x**3+x*y

def rho2y(y,x): # y-onom is
    return x**2*y+y**2


# In[15]:


M2=dblquad(rho2,0,1,lambda x:x**2, lambda x:x )# kiintegrálom mind a 3-at
y21=dblquad(rho2y,0,1,lambda x:x**2, lambda x: x) # ugyanúgy integrálok, mint az elsőnél, csak más adatokkal
x21=dblquad(rho2x,0,1,lambda x:x**2, lambda x:x)
y22=y21[0]/M2[0] # mostmár inkább nem kimásolom kézzel, hanem megadom így hogy 1/M, első eleme kell
x22=x21[0]/M2[0]


# In[16]:


x=linspace(0,1,100) # ugyanúgy plotolok, csak más értékek szerint
y1=x
y2=x**2
plot(x,y1,color='red')
plot(x,y2,color='blue')
plot(x22,y22,marker='o',color='purple')
xlabel('X tengely')
ylabel('y tengely')
title('A 2. ábra súlypontja')


# In[8]:


def rho3(y,x):  # ugyanazt megcsinálom, csak másik megadot képlettekkel
    return x**2+y**2
def rhox3(y,x):
    return x**3+x*y**2
def rhoy3(y,x):
    return x**2*y+y**3


# In[9]:


M3=dblquad(rho3,0,sqrt(2),lambda x:sqrt(2) ,lambda x: sqrt(4-x**2))  # ugyanúgy integrálok, mint az elsőnél, csak más adatokkal
x31=dblquad(rhox3,0,sqrt(2),lambda x: sqrt(2),lambda x: sqrt(4-x**2))
y31=dblquad(rhoy3,0,sqrt(2),lambda x: sqrt(2),lambda x: sqrt(4-x**2))
x32=x31[0]/M3[0] # gyakorlatilag ugyanazt csinálom, csak mindig mást helyettesítek be
y32=y31[0]/M3[0]


# In[10]:


x=linspace(0,sqrt(2),100) # más értékek szerint és más helyre plotolok, de ugyanúgy
y1=2
y2=sqrt(4-x**2)
plot(x,y2,color='red')
hlines(y=sqrt(2),xmin=0,xmax=sqrt(2),color='blue')
plot(x32,y32,marker='o',color='purple')
xlabel('X tengely')
ylabel('y tengely')
title('A 3. ábra súlypontja')


# In[ ]:





# In[ ]:




