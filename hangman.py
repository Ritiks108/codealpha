import random
def choose_word():
    words = ["python", "hangman", "programming", "developer", "computer",]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum incorrect guesses allowed

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good job! That letter is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return "win"
    
    print("\nGame over! The word was:", word)
    return "lose"

if __name__ == "__main__":
    hangman()