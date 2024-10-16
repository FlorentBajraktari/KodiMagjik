# character.py
from main import KodiMagjikApp


class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.health = 100
        self.mana = 50
        self.inventory = []
        self.skills = []

    def add_item(self, item):
        self.inventory.append(item)

    def add_skill(self, skill):
        self.skills.append(skill)

    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        required_exp = self.level * 100
        if self.experience >= required_exp:
            self.level += 1
            self.experience -= required_exp
            self.health += 20
            self.mana += 10

    def is_alive(self):
        return self.health > 0


if __name__ == "__main__":
    test_character = Character("Test")
    test_character.add_item("Shkopi Magjik")
    test_character.add_skill("Magjia Bazë")
    print(f"Emri: {test_character.name}")
    print(f"Inventari: {test_character.inventory}")
    print(f"Aftësitë: {test_character.skills}")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, target):
        if hasattr(self, 'weapon'):
            self.weapon.use(self, target)
        else:
            # Sulm pa armë
            target.health -= 5  # Dëmi standard
