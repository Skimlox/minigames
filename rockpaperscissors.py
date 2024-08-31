import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

def computer_choice():
    return random.choice(game_images)

def user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice == "rock":
            return rock
        elif choice == "paper":
            return paper
        elif choice == "scissors":
            return scissors
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"

    if (user_choice == rock and computer_choice == scissors) or \
       (user_choice == paper and computer_choice == rock) or \
       (user_choice == scissors and computer_choice == paper):
        return "You win!"

    return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    user_choice = user_choice()
    computer_choice = computer_choice()

    print(f"\nYour choice:\n{user_choice}")
    print(f"Computer's choice:\n{computer_choice}")

    result = winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()