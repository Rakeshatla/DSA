class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeab(s, x):
            res = ""
            c = 0
            for ch in s:
                if res and res[-1] == 'a' and ch == 'b':
                    c += x
                    res = res[:-1]
                else:
                    res += ch
            return c, res

        def removeba(s, y):
            res = ""
            c = 0
            for ch in s:
                if res and res[-1] == 'b' and ch == 'a':
                    c += y
                    res = res[:-1]
                else:
                    res += ch
            return c, res

        ans = 0
        if x > y:
            gain, s = removeab(s, x)
            ans += gain
            gain, s = removeba(s, y)
            ans += gain
        else:
            gain, s = removeba(s, y)
            ans += gain
            gain, s = removeab(s, x)
            ans += gain

        return ans
