"""
Filename: Trivia_Game.py
Author: <Melendez, Jacob>
Created: <09/29/2026>
Instructor: burgess
"""
import random
import time

# --- TYPE ADVANTAGE MATRIX ---
# Format: [Attacker][Defender] = Multiplier
TYPE_MODIFIERS = {
    "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Normal": 1.0},
    "Water": {"Fire": 2.0, "Water": 0.5, "Grass": 0.5, "Normal": 1.0},
    "Grass": {"Fire": 0.5, "Water": 2.0, "Grass": 0.5, "Normal": 1.0},
    "Normal": {"Fire": 1.0, "Water": 1.0, "Grass": 1.0, "Normal": 1.0}
}

# --- POKEMON TEMPLATES ---
POKEMON_SPECIES = {
    "Charmander": {"type": "Fire", "hp": 39, "attack": 12, "speed": 13, "evolve_lvl": 5, "evolves_into": "Charmeleon"},
    "Charmeleon": {"type": "Fire", "hp": 58, "attack": 16, "speed": 17, "evolve_lvl": 99, "evolves_into": None},
    "Squirtle": {"type": "Water", "hp": 44, "attack": 10, "speed": 11, "evolve_lvl": 5, "evolves_into": "Wartortle"},
    "Wartortle": {"type": "Water", "hp": 59, "attack": 14, "speed": 15, "evolve_lvl": 99, "evolves_into": None},
    "Bulbasaur": {"type": "Grass", "hp": 45, "attack": 11, "speed": 11, "evolve_lvl": 5, "evolves_into": "Ivysaur"},
    "Ivysaur": {"type": "Grass", "hp": 60, "attack": 15, "speed": 14, "evolve_lvl": 99, "evolves_into": None},
    # Wild Pokémon
    "Rattata": {"type": "Normal", "hp": 30, "attack": 8, "speed": 14, "evolve_lvl": 99, "evolves_into": None},
    "Pidgey": {"type": "Normal", "hp": 35, "attack": 9, "speed": 12, "evolve_lvl": 99, "evolves_into": None},
    "Geodude": {"type": "Normal", "hp": 40, "attack": 11, "speed": 5, "evolve_lvl": 99, "evolves_into": None},
    # Boss Pokémon
    "Onix": {"type": "Normal", "hp": 65, "attack": 15, "speed": 12, "evolve_lvl": 99, "evolves_into": None}
}


class Pokemon:
    def __init__(self, name, level=3):
        self.name = name
        self.level = level
        stats = POKEMON_SPECIES[name]
        self.type = stats["type"]

        # Scale stats dynamically based on level
        self.max_hp = stats["hp"] + (level * 3)
        self.hp = self.max_hp
        self.attack = stats["attack"] + (level * 2)
        self.speed = stats["speed"] + (level * 2)
        self.exp = 0
        self.exp_needed = level * 20

    def check_evolution(self):
        template = POKEMON_SPECIES[self.name]
        if self.level >= template["evolve_lvl"] and template["evolves_into"]:
            old_name = self.name
            self.name = template["evolves_into"]

            # Recalculate stats based on new species template
            stats = POKEMON_SPECIES[self.name]
            self.type = stats["type"]
            self.max_hp = stats["hp"] + (self.level * 3)
            self.hp = self.max_hp
            self.attack = stats["attack"] + (self.level * 2)
            self.speed = stats["speed"] + (self.level * 2)

            print(f"\n✨ What? {old_name} is evolving!")
            time.sleep(1.5)
            print(f"🎉 Congratulations! {old_name} evolved into {self.name}! ✨\n")

    def gain_exp(self, amount):
        print(f"{self.name} gained {amount} EXP!")
        self.exp += amount
        if self.exp >= self.exp_needed:
            self.exp -= self.exp_needed
            self.level += 1
            self.exp_needed = self.level * 20

            # Boost stats on level up
            self.max_hp += 4
            self.hp = self.max_hp
            self.attack += 2
            self.speed += 2

            print(f"🆙 {self.name} grew to Level {self.level}!")
            self.check_evolution()


class Player:
    def __init__(self, name):
        self.name = name
        self.party = []
        self.potions = 3

    def choose_starter(self):
        print("\nProfessor: Welcome to the world of Pokémon! Choose your partner:")
        print("1. Charmander (Fire)\n2. Squirtle (Water)\n3. Bulbasaur (Grass)")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            self.party.append(Pokemon("Charmander"))
        elif choice == "2":
            self.party.append(Pokemon("Squirtle"))
        else:
            self.party.append(Pokemon("Bulbasaur"))

        print(f"\nYou received {self.party[0].name}!")


