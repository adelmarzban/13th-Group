# this program is RPS game simulator#
import random

i = 0
player = 0
pc = 0

# the list of option that player or pc can select them#
opt = ["Rock", "Paper", "Scissor"]

# Making ensure that player enter a valid value#
try:
    no_turn = int(float(input("please insert your desired turn number=")))
except:
    no_turn = int(float(input("OOPS, You must enter a number, please insert your desired turn number=")))
while i < no_turn:

    # player value will be inputted #
    player_choice = int(float(input(""" Rock =0, Paper = 1, Scissor=2
                                    chose an option:""")))
    if player_choice > 2:
        print("OOPS, insert a number less than 3")
    while player_choice > 2:
        player_choice = int(float(input(""" Rock =0, Paper = 1, Scissor=2
                                        chose a new option again:""")))

    player_choice = opt[player_choice]

    # else: my_choice2= int(input(""" Rock =0, Paper = 1, Scissor=2 ,         chose a new option:""" ))
    print("Player choice is = ", player_choice)
    pc_choice = opt[(random.randint(0, 2))]
    print("PC choice is= ", pc_choice)

    # calculation the result #
    if player_choice == pc_choice:

        print("you=", player, "pc=", pc)

    elif player_choice == "Scissor" and pc_choice == "Paper":
        player = player + 1
        print("you=", player, "pc=", pc)

    elif player_choice == "Paper" and pc_choice == "Rock":
        player = player + 1
        print("you=", player, "pc=", pc)

    elif player_choice == "Rock" and pc_choice == "Scissor":
        player = player + 1
        print("you=", player, "pc=", pc)

    elif player_choice == "Paper" and pc_choice == "Scissor":
        pc = pc + 1
        print("you=", player, "pc=", pc)

    elif player_choice == "Scissor" and pc_choice == "Rock":
        pc = pc + 1
        print("you=", player, "pc=", pc)
    i = i + 1

# final printing the result #
print("=" * 30)
if pc == player:
    print("the game has no winner")
elif player > pc:
    print("You win!")
else:
    print("the are not winner")
print("=" * 30)

print("Thanks for Playing. See You Again!")