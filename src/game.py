import random

from npc import NPC
from player import Player


def fight(player, enemy):
    print(f"\n⚔️ A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} HP: {player.hp}/{player.max_hp} | MP: {player.mp}/{player.max_mp}")
        print(f"{enemy.name} HP: {enemy.hp}")
        choice = input("Do you want to (A)ttack, (C)ast Spell, or (R)un? ").lower()

        if choice == 'a':
            damage = max(0, player.attack - random.randint(0, 3))
            enemy.hp -= damage
            print(f"{player.name} hits {enemy.name} for {damage} damage!")

        elif choice == 'c':
            print("\nAvailable spells:")
            for spell in player.spells:
                info = player.spells[spell]
                print(f" - {spell.capitalize()} (Cost: {info['cost']} MP)")
            selected = input("Which spell do you want to cast? ").lower()
            player.cast_spell(selected, enemy)

        elif choice == 'r':
            print(f"{player.name} runs away!")
            return
        else:
            print("Invalid choice!")

        # Enemy attacks if still alive
        if enemy.is_alive():
            enemy_damage = max(0, enemy.attack - player.defense)
            player.hp -= enemy_damage
            print(f"{enemy.name} hits back for {enemy_damage} damage!")

    if player.is_alive():
        print(f"\n{player.name} defeated {enemy.name}!")
        player.gain_exp(enemy.exp)
    else:
        print("\n💀 You have fallen in battle...")


def main():
    name = input("Enter your hero's name: ")
    player = Player(name)

    print(f"\nWelcome, {player.name}! Your quest begins...\n")

    while player.is_alive():
        enemy_type = random.choice([
            NPC("Goblin", 30, 5, 10),
            NPC("Skeleton", 40, 7, 15),
            NPC("Wolf", 35, 6, 12)
        ])
        fight(player, enemy_type)
        if not player.is_alive():
            break
        continue_adventure = input("\nDo you want to continue adventuring? (y/n): ").lower()
        if continue_adventure != 'y':
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
