# this program is a RPS game simulator#
import random

i = 0
player = 0
pc = 0

opt = ["Rock", "Paper", "Scissor"]
no_turn = int(float(input("please insert your desired turn number=")))
while i < no_turn:
    player_choice = int(float(input(""" Rock =0, Paper = 1, Scissor=2
                                    chose an option:""")))
    if player_choice > 2:
        print("insert a number less than 3")
    while player_choice > 2:
        player_choice = int(float(input(""" Rock =0, Paper = 1, Scissor=2
                                        chose a new option:""")))

    player_choice = opt[player_choice]

    # else: my_choice2= int(input(""" Rock =0, Paper = 1, Scissor=2 ,         chose a new option:""" ))
    print("your choice is = ", player_choice)
    pc_choice = opt[(random.randint(0, 2))]
    print("PC choice is= ", pc_choice)

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
