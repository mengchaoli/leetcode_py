class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        row1 = [1] * n
        row2 = [0] * n
        row2[0] = 1
        row1_to_row2 = True

        for i in range(k):
            if row1_to_row2:
                for j in range(1, n):
                    row2[j] = row2[j - 1] + row1[j]
            else:
                for j in range(1, n):
                    row1[j] = row1[j - 1] + row2[j]
            row1_to_row2 = not row1_to_row2

        return row2[-1] % (10**9 + 7) if k % 2 != 0 else row1[-1] % (10**9 + 7)
