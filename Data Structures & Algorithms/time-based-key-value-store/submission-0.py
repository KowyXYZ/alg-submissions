class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        entry = self.data.get(key, [])

        l = 0
        r = len(entry) - 1
        res = ""

        while l <= r:
            k = (l + r) // 2
            stored_timestamp = entry[k][0]
            stored_value = entry[k][1]

            if stored_timestamp <= timestamp:
                res = stored_value
                l = k + 1
            else:
                r = k - 1
        return res


