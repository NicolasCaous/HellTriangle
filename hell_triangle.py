class HellTriangle:

    def __init__(self, input):
        # The variable for the multidimensional array
        self.triangle = input

    def find_sum(self):
        return self.__find_sum(0, 0, self.triangle[0][0])

    #
    #   The solution is a simple recursive iteration over the multidimensional array
    #
    #   Complexity: 2^n
    #
    def __find_sum(self, row, i, sum):
        # Breakpoint
        if row + 1 == len(self.triangle):
            return sum

        # Recursive call
        left_sum = self.__find_sum(row + 1, i, sum + self.triangle[row + 1][i])
        right_sum = self.__find_sum(row + 1, i + 1, sum + self.triangle[row + 1][i + 1])

        # Returns the largest between two partial sums
        return max(left_sum, right_sum)
