class Solution:
    # Bruteforce
    def sorting(self, strs):
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

    # Better
    def hashTable(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
                    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return self.sorting(strs)
        return self.hashTable(strs)