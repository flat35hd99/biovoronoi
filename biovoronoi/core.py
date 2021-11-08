import numpy as np
from scipy.spatial import Voronoi, ConvexHull


class Core:
    def set_structure(self, structure):
        self.structure = structure

    def calculate_voronoi_obejct(self):
        atoms = self.structure.get_atoms()
        atom_coordinates = np.array([atom.get_coord() for atom in atoms])
        v = Voronoi(atom_coordinates)
        self.voronoi = v

    def calculate_voronoi_volumes(self):
        volumes = []
        for i, atom in enumerate(self.structure.get_atoms()):
            convex = ConvexHull(
                self.voronoi.vertices[
                    self.voronoi.regions[self.voronoi.point_region[i]]
                ]
            )
            volumes.append(convex.volume)
        self.voronoi_volumes = np.array(volumes)

    def get_voronoi_vertices(self):
        return self.voronoi.vertices

    def get_voronoi_volumes(self):
        return self.voronoi_volumes
