class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        pairs = sorted(Counter(words).items(), key=lambda a: (-a[1], a[0]))
        return [word for word, _ in pairs[0: k]]