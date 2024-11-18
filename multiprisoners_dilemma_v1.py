# Version 1 gives more incentive to confess with n years pardoned, suitable for 3+ players, the more the merrier!
print("Welcome to Prisoner's Dilemma - Multiplayer Mode 1")
print("Here we extend the classic Prisoner's Dilemma to more players!")
print("Context:")
print(
    "n members of a gang have been arrested. The police possess evidence of one offense committed by the gang, enabling "
    "them to sentence each member to n years in prison. However, the police has made a bargain with each and every member: "
    "Your part in this offense will be pardoned if you confess to the ongoing criminal activity undertaken by the gang. "
    "Your own confession will not incriminate yourself, but each confession from another member will add TWO years to "
    "your prison sentence."
)
print(
    "Put mathematically, a member's sentence with be 2 * number_of_other_confessions if they confess, and n + 2 * number_of_"
    "confessions if they do not."
)
print("Rules:")
print("The game will take place in rounds. In each round, each player will decide to confess or keep silent. The player's "
      "score in the round will be a negative integer number of years sentenced. This score will be added to the cumulative "
      "score. To stop playing, enter 'e' at the end of a round. To continue playing, enter anything else."
)

players = int(input("Enter number of players: "))

names = []

cumulative_scores = []

for i in range(players):
    names.append(input("Enter name: "))
    cumulative_scores.append(0)

round = 0

def collect_choices(names):
    choices = []
    for name in names:
        while True:
            choice = input(name + ", do you wish to confess(o) or keep silent(x)? ")
            if choice == "o" or choice == "x":
                choices.append(choice)
                break
            print("Invalid input. ", end="")
        for i in range(10):
            print("###")
    return choices

def choices_to_scores(choices):
    num_players = 0  # number of players
    num_comp = 0  # number of players who chose to compete
    round_scores = []  # scores of each player in this round
    for choice in choices:  # counts number of players who chose to compete
        num_players += 1
        if choice == "o":
            num_comp += 1
    for choice in choices:  # calculates score based on choices
        if choice == "x":
            round_scores.append(-num_players - 2 * num_comp)
        else:
            round_scores.append(2 - 2 * num_comp)
    return round_scores

while True:
    print("ROUND " + str(round) + " HAS STARTED!")
    choices = collect_choices(names)
    round_scores = choices_to_scores(choices)
    print("ROUND " + str(round) + " RESULTS:")
    for i in range(players):
        cumulative_scores[i] += round_scores[i]
        print(names[i] + ":")
        print("Choice: " + choices[i] + ", Round score: " + str(round_scores[i]) + ", Total Score: " + str(cumulative_scores[i]))
    if input("Stop playing? Enter 'e'. ") == "e":
        print("Thank you for playing!")
        break
    round += 1


