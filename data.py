import numpy as np
import pandas as pd
from sage import *

names = ["Mercure","Vénus","Terre","Mars","Jupyter","Saturne","Uranus","Neptune"]
planete = np.zeros((8,3))
planete[0] = np.array([1728*10e2,58*10e6,0])
planete[1] = np.array([1260*10e2,108*10e6,0])
planete[2] = np.array([1044*10e2,150*10e6,0])
planete[3] = np.array([864*10e2,228*10e6,0])
planete[4] = np.array([468*10e2,778*10e6,0])
planete[5] = np.array([360*10e2,1427*10e6,0])
planete[6] = np.array([252*10e2,2870*10e6,0])
planete[7] = np.array([180*10e2,4497*10e6,0])

for i in range(8):
    planete[i,2] = 1000*planete[i,0]/planete[i,1]

espace=pd.DataFrame(planete,index=names,columns=['Vitesse (km/h)','Rayon (km)','Vitesse angulaire (radian)'])

espace.style.format({"Vitesse (km/h)":"{:.3e}","Rayon (km)":"{:.3e}"})





namesL = ["Lune","Phobos","Deimos"]
lunes = np.zeros((3,4))
lunes[0] = np.array([2,3685,50*384*10e3,0]) ### MULTIPLIE RAYON LUNE X50
lunes[1] = np.array([3,7697,1000*9.4*10e3,0])
lunes[2] = np.array([3,4846,1000*23*10e3,0])

for i in range(3):
    lunes[i,3] = 10000*lunes[i,0]/lunes[i,1]  ###ATTENTION 

espaceL=pd.DataFrame(lunes,index=namesL,columns=['Indice Planète','Vitesse (km/h)','Rayon (km)','Vitesse angulaire (radian)'])

espaceL.style.format({"Vitesse (km/h)":"{:.3e}","Rayon (km)":"{:.3e}"})





namesE = ["Mercure","Vénus","Terre","Mars","Jupyter","Saturne","Uranus","Neptune"]
planete2 = np.zeros((8,5))
planete2[0] = np.array([1728*10e2,58*10e6,0,0.2056,0])
planete2[1] = np.array([1260*10e2,108*10e6,0,0.00678,0])
planete2[2] = np.array([1044*10e2,150*10e6,0,0.01671022,0])
planete2[3] = np.array([864*10e2,228*10e6,0,0.09339,0])
planete2[4] = np.array([468*10e2,778*10e6,0,0.04839,0])
planete2[5] = np.array([360*10e2,1427*10e6,0,0.0539,0])
planete2[6] = np.array([252*10e2,2870*10e6,0,0.04726,0])
planete2[7] = np.array([180*10e2,4497*10e6,0,0.00859,0])

for i in range(8):
    planete2[i,2] = 1000*planete2[i,0]/planete2[i,1]
    planete2[i,4] = planete2[i,1]*np.sqrt(1-planete2[i,3]**2)

espaceE=pd.DataFrame(planete2,index=namesE,columns=['Vitesse (km/h)','Demi-GA (km)','Angle de départ (radian)','Excentricité','Demi-PA (km)'])

espace.style.format({"Vitesse (km/h)":"{:.3e}","Demi-GA (km)":"{:.3e}","Demi-PA (km)":"{:.3e}"})



nameGeo = ["Lune","Mercure","Venus","Soleil","Mars","Jupiter","Saturne"]
geo = np.zeros((7,4))

geo[0] = np.array([1728*10e2,35,0,0])
geo[1] = np.array([1260*10e2,45,0,6])
geo[2] = np.array([1044*10e2,66,0,9])
geo[3] = np.array([864*10e2,95,0,0])
geo[4] = np.array([468*10e2,120,0,10])
geo[5] = np.array([360*10e2,140,0,10])
geo[6] = np.array([252*10e2,160,0,10])
             
for i in range(7):
    geo[i,1] *= 11000
    geo[i,2] = geo[i,0]/geo[i,1]
    geo[i,3] = geo[i,3] * 70000/6

espaceGeo=pd.DataFrame(geo,index=nameGeo,columns=['Vitesse (km/h)','Rayon (km)','Vitesse angulaire (radian)','Rayon interne'])


namesPG = ["Mercure","Venus","Mars","Jupiter","Saturne"]
geoP = np.zeros((5,4))
geoP[0] = np.array([1,3685,0,geo[1,3]])
geoP[1] = np.array([2,7697,0,geo[2,3]])
geoP[2] = np.array([4,8192,0,geo[4,3]])
geoP[3] = np.array([5,10896,0,geo[5,3]])
geoP[4] = np.array([6,11987,0,geo[6,3]])

for i in range(5):
    geoP[i,2] = 100*geoP[i,1]/geoP[i,3]  ###ATTENTION 

espaceGeoP=pd.DataFrame(geoP,index=namesPG,columns=['Indice Planète','Vitesse (km/h)','Vitesse angulaire (radian)','Rayon'])  
             
             
             




