class Solution:
    def charCount(self, s: str):
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        return count
    
    def isAnagram(self, s: str, t: str) -> bool:
        return self.charCount(s) == self.charCount(t)