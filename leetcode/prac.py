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

# t1 = [1, 1, 2, 3]
# t2 = [2, 3, 3, 4]
# t3 = [6, 1, 2, 4]
# t4 = [8, 9, 4, 7]
# s = Solution()
# print(s.maxNonOverlapping(t1, t2))
# print(s.maxNonOverlapping(t3, t4))




def maxDifference(arr):
    min_so_far = arr[0]
    max_diff = -1

    for i in range(1, len(arr)):
        if arr[i] > min_so_far:
            max_diff = max(max_diff, arr[i] - min_so_far)
        
        min_so_far = min(min_so_far, arr[i])

    return max_diff

for i in range(2,2):
    print(i)