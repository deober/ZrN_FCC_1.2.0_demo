import djlib as dj
import numpy as np

const_t_dir = "/media/derick/DeoResearch/experiments/rocksalt3_ZrN_casm/mc_coarse_new_scel/t_const/mu_3.0_0_0.005_T_2000"
cooling_dir = "/media/derick/DeoResearch/experiments/rocksalt3_ZrN_casm/mc_coarse_new_scel/cooling"

mu_values = np.linspace(1, 0, 41)
dj.mc.run_cooling_from_const_temperature(
    mu_values, cooling_dir, const_t_dir, temp_final=20, temperature_increment=-20
)
