class Solution:
    MOD = 10**9 + 7
    MAX = 100005

    # Precompute factorials and inverse factorials
    fact = [1] * MAX
    inv_fact = [1] * MAX

    for i in range(1, MAX):
        fact[i] = (fact[i - 1] * i) % MOD

    inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
    for i in range(MAX - 2, 0, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def countAnagrams(self, s: str) -> int:
        words = s.split()
        result = 1

        for word in words:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            total = self.fact[len(word)]
            for count in freq:
                if count > 1:
                    total = (total * self.inv_fact[count]) % self.MOD

            result = (result * total) % self.MOD

        return result