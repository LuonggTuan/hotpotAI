
class PrefixSum:
    def __init__(self, arr: list[int]):
        len_arr = len(arr)
        self.prefix_sum = [0]

        if len_arr > 0:
            for i in range(len_arr):
                self.prefix_sum.append(self.prefix_sum[i] + arr[i])
    
    def __repr__(self):
        return f"PrefixSum({self.prefix_sum})"
    
    def range_sum(self, left: int, right: int) -> int:
        """
        Get the sum of elements in the range [left, right] of the original array.
        1-based indexing.

        >>> PrefixSum([1, 2, 3, 4, 5]).range_sum(1, 4)
        10
        >>> PrefixSum([1, 2, 3, 4, 5]).range_sum(2, 4)
        9
        """
        if not self.prefix_sum:
            raise ValueError("The array is empty.")

        if left < 1 or right >= len(self.prefix_sum) or left > right:
            raise ValueError("Invalid range specified.")

        if left == 1:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left - 1]

    def contains_sum(self, target_sum: int) -> bool:
        """
        Check if there exists a subarray in the original array that sums to target_sum.

        >>> PrefixSum([1, 2, 3, 4, 5]).contains_sum(9)
        True
        >>> PrefixSum([1, 2, 3, 4, 5]).contains_sum(15)
        True
        >>> PrefixSum([1, 2, 3, 4, 5]).contains_sum(16)
        False
        """
        seen_sums = set()
        for ps in self.prefix_sum:
            if (ps - target_sum) in seen_sums:
                return True
            seen_sums.add(ps)
        return False
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()