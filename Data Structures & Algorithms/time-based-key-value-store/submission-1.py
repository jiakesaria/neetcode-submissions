class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        return None
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ''
        if timestamp < self.hashmap[key][0][-1]:
            return ''
        l = 0 
        r = len(self.hashmap[key]) - 1
        while l <= r:
            m = l + (r-l)//2 
            if self.hashmap[key][m][-1] == timestamp:
                return self.hashmap[key][m][0]
            elif self.hashmap[key][m][-1] > timestamp:
                r = m - 1
            else:
                l = m + 1 #?
        return self.hashmap[key][r][0]    