import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'pear', 'grape', 'pineapple', 'strawberry', 'melon']
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts/chances

    print("Welcome to Hangman!")
    print("Try to guess the word within", attempts, "attempts.")

    while attempts > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"
        
        print("\nWord to guess:", guessed_word)

        if guessed_word == word:
            print("\nCongratulations! You guessed the word correctly:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess! You have", attempts, "attempts left.")

            if attempts == 0:
                print("\nSorry, you've run out of attempts. The word was:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing Hangman!")

# Start the game
hangman()
