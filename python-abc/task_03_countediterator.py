class CountedIterator:
    """Concrete class for CountedIterator"""

    def __init__(self, data):
        """Initialize the CountedIterator object"""
        self.iterator = iter(data)
        self.count = 0

    def __next__(self):
        """Implementation of the next method"""
        try:
            self.count += 1
            return next(self.iterator)
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Get the count of items iterated"""
        return self.count
