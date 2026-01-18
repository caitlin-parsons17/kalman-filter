#imports
from dataclasses import dataclass
import numpy as np

## z_k = x_k + n_k

# (motion equation) x_k = x_0 + v * k dt
# (noise model) n ~ N(0, sigma^2)



@dataclass (frozen= True)
class SimulationConfig:
    dt: float = 0.01  # time step
    t_end : float = 10.0  # end time
    x0: float = 0.0  # initial position
    v: float = 1.0  # constant velocity
    sigma: float = 0.1  # standard deviation of noise
    seed: int = 42 

def simulate_motion(cfg: SimulationConfig):
# simulate 1D constant velocity motion and noisy position measurements. 
#returns: t: time array, x_true: true positions, z_meas: noisy measurements
    rng = np.random.default_rng(cfg.seed)
    t = np.arange(0, cfg.t_end, cfg.dt)
    x_true = cfg.x0 + cfg.v * t
    noise = rng.normal(loc=0.0, scale=cfg.sigma, size=t.shape)
    z_meas = x_true + noise
    return t, x_true, z_meas

