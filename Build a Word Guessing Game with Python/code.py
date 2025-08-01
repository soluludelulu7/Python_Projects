import random

wordList = ["rizz", "ohio", "sigma", "tiktok", "skibidi"]
word = random.choice(wordList).lower()

guessedWord = ['_'] * len(word)
attempts = 10
guessedLetters = set()

# Each stage of the hangman (from 10 attempts down to 0)
hangman_stages = [
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |
    ---------
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / 
    |
    ---------
    """,
    """
     _______
    |       |
    |       O
    |      /|\\
    |      
    |
    ---------
    """,
    """
     _______
    |       |
    |       O
    |      /|
    |      
    |
    ---------
    """,
    """
     _______
    |       |
    |       O
    |       |
    |      
    |
    ---------
    """,
    """
     _______
    |       |
    |       O
    |      
    |      
    |
    ---------
    """,
    """
     _______
    |       |
    |       
    |      
    |      
    |
    ---------
    """,
    """
     _______
    |       
    |       
    |      
    |      
    |
    ---------
    """,
    """
     
    |       
    |       
    |      
    |      
    |
    ---------
    """,
    """
    
    
    
        
    
    
    ---------
    """,
]

while attempts > 0:
    print(hangman_stages[10 - attempts])  # Show current hangman state
    print("Guessed letters:", " ".join(sorted(guessedLetters)))
    print("Current word: " + ' '.join(guessedWord))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessedLetters:
        print("You've already guessed that letter.")
        continue

    guessedLetters.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Nice! You got a letter.")
    else:
        attempts -= 1
        print(f"Nope! That letter’s not in the word. Attempts left: {attempts}")

    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word: " + word)
        break
else:
    print(hangman_stages[0])  # Final hangman state
    print("\nYou're out of attempts! The word was: " + word)
