import numpy as np
import matplotlib.pyplot as plt
import control as ct


# x_dot = Ax + Bu + w ,  where w is the outside physical disturbance

#z = Hx + v 



m = 1
d = 0.1
dt = 0.01


#----------------------------
#defining lqr matrices

A= np.array(
    [[0,1],
     [0, -d/m]]
)

B= np.array(
    [[0],
     [1/m]]
)

ql = np.array([
    [10,0],#position error weightage
    [0, 1] #velocity error weightage
])

rl = np.array([[0.1]]) #to discourage motor usage to save battery (not much becuase small value)



K, S, E = ct.lqr(A, B,  ql, rl) #solves the riccati equation to give k s and e 

print(f"LQR K Matrix: {K}") # k tell what is the optimal weightage for the system after you define the Q
print(f"Closed-loop Eigen value matrix:{E}") #magnitude of these numbers tells you the speed of the response

x_state = np.array([[0]
                    ,[0]])


A_d = np.array([[1, dt], [0, 1 - (d/m)*dt]]) 
B_d = np.array([[0], [(1/m) * dt]]) #  multiplied by dt for discrete time
#----------------------
#now for kalman filter

H = np.array([[1,0]]) 

Q_k = np.diag([0.1,0.1]) #for processing noise 

R_k = np.array([[50.0]])  #noisy sensor


time  = np.arange(0,20,dt) #cant use linspace because dt is a float value

x_true = np.array([[10.0],[0.0]]) # 10 metres high 
x_est = np.array([[0.0],[0.0]]) #starting value


P = np.eye(2) #identity matrix meaning 100% uncertainity 

#for plotting
history_true = []
history_est = []
history_z = []

#prediction
for t in time:
    z = H@x_true + np.array(np.random.normal(0,5.0)) 


    kf= P@(np.transpose(H))@(np.linalg.inv(H@P@(np.transpose(H)) +R_k))

    x_est = x_est + kf@(z- H@x_est)


    pf = (np.eye(2) - kf @ H) @ P
    P = pf

    u = -K @ x_est

    #moving the real values
    x_true = A_d@x_true + B_d@u

    #moving the estimate
    x_est = A_d@x_est + B_d@u

    P = A_d @ P @ A_d.T + Q_k

    #for plotiing
    history_true.append(x_true[0, 0])
    history_est.append(x_est[0, 0])
    history_z.append(z[0, 0])

plt.plot(time ,history_est ,  color ="red", label= "Estimated path")
plt.plot(time, history_true, color = 'blue', label ='Actual path')
plt.plot(time, history_z , "o" , markersize = '0.5', alpha= 0.2, color = "black", label= 'noise')
plt.grid(True)
plt.title("LQG")
plt.xlabel("Time")
plt.ylabel("position")
plt.legend()
plt.show()