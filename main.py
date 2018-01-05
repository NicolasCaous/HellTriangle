from hell_triangle import HellTriangle
from hell_triangle_unittest import HellTriangleTest
import sys

if __name__ == '__main__':

    input = None

    # Handling input
    try:
        input = eval(sys.argv[1])
        if not isinstance(input, list):
            raise ValueError("Not a multidimensional array of integers")
        for row in input:
            if not isinstance(row, list):
                raise ValueError("Not a multidimensional array of integers")
            for integer in row:
                if not isinstance(integer, int):
                    raise ValueError("Not a multidimensional array of integers")

    except Exception, e:
        print(str(e))
        print("Halting...")
        sys.exit()

    hell_triangle = HellTriangle(input)

    print("Result for the input: " + str(hell_triangle.find_sum()))

    HellTriangleTest.start()
