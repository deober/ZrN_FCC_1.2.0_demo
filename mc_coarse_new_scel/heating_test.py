import djlib.mc as mc
import numpy as np

mc_heating_dir = "/media/derick/DeoResearch/experiments/rocksalt3_ZrN_casm/mc_coarse_new_scel/heating"

mu_values = np.linspace(-1, 1, 81)
superdupercell = [[-4, 4, -20], [-4, 0, 24], [6, 4, 4]]
mc.run_heating(
    mc_heating_dir,
    mu_values,
    superdupercell,
    temp_init=20,
    temp_final=2000,
    temp_increment=20,
)
