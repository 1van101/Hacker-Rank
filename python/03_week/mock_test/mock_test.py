#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def getTotalX(a, b):
    nums = []
    for i in range(a[-1], b[0] + 1):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            nums.append(i)

    return len(nums)
