# The Model has no idea about the view or controller.
# The View relies on the Controller interface.
# The Controller relies only on the Model's interface.
# Loose coupling is maintained
class StoreOrder:
    def __init__(self):
        self.items = []
        self.prices = []
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self.items, self.prices)

    def add_item(self, item, price):
        self.items.append(item)
        self.prices.append(price)
        self.notify()

    def delete_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)
            self.prices.pop(index)
            self.notify()

    def change_price(self, index, new_price):
        if 0 <= index < len(self.prices):
            self.prices[index] = new_price
            self.notify()

# Controller Interface
class OrderControllerInterface:
    def delete_item(self, index): pass
    def change_price(self, index, new_price): pass

# Controller
class OrderController(OrderControllerInterface):
    def __init__(self, model):
        self.model = model

    def delete_item(self, index):
        self.model.delete_item(index)

    def change_price(self, index, new_price):
        self.model.change_price(index, new_price)

# View
class OrderView:
    def __init__(self, controller):
        self.controller = controller

    def update(self, items, prices):
        print("Current Order:")
        for i, (item, price) in enumerate(zip(items, prices)):
            print(f"{i+1}. {item} - ${price:.2f}")
        print()

    def simulate_user_delete(self, index):
        self.controller.delete_item(index)

    def simulate_user_change_price(self, index, new_price):
        self.controller.change_price(index, new_price)

# Demo
model = StoreOrder()
controller = OrderController(model)
view = OrderView(controller)

model.add_observer(view)

# Simulate actions
model.add_item("Milk", 2.5)
model.add_item("Bread", 1.5)
view.simulate_user_change_price(0, 3.0)
view.simulate_user_delete(1)
