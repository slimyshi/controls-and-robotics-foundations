#no i :( only pd
import numpy as py
import control 
import matplotlib.pyplot as plt

dt = 0.01
tmax = 10
step = int(tmax/dt)
time = py.linspace(0, tmax, step)

#comparing p and pd controllers
state_p = [0.0, 0.0]             # state_pd[1] means VELOCITY and state[0] is POSITION
state_pd = [ 0.0, 0.0]

from pid import pidcontroller
pid_p = pidcontroller(kp= 10 , kd = 0.0 , ki = 0)
pid_pd = pidcontroller(kp = 10 , kd= 2.0 , ki = 0)

history_p = []
history_pd = []
target = 1.0

for t in time:
    #for pd system 
    error_pd = target - state_pd[0]  #the difference between target and actual position
    force_pd = pid_pd.update(error_pd , dt)


#calculating accelaration and 
    acl_pd = force_pd - 0.5 * state_pd[1]
    state_pd[1] += acl_pd * dt
    state_pd[0] += state_pd[1] * dt         # state_pd[1] means VELOCITY and state[0] is POSITION
    
    #now for p only system 

    error_p = target - state_p[0]
    force_p = pid_p.update(error_p , dt)

    acl_p = force_p - 0.5*(state_p[1])
    state_p[1] += acl_p * dt
    state_p[0] += state_p[1]*dt
#for plottinf
    history_p.append(state_p[0])    #for ploting the positions for both 
    history_pd.append(state_pd[0])


plt.figure(figsize=(10, 6))
plt.plot(time, history_p, label='Only P', color='red', linestyle='--')
plt.plot(time, history_pd, label='P + D (Controlled)', color='green', linewidth=2)
plt.axhline(target, color='black', linestyle=':', label='Target')
plt.title('Impact of Derivative (D) Gain')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid(True)
plt.legend()
plt.show()