class SwimMixin:
    """Mixin class for swimming"""

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class for flying"""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Concrete class for Dragon"""

    def roar(self):
        print("The dragon roars!")
