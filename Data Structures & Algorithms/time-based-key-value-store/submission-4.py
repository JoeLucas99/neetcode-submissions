class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        listLen = len(self.timeMap[key])
        if listLen == 0:
            return ""
        l , r = 0 , listLen - 1
        res = ""
        while l <= r:
            mid = l + (r - l) // 2
            value, cur_timestamp = self.timeMap[key][mid]
            if cur_timestamp <= timestamp:
                res = value
                l = mid + 1
            else:
                r = mid - 1
        return res

        
