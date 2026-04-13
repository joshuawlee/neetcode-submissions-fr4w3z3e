class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #26 lowercase letters 

            for c in s:
                count[ord(c) - ord("a")] += 1 #counts occurence of each char in alpha order
            
            res[tuple(count)].append(s) #group strings together with map

        return list(res.values())