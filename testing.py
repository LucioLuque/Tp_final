import numpy as np

lista_final=np.array([1,1,1,1,1,1,1,1])
empty_composition=np.zeros(8)
print(len(empty_composition))
note=np.array([3,4])
e=4
s=2
empty_composition[s:e]=note
print(empty_composition)

x=sum([lista_final, empty_composition])
print(x)




"""
l1=empty_composition[0:s]
print(l1)
l2=empty_composition[s:e]
l3=empty_composition[e:]
l=sum(l2, note)
print(l)
f=np.append(l1, l)
f=np.append(f, l3)
print(f)
"""