

class Equilibrium_Index:
    def __init__(self, arr: list[int]):
        self.arr = arr

    def find_equilibrium_index(self) ->int:
        """
        Find the equilibrium index of the array where the sum of elements
        on the left is equal to the sum of elements on the right.

        An equilibrium index is an index such that the sum of elements at lower
        indices is equal to the sum of elements at higher indices.

        >>> Equilibrium_Index([-7, 1, 5, 2, -4, 3, 0]).find_equilibrium_index()
        [3, 6]
        >>> Equilibrium_Index([1, 2, 3]).find_equilibrium_index()
        []
        """
        total_sum = sum(self.arr)
        left_sum = 0
        result = []

        for i, num in enumerate(self.arr):
            total_sum -= num
            if left_sum == total_sum:
                result.append(i)
            left_sum += num
        
        return result
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
        