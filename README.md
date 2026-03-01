# Controls and Robotics Foundations

A repository for simulation-based control systems projects. The focus is on implementing mathematical models (ODEs), classical control (PID), and modern control (LQR/State-Space) using Python.

**Current Maintainer:** satvik vyas

---

## Project Status

### 1. Second-Order System Simulation (Completed)
Modeled a standard mass-spring-damper system to analyze the effect of the damping ratio ($\zeta$) on stability and rise time.
* **Source:** `src/secondodsim.py`
* **Results:** Verified that $\zeta = 1.0$ (Critical Damping) provides the optimal balance between speed and stability, while $\zeta < 1.0$ introduces oscillation.
* **Plot:** [View Mass-Spring-Damper Step Response](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/mass_spring_damper.png)

### 2. PID Control & Trajectory Tracking (Completed)
Modeled a drone system with gravity and drag, with fixed target (10 meters) and tracked path ($10 + 5\sin(t)$) and analyzed the impact of $K_p$, $K_d$, and $K_i$ on the system. Added Feedforward prediction to eliminate phase lag during tracking.
* **Source:** `src/pid.py`, `src/pid_test.py`
* **Results:** * [View Fixed 10m Target Response](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/drone_with%20_pd_controller_and_10m_target.png)
    * [View Sine Wave Path Tracking](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/drome%20with%20sine%20wave%20path.png)
    * [View Kp Gain Comparison](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/Kp_controller_comparision.png)
    * [View Kd Gain Impact](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/impact%20of%20d_GAIN.png)
    * [View PD Control Analysis](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/pd_control.png)

### 3. 2D Waypoint Navigation (Completed)
Implemented a dual-PID control system to navigate a drone through a 2D environment across multiple waypoints using dynamic distance thresholds.
* **Source:** `src/2d_controller.py`
* **Results:** System successfully executed path tracking across coordinates [(0,0) -> (0,10) -> (15,10) -> (20,25)] with a 0.1m cornering tolerance.
* **Plot:** [View 2D Path Tracking](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/2d_drone_tracking.png)

### 4. State Space Representation (Completed)
Transitioned the physics engine from scalar variables to a state-space matrix formulation ($\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$) to handle multi-variable physics (inertia and drag) simultaneously using NumPy.
* **Source:** `src/state_space.py`
* **Results:** * [View State-Space Equation Validation](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/state_SPACEequation.png)
    * [View State Response Comparison](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/State_response_comparision.png)

### 5. LQR Optimal Control (Completed)
Implemented Linear Quadratic Regulator (LQR) control to automate gain calculation by minimizing a quadratic cost function ($Q$ and $R$ matrices).
* **Source:** `src/lqr.py`, `src/cartpole.py`
* **Results:** * [View 1D Drone LQR Stability]()
    * [View Inverted Pendulum (Cart-Pole) Balance](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/Cartpole.png)

### 6. Linear Quadratic Gaussian (LQG) Control (Completed)
Integrated the optimal LQR controller with a Kalman Filter to build a complete LQG autonomous flight controller. The system successfully estimates the true state from heavily corrupted ultrasonic sensor data and computes the optimal thrust to stabilize the drone.
* **Source:** `src/day12_lqg.py` (or the name of your final LQG script)
* **Results:** Demonstrated the Separation Principle by successfully driving the system from a 10m initial state to 0m while filtering out severe Gaussian measurement noise.
* **Plot:** [View LQG Autonomous Landing](https://github.com/satvikvyas/controls-and-robotics-foundations/blob/main/results/LQGpng.png)


## Usage

**1. Clone the repository**
```bash
git clone [https://github.com/slimyshi/controls-and-robotics-foundations.git](https://github.com/slimyshi/controls-and-robotics-foundations.git)