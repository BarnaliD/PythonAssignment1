import random

#intilise variables to track scores of user and the computer
user_score = 0
computer_score= 0

# Start the game loop
while True:
    # Ask the user for their choice
    user_choice = input("Please enter your choice (rock, paper, scissors): ")
    possible_outcomes = ["rock", "paper", "scissors"]
    #Now computer makes a choice
    computer_choice = random.choice(user_choice)
    #Displaying the computer choice and the user choice
    print(f"\n Hey you chose {user_choice}, computer chose {computer_choice}.\n")
    #Dertermine the outcome of the game and calculate scores
    if user_choice == computer_choice:
        print(f"Both players selected the same{user_choice}.It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Hey,paper covers rock! You win!")
            user_score += 1
        else:
            print("Hey, scissor cuts paper! You lose.")
            computer_score += 1
    elif user_choice == "Scissor":
        if computer_choice == "paper":
            print("Hey,scissor cut paper! You win!")
            user_score += 1
        else:
            print(" Hey,Rock smashes scissor! You lose.")
            computer_score += 1
    #Display the current score
   
    print(f"Your score: {user_score}, Computer's score: {computer_score}")
    
    # Ask the user if they want to play again
    play_again = input("Play again? (y/n): ")
    # If the user chooses not to play again, exit the loop
    if play_again.lower() != "y":
        break


