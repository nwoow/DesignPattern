class CharacterPrototype:
    def clone(self):
        pass

class Warrior(CharacterPrototype):
    def clone(self):
        return Warrior()

class Mage(CharacterPrototype):
    def clone(self):
        return Mage()

class CharacterFactory:
    characters = {}

    @classmethod
    def add_character(cls, name, prototype):
        cls.characters[name] = prototype

    @classmethod
    def create_character(cls, name):
        return cls.characters[name].clone()

# Usage
CharacterFactory.add_character("Warrior", Warrior())
CharacterFactory.add_character("Mage", Mage())

warrior1 = CharacterFactory.create_character("Warrior")
mage1 = CharacterFactory.create_character("Mage")
