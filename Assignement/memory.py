import random
import os
import time

class MemoryGame:
    def __init__(self):
        # Initialize variables to store sequence, length, and difficulty
        self.sequence = []
        self.length = 0
        self.difficulty = ""
        self.score = 0

    def generate_sequence(self):
# Generate a sequence of numbers or letters based on difficulty level            
        self.sequence = []        
        if self.difficulty == "e":
            self.sequence = [str(random.randint(1, 9)) for _ in range(self.length)]
        elif self.difficulty == "m":
            self.sequence = [str(random.randint(41, 99)) for _ in range(self.length)]
        elif self.difficulty == "h":
            self.sequence = [random.choice([str(random.randint(0, 9)), random.choice('abcdefghijklmnopqrstuvwxyz')]) for _ in range(self.length)]

    def display_sequence(self):
        """
        Display the sequence of numbers or letters.
        """
        print("Remember the sequence displayed on the screen ")
        print(" ".join(map(str, self.sequence)))
         # Wait for some time to let the player memorize the sequence
        time.sleep(2)
        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def getPlayerGuess(self):
        # Get the player guess for the sequence
        print("\nEnter your guess")
        guess = input().split()
        if len(guess) != self.length:
            print(f"Please enter {self.length} {'number' if self.length == 1 else 'numbers or letters'}")
            return self.getPlayerGuess()
        return guess

    def checkGuess(self, guess):
        # Check if player's guess matches the sequence
        return self.sequence == guess

    def update_score(self, correct_guess):
        """
        Update the score based on whether the player's guess is correct.
        """
        if correct_guess:
            self.score += 1
        else:
            self.score -= 1

    def play(self):
        # Message to start the game
        print("Welcome to the Memory game:")
        print("-------------------------------------------------------------")
        print("You will be given a sequence ofnumbers or letters to remember")
      
        while True:
         self.length = int(input("Enter the length of the sequence you would like to remember and press enter "))
          
         while True:
            self.difficulty = input("Choose difficulty (easy, medium, hard) enter e, m or h: ").lower()
            if( self.difficulty == "e" or self.difficulty == "m" or self.difficulty == "h"):
              break  
       
         
        # Generate the sequence
         self.generate_sequence()
          
        # Display the sequence for the player to memorize
         self.display_sequence()
          
        # Waiting time for the player to remember the sequence
         input("Please press Enter to continue")
          
        # Shuffle the sequence for the player to guess
#         random.shuffle(self.sequence)
         print("\nNow guess the sequence. Enter each number with a space in between ")
          
        # Continue until the player guesses the correct sequence
         player_guess = self.getPlayerGuess()
         correct_guess = self.checkGuess(player_guess)
         self.update_score(correct_guess)
         if correct_guess:
          print("WOW ! Congratulations! You are the best")
          print(f"Your score: {self.score}")
         else:
          print("Bad luck - Incorrect guess.")
          print(f"Your score: {self.score}")
         print("WOuld you like to continue y/n ?")
         choice = input().lower()
         self.length = 0         
         if choice == 'n':
          print("Bye - see you next time")
          break
            
# Instantiate and play the game
game = MemoryGame()
game.play()

