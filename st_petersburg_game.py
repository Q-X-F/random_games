import random

print("Welcome to the St Petersburg Paradox Program!")
print("Rules of the St Petersburg Game:")
print("* Initial stake is $2")
print("* The number 0 or 1 will be randomly generated with 50% chance for each")
print("* If the number is 0, the stake is doubled and the previous step repeated")
print("* If the number is 1, the game ends and you receive the stake as winnings")
print("The paradox here is that the game's expected winnings is infinite, meaning a mathematically rational agent will pay any finite amount to play it just once.")
print("One might sneakily draw similarities between this paradox and a long-debunked argument for belief in God... I'm looking at you, Pascal.")

def main():
    print("~~~")
    print("Game Demo: the game will be played, the generated numbers displayed and the winnings outputted.")
    response = input("Enter 'x' to skip demo and any other key to continue: ")
    while True:
        if response == "x":
            break
        demo()
        response = input("Enter 'x' to exit demo and any other key to repeat demo: ")

    print("~~~")

    print("Game Rapid Run: the game will be played a certain number of times and the winnings outputted.")
    response = input("Enter 'x' to skip rapid run and any other key to continue: ")
    while True:
        if response == "x":
            break
        rapid()
        response = input("Enter 'x' to exit rapid run and any other key to reset rapid run: ")

    print("~~~")

    print("Gambling mode: You have $p, each game costs $c, you win if you make a total of $T before running out of money to play.")
    response = input("Enter 'x' to skip gambing and any other key to continue: ")
    while True:
        if response == "x":
            break
        gamble()
        response = input("Enter 'x' to finish and any other key to reset gambling: ")

    print("Thank you for visiting this program!")



def demo():
    stake = 2
    generated = []
    while True:
        if random.randint(0,1) != 0:
            generated.append(1)
            print("List of numbers generated: ")
            print(generated)
            print("Total winnings: " + str(stake))
            return
        stake *= 2
        generated.append(0)


def play():
    stake = 2
    while True:
        if random.randint(0,1) == 0:
            return stake
        stake *= 2


def rapid():
    repeats = int(input("Enter number of times the game is to be played: "))
    winnings = []
    total_winnings = 0
    for i in range(repeats):
        winning = play()
        winnings.append(winning)
        total_winnings += winning
    if repeats != 0:
        print("The winnings for each game are:")
        print(winnings)
        print("Total winnings: " + str(total_winnings))
        print("Average winnings per game: " + str(total_winnings / repeats))


def gamble():
    principal = int(input("Enter p, your betting limit in dollars: "))
    cost = int(input("Enter c, the cost to play each game: "))
    total = int(input("Enter T, the amount you reach for a win: "))
    balance = principal
    num_games_played = 0
    winnings = []
    while balance - cost >= 0:
        winning = play()
        winnings.append(winning)
        balance = balance - cost + winning
        num_games_played += 1
        if balance >= total:
            print("You won!")
            break
    else:
        print("You lost.")
    print("Number of games played: " + str(num_games_played))
    print("Winnings for each game: ")
    print(winnings)
    print("Final balance: " + str(balance))


# def pwin(principal, cost, total):
#     # reversed_pwins[i] means the probabilty of winning from $(total-i)
#     reversed_pwins = [1]
#     for i in range(cost):
#         reversed_pwins.append(0)



main()