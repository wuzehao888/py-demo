class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        new_health = 0 if new_health < 0 else new_health
        new_health = 100 if new_health > 100 else new_health
        self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        new_mana = 0 if new_mana < 0 else new_mana
        new_mana = 50 if new_mana > 50 else new_mana
        self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self._level}!")

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)
