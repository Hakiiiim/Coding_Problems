from typing import List


class Solution:
    def minimumTime(self, N: int, cur: int, pos: List[int], time: List[int]) -> int:
        # code here
        min_time = float('inf')
        for i in range(N):
            taxi_pos = pos[i]
            taxi_unit_time = time[i]

            taxi_time = abs(taxi_pos - cur) * taxi_unit_time

            if taxi_time < min_time:
                min_time = taxi_time

        return min_time


# {
# Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        cur = int(input())

        pos = IntArray().Input(N)

        time = IntArray().Input(N)

        obj = Solution()
        res = obj.minimumTime(N, cur, pos, time)

        print(res)

# } Driver Code Ends