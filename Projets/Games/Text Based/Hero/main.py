from character import Player, Computer

def main():
    player1 = Player(name="Player 1", health=100)
    player2 = Computer(name="Player 2", health=100)
    round=1
    while True:
        
        print(f"Round {round}, attack")

        player1.attack(player2)
        player2.attack(player1)
        input()
        round += 1

if __name__ == "__main__":
    main()