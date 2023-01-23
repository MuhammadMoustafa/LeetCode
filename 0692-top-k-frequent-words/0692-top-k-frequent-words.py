class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:        
        words.sort()
        m = Counter(words)
        h = []
        for key, val in m.items():
            heappush(h, (val, key))
            
        def keySort(ele):
            key1 = ele[0]
            key2 = []
            for i in range(10):
                r = -ord(ele[1][i]) if i < len(ele[1]) else inf
                key2.append(r)
            return (key1, key2)
        
        print("result", nlargest(k, h, key=keySort))
        keys, values = zip(*nlargest(k, h, key=keySort))
        return values