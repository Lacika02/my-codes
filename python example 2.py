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

# ## Feladat 2 (2.5 pont)

# Kétdimenziós kúpszeletek általános alakja a következő másodfokú kifejezés:
# 
# $$ Ax^2+Bxy+Cy^2+Dx+Ey+F=0. $$
# 
# A fenti kifejezés nem minden esetben ír le egy valós kúpszeletet, de az együtthatói segítségével ez egyértelműen eldönthető. Az együtthatókból képezhető egy mátrix, jelöljük $M$-mel:
# 
# $$\mathbf{M}=\begin{pmatrix}
# A & B/2 & D/2 \\
# B/2 & C & E/2 \\
# D/2 & E/2 & F 
# \end{pmatrix}.$$
# 
# A fenti mátrix segítségével megállapításokat tehetünk a fent definiált másodrendű kifejezésünkkel kapcsolatban.
# 
# - Ha $\mathbf{M}$ determinánsa nulla, abban az esetben a kúpszeletünk degenerált.
# 
# Ha a kúpszelet nem degenerált és az $\mathbf{M}$ mátrixból képezhető $\Delta = \begin{pmatrix}
# A & B/2  \\
# B/2 & C  \\ 
# \end{pmatrix}$ almátrix determinánsa
# 
# - negatív, akkor a kúpszelet egy hiperbola
# - nulla, akkor a kúpszelet egy parabola
# - pozitív, akkor a kúpszelet egy ellipszis (abban a speciális esetben, ha A=C és B=0, a kúpszelet kör).
# 
# Az ellipszis annyiban speciális, hogy további két kategóriára osztható. Ha a kúpszelet ellipszis és 
# 
# - ha $(A+C)\cdot\mathrm{det}(\mathbf{M})) < 0$ a kúpszelet valós.
# - ha $(A+C)\cdot\mathrm{det}(\mathbf{M})) > 0$ a kúpszelet képzetes.
# 
# A kúpszeleteket kanonikus alakjukra lehet hozni az általános helyett a következő transzformációva:
# 
# $$\frac{\tilde{x}^2(\lambda_1^2\lambda_2)}{S}+\frac{\tilde{y}^2(\lambda_1\lambda_2^2)}{S}=-1,$$
# ahol $S$ az M mátrix determinánsa, $\lambda_1$ és $\lambda_2$ a $\Delta$ mátrix két sajátértéke.
# 
# Ezen tudás birtokában írjunk egy olyan, `kupszelet` nevű függvényt ami bemeneti paraméterként várja az $A,B,C,D,E,F$ számokat (a sorrendre nem kell figyelni, feltehetjük, hogy az együtthatók a másodrendű kifejezés általános alakjának megfelelő sorrendjében érkeznek.), ezentúl rendelkezik egy `kep` nevű alapértelmezetten `False` értékű változóval is. 
# A függvény az alábbiak szerint viselkedjen:
# - Elsőként elvégzi a kúpszelet osztályozását.<span style="color:red">(1.0p)</span>
#   - Ha a kúpszelet degenerált, akkor a függvény visszatérési értéke egy `string` legyen a következő tartalommal: "A másodrendű kifejezésünk degenerált kúpszeletre vezet, ezért a továbbiakban nem foglalkozunk vele." majd lépjen ki a függvény.
#   - Ha nem degenerált, akkor döntse el, hogy hiperbola, ellipszis, vagy parabola-e és ha ellipszis, akkor valós vagy képzetes. 
#   - Ha imaginárius ellipszis, akkor a függvény visszatérési értéke legyen megint egy `string` ami erről tartalmaz információt.
# - Ha hiperbola vagy valós ellipszis, akkor végezze el a fent mutatott kanonikus transzformációt. Parabola esetén ne történjen kanonikus transzormáció! <span style="color:red">(0.5p)</span>
# - Ha a függvény `kep` bemeneti változójának értéke nem `False` hanem `True` akkor a függvény, amenyiben ábrázolható kúpszelet-et definiálnak az $A,B,C,D,E,F$ számok, készítsen egy ábrát is amely az eredeti kúpszeletet és az eltranszformált kúpszeletet (ha elkészült a transzformáció) ugyanabban a koordinátarendszerben ábrázolja. Parabola, vagy képzetes ellipszis esetén ne történjen se ábrázolás, se kanonikus transzformáció! <span style="color:red">(1.0p)</span>
# 
# Ügyeljetek arra, hogy ahol szükséges determinánst vagy sajátértéket számítani, azt a `numpy` beépített [det](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html) és [eigvalsh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html) parancsaival tegyétek, vagy nem kaptok pontot a házi feladatra. 
# 
# 
# 
# Próbáld ki a függvényedet a következő tesztrendszerekkel:
# 
# - $-3x^2+y+2=0$ (parabola)
# - $2x^2 + 3xy −4y^2 + 2x − 3y + 1 = 0 $ (hiperbola)
# - $−3x^2 + xy −2y^2 + 4 = 0$ (valós ellipszis)

