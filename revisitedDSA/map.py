# list map

class Map:
    def __init__(self):
        self._entries = list()

    def __len__(self):
        return len(self._entries)

    # determines if the map contains the given key
    def __contains__(self, key):
        k = self._findPosition(key)
        return k is not None

    # adds to map if key doesn't exist else replace
    def add(self, key, value):
        k = self._findPosition(key)
        if k is not None:
            self._entries[k].value = value

    def therestofit(self):
        pass




