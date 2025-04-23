class Subsets:
    def get_subsets(self, nums):
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, index, path, result):
        result.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, result)
            path.pop()

# Example usage:
s = Subsets()
print("All subsets:", s.get_subsets([1, 2, 3]))