# In[21]:


get_ipython().run_line_magic('pylab', 'inline')
def kupszelet(A,B,C,D,E,F,kep=False): #megadom a definíciót a leírtak szerint
    M=array([[A,B/2,D/2],[B/2,C,E/2,],[D/2,E/2,F]]) # megadottak alapján mátrixok csinálok belőle
    if det(M)==0: # ha a determinánsom 0, az nem fog tetszeni, ezért nem foglalkozok vele
        return("A másodrendű kifejezésünk degenerált kúpszeletre vezet, ezért a továbbiakban nem foglalkozunk vele.")
    else : # ha az almátrix determinánsa
        Delta=M[0:2,0:2] # ez az almátrixom
        if det(Delta)==0: # =0, akkor ez egy parabola, és ki is iratom
            return("Ez egy parabola.")
        elif det(Delta)<0 : # ha ez a determináns kisebb, mint 0
            L=eigvalsh(Delta) # akkor kiszámoltatom funkcióval a valós értékeit
            S=det(M) # képlet leírásának egyszerüsége miatt elnevezem a valós értékeket, és a determinánst is
            szam1=(L[0]**2*L[1])/S # egyik másik valósértékkel
            szam2=(L[0]*L[1]**2)/S # kiszámolom a képletet
            print(str(szam1)+"*x^2"+str(szam2)+"*y^2=-1") # kiprintelem ezt a képletet
            if kep: #ha a képem nem False(hanem true)
                x = np.linspace(-5, 5, 400) #-5-től 5-ig 400 pontban nézem meg mindkét tengelye
                y = np.linspace(-5, 5, 400)
                x, y = np.meshgrid(x, y) # x, és y szerint szeretném ábrázolni
                contour(x,y,A*x**2+B*x*y+C*y**2+D*x+E*y+F,[0],colors='r')# beirom a képletet, és pirosra szinezem
                contour(x,y,x**2*szam1+y**2*szam2,[-1],colors='k') # itt meg feketére
                axis("equal")   # ugyanolyan széles legyen mint magas az ábrám
                plt.xlabel("x tengely") # elnevezem a tengelyeket
                plt.ylabel("y tengely")
                print("Pirossal van a hiperbola, míg feketével a kanonikus alak")
            return("Ez egy hiperbola.") #visszatérek azzal, hogy ez egy hiperbola
        
        else:   
            if (A+C)*det(M)<0: #ha valós az elipszisem
                L=eigvalsh(Delta) # uyganúgy mint multkor nevezgettek ,számolok és ábrázolok
                S=det(M)
                szam1=(L[0]**2*L[1])/S
                szam2=(L[0]*L[1]**2)/S
                print(str(szam1)+"*x^2"+str(szam2)+"*y^2=-1")
                if kep:
                    x = np.linspace(-5, 5, 400)
                    y = np.linspace(-5, 5, 400) 
                    x, y = np.meshgrid(x, y)
                    contour(x,y,A*x**2+B*x*y+C*y**2+D*x+E*y+F,[0],colors='r')
                    contour(x,y,x**2*szam1+y**2*szam2,[-1],colors='k')
                    axis("equal")
                    plt.xlabel("x tengely")
                    plt.ylabel("y tengely")
                    print("Pirossal van az elipszis, míg feketével a kanonikus alak")
                return("Ez egy valós elipszis.")
            elif (A+C)*det(M)>0: # ha képzetes része is lenne, akkor csak kiiratom, hogy imaginárius, de ezen kívül hagyom.
                return("Ez egy imaginárius elipszis.")
    
        


# In[24]:


kupszelet(-3,0,0,0,1,2)
kupszelet(2,3,-4,2,-3,1,True) #kiprógálgatom a megadott mintákra


# In[25]:


kupszelet(-3,1,-2,0,0,4,True)


# In[22]:


kupszelet(1,0,1,0,0,-1,True) # itt egyben van a két eredmény, amit a szaggatott fekete piros vonal mutat.
# tudom hogy nem kellett, de én akartam egy kört ábrázolni, mert kiváncsi voltam hogy oldja meg


# In[ ]:




