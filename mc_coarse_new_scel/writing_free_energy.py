import djlib as dj
import json
import os
from glob import glob
import numpy as np
import djlib.mc as mc

mu_values = np.linspace(-1, 1, 81)
t_high = 2000
t_low = 20
user="jonny" #Options: jonny, derick
overwrite=True
# hard-coding this now, change later
if(user=="jonny"):
    print("using Jonny's paths")
    t_const_right_dir = "/home/jonnyli/Desktop/CASM/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/t_const/mu_3.0_0_0.005_T_2000"
    t_const_left_dir = "/home/jonnyli/Desktop/CASM/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/t_const/mu_-3.0_0_0.005_T_2000"
    heating_dir = "/home/jonnyli/Desktop/CASM/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/heating"
    cooling_dir = "/home/jonnyli/Desktop/CASM/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/cooling"
    lte_dir = (
        "/home/jonnyli/Desktop/CASM/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/lte")    
else:
    print("using Derick's paths")
    t_const_right_dir = "/media/derick/DeoResearch/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/t_const/mu_3.0_0_0.005_T_2000"
    t_const_left_dir = "/media/derick/DeoResearch/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/t_const/mu_-3.0_0_0.005_T_2000"
    heating_dir = "/media/derick/DeoResearch/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/heating"
    cooling_dir = "/media/derick/DeoResearch/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/cooling"
    lte_dir = (
    "/media/derick/DeoResearch/experiments/ZrN_FCC_1.2.0_demo/mc_coarse_new_scel/lte")


for mu in mu_values:
    heating_run_name = os.path.join(
        heating_dir, "mu_%.4f_%.4f_T_%d_%d" % ((mu), (mu), t_low, t_high)
    )
    cooling_run_name = os.path.join(
        cooling_dir, "mu_%.4f_%.4f_T_%d_%d" % ((mu), (mu), t_high, t_low)
    )
    if os.path.isfile(
        os.path.join(heating_run_name, "results.json")
    ) and os.path.isfile(os.path.join(cooling_run_name, "results.json")):
        t_const_left = mc.constant_t_run(t_const_left_dir)
        t_const_right = mc.constant_t_run(t_const_right_dir)
        lte_run = mc.lte_run(lte_dir)
        heating_run = mc.heating_run(heating_run_name, lte_run)
        if mu < 0:
            cooling_run = mc.cooling_run(cooling_run_name, t_const_left)
        else:
            cooling_run = mc.cooling_run(cooling_run_name, t_const_right)

        # Append integrated free energy to heating results file
        with open(os.path.join(heating_run_name, "results.json")) as f:
            print("Writing %s" % os.path.join(heating_run_name, "results.json"))
            results = json.load(f)
            if((not "integ_grand_free_energy" in results) or overwrite == True):
                results[
                    "integ_grand_free_energy"
                ] = heating_run.integ_grand_canonical.tolist()
        with open(os.path.join(heating_run_name, "results.json"), "w") as f:
            json.dump(results, f)

        # Append integrated free energy to cooling results file
        with open(os.path.join(cooling_run_name, "results.json")) as f:
            print("Writing %s" % os.path.join(cooling_run_name, "results.json"))
            results = json.load(f)
            if((not "integ_grand_free_energy" in results) or overwrite == True):
                results[
                    "integ_grand_free_energy"
                ] = cooling_run.integ_grand_canonical.tolist()
        with open(os.path.join(cooling_run_name, "results.json"), "w") as f:
            json.dump(results, f)