import random

words = ["python", "apple", "computer", "science", "data"]
word = random.choice(words)

guessed_letters = []
display_word = ["_"] * len(word)
chances = 6

print("🎮 Welcome to Hangman Game!")
print("You have 6 chances to guess the word.")

while chances > 0:
    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Chances left:", chances)

    # WIN check
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        chances -= 1
        print("❌ Wrong guess!")

# LOSE condition
if "_" in display_word:
    print("\n💀 Game Over! The word was:", word)