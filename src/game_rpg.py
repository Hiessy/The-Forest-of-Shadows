
from game_engine import GameEngine

def main():
    game = GameEngine("Hero")
    print("Welcome to the Forest!")

    while game.is_player_alive():
        input("Press Enter to explore...")
        if game.check_for_encounter():
            print(f"You encountered a {game.get_enemy_stats()['name']}!")
            log = game.engage_combat()
            for line in log:
                print(line)
        else:
            print("Nothing here...")

        print("Your stats:", game.get_player_stats())
        print("-" * 40)

    print("Game Over.")

if __name__ == "__main__":
    main()