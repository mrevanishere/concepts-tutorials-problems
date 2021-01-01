# Set implementation

class Set:
    def __init__(self):
        self._elements = list()

    def __len__(self):
        return len( self._elements)

    def __contains__(self, item):
        return item in self._elements

    def add(self, item):
        if item not in self:
            self._elements.append(item)

    def remove(self, item):
        assert item in self, "The element must be in the set."
        self._elements.remove(item)

    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.is_subset_of(setB)

    def is_subset_of(self, setB):
        for e in self:
            if e not in setB:
                return False
        return True

    def union(self, setB):
        new_set = Set()
        new_set._elements.extend(self._elements)
        for e in setB:
            new_set._elements.append(e)
        return new_set

    def intersect(self, setB):
        pass

    def difference(self, setB):
        pass

    def __iter__(self):
        pass


