class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        max_val = 1

        for i in range(len(flips)):
            max_val = max(max_val, flips[i])
            if max_val == i + 1:
                res += 1

        return res
