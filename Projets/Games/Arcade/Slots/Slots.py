import random

def get_spin():
    game_symbols = ["🟢", "🔵", "🟣", "🟤", "⚫"]
    return [random.choice(game_symbols) for symbol in range(3)]

def check_spin(spin):
    multipler = 0
    if spin[0]==spin[1]==spin[2]:
        if spin[0]=="🟢":
            multipler += 1
        elif spin[0]=="🔵":
            multipler += 2
        elif spin[0]=="🟣":
            multipler += 3
        elif spin[0]=="🟤":
            multipler += 4
        elif spin[0]=="⚫":
            multipler += 5
    return multipler

def get_winnings(bet,multipler):
    return (bet*multipler)



def main():
    deposit = 100

    print("*******************************")
    print("Welcome to Slots")
    print("Match any of these for winnings")
    print("🟢 🔵 🟣 🟤 ⚫")
    print("*******************************")

    print(f"Balance: {deposit}")

    print("When ready place your bet, Good Luck!")

    while True:
        bet = input("Bet: ")
        
        if bet.isdigit() == False:
            print("false")
            continue
        
        if int(bet) > deposit:
            print("Not enough money, bet again")
            continue
        deposit = deposit-int(bet)
        print(f"Balance: {deposit}")
        print("Spinning.....")

        spin = get_spin()
        print(*spin, sep=" | ")

        multiplier = check_spin(spin)
        winnings = get_winnings(int(bet),multiplier)
        if winnings > 0:
            print(f"You won: {winnings}")
            deposit += winnings
            print(f"Balance: {deposit}")
        else:
            print("You did no win")
            print(f"Balance: {deposit}")

        if deposit ==0:
            print("No money left, Goodbye")
            break
        spin_again= input("Do you wish to spin again [Y/N]: ").upper()
        
        if spin_again != 'Y':
            break

    print("************************************************")
    print(f"Game over, withdrawing {deposit}")
    print("************************************************")

if __name__ == "__main__":
    main()