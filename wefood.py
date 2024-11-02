import numpy as np

print("ITS OMORIN TIME")
chars_det = [('nem','S15'),('ded', int),('i omor','S15')]
demchars = [('snuuy',1,'yes'),('auby',1,'yes'),('pizzaMARII',2,'i mar')]
so = np.array(demchars, dtype=chars_det)  
print(so)
print('hipressurewashingmachine')
print(np.sort(so, order='ded'))
print(so.dtype)
print(so.shape)
son = so.reshape(3,1)
for i in so:
    print(i)
sonon = so
argh = np.concatenate((so,sonon))
y = np.random.randint(2147483647)
print(y)