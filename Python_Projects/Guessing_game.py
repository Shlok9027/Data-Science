import random



easy_words = ['cat', 'dog', 'apple', 'ball', 'tree', 'tiger', 'house', 'car', 'book', 'sun', 'moon', 'star', 'fish', 'bird', 'cup', 'pen', 'table', 'chair', 'shoe', 'hat']

medium_words = ['python', 'guitar', 'elephant', 'computer', 'bicycle', 'mountain', 'ocean', 'library', 'puzzle', 'jungle', 'desert', 'island', 'castle', 'forest', 'river', 'planet', 'rocket', 'camera', 'diamond', 'festival']    

hard_words = ['encyclopedia', 'architecture', 'philosophy', 'psychology', 'astronomy', 'metamorphosis', 'consciousness', 'transcendence', 'extraordinary', 'phenomenon', 'quintessential', 'juxtaposition', 'idiosyncratic', 'serendipity', 'ephemeral', 'labyrinthine', 'magnanimous', 'obfuscation', 'perpendicular', 'ubiquitous']

print("Welcome to the Amazing Guessing Game!")

print("Choose a difficulty level: EASY, MEDIUM, HARD")


level = input("Enter Difficulty : ").lower()

if level == 'easy':
    secret = random.choice(easy_words)

elif level == 'medium':
    secret = random.choice(medium_words)    
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print("Invalid level. Defaulting to EASY.")
    secret = random.choice(easy_words)



attempts = 0

print("\nGuess the Secret Word?????")

while True:
    guess = input("Enter your guess: ").lower()

    attempts += 1

    if guess == secret:
        print(f'Congratulations! You guessed the word "{secret}" in {attempts} attempts.')
        break
    
    hint = ''
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += '_'

    print("Hint : ", {hint})

print("Thanks for playing the Guessing Game!")