import numpy as np
import control as ct
import matplotlib.pyplot as plt


m = 1
d = 0.1
dt = 0.01

A= np.array(
    [[0,1],
     [0, -d/m]]
)

B= np.array(
    [[0],
     [1/m]]
)

# q penalize [X error, Y error, X velocity, Y velocity]
q = np.diag([10, 10, 1, 1])

r = np.array([[0.1, 0.1]]) #to discourage motor usage to save battery (not much becuase small value)



K, S, E = ct.lqr(A, B,  q, r)

print(f"LQR K Matrix: {K}")


x_state = np.array([
    [10.0],  # Initial Position
    [0.0]    # Initial Velocity
])
#started in the air at meters with zero velocity


time = np.linspace(0, 10, 1000)
history_pos = []
history_vel = []
history_force = []



for t in time:
    # optimal force: u = -Kx
    u = -K @ x_state
    
    #limit the force so its realistic (eg.this motor can only push between -20N and 20N)
    u = np.clip(u, -20.0, 20.0)
    
    # update: x_dot = Ax + Bu
    x_dot = A @ x_state + B @ u
    x_state = x_state + x_dot * dt
    
    # 3. Log data
    history_pos.append(x_state[0, 0])
    history_vel.append(x_state[1, 0])
    history_force.append(u[0, 0])



plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, history_pos, 'b', label="Position")
plt.axhline(0, color='k', linestyle='--')
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(time, history_vel, 'g', label="Velocity")
plt.axhline(0, color='k', linestyle='--')
plt.legend()
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(time, history_force, 'r', label="Motor Force (u)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()