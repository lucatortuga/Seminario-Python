# coding: utf-8
```
 esempio di grafica di una sinusoide
```
import numpy as np
import scipy 
import matplotlib.pyplot as plt
t = np.arange(0.0, 1.0, 0.01) # crea un numpy array con val. da 0 a 1 step 0.01
s = scipy.sin(2*scipy.pi*t) # crea una sinusoidale
plt.ion() #attiva la modalità interattiva
plt.plot(t,s) # genera il grafico
plt.xlabel('time(s)') # aggiunge la labex x
plt.ylabel('Voltage(mV)') #aggiunge la label y
plt.grid(True) #abilita la griglia
