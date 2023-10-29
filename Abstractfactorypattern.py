from abc import ABC, abstractmethod

# Abstract classes for UI elements
class AbstractButton(ABC):
    @abstractmethod
    def display(self):
        pass

class LightButton(AbstractButton):
    def display(self):
        return "Light Button"

class DarkButton(AbstractButton):
    def display(self):
        return "Dark Button"

# Similar abstract and concrete classes can be defined for other UI elements.

# Abstract Factory for creating UI elements
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

class LightUIFactory(UIFactory):
    def create_button(self):
        return LightButton()

class DarkUIFactory(UIFactory):
    def create_button(self):
        return DarkButton()

# Client code
theme = "Light"  # You can change the theme dynamically
factory = LightUIFactory() if theme == "Light" else DarkUIFactory()
button = factory.create_button()
print(button.display())  # Output: Light Button or Dark Button based on the theme
