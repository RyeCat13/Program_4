'''Rye Ledford - Comp Science Lab 101 - Reels and bets'''

import random 
if __name__ == '__main__':
    spins = 1

    def main():
        spins = 1

while True:
    bank = int(input('How many chips do you want to start with? ==> '))
    if bank <= 0:
        print('Too low a value, you can only choose 1 - 100 chips')
        continue
    elif bank >= 101:
        print('Too high a value, you can only choose 1 - 100 chips')
        continue
    else:
        break

while True:
    chips = int(input('How many chips do you want to wager? ==> '))
    for wager in range (-110, chips):
        if (chips <= 0):
            print('The wager amount must be greater than 0. Please enter again.')
            continue
        elif (chips > bank):
            print('The wager amount cannot be greater than how much you have.', bank)
            continue
        else:
            break

    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10) 

    def matches(reel1, reel2, reel3):
        total_matches = 0 
        if reel1 == reel2:
            total_matches += 2
        elif reel1 == reel3:
            total_matches += 1
        elif reel1 == reel3:
            total_matches += 2
        elif reel2 == reel3:
            otal_matches += 1
        else:
            total_matches = 0
        return total_matches

    payout = 0
    total_matches = 0
    pay = 0
    total_payout = 0
    total_wager = 0

    def real_matches(payout):
        if total_matches == 3:
            pay == (chips * 10) - chips
        elif total_matches == 2:
            pay == (chips * 3) - chips
        else:
            pay == chips - (chips * 2)
        return total_payout

    total_bank = pay + bank
    total_bank = bank - chips
    bank = total_bank


    while True:

        total_matches = matches(reel1, reel2, reel3)
        payout_won = real_matches(payout)

        print('Your reels were,', reel1, reel2, reel3)
        print('You matched', real_matches(chips), 'reels')
        print('You won/lost', chips)
        print('Current bank', bank)
        print()
        print('The most chips you had was', bank)
        spins += 1
        break


    while True:
        user_input = input('Play again?\n')
        if user_input == 'Y' or 'Yes':
            main()
        elif user_input == 'N' or 'No':
            break
        else:
            continue

    while False:
        print('You lost all', bank, 'in', spins, 'spins')

main()