# --- COMBAT SYSTEM ---
def battle(player, enemy):
    print(f"\nA wild {enemy.name} (Lvl {enemy.level}) appeared!")
    my_pkm = player.party[0]

    while enemy.hp > 0 and my_pkm.hp > 0:
        print(f"\n--- {my_pkm.name}: {my_pkm.hp}/{my_pkm.max_hp} HP | {enemy.name}: {enemy.hp}/{enemy.max_hp} HP ---")
        print("1. Fight\n2. Use Potion\n3. Run")
        action = input("What will you do? ").strip()

        if action == "2":
            if player.potions > 0:
                my_pkm.hp = min(my_pkm.max_hp, my_pkm.hp + 30)
                player.potions -= 1
                print(f"Used Potion! {my_pkm.name} restored 30 HP. (Potions left: {player.potions})")
            else:
                print("No potions left!")
                continue
        elif action == "3":
            if random.random() > 0.4:
                print("Got away safely!")
                return False
            else:
                print("Can't escape!")
        elif action != "1":
            print("Invalid choice!")
            continue

        # Determine turn order based on Speed stat
        if my_pkm.speed >= enemy.speed:
            # Player attacks first
            if action == "1":
                execute_attack(my_pkm, enemy)
            if enemy.hp > 0:
                execute_attack(enemy, my_pkm)
        else:
            # Enemy attacks first
            execute_attack(enemy, my_pkm)
            if my_pkm.hp > 0 and action == "1":
                execute_attack(my_pkm, enemy)

    if my_pkm.hp <= 0:
        print(f"\n💀 {my_pkm.name} fainted! You rushed to the Pokémon Center.")
        my_pkm.hp = my_pkm.max_hp  # Auto-heal for accessibility
        return False
    else:
        print(f"\n🎉 Enemy {enemy.name} fainted!")
        exp_gain = enemy.level * 10
        my_pkm.gain_exp(exp_gain)
        return True


def execute_attack(attacker, defender):
    # Calculate type modifier multipliers
    modifier = TYPE_MODIFIERS[attacker.type].get(defender.type, 1.0)

    # Standard variation randomness
    base_dmg = attacker.attack - (defender.level * 0.5)
    damage = max(2, int(base_dmg * modifier * random.uniform(0.85, 1.15)))

    defender.hp = max(0, defender.hp - damage)
    print(f"⚔️ {attacker.name} attacked {defender.name} for {damage} damage!")

    if modifier > 1.0:
        print("💥 It's super effective!")
    elif modifier < 1.0:
        print("🛡️ It's not very effective...")


# --- MAIN ENGINE LOOP ---
def main():
    print("=========================================")
    print("        WELCOME TO POKEMON TEXT VERSION   ")
    print("=========================================")

    name = input("Enter your Trainer name: ").strip()
    if not name:
        name = "Red"

    player = Player(name)
    player.choose_starter()

    wild_pool = ["Rattata", "Pidgey", "Geodude"]

    while True:
        print(f"\n--- {player.name}'s Adventure Hub ---")
        print("1. Walk in the Tall Grass (Battle & Level Up)")
        print("2. Challenge the Pewter Gym Leader")
        print("3. Check Pokémon Status")
        print("4. Quit Game")

        choice = input("Select an option: ").strip()

        if choice == "1":
            wild_name = random.choice(wild_pool)
            wild_level = random.randint(player.party[0].level - 1, player.party[0].level + 1)
            wild_level = max(2, wild_level)
            enemy = Pokemon(wild_name, wild_level)
            battle(player, enemy)

        elif choice == "2":
            print("\n🗿 Gym Leader Brock challenges you to a battle!")
            time.sleep(1)
            boss = Pokemon("Onix", level=6)
            victory = battle(player, boss)
            if victory:
                print(f"\n🏆 Congratulations {player.name}! You defeated Brock and earned the Boulder Badge!")
                print("Thanks for playing!")
                break

        elif choice == "3":
            pkm = player.party[0]
            print(f"\n📜 PARTY STATUS:")
            print(f"Name:    {pkm.name} ({pkm.type} Type)")
            print(f"Level:   {pkm.level}")
            print(f"HP:      {pkm.hp}/{pkm.max_hp}")
            print(f"Attack:  {pkm.attack}")
            print(f"Speed:   {pkm.speed}")
            print(f"EXP:     {pkm.exp}/{pkm.exp_needed}")
            print(f"Potions: {player.potions}")

        elif choice == "4":
            print("Goodbye! Thanks for playing!")
            break
        else:
            print("Invalid command choice!")


if __name__ == "__main__":
    main()

