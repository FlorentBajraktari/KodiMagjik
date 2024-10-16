# enemy

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player, game_screen):
        # Logjika e sulmit
        player.health -= self.attack_power
        # Përditëso ndërfaqen nëse është e nevojshme
        game_screen.update_status()

# enemy.py


class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0


if __name__ == "__main__":
    enemy = Enemy("Goblin", 50, 10)
    print(
        f"Enemy Name: {enemy.name}, Health: {enemy.health}, Attack Power: {enemy.attack_power}")
