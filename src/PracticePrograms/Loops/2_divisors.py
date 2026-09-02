import math
class Solution:
    def getDivisors(self, n):
        # code here
        result = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n%i == 0:
                result.append(i)
                if i != n//i:
                    result.append(n//i)
        result.sort()
        return result

sol = Solution()
divisors = sol.getDivisors(20)
for divisor in divisors:
    print(divisor)