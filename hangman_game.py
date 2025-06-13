import random

print('\n 💻 Welcome to Hangman!')

choices= ['python','algorithm','developer','iteration','conditions','programming']
words = random.choice(choices)

attempts = 6 
word_display =['_' for alphabets in words]

def state():
    print(f"attempts = {attempts}")
    print(' '.join(word_display))

while attempts > 0 and '_' in word_display:
    state()
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in words:
        for index, letter in enumerate(words):
            if letter == guess:
                if word_display[index] == '_':    # Check if the letter hasn't already been revealed
                    word_display[index] = guess 
                else:
                    print(f'👉 You already guessed the letter " {guess} ", Try again.')    
    else: 
        print("⭕ Incorrect. Try again.")
        attempts -= 1
    
    # Check for win condition
    if '_' not in word_display:
        state()
        print("🏅Congratulations, you won! ")
        break

# If loop ends because of running out of attempts
if attempts == 0:
    state()
    print(f" You lost. The word was:, {words} ✔️")

