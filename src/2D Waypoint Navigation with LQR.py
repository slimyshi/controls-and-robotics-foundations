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
    [0,0],
    [0,0],
    [1/m, 0],
    [0, 1/m]
]
)
 

target = np.array([
    [5], 
    [10],
    [0],
    [0]#both vel 0 for hovering
])

x_state =np.array([
    [0],
    [0],
    [0],
    [0]   
])




#x and y state then x and y vel
q = np.diag([100 , 10, 1 , 1 ]) #x is given more importance 

r = np.diag([0.1, 0.1]) #to discourage motor usage to save battery (not much becuase small value)

K, S, E = ct.lqr(A, B,  q, r)

time = np.linspace(0, 10, 1000)

history_pos_x = []
history_pos_y = []

for t in time :
    error =  x_state - target
    u = -K @ error

    x_dot = A @ x_state + B @ u
    x_state = x_state + x_dot * dt

    history_pos_x.append(x_state[0, 0])
    history_pos_y.append(x_state[1, 0])

plt.plot(history_pos_x, history_pos_y, label="Flight Path", color="blue")
plt.plot(target[0, 0], target[1, 0], 'rx', markersize=10, label="Target (5,10)")
plt.grid(True)
plt.legend()
plt.title("2D Waypoint Navigation with LQR")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()