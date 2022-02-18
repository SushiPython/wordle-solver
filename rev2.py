import pyautogui as pg
import collections

words_list = []

# Get all of the words, add them to the words_list array
for i in open("wordle-solver/words.txt", "r").read().split('\n'):
    if len(i) == 5:
        words_list.append(i)

starting_guess = "train"


# Set restrictions for the word
definitive_letters = ['', '', '', '', '']
possible_letters = []
guessed_letters = []
negative_letters = []
remaining_words = words_list


current_word = starting_guess

print(starting_guess)
stage = 'narrowing'
guess_index = 0

for guess in range(1, 7):


    print(len(remaining_words))
    print(guessed_letters)
    print(possible_letters)
    print(definitive_letters)
    print(negative_letters)
    # Set game stage
    if len(remaining_words) <= 7 - guess:
        stage = 'guessing'
    
    print(stage)
    if stage == 'narrowing':

        # Get colors for the word
        colors = input('> ')

        # Define the restrictions
        for i in range(0, 5):
            if current_word[i] not in guessed_letters:
                guessed_letters.append(current_word[i])
            if colors[i] == "g":
                definitive_letters[i] = current_word[i]
            if colors[i] == "y" and current_word[i] not in possible_letters:
                possible_letters.append(current_word[i])
            if colors[i] == "b" and current_word[i] not in negative_letters:
                negative_letters.append(current_word[i])

        # Eliminate the impossible words

        for word in words_list:
            for possible_letter in possible_letters:
                if possible_letter not in word and word in remaining_words:
                    remaining_words.remove(word)
            for definitive_index in range(0, 5):
                if definitive_letters[definitive_index] != '' and definitive_letters[definitive_index] != word[definitive_index] and word in remaining_words:
                    remaining_words.remove(word)
            for negative_letter in negative_letters:
                if negative_letter in word and word in remaining_words:
                    remaining_words.remove(word)
            

        # Generate next guess

        best_word = ''
        highest_score = 0

        for word in words_list:
            score = 0
            indice = 0

            # Algorithm for score assignment
            for i in word:
                if i in guessed_letters:
                    score -= 2
                if i not in possible_letters:
                    score += 1
                if i == definitive_letters[indice]:
                    score -= 4
                #if i == collections.Counter(''.join(remaining_words)).most_common(1)[0]:
                #    score += indice*3
                score += len(set(word))
                indice += 1

            if score > highest_score:
                best_word = word
                highest_score = score
            

            
        print(best_word)
        current_word = best_word
    
    elif stage == 'guessing':
        print(remaining_words[guess_index])
        current_word = remaining_words[guess_index]
        guess_index += 1
        
