import random

def hangman():
    words = {
        "python": "A popular programming language",
        "hangman": "The name of this game",
        "engineer": "A professional who designs and builds things",
        "college": "A place where students study after school",
        "computer": "An electronic device used for programming"
    }

    word, hint = random.choice(list(words.items()))
    display = ["_"] * len(word)
    guessed = set()
    attempts = 6

    print("\n=== Hangman Game ===")
    print(f"Hint: {hint}")
    print(f"The word has {len(word)} letters.")
    print(" ".join(display))

    while attempts > 0 and "_" in display:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter one valid letter.")
            continue
        if guess in guessed:
            print("⚠️ Already tried that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    display[i] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        print(" ".join(display))
        print("Guessed:", " ".join(sorted(guessed)), "\n")

    if "_" not in display:
        print(f"🎉 You won! The word was '{word}'.")
    else:
        print(f"💀 You lost! The word was '{word}'.")

    input("\nPress Enter to exit the game...")  # <-- pause before exit

if __name__ == "__main__":
    hangman()
