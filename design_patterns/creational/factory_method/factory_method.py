from abc import ABC, abstractmethod

# Step 1: Define the Abstract Product
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

# Step 3: Create the Abstract Creator Class
class KnifeStore(ABC):
    def order_knife(self, knife_type):
        knife = self.create_knife(knife_type)
        knife.sharpen()
        knife.polish()
        knife.package()
        return knife

    @abstractmethod
    def create_knife(self, knife_type):
        pass

# Step 4: Implement Concrete Creator Classes
class BudgetKnifeStore(KnifeStore):
    def create_knife(self, knife_type):
        if knife_type == "steak":
            return SteakKnife()
        elif knife_type == "chefs":
            return ChefsKnife()
        return None

# Step 5: Use the Factory Method in Client Code
if __name__ == "__main__":
    store = BudgetKnifeStore()
    knife = store.order_knife("steak")
