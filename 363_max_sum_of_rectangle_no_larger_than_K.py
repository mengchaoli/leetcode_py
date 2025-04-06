'''
Three steps/knowledges in this question.
1. when dealing with finding 2D array in 2D array, consider compressing/zipping(压缩). Set a upper boundary and a lower boundary, and compress them into one line, which turns it to a 1D array.
And this turns the 2D array question to a subarray question.
This requires 2 for loops

2. When handling a 1D array in this question(find a subarray in an array), consider 2 things: 1-presum, 2-heap(sorted list, treeset in java)

3. When handing 2D array question, think about if turning the matrix 90 degree will help the performance. So think about the relationship between M and N.

'''


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = float('-inf')
        for i in range(m):
            dp = [0] * n
            for j in range(i, m):
                for l in range(n):
                    dp[l] = dp[l] + matrix[j][l]
                res = max(res, self.helper(dp, k))

        return res

    def helper(self, dp, k):
        m = len(dp)
        set = SortedSet()
        set.add(0)
        res = float('-inf')
        sum = 0

        for i in range(m):
            sum = sum + dp[i]
            idx = set.bisect_left(sum - k)
            if idx != len(set):
                res = max(res, sum - set[idx])
            set.add(sum)
        return res
