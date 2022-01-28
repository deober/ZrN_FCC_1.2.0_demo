from turtle import left
import djlib.clex as cl
import matplotlib.pyplot as plt
import numpy as np
import djlib as dj


fcc_data = cl.read_corr_comp_formation("ZrN_FCC_query_data.json")
hcp_data = cl.read_corr_comp_formation("ZrN_HCP_query_data.json")

all_comps = np.concatenate((hcp_data["comp"], fcc_data["comp"]), axis=0)
all_energies = np.concatenate(
    (hcp_data["formation_energy"] / 2, fcc_data["formation_energy"]), axis=0
)
points = np.concatenate((all_comps, np.reshape(all_energies, (-1, 1))), axis=1)

hull = cl.ConvexHull(points)
trash, lower_hull_indices = cl.lower_hull(hull)
hull_vertices = points[lower_hull_indices]
hull_vertices = dj.column_sort(hull_vertices, 0)

#TODO:Check the HCP GS @ 50%
plt.plot(hull_vertices[:, 0], hull_vertices[:, 1], color="k", label="Convex Hull",zorder=1)

# Need to divide formation energy by number of sites per prim
plt.scatter(
    np.array(hcp_data["comp"]), np.array(hcp_data["formation_energy"]) / 2, label="HCP",zorder=5
)
plt.scatter(
    np.array(fcc_data["comp"]), np.array(fcc_data["formation_energy"]), label="FCC",zorder=6
)
plt.hlines(0, 0, 1, linestyles="dashed",color="k",zorder=0)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

#TODO: Increase font size of scaling

plt.legend(fontsize=15)
#plt.title(r"ZrN$_{x}$ HCP and FCC Convex Hull", fontsize=30)
plt.xlabel("Composition (x)", fontsize=20)
plt.ylabel("Formation Energy per Zr (eV)", fontsize=20)

fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.subplots_adjust(left=0.15,bottom=0.11)

plt.show()
