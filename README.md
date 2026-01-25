# Controls and Robotics Foundations

A repository for simulation-based control systems projects. The focus is on implementing mathematical models (ODEs), classical control (PID), and modern control (LQR/State-Space) using Python.

**Current Maintainer:** satvik vyas

---

## Project Status

### 1. Second-Order System Simulation (Completed)
Modeled a standard mass-spring-damper system to analyze the effect of the damping ratio ($\zeta$) on stability and rise time.

* **Source:** `src/second_order_sim.py`
* **Results:** Verified that $\zeta = 1.0$ (Critical Damping) provides the optimal balance between speed and stability, while $\zeta < 1.0$ introduces oscillation.
* **Plot:** See `results/damping_comparison.png` for the step response analysis.

### 2. PID Control (In Development)
Implementation of a manual PID class to close the feedback loop and minimize steady-state error.

---

## Usage

**1. Clone the repository**
```bash

git clone [https://github.com/slimyshi/controls-and-robotics-foundations.git](https://github.com/slimyshi/controls-and-robotics-foundations.git)