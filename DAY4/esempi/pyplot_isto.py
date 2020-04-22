# coding: utf-8
``` 
Aprire consolle ipython e copiare codice
Esempio grafico istogramma
```
# %load /Users/luca/ownCloud/Seminario Python/DAY2/esempi/pyplot_esempio.py
import numpy as np
import scipy 
import matplotlib.pyplot as plt
import scipy.stats
q = scipy.stats.beta(5, 5) # genera una beta(5,5)
obs = q.rvs(2000) # produce 2000 osservazioni
plt.hist(obs, bins=40, normed=True) 
