class MySet:
    """Here is my doc string..."""

    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for val in enumerable:
            self.dictionary[val] = True

    def __str__(self):
        # f"MySet: {','.join([str(key) for key in self.dictionary])}"
        return "MySet: {" + ",".join([str(key) for key in self.dictionary]) + "}"

    def has(self, val):
        return val in self.dictionary

    def add(self, val):
        self.dictionary[val] = True
        return self

    def delete(self, val):
        self.dictionary.pop(val, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary = {}
        return self
