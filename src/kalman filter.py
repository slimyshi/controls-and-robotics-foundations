import numpy as np
import control as ct
import matplotlib.pyplot as plt


dt = 0.01
m=1
d=0.1


A = np.array(
    [[1,dt],  #the top left is 1 this time because we dont want it to forget the postion when multiplied with x state
     [0,1 - (d/m)*dt]])

B =  np.array([
    [0],
    [1/m]
])
#the h matrix is for 
H = np.array([[1,0]]) #because our ultrasonic sensor only measures position, not velocity

Q = np.diag([0.1,0.1]) #for processing noise 

R = np.array([[50.0]])  #our sensor is noisy


#creating "real" data
time =  np.arange(0 , 20, dt)

true_pos = 10 + 5*(np.sin(time))

noisy_sensor = true_pos +np.random.normal(0, 5.0, len(time))


P= np.identity(2) #uncertainity 

x_state = np.array(
    [[0],
     [0]]
)
history_predicted =[]



    #for prediction equations
for i ,t in enumerate(time):

    u = np.array([[0]])  #set to zero
    x_pred = A@x_state + B@u
    
    x_state=x_pred

    p_pred = A@P@(np.transpose(A)) + Q
    P = p_pred

    #for updating equation
   
    z=np.array([[noisy_sensor[i]]])

    k= P@(np.transpose(H))@(np.linalg.inv(H@p_pred@(np.transpose(H)) +R))
    xf = x_pred + k@(z- H@x_pred)
    pf = (np.eye(2) - k @ H) @ p_pred

    x_state= xf
    P = pf
    history_predicted.append(xf[0,0])

plt.plot(time , history_predicted , color = "r", label = "Kalman estimate path")
plt.plot(time , noisy_sensor,'o', alpha = 0.5, markersize = 1,  color="black",label = 'noise' )
plt.plot(time , true_pos, color = "blue", label= "actual path")
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Position')
plt.title("Kalman Filter")
plt.legend()
plt.show()