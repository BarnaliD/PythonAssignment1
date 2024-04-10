import random

def choose_word():
    # List of words to choose from
    words = ['apple', 'Florida', 'Chocolate', 'Jasmine', 'Mountain', 'Crocodile', 'Microwave']
    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        # If the letter has been guessed, show it, otherwise show '_'
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    # Choose a word for the game
    word = choose_word()
    # List to store guessed letters
    guessed_letters = []
    # Maximum attempts allowed
    max_attempts = 6
    # Current number of attempts
    attempts = 0

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    # Main game loop
    while True:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is not in the word
        if guess not in word:
            attempts += 1
            print("Sorry, {} is not in the word.".format(guess))
            print("Attempts left:", max_attempts - attempts)
            # Check if the player has used all attempts
            if attempts >= max_attempts:
                print("You ran out of attempts. The word was:", word)
                break
        else:
            print("Good guess!")

        # Check if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    # Start the game
    hangman()
