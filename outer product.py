# -*- coding: utf-8 -*-
"""numpy exercises

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12gp3y-CmIEJiHrtWqp6xiBNVJCycUUlh
"""

import numpy as np
#Outer product

def outer_product(vec1, vec2):
  result=np.zeros((len(vec1), len(vec2)))
  for j in range(0,len(vec1)):
    for i in range(0, len(vec2)):
      result[j][i]=vec1[j]*vec2[i]
  return result

#height of matrix given by v1
#width of matrix given by v2

#Example
vec1=np.array([1,-2,0], dtype=int)
vec2=np.array([2,-2,3,-6], dtype=int)
print(outer_product(vec1, vec2))