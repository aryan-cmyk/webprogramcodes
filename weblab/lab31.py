nums = []
n = int(input("How many numbers? "))

for i in range(n):
    num = float(input("Enter number: "))
    nums.append(num)

mean = sum(nums) / n

var = 0
for x in nums:
    var += (x - mean) ** 2
var = var / n

std = var ** 0.5

print("Mean:", mean)
print("Variance:", var)
print("Standard Deviation:", std)
