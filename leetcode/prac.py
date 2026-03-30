class Solution:
    def maxNonOverlapping(self, startTime, endTime):
        intervals = sorted(zip(startTime, endTime), key=lambda x: x[1])
        print(intervals)
        # [(1, 2), (1, 3), (2, 3), (3, 4)]
        count = 0
        prev_end = 0

        for start, end in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end

        return count

t1 = [1, 1, 2, 3]
t2 = [2, 3, 3, 4]
t3 = [6, 1, 2, 4]
t4 = [8, 9, 4, 7]
s = Solution()
print(s.maxNonOverlapping(t1, t2))
print(s.maxNonOverlapping(t3, t4))