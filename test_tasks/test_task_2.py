
import unittest
from task_2 import maskify


class TestMask(unittest.TestCase):

    def test_success(self):

        self.assertEqual(maskify("4556364607935616"), "############5616")
        self.assertEqual(maskify("64607935616"), "#######5616")
        self.assertEqual(maskify("1"), "1")
        self.assertEqual(maskify(""), "")
        self.assertEqual(maskify("Skippy"), "##ippy")
        self.assertEqual(maskify("Nananananananananananananananana Batman!"),
                         "####################################man!")
