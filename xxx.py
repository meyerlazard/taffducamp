from numpy import numpy as np
a = input ('cf 1 :')
b = input ('cf 2 :')
c = input ('cf 3 :')
d = input ('cf 3 :')
cf_series = np.array([int(a),int(b),int(c),int(d)])
z = np.npv (rate = 0.05, values = cf_series )
print(z)
