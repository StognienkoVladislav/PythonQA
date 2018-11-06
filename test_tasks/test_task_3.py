
import unittest
from task_3 import same_structure_as


class TestMask(unittest.TestCase):

    def test_success(self):

        self.assertEqual(same_structure_as([1, 1, 1], [2, 2, 2]), True)
        self.assertEqual(same_structure_as([1, [1, 1]], [2, [2, 2]]), True)

        self.assertEqual(same_structure_as([1, [1, 1]], [[2, 2], 2]), False)
        self.assertEqual(same_structure_as([1, [1, 1]], [[2], 2]), False)

        self.assertEqual(same_structure_as([[[], []]], [[[], []]]), True)

        self.assertEqual(same_structure_as([[[], []]], [[1, 1]]), False)
