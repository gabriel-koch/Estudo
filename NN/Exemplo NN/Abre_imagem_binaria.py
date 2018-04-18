# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""


import matplotlib.pyplot as plt
import numpy as np
a = ()

arquivo_binario =  open(r'data0', 'rb')
"""
data = arquivo_binario.read(1)
print(data)
"""

pixels = np.fromfile(arquivo_binario, dtype=np.uint8)
print(pixels)


i=0
j=1+i
prim_zero = pixels[i*784:(j(784)+1)]

#prim_zero = pixels[784:784*2+1]

print(prim_zero)

im = prim_zero.reshape(28,28)

#plt.gray()
plt.imshow(im, cmap='gray_r')

arquivo_binario.close()
