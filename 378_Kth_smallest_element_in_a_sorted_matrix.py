'''
Kth smallest/largest questions solution:
normally use heap

both min-heap and max-heap can solve this problem. but they differ a little bit:
min-heap can always maintain the smallest number. if we use min-heap, normally we need a first round to init the heap with the small values, such as each head of the list, or first col of the matrix
and then it feels like a bfs. we pop out the element in the heap(it's the current smallest one). and based on that, we add its next value(e.g. its next node or its next column value in its row) into heap
when k is met, we get the answer

if we use max-heap for k-th smallest question:
大顶堆解法也是可行的，思想是：

使用大顶堆来维护当前前k个最小和的配对。

如果堆中的元素不足k个，直接加入。

如果堆中的元素已经有k个，则比较堆顶元素与当前配对元素的和，如果当前配对更小，则替换堆顶元素。

'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # maintain a k size heapq

        # put first col in hq
        hq = []
        for i in range(len(matrix)):
            heapq.heappush(hq, (matrix[i][0], i, 0))

        # pop up element in hq and offer in next one. return k th
        res = 0
        while k > 0:
            val, r, c = heapq.heappop(hq)
            res = val
            if c + 1 < len(matrix[0]):
                heapq.heappush(hq, (matrix[r][c + 1], r, c + 1))
            k -= 1

        return res