class PairFinder:
    def find_pair(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None

# Example usage:
pf = PairFinder()
print("Pair indices:", pf.find_pair([2, 7, 11, 15], 9))  # Output: (0, 1)
