import random
item_list =["Rock", "paper","Scissor"]
user_choice =input("enter your move = Rock,paper,Scissor")
comp_choice =random.choice(item_list)
print(f"user choice = {user_choice}.\ncomputer choice={comp_choice}")
if user_choice == comp_choice :
    print("Both chosses same : = Match Tie")
elif user_choice == "Rock":

    if comp_choice == "paper":
        print("paper covers Rock = computer win")
    else:
            print("Rock smases Scissor = you win")
elif user_choice == "paper":

    if comp_choice == "Rock":
        print("paper covers Rock = computer  win")
    else:
            print("Scissor cuts paper = you win")
elif user_choice == "Scissor":

    if comp_choice == "Rock":
        print("Rock smases Scissor = computer  win")
    else:
            print("Scissor cuts paper = you win")