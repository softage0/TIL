# Find nCr for given n and r.
# Input:
# First line contains no of test cases T, for every test case 2
# integers as inputs (n,r).
# Output:
# Compute and print the value in seperate line. Modulus your output
# to 10^9+7. If n
# Constraints:
# 1<=T<=50
# 1<=n<=1000
# 1<=r<=800
# Example:
# Input:
# 1
# 3 2
# Output:
# 3


# solve(5, 2)
# solve(4, 1) + solve(4, 2)
# solve(3, 1) + solve(3, 2)
# solve(2, 1) + solve(2, 2)


# solve(6, 3)
# (5, 2) + (5, 3)
# (4, 1) (4 2) + (4 2) (4 3)


ncrs = [[-1] * 801] * 1001


def get_bc(n, r):
    if n == r:
        return 1

    if r == 1:
        return n

    if ncrs[n][r] == -1:
        result = get_bc(n - 1, r - 1) + get_bc(n - 1, r)
        _, reminder = divmod(result, 1000000007)
        ncrs[n][r] = reminder

    return ncrs[n][r]


T = int(1)

for _ in range(T):
    # N, R = map(int, input().split())

    print(get_bc(1000, 200))
