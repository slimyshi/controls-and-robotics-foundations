import control
from matplotlib import pyplot as plt 
import numpy as np 

def simulate_system(z,w):
    sys = control.tf([w**2], [1, 2*z*w, w**2])
    print(f'\nsimulating with zeta={z}and Wn={w}')
    print('sys')

    t, y =control.step_response(sys)
    return t,y 

test_subjects = [0.2, 0.7, 1 , 2]
w= 5.0
for z in test_subjects:
    t, y = simulate_system(z=z, w=w)
    plt.plot(t, y , label = f'zeta = {z}')

plt.axhline(1.0, color='black', linestyle='--', label='Target')
plt.title(f"Step Response Comparison (Natural Freq = {w} rad/s)")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (meters)")
plt.grid(True)
plt.legend()
plt.show()