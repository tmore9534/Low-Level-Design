from abc import ABC, abstractmethod

# The handler interface declares a method for executing a request.
class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass

# The base class for simple components.
class Component(ComponentWithContextualHelp):
    def __init__(self, tooltip_text=None):
        self.tooltip_text = tooltip_text
        self.container = None  # The component's container

    def show_help(self):
        if self.tooltip_text:
            print(f"Tooltip: {self.tooltip_text}")
        elif self.container:
            self.container.show_help()

# Containers can contain both simple components and other containers.
class Container(Component):
    def __init__(self, tooltip_text=None):
        super().__init__(tooltip_text)
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.container = self

# Primitive components may use the default help implementation.
class Button(Component):
    pass

# Complex components may override the default implementation.
class Panel(Container):
    def __init__(self, modal_help_text=None):
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text:
            print(f"Modal Help: {self.modal_help_text}")
        else:
            super().show_help()

class Dialog(Container):
    def __init__(self, wiki_page_url=None):
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        if self.wiki_page_url:
            print(f"Open Wiki: {self.wiki_page_url}")
        else:
            super().show_help()

# Client code
class Application:
    def create_ui(self):
        dialog = Dialog(wiki_page_url="http://help.example.com")
        panel = Panel(modal_help_text="This panel provides detailed help.")
        ok_button = Button(tooltip_text="Click to confirm action.")
        cancel_button = Button(tooltip_text="Click to cancel action.")

        panel.add(ok_button)
        panel.add(cancel_button)
        dialog.add(panel)

        self.dialog = dialog  # Keep reference to the root container

    def on_f1_key_press(self, component):
        component.show_help()

# Example usage
app = Application()
app.create_ui()

# Simulating F1 key press on different components
app.on_f1_key_press(app.dialog.children[0].children[0])  # OK Button
app.on_f1_key_press(app.dialog.children[0])  # Panel
app.on_f1_key_press(app.dialog)  # Dialog
