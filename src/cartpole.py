import numpy as np
import matplotlib.pyplot as plt

m = 1.0
mp = 0.1
l = 1.0
g = 9.81
dt = 0.01

a = np.array([
    [0, 1, 0, 0],
    [0, 0, (mp*g)/m, 0],
    [0, 0, 0, 1],
    [0, 0, ((m+mp)*g)/(m*l), 0]
])

b = np.array([
    [0],
    [1/m],
    [0],
    [1/(m*l)]
])

q = np.diag([1.0, 1.0, 100.0, 1.0])
r = np.array([[0.1]])

k, s, e = ct.lqr(a, b, q, r)
print(f"optimal gain matrix k: {k}")

# starting with the pendulum slightly tipped over (0.1 radians)
state = np.array([[0.0], [0.0], [0.1], [0.0]])
time = np.linspace(0, 5, 500)

hist_x = []
hist_theta = []

for t in time:
    u = -k @ state
    state_dot = a @ state + b @ u
    state = state + state_dot * dt
    
    hist_x.append(state[0, 0])
    hist_theta.append(state[2, 0])

plt.plot(time, hist_x, label="cart position")
plt.plot(time, hist_theta, label="pendulum angle")
plt.legend()
plt.grid(True)
plt.show()