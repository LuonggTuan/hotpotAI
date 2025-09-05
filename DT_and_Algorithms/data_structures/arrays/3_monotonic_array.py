
class MonotonicArray:
    def __init__(self, arr: list[int]):
        self.arr = arr

    def is_monotonic(self):
        """
        Check if the array is monotonic (entirely non-increasing or non-decreasing).
        >>> MonotonicArray([1, 2, 2, 3]).is_monotonic()
        True
        >>> MonotonicArray([6, 5, 4, 4]).is_monotonic()
        True
        >>> MonotonicArray([1, 3, 2]).is_monotonic()
        False
        >>> MonotonicArray([1, 2, 4, 5]).is_monotonic()
        True
        >>> MonotonicArray([1, 1, 1]).is_monotonic()
        True
        >>> MonotonicArray([]).is_monotonic()
        True
        >>> MonotonicArray([1]).is_monotonic()
        True
        """
        if not self.arr or len(self.arr) == 1:
            return True

        increasing = decreasing = True

        for i in range(1, len(self.arr)):
            if self.arr[i] > self.arr[i - 1]:
                decreasing = False
            elif self.arr[i] < self.arr[i - 1]:
                increasing = False

        return increasing or decreasing

if __name__ == "__main__":
    import doctest
    doctest.testmod()