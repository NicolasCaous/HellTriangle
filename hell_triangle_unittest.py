from hell_triangle import HellTriangle
import sys, unittest

# Class for automated tests
class HellTriangleTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        hell_triangle = HellTriangle([[6],[3,5],[9,7,1],[4,6,8,4]])
        print("\nInput: [[6],[3,5],[9,7,1],[4,6,8,4]] Expected output: 26")
        self.assertEqual(hell_triangle.find_sum() , 26)
        print("OK\n")

    def test2(self):
        hell_triangle = HellTriangle([[1],[2,3],[4,5,6],[7,8,9,10]])
        print("\nInput: [[1],[2,3],[4,5,6],[7,8,9,10]] Expected output: 20")
        self.assertEqual(hell_triangle.find_sum() , 20)
        print("OK\n")

    def test3(self):
        hell_triangle = HellTriangle([[10],[9,8],[7,6,5],[4,3,2,1]])
        print("\nInput: [[10],[9,8],[7,6,5],[4,3,2,1]] Expected output: 30")
        self.assertEqual(hell_triangle.find_sum() , 30)
        print("OK\n")

    @staticmethod
    def start():
        print("\n")
        print("#######################")
        print("### Automated Tests ###")
        print("#######################")
        print("\n")

        # Resizing argv to make unittest stop whining...
        del sys.argv[1:]
        unittest.main()
