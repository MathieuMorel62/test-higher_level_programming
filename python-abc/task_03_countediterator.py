class CountedIterator:
    """Concrete class for CountedIterator"""

    def __init__(self, data):
        """Initialize the CountedIterator object"""
        self._iterator = iter(data)
        self._count = 0

    def __next__(self):
        """Implementation of the next method"""
        try:
            item = next(self._iterator)
            self._count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Get the count of items iterated"""
        return self._count
