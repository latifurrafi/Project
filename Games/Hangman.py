import random

word_list = ["python", "programming", "hangman", "developer", "algorithm"]

def choose_word():
    return random.choice(word_list)
    
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1:
            print("Please guess only one letter at a time.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")

            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        print(display_word(word, guessed_letters))
        
    if attempts == 0:
        print("\nOut of attempts! The word was:", word)

hangman()
