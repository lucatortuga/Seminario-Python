# coding: utf-8
```
Aprire consolle ipython e copiare codice
Esempio di grafico regressione lineare
```
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def f(x, g, i):
 return g*x + i 
 
x = np.arange(1.0, 11.0, 1.0)
y = np.array([1.0, 1.0, 4.0, 3.0, 6.0, 5.0, 8.0, 10.0, 9.0, 11.0])
gradient, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
plt.plot(x,y,'ro') #'ro' red marker rotondi
plt.plot(x, f(x, gradient, intercept), 'k-', linewidth=2)
