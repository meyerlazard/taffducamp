import numpy as np
a = input ('cf 1 :')
b = input ('cf 2 :')
c = input ('cf 3 :')
d = input ('cf 4 :')
cf_series = np.array([int(a),int(b),int(c),int(d)])
z = np.npv (rate = 0.05, values = cf_series )
y = np.irr (cf_series)
print("net present value =",round(z,2),"internal rate of return",round(y,5))
