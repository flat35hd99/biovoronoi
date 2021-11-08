import numpy
from scipy.spatial import Voronoi


class Core:
    def set_structure(self, structure):
        self.structure = structure

    def calculate_voronoi_points(self):
        atoms = self.structure.get_atoms()
        atom_coordinates = numpy.array([atom.get_coord() for atom in atoms])
        v = Voronoi(atom_coordinates)
        self.voronoi = v

    def get_voronoi_vertices(self):
        return self.voronoi.vertices
