from abc import ABC, abstractmethod

class Mediator:
    @abstractmethod
    def notify(self, sender: "Component", event: str):
        pass
    
class Component:
    def __init__(self, dialog: Mediator):
        self.dialog: Mediator = dialog

    def click(self):
        self.dialog.notify(self, "click")
       

class LoginButton(Component):
    pass

class TextBox(Component):
    pass

class CheckBox(Component):
    def check(self):
        self.dialog.notify(self, "check")


class AuthentcationMediator(Mediator):
    def __init__(self):
        self.submitButton = LoginButton(self)
        self.userTextBox = TextBox(self)
        self.loginOrRegistercheckBox = CheckBox(self)
    
    def notify(self, sender: Component, event: str):
        if type(sender) == type(self.submitButton) and event == "click":
            print("Authenticate or show error")
        if type(sender) == type(self.loginOrRegistercheckBox)  and event == "check":
            print("Show Login window or signup based on conditions")

authDialog = AuthentcationMediator()
authDialog.submitButton.click()
authDialog.loginOrRegistercheckBox.check()

                    