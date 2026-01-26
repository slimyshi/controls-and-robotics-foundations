import control
import numpy as np
import matplotlib.pyplot as plt

G = control.tf([1], [1, 0.5, 0])
#the transfer function 1/ s^2 + s/2 

print("System Model (G):")
print(G)

Kp_w = 1
Kp_s = 10

sys_w   = control.feedback(Kp_w * G, 1)
sys_s = control.feedback(Kp_s * G, 1)
t = np.linspace(0, 20, 1000)

t1, y1 = control.step_response(sys_w, t)
t2, y2 = control.step_response(sys_s, t)

plt.plot(t1, y1, label=f'Weak Driver (Kp={Kp_w})', color='blue')
plt.plot(t2, y2, label=f'Stromg Driver(Kp={Kp_s})', color = 'red')

plt.axhline(1.0, color='black', linestyle='--', label='Target Position')
plt.xlabel("Time (seconds)")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.show()