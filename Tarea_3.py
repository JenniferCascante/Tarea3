#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Tarea 3     Jennifer Cascante Peraza B51626
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import mpl_toolkits.mplot3d as mpl
from scipy import stats
import matplotlib.pyplot as plt
from pylab import linspace, plot
import scipy.stats


dxy = pd.read_csv("xy.csv",header=0,index_col=0)
dxyp = pd.read_csv("xyp.csv",header=0)

#print(dxy)
#print(dxyp)

#PUNTO 1
#vector de filas,tamaño
xs=np.linspace(5,15,11)
#vector de columnas,tamaño
ys=np.linspace(5,25,21)

filas=np.sum(dxy,axis=1)
#print(filas)
columnas=np.sum(dxy,axis=0)
#print(columnas)
#Se procede a graficarlas para definir el mejor ajuste
plt.plot(xs, filas)

plt.title('Curva de  datos filas')
plt.show()

plt.plot(ys,columnas)
plt.title('Curva de datos columnas')
plt.show()

#las gráficas, anteriores generan una distribuación similar a la Gaussiana.

def gaussiana(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

#Ajuste
paramX,_=curve_fit(gaussiana,xs,filas)
print('Ajuste para filas',paramX)

paramY,_=curve_fit(gaussiana,ys,columnas)
print('Ajuste para columnas', paramY)


# In[14]:


#PUNTO 3:

#Correlación
#asignación de los datos desde el archivo
X = dxyp["x"]
Y= dxyp["y"]
P= dxyp["p"]
correlacion=0;

n=231;
for i in range(n):
    correlacion= correlacion + X[i]*Y[i]*P[i];
    
print('La correlación es:', correlacion)

#Covarianza 
#Apartir de los valores de mu, con los valores de la curva con mejor ajuste
mu_x=9.90484381 
mu_y=15.0794609
covarianza= correlacion-(mu_x*mu_y)

print('La covarianza es:', covarianza)

#Coeficiente de covarianza
#Apartir de los valores de sigma, con los valores de la curva con mejor ajuste
sigma_x=3.29944288
sigma_y=6.02693775

coeficiente=covarianza/(sigma_x*2*sigma_y*2)
print('El coeficiente de covarianza es:', coeficiente)


# In[24]:


#PUNTO 4:
#Para este punto se utilizaron paquetes ya esteblecidos para graficar, y como todo es apartir de valores conocidos 
#o calculados, resulta bastante simple.
#Note que las curvas 2D sin el ajuste están en el punto 1, ya que son las utilizadas para identificar.

# 2D
plt.plot(xs,gaussiana(xs,paramX[0],paramX[1]));
plt.xlabel('X');
plt.ylabel('fx');
plt.title('Mejor curva de ajuste de  datos filas')
plt.show()

plt.plot(ys,gaussiana(ys,paramY[0],paramY[1]));
plt.xlabel('Y');
plt.ylabel('fy');
plt.title('Mejor curva de ajuste de datos columna')
plt.show()

#  3D

ax = plt.axes(projection='3d')


ax.plot_trisurf(X, Y, P, cmap='twilight_shifted')

ax.set_title('Curva 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y ')
ax.set_zlabel('Z ')




# In[ ]:




