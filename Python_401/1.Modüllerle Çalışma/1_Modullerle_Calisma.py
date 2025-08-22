# -*- coding: utf-8 -*-

# builtin

# import benimModulum

# from benimModulum import topla
# print(topla(39,35))

from benimModulum import pi,daireCevreHesapla,daireAlanHesapla

print(pi)

#overwrite - üzerine yazmak
from math import pi

print(pi)

#overwrite - üzerine yazmak
pi = 3.14159
print(pi)

r = 5
print(daireAlanHesapla(r))
print(daireCevreHesapla(r))

#%%
print(__name__)
#from benimModulum import * 

import benimModulum as bm

#benimModulum.daireAlanHesapla()
bm.daireAlanHesapla(5)