class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            table = [0] * 27
            for char in strs[i]:
                number = (ord(char)) - ord('a') + 1 
                table[number] += 1
            anagrams[tuple(table)].append(strs[i])
        return list(anagrams.values())
            