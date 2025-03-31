from abc import ABC, abstractmethod

class PastaDish(ABC):
    def make_recipe(self):
        self.boil_water()
        self.add_pasta()
        self.cook_pasta()
        self.drain_and_plate()
        self.before_sauce()  # Hook 1
        self.add_sauce()
        self.after_sauce()   # Hook 2
        self.add_protein()
        self.add_garnish()
    
    def boil_water(self):
        print("Boiling water")
    
    def cook_pasta(self):
        print("Cooking pasta")
    
    def drain_and_plate(self):
        print("Draining and plating pasta")
    
    @abstractmethod
    def add_pasta(self):
        pass
    
    @abstractmethod
    def add_sauce(self):
        pass
    
    @abstractmethod
    def add_protein(self):
        pass
    
    @abstractmethod
    def add_garnish(self):
        pass

    # Hooks with default implementations (subclasses may override)
    def before_sauce(self):
        pass
    
    def after_sauce(self):
        pass


class SpaghettiMeatballs(PastaDish):
    def add_pasta(self):
        print("Add spaghetti")
    
    def add_sauce(self):
        print("Add tomato sauce")
    
    def add_protein(self):
        print("Add meatballs")
    
    def add_garnish(self):
        print("Add Parmesan cheese")

    def before_sauce(self):
        print("SpaghettiMeatballs: Adding extra olive oil before sauce")

class PenneAlfredo(PastaDish):
    def add_pasta(self):
        print("Add penne")
    
    def add_sauce(self):
        print("Add Alfredo sauce")
    
    def add_protein(self):
        print("Add chicken")
    
    def add_garnish(self):
        print("Add parsley")
        
# Example usage:
if __name__ == "__main__":
    print("Making Spaghetti Meatballs:")
    spaghetti = SpaghettiMeatballs()
    spaghetti.make_recipe()
    
    print("\nMaking Penne Alfredo:")
    penne = PenneAlfredo()
    penne.make_recipe()
