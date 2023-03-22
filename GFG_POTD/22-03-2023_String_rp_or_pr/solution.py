# User function Template for python3

from copy import copy


class Solution_beta:
    def solve(self, X, Y, S):
        # code here
        if X > Y:
            big, small = 'pr', 'rp'
            big_amount, small_amount = X, Y
        else:
            big, small = 'rp', 'pr'
            big_amount, small_amount = Y, X

        def compute_amount(string, big, small, big_amount, small_amount, debug):
            pointer = 0
            amount = 0
            # First pass: detect big ones
            while pointer < len(string) - 1:
                substr = string[pointer:pointer + 2]

                if debug:
                    print("1st pass, S: ", string, " | pointer: ", pointer, " | substr: ", substr, " | amount: ",
                          amount)

                if substr == big:
                    amount += big_amount
                    string = string[0:pointer] + string[pointer + 2:]
                    if pointer != 0:
                        pointer -= 1
                else:
                    pointer += 1

            # Second pass: detect small ones ones
            pointer = 0
            while pointer < len(string) - 1:
                substr = string[pointer:pointer + 2]

                if debug:
                    print("2d pass, S: ", string, " | pointer: ", pointer, " | substr: ", substr, " | amount: ", amount)

                if substr == small:
                    amount += small_amount
                    string = string[0:pointer] + string[pointer + 2:]
                    if pointer != 0:
                        pointer -= 1
                else:
                    pointer += 1

            return amount

        amount_S = compute_amount(string=S, big=big, small=small, big_amount=big_amount, small_amount=small_amount,
                                  debug=False)
        return amount_S


class Solution:
    def solve(self, X, Y, S):
        # code here
        if X > Y:
            big, small = 'pr', 'rp'
            big_amount, small_amount = X, Y
        else:
            big, small = 'rp', 'pr'
            big_amount, small_amount = Y, X

        def compute_amount(string, big, small, big_amount, small_amount, debug):
            amount = 0

            pr_count = string.count(big)
            while pr_count > 0:
                string = string.replace(big, '', pr_count)

                # compute the amount based on the counts and the prices
                amount += pr_count * big_amount

                # count the number of replacements
                pr_count = string.count(big)

            rp_count = string.count(small)
            while rp_count > 0:
                string = string.replace(small, '', rp_count)

                # compute the amount based on the counts and the prices
                amount += rp_count * small_amount

                # count the number of replacements
                rp_count = string.count(small)

            return amount

        amount_S = compute_amount(string=S, big=big, small=small, big_amount=big_amount, small_amount=small_amount,
                                  debug=False)
        return amount_S


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()

        ob = Solution()
        print(ob.solve(X, Y, S))
# } Driver Code Ends