class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(hq, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        res = []
        while (k > 0 and hq):
            _, n1, n2, idx = heapq.heappop(hq)
            res.append([n1, n2])
            if idx + 1 < len(nums2):
                heapq.heappush(hq, (n1 + nums2[idx + 1], n1, nums2[idx + 1], idx + 1))
            k -= 1
        return res