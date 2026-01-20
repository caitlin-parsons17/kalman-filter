import numpy as np

def kalman_filter(zs, dt, q, r, x0=0.0, v0=0.0):
    # state transition matrix
    F = np.array([[1.0, dt],
                  [0.0, 1.0]])
    # position measurement matrix
    H = np.array([[1.0, 0.0]])
    # process noise covariance
    Q = np.array([[q*dt**3/3, q*dt**2/2],
                  [q*dt**2/2, q*dt]])
    # measurement noise covariance
    R = np.array([[r]])
    x = np.array([[x0],
                  [v0]])
    P = np.eye(2) * 1.0  # initial estimate covariance
    I = np.eye(2)
    x_est = np.zeros((len(z_meas), 2))
    
