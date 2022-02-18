words_list = []

# Get all of the words, add them to the words_list array
for i in open("words.txt", "r").read().split('\n'):
    if len(i) == 5:
        words_list.append(i)

starting_guess = "train"


# Set restrictions for the word
definitive_letters = ['', '', '', '', '']
possible_letters = []
guessed_letters = []

current_word = starting_guess

print(starting_guess)

for letter in starting_guess:
    if letter not in guessed_letters:
        guessed_letters.append(letter)

for guess in range(1, 7):

    # Get colors for the word
    colors = input('> ')

    # Define the restrictions
    for color_index in range(0, 5):
        if color_index == 'g':
            definitive_letters[color_index] = current_word[color_index]
        if color_index == 'y':
            possible_letters.append(current_word[color_index])

    # Eliminate the impossible words
    remaining_words = words_list

    for word in words_list:
        for possible_letter in possible_letters:
            if possible_letter not in word:
                if word in remaining_words:
                    remaining_words.remove(word)
        for definitive_index in range(0, 5):
            if definitive_letters[i] != '?' and definitive_letters[i] != word[i]:
                if word in remaining_words:
                    remaining_words.remove(word)

    # Generate next guess

    for word in words_list:
        score = 0
        for letter in word:
            if letter not in guessed_letters:
                score +=5 
