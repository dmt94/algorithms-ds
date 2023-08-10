secret_word = 'rose'
hidden_word = ['_' for char in secret_word]
trial = 0

def char_guess():
    char_guess = input("Guess a letter\n")
    return char_guess

while trial < 3 and '_' in hidden_word: 
    user_guess = char_guess()
    if user_guess not in secret_word:
        trial += 1
        print(trial)
        print('Guess again')
    else:
        indices = [index for index, char in enumerate(secret_word) if char == user_guess]
        for index in indices:
            hidden_word[index] = user_guess
        print(hidden_word)

if '_' not in hidden_word:
    print('Congrats! You guessed the word, ', secret_word)
else:
    print('Game Over!! THe secret word was:', secret_word)