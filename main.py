<<<<<<< Updated upstream
import random
import collections
from termcolor import colored
=======
import pyautogui
>>>>>>> Stashed changes

words_list = []

for i in open("words.txt", "r").read().split('\n'):
    if len(i) == 5:
        words_list.append(i)

<<<<<<< Updated upstream
color = colored('C', 'red') + colored('O', 'yellow') + colored('L', 'green') + colored('O', 'blue') + colored('R', 'magenta') + colored('S', 'cyan') + colored(' > ', 'white')
possible_letters = []
definitive_letters = ['','','','','']
negative_letters = []
guessed_letters = []
game_running = True
word_to_guess = input(colored('Starting word > ', 'blue'))

if word_to_guess == '':
    word_to_guess = random.choice(words_list)
    print(colored('Alright, try ', 'red') + colored(word_to_guess, 'blue'))


for guess_number in range(1, 7):
    if guess_number == 6:
        print(colored('Alright, try ', 'red') + word_list[0])
    else:
        word_list = []
        new_word_info = word_to_guess
        new_color_info = input(color).lower()
        if new_color_info == 'ggggg':
            print('Good Game!')

        for i in range(0, 5):
            if i not in guessed_letters:
                guessed_letters.append(new_word_info[i])
            if (new_color_info[i]) == "g":
                definitive_letters[i] = new_word_info[i]
            if (new_color_info[i]) == "y":
                possible_letters.append(new_word_info[i])
            if (new_color_info[i]) == "b":
                negative_letters.append(new_word_info[i])       


        reccomended_guess = ''
        reccomended_score = 5
        for word in words_list:
            stage = 0
            for i in range(0,5):
                if definitive_letters[i] == word[i] or definitive_letters[i] == '':
                    stage += 1
            for i in possible_letters:
                if i not in word:
                    stage += -1
            for i in negative_letters:
                if i in word:
                    stage += -1
            if stage == 5:
                word_list.append(word)
        
        best_word = ''
        highest_score = 0

        for word in words_list:
            score = 0
            indice = 0
            for i in word:
                if i in guessed_letters:
                    score -= 2
                if i not in possible_letters:
                    score += 1
                if i == definitive_letters[indice]:
                    score -= 4
                if i == collections.Counter(''.join(word_list)).most_common(1)[0]:
                    score += guess_number*3
                score += len(set(word))
                indice += 1
            #print(f'Word: {word}, Score: {score}')
            if len(word_list) <= 6 - guess_number:
                game_running = False
            if score > highest_score:
                best_word = word
                highest_score = score
                #print('Highest score was ' + str(score))


        if game_running and guess_number != 5:
            print(colored('Try', 'blue'), best_word)
            word_to_guess = best_word
        else:
            it = len(word_list)
            for i in word_list:
                print(colored('Try', 'blue'), i)
                _ = input(color)
                print('Estimated Guesses Remaining: ' + str(it))
                print(len(word_list))
                it -= 1
        guesses_left = 6
        if len(word_list) < 5000:
            guesses_left = 5
        if len(word_list) < 1000:
            guesses_left = 3
        if len(word_list) < 100:
            guesses_left = 2
        
        print('Estimated Guesses Remaining: ' + str(guesses_left))
        print(len(word_list))

    
=======

def generate_colors(guess, real):
    output = ['','','','','']
    for letter_index in range(0, 5):
        if guess[letter_index] in real:
            output[letter_index] = 'y'
        if guess[letter_index] == real[letter_index]:
            output[letter_index] = 'g'
        if guess[letter_index] not in real:
            output[letter_index] = 'b'
    return ''.join(output)

while True:

    guess_number = 0
    possible_letters = []
    definitive_letters = ['','','','','']
    negative_letters = []
    guessed_letters = []
    game_running = True
    word_to_guess = "adieu"

    final_guess_number = 0
    guessing_stage = 0 # 0 is guessing, 1 is definitive, 2 is guessed

    while guessing_stage != 2:
        guess_number += 1
        if guessing_stage == 1:
            print(word_list[final_guess_number])
            new_color_info = input('> ')
            if new_color_info == 'ggggg':
                possible_letters = []
                definitive_letters = ['','','','','']
                negative_letters = []
                guessed_letters = []
                game_running = True
                guessing_number = 0
                final_guess_number = 0
                word_to_guess = "adieu"
                print(f'Alright, going again. Got it in {guess_number} guesses!')
                guessing_stage = 2
        else:
            if guess_number == 1:
                print(word_to_guess)
            if guess_number == 6:
                print(word_list[0])
            else:
                word_list = []
                new_word_info = word_to_guess
                new_color_info = input('> ').lower()
                if new_color_info == 'ggggg':
                    possible_letters = []
                    definitive_letters = ['','','','','']
                    negative_letters = []
                    guessed_letters = []
                    game_running = True
                    word_to_guess = "adieu"
                    print(f'Alright, going again. Got it in {guess_number} guesses!')
                    guessing_stage = 2

                for i in range(0, 5):
                    if i not in guessed_letters:
                        guessed_letters.append(new_word_info[i])
                    if (new_color_info[i]) == "g":
                        definitive_letters[i] = new_word_info[i]
                    if (new_color_info[i]) == "y":
                        possible_letters.append(new_word_info[i])
                    if (new_color_info[i]) == "b":
                        negative_letters.append(new_word_info[i])       


                for word in words_list:
                    stage = 0
                    for i in range(0,5):
                        if definitive_letters[i] == word[i] or definitive_letters[i] == '':
                            stage += 1
                    for i in possible_letters:
                        if i not in word:
                            stage += -1
                    for i in negative_letters:
                        if i in word:
                            stage += -1
                    if stage == 5:
                        word_list.append(word)
                
                if len(word_list) <= 6 - guess_number:
                    guessing_stage = 1
                
                best_word = ''
                highest_score = 0

                for word in words_list:
                    score = 0
                    indice = 0
                    for i in word:
                        if i not in guessed_letters:
                            score += 1.5
                        if i not in possible_letters:
                            score += 1
                        if i == definitive_letters[indice]:
                            score -= 1
                        score += len(set(word))
                        indice += 1
                    if score > highest_score:
                        best_word = word
                        highest_score = score

                

                if guessing_stage == 0 and guess_number != 5:
                    print(best_word)
                    word_to_guess = best_word
                
                


>>>>>>> Stashed changes
