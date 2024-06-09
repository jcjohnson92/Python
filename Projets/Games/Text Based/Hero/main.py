from character import Character


weapon_choices = '''
1.fists : Price = Free
2.mace : Price = 7
3.sword : Price = 10
4.dagger : Price = 5

'''

def main():
    player1 = Character(name="Player 1", health=100)
    player2 = Character(name="Player 2", health=100)
    round=0
    while True:
     

                



        input()

        # player1.attack(player2,0)
        # player2.attack(player1,1)
        # if player1.health == 0:
        #     print("Player 2 wins")
        # elif player2.health == 0:
        #     print("Playter 1 wins")
        # input()


        round += 1

if __name__ == "__main__":
    main()