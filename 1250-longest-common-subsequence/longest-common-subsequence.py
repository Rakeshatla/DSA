class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = {} 
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                res = 1 + dfs(i - 1, j - 1)
            else:
                res = max(dfs(i - 1, j), dfs(i, j - 1))
            memo[(i, j)] = res
            return res
        return dfs(n - 1, m - 1)
