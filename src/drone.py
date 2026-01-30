#the perfect human knows how to code a dromne to float and stay at exactly 10 meters 
import numpy as np
import matplotlib.pyplot as plt
import control 

target = 10.0
g = 9.81 #gravity
m = 1.0 #massdcc
dc = 0.1 #drag

dt= 0.01
tmax = 10 #the time limit
step = round(tmax/dt) 
time = np.linspace(0, tmax, step)


from pid import pidcontroller
d = pidcontroller(kp= 2 , kd = 4, ki = 0)
state = [0.0 , 0.0]
history = [] # the thing i will use to plot 

for t in time :
    error = target - state[1]  #target position - actual position
    force = d.update(error , dt) 

    acc = force/m - g - (dc*state[0])/m
    state[0] += acc*dt #updating velocity
    state[1] += state[0]*dt #updating position 
    #so here index 0 is velocity and 1 is position, and thats the opposite of what i did in the pid smthg , so dont get confused

    history.append(state[1]) #state[1] for position

    #will run for for "time" then stop 

plt.plot(time , history , color = 'red' )
plt.axhline(target, color='black', linestyle=':', label='Target')
plt.title('Drone with 10 meter target')
plt.xlabel('Time (s)')
plt.ylabel('Position')
plt.grid(True)
plt.legend()
plt.show()


#at first the value of dt was 0.1 and kd was 10 so the force was so high that it instantly had 10m and kp not being high enough , it started to drop until it found equilibrium at near 8 meters , then i changed dt to 0.01 to see the graph. 
#now after tweaking the values it peaks and drops and stays there but never reaches the target point , i will have to learn to implement the "i"