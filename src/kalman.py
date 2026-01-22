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
    x_est = np.zeros((len(zs), 2))

    for i, z in enumerate(zs):
        x_pred = F @ x
        P_pred = F @ P @ F.T + Q
        y = np.array([[z]]) - (H @ x_pred)
        S = H @ P_pred @ H.T + R
        K = P_pred @ H.T @ np.linalg.inv(S)
        x = x_pred + K @ y
        P = (I - K @ H) @ P_pred
        # position and velocity estimates
        x_est[i,0] = x[0,0]
        x_est[i,1] = x[1,0]
    return x_est




    
