#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if 0 <= n <= 1:
            return n
        prev_1, prev_2 = 1, 0
        for _ in range(2, n + 1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return prev_1
# @lc code=end
# iterative solution
# class Solution:
#     def fib(self, n: int) -> int:
#         if 0 <= n <= 1:
#             return n
#         memo = [None for _ in range(n + 1)]
#         memo[0], memo[1] = 0, 1
#         for i in range(2, n + 1):
#             memo[i] = memo[i - 1] + memo[i - 2]
#         return memo[n]
# recursion solution
# class Solution:
#     def fib(self, n: int) -> int:
#         memo = [None for _ in range(n + 1)]

#         def dp(n):
#             if 0 <= n <= 1:
#                 return n
#             if memo[n]:
#                 return memo[n]
#             memo[n] = dp(n - 2) + dp(n - 1)
#             return memo[n]
#         return dp(n)
