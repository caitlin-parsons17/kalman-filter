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

