import numpy as np
import matplotlib.pyplot as plt
import control as ct

#4x4 matrices intead of 2x2 because 2d instead of 1d 

m =1 
dt = 0.01
d = 0.1

A = np.array([
    [0,0,1,0],
    [0,0,0,1],
    [0, 0, -d/m,0],
    [0,0,0,-d/m]
])

B = np.array([
    [0,0]
    [0,0],
    [1/m, 0]
    [0, 1/m]
]
)
 