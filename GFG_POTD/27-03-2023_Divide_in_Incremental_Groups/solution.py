# User function Template for python3

from copy import copy


class Solution_recursive:
    def countWaystoDivide(self, N, K):
        # Code here
        if K == 1:
            return 1
        elif K == N:
            return 1
        else:
            debug = False

            def recursive(N, K, start, elements, groups):
                if debug:
                    print("N: ", N, " K: ", K, " start: ", start, " elements: ", elements, " groups: ", groups)
                if K == 1:
                    if start > N - sum(elements):
                        return groups
                    else:
                        elements.append(N - sum(elements))
                        groups.add(tuple(elements))
                        return groups
                else:
                    elements.append(start)
                    for integer in range(start, N - K + 1):
                        if integer * (K - len(elements)) <= N - sum(elements):
                            if K - 1 == 1:
                                return recursive(
                                    N=N, K=K - 1, start=copy(integer), elements=copy(elements), groups=groups)
                            else:
                                groups = recursive(
                                    N=N, K=K - 1, start=copy(integer), elements=copy(elements), groups=groups)
                        else:
                            break
                    return groups

            start = 1
            groups = set()
            while start * K <= N:
                groups = recursive(N=N, K=K, start=start, elements=[], groups=groups)
                start += 1

            return len(groups)


class Solution:
    # Memoization
    # Let dp[i][j] be the number of options to split j numbers into i groups.
    # The solution the would be dp[k][n]. It can be calculated recursively as follows dp[i][j] = sum (dp[i-1][s] for s
    # from 1 to j.
    # Base cases are dp[i][i] = 1 for all i, dp[i][j] = 0 for all i > j. So it can be solved using dynamic programming
    # approach at O(n^2*k).
    def countWaystoDivide(self, N, K):
        def find(n, k, v):
            if k == 0 and n == 0: return 1
            if k > n or k < 0 or n < 0: return 0

            if (n, v, k) in dp: return dp[(n, v, k)]

            ans = 0
            for i in range(v, n + 1):
                ans += find(n - i, k - 1, i)

            dp[(n, v, k)] = ans

            return dp[(n, v, k)]

        dp = {}

        return find(n=N, k=K, v=1)


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N = int(input())
        K = int(input())
        ob = Solution()
        print(ob.countWaystoDivide(N, K))

        T -= 1
# } Driver Code Ends
