class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        
        sum = 91

        for i in range(3, n + 1):
            x = 1
            for j in range(i - 1):
                x = x * (9 - j)
            x = x * 9
            sum = sum + x
        
        return sum
