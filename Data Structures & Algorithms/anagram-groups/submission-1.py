class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue

            sub = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and self.checkAnagram(strs[i], strs[j]):
                    sub.append(strs[j])
                    used[j] = True

            groups.append(sub)

        return groups

    def checkAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)
