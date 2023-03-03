# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:24:20 2022

@author: diosimarcardoza
"""
## oil field volumetrics

import pandas  as pd
import numpy as  np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import griddata
from volumetrics.volumetrics import get_contours, compute_area, trapezoid, pyramidal, simpson


welldat =  pd.read_csv("Data/volumetric_data.csv")


##boxplots de  las variables de interes 
# h = espesor del yacimiento
#depth = profundidad del yacimiento
#poro = porosidad
#sw = saturacion de  agua
columns = ['depth', 'h', 'poro', 'sw']

fig, ax = plt.subplots(2, 2, figsize=(15, 10))
for col, subplot in zip(columns, ax.flatten()):
    sns.boxplot(x= welldat[col], ax=subplot)

descriptivas = welldat.describe()



x, y, z, h, poro, sw = welldat.x, welldat.y, welldat.depth, welldat.h, welldat.poro, welldat.sw

# conocido factor de volumen de formación de petróleo, bbl/STB
#STB = barrir de tanque en almacenamiento
Bo = 1.435 # in RB/STB

#### grafico de superfiecie del yacimiento 

# define the z values for plotting
z_ = np.array([[z, h],
               [poro, sw]])


# grid x and y coordinate data
xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)
x_i, y_i = np.meshgrid(xi, yi)


# define subplots and colormap
figs, ax = plt.subplots(nrows=2, ncols=2, figsize=(12,10))


# define each subplot title
title = np.array([['Mapa Profundidad ', 'Mapa de Espesor'],
                  ['Mapa Porosidad', 'Mapa Saturacion de agua']])


for i in range(2):
  for j in range(2):
    zi = griddata((x,y), z_[i,j], (x_i,y_i), method='cubic')
    levels = np.linspace(min(z_[i,j])-0.1, max(z_[i,j])+0.1, 10)
    ax[i,j].contourf(x_i, y_i, zi, levels=levels, cmap='rainbow')  
    ax[i,j].plot(x, y, 'ko', ms=3) # plot the well points
    ax[i,j].set_title(title[i,j], pad=10, size=15)
    
##### calculo de cantidad petrolio original (OIP) por unidad de área de cada pozo individual

N = h * poro * (1 - sw) / Bo
N = N * (1 / 5.61458) # convert the result from ft3/ft2 to standard STB/ft2
df = pd.DataFrame({"well_id": welldat.well_id, "N (STB/ft2)": N})
df = pd.merge(welldat, df, on='well_id')


# define z value for plotting as: N (OIP per area)
z = N 
# grid N data with cubic interpolation method
zi = griddata((x,y),z,(x_i,y_i),method='cubic')


levels = np.arange(0, 1.1, 0.1)


# mapa de origen de petroleo en el lugar (OIP) por area
plt.figure(figsize=(10, 10))
figs = plt.contour(x_i, y_i, zi, levels=levels, colors=['0.25', '0.5', '0.25', '0.5', '0.25'], linewidths=[1.0, 0.5, 1, 0.5, 1])
plt.contourf(x_i,y_i,zi,levels=levels, cmap="rainbow")
plt.plot(x, y, 'ko', ms=3) # plot the well points
plt.clabel(figs, figs.levels[::2], inline=1, fontsize=10) # give labels for contours
plt.title("Mapa de contorno OIP", pad=10, size=20)
plt.colorbar()
plt.show()


# get the individual contour lines and plot
contour_all = get_contours(figs, x_i, y_i, plot='No')
contour_area = compute_area(contour_all)


areas = pd.DataFrame({"OIP Contour(STB)": levels, "Area(ft2)": contour_area})
areas


oip_trapezo = trapezoid(contour_area, 0.1)
oip_pyramidal = pyramidal(contour_area, 0.1)
oip_simpson = simpson(contour_area, 0.1)


print("Oil in Place using Trapezoidal Method:", np.round((oip_trapezo / 1E+06), 3), "million STB")
print("Oil in Place using Pyramidal Method:", np.round((oip_pyramidal / 1E+06), 3), "million STB")
print("Oil in Place using Simpson 1/3 Method:", np.round((oip_simpson / 1E+06), 3), "million STB")
##############################################################################
#_________________ simulacion_____________________#

def elicitacion(val_min, val_max, confianza,n ):
    theta_inicial =  (val_min + val_max)/2
    var_inicial = alpha_confianza*((val_min - theta_inicial)**2)
    w =  theta_inicial/(1-theta_inicial)
    b =( w -( ((w+1)**2)*var_inicial)) / ( ( (w**3) + 3*(w**2) +3*w + 1)*var_inicial)
    a = w*b
    nums = []
      
    for i in range(n):
        temp = random.betavariate(a, b)
        nums.append(temp)
    return nums    
    
sim_poro = elicitacion(min(poro), max(poro), 0.05,100)
sim_sw = elicitacion(min(sw), max(sw), 0.05,100)

intervalo_inicial = [min(poro), max(poro)]
theta_inicial =(intervalo_inicial[0] + intervalo_inicial[1])/2
alpha_confianza = 0.05
var_inicial = alpha_confianza*((intervalo_inicial[0]-theta_inicial)**2)
w =  theta_inicial/(1-theta_inicial)
b =( w -( ((w+1)**2)*var_inicial)) / ( ( (w**3) + 3*(w**2) +3*w + 1)*var_inicial)
a = w*b

from scipy.stats import beta
beta_dist = beta(a, b)
x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
fp = beta.pdf(x, a, b) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución Beta')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

import random
'''
# store the random numbers in a 
# list
nums = []
  
for i in range(10):
    temp = random.betavariate(a, b)
    nums.append(temp)
      
# plotting a graph
plt.plot(nums)
plt.show()
'''
plt.plot(elicitacion(min(poro), max(poro), 0.05,10))
plt.show()