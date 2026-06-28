class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        freq = []
        for _ in range(k):
            max_num = max(counter, key = counter.get)
            freq.append(max_num)
            del counter[max_num]
        return freq