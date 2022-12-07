class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None

        value = self._data[0]
        del self._data[0]
        return value

    def search(self, index):
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError
