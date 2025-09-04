class PrefixSum:
    def __init__(self, arr: list[int]):
        len_arr = len(arr)
        
        self.prefix_sum = [0]
        if len_arr > 0:
            for i in range(1,len_arr+1):
                self.prefix_sum.append(self.prefix_sum[i-1] + arr[i-1])
    
    def __repr__(self) -> str:
        return f"PrefixSum({self.prefix_sum})"

    def get_sum(self, left: int, right: int) -> int:
        """
        Get the sum of elements in the range [left, right] of the origin array.
        1-based indexing.
        >>> PrefixSum([1,2,3,4,5]).get_sum(2,4)
        9
        >>> PrefixSum([1,2,3,4,5]).get_sum(1,5)
        15
        """
        if left > right or left < 1 or right >= len(self.prefix_sum):
            raise ValueError("Invalid range")

        return self.prefix_sum[right] - self.prefix_sum[left-1]
    
    def contains_target_sum(self, target: int) -> bool:
        """
        The function returns True if array contains the target_sum,
        False otherwise.

        >>> PrefixSum([1,2,3,4,5]).contains_target_sum(9)
        True
        >>> PrefixSum([1,2,3,4,5]).contains_target_sum(15)
        True
        >>> PrefixSum([1,2,3,4,5]).contains_target_sum(8)
        False
        """
        seen = set()
        for num in self.prefix_sum:
            if (num - target) in seen:
                return True
            seen.add(num)
        
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
