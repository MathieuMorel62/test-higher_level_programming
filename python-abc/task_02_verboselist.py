class VerboseList(list):
    """Concrete class for VerboseList"""

    def append(self, item):
        """Implementation of the append method"""
        print(f"Added {[item]} to the list.")
        super().append(item)

    def extend(self, items):
        """Implementation of the extend method"""
        print(f"Extended the list with {[len(items)]} items.")
        super().extend(items)

    def remove(self, item):
        """Implementation of the remove method"""
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Implementation of the pop method"""
        print(f"Popped {[self[index]]} from the list.")
        return super().pop(index)
