
import unittest
from task_1 import binary_count


class TestBinaryCount(unittest.TestCase):

    def test_success(self):

        self.assertEqual(binary_count(1234), 5)
        self.assertEqual(binary_count(777), 4)
        self.assertEqual(binary_count(12344252), 15)
        self.assertEqual(binary_count(9412413), 16)
        self.assertEqual(binary_count(55697), 8)
        self.assertEqual(binary_count(123456789), 16)

        self.assertEqual(binary_count(95847654321235436547578), 40)
        self.assertEqual(binary_count(67589238504923876598324675098234), 65)
