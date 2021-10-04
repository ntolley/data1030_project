import numpy as np
import pandas as pd
from utils import linear_scale_forward

dpl = np.load('../data/dpl_sim_fitted_prior_1.npy')
theta_orig = np.load('../data/theta_sim_fitted_prior_1.npy')

prior_dict = {'gbar_evprox_1_L2Pyr_ampa': (1e-10, 1e-1), 
               'gbar_evprox_1_L5Pyr_ampa': (1e-10, 1e-1), 
               'gbar_evdist_1_L2Pyr_ampa': (1e-10, 1e-1), 
               'gbar_evdist_1_L5Pyr_ampa': (1e-10, 1e-1),
               'sigma_t_evprox_1': (1, 100),
               'sigma_t_evdist_1': (1, 100),
               't_evprox_1': (200, 300),
               't_evdist_1': (200, 300)}

theta = np.array([linear_scale_forward(theta_orig[:,idx], bounds) for idx, bounds in enumerate(prior_dict.values())]).T
columns = list(prior_dict.keys())

df = pd.DataFrame(theta, columns=columns)
df['amplitude']  = [np.min(dpl[idx, :]) for idx in range(dpl.shape[0])]

df.to_csv('../data/beta_event_amplitude.csv')
