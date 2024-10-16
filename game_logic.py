class GameLogic:
    def first_choice(self, player, choice):
        if choice == 'Magjia':
            player.mana += 50
            player.add_item("Shkopi Magjik")
            player.add_skill("Magjia Bazë")
        elif choice == 'Shkenca':
            player.health += 50
            player.add_item("Vegla Shkencore")
            player.add_skill("Analiza Shkencore")
        else:
            # Trajtimi i zgjedhjeve të pavlefshme
            print("Zgjedhje e pavlefshme! Zgjidhni ose 'Magjia' ose 'Shkenca'.")

    def coding_puzzle(self, player):
        print("Puzzle i Kodimit: Zgjidh problemin e mëposhtëm.")
        # Puzzle i thjeshtë i kodimit
        problem = "Cili është rezultati i 2 ** 3 në Python?"
        print(problem)
        answer = input("Shkruani përgjigjen tuaj: ")

        if answer == "8":
            print("Përgjigje e saktë!")
            player.add_skill("Zgjidhësi i Puzzleve")
        else:
            print("Përgjigje e gabuar. Provo përsëri më vonë.")

    def battle(self, player, enemy):
        print(f"Luftë midis {player.name} dhe {enemy.name}!")

        while player.health > 0 and enemy.health > 0:
            # Zgjedhja e lojtarit
            action = input("Zgjidh veprimin: [SULMO/MBROHU/MAGJI]: ").lower()

            if action == "sulmo":
                damage = player.attack() - enemy.defend()
                if damage > 0:
                    enemy.health -= damage
                    print(
                        f"Ti godite {enemy.name} dhe shkaktove {damage} dëme.")
                else:
                    print(f"{enemy.name} bllokoi sulmin tënd!")

            elif action == "mbrohu":
                print(f"Ti u mbrojte nga sulmi i {enemy.name}.")
                player.defense_boost()

            elif action == "magji":
                if player.mana >= 20:
                    spell_damage = player.cast_spell()
                    enemy.health -= spell_damage
                    print(
                        f"Ti përdore magji dhe shkaktove {spell_damage} dëme.")
                else:
                    print("Nuk ke mjaftueshëm mana për të përdorur magji!")

            else:
                print("Veprim i pavlefshëm!")

            # Sulmi i armikut
            if enemy.health > 0:
                enemy_damage = enemy.attack() - player.defend()
                if enemy_damage > 0:
                    player.health -= enemy_damage
                    print(
                        f"{enemy.name} të goditi dhe shkaktoi {enemy_damage} dëme.")
                else:
                    print(f"Ti bllokove sulmin e {enemy.name}!")

        if player.health > 0:
            print(f"{player.name} fitoi!")
        else:
            print(f"{enemy.name} fitoi!")

# Shembull për klasat e lojtarit dhe armikut


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.items = []
        self.skills = []

    def add_item(self, item):
        self.items.append(item)

    def add_skill(self, skill):
        self.skills.append(skill)

    def attack(self):
        return 10  # Vlera e sulmit bazik

    def defend(self):
        return 5  # Mbrojtja bazike

    def cast_spell(self):
        self.mana -= 20
        return 15  # Dëmi i shkaktuar nga magjia

    def defense_boost(self):
        print("Mbrojtja u rrit për këtë turn.")
        # Këtu mund të shtoni logjikën që rrit përkohësisht mbrojtjen
