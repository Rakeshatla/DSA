class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
                # print(count)
            ans[tuple(count)].append(s)
        return list(ans.values())