class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            table = [0] * 26
            for char in s:
                table[ord(char) - ord('a')] += 1
            anagrams[tuple(table)].append(s)

        return list(anagrams.values())