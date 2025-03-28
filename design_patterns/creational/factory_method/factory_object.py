# Step 1: Define the Abstract Product
from abc import ABC, abstractmethod

class Knife(ABC):
    @abstractmethod
    def sharpen(self):
        pass

    @abstractmethod
    def polish(self):
        pass

    @abstractmethod
    def package(self):
        pass

# Step 2: Implement Concrete Product Classes
class SteakKnife(Knife):
    def sharpen(self):
        print("Sharpening steak knife")

    def polish(self):
        print("Polishing steak knife")

    def package(self):
        print("Packaging steak knife")

class ChefsKnife(Knife):
    def sharpen(self):
        print("Sharpening chef's knife")

    def polish(self):
        print("Polishing chef's knife")

    def package(self):
        print("Packaging chef's knife")

# Step 3: Create the Factory Class
class KnifeFactory:
    def create_knife(self, knife_type):
        if knife_type == "steak":
            return SteakKnife()
        elif knife_type == "chefs":
            return ChefsKnife()
        return None

# Step 4: Use the Factory Object in the Client Code
class KnifeStore:
    def __init__(self, factory: KnifeFactory):
        self.factory = factory

    def order_knife(self, knife_type):
        knife = self.factory.create_knife(knife_type)
        if knife:
            knife.sharpen()
            knife.polish()
            knife.package()
        return knife

# Client Code
if __name__ == "__main__":
    factory = KnifeFactory()
    store = KnifeStore(factory)
    
    # Order a steak knife
    knife = store.order_knife("steak")
