import random


def get_name():
  name = input("Enter your name: ")
  display_name = name[0].upper() + name[1:]
  return display_name


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissor"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer, display_name):
    print(f"You chose {player}, Computer chose {computer}")

    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "paper":
            return f"Paper covers rock, {display_name} lost"
        if computer == "scissors":
            return f"Rock smashes scissors, {display_name} won!"
    elif player == "paper":
        if computer == "rock":
            return f"Paper covers rock, {display_name} won"
        if computer == "scissors":
            return f"Scissors cuts paper, {display_name} lost!"
    elif player == "scissors":
        if computer == "rock":
            return f"Rock smashes scissors, {display_name} lost"
        if computer == "paper":
            return f"Scissors cuts paper, {display_name} won!"


player_name = get_name()
choices = get_choices()

result = check_win(choices["player"], choices["computer"],
                   player_name)  
print(result)
