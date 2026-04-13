class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            chars = [0] * 26 #define char map for each s

            for c in s: 
                chars[ord(c) - ord("a")] += 1 #map char occurences

            res[tuple(chars)].append(s) #add values with char map as key
        
        return list(res.values())