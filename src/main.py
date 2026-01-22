import matplotlib.pyplot as plt
from simulation import SimulationConfig, simulate_motion
from kalman import kalman_filter

def main():
    cfg = SimulationConfig(dt=0.01, t_end=4.0, x0=0.0, v=1.0, sigma=0.1, seed=42)
    t, x_true, z_meas = simulate_motion(cfg)
    plt.figure()
    plt.plot(t, x_true, label="true position")
    plt.scatter(t, z_meas, label="noisy measurements", s=8)
    r = cfg.sigma ** 2 # measurement noise variance
    q = 0.01  # process noise strength
    x_est = kalman_filter(z_meas, cfg.dt, q, r, x0=cfg.x0, v0=cfg.v)
    pos_est = x_est[:, 0]
    plt.plot(t, pos_est, label="Kalman estimate")


    plt.xlabel("time (s)")
    plt.ylabel("position")
    plt.title("motion with noisy sensor measurements")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()