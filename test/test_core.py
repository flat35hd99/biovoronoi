import unittest
from biovoronoi.core import Core
from Bio.PDB import PDBParser
import os
import numpy as np
from numpy import float32, testing


class TestCoreVolonoi(unittest.TestCase):
    def setUp(self) -> None:
        self.truncated_pdb_file = (
            f"{os.path.dirname(os.path.abspath(__file__))}/assets/truncated.pdb"
        )
        return super().setUp()

    def test_calculate_voronoi_points(self):
        core = Core()
        structure = PDBParser(QUIET=True).get_structure(
            "truncated_test_structure", self.truncated_pdb_file
        )
        core.set_structure(structure)
        core.calculate_voronoi_points()
        voronoi_points = core.get_voronoi_points()
        print(voronoi_points)
        expected = np.array(
            [
                [24.18799973, -18.76300049, 55.36800003],
                [22.90200043, -18.59300041, 54.57099915],
                [21.80200005, -18.67200089, 55.14099884],
                [23.01099968, -18.38800049, 53.27999878],
                [21.85700035, -18.18099976, 52.36999893],
                [20.96299934, -19.41600037, 52.28099823],
                [21.36599922, -20.59300041, 52.26100159],
                [22.39100075, -17.68700027, 51.01499939],
                [21.49200058, -17.86899948, 49.92399979],
                [19.65600014, -19.11100006, 52.22700119],
                [18.56599998, -20.0720005, 52.1570015],
                [18.5720005, -20.85400009, 50.84400177],
                [17.98699951, -21.9109993, 50.6629982],
                [17.22400093, -19.35499954, 52.29199982],
                [16.98600006, -18.56900024, 50.96699905],
                [15.82800007, -17.61400032, 51.17699814],
                [14.88199997, -17.92499924, 51.88199997],
                [15.86299992, -16.4260006, 50.59700012],
            ],
            dtype=float32,
        )
        testing.assert_array_equal(voronoi_points, expected)
