import random
import collections

words_list = []

for i in open("words.txt", "r").read().split('\n'):
    if len(i) == 5:
        words_list.append(i)

possible_letters = []
definitive_letters = ['','','','','']
negative_letters = []
guessed_letters = []
game_running = True
word_to_guess = "train"


while True:

    if word_to_guess == '':
        word_to_guess = random.choice(words_list)
        print(word_to_guess)


    for guess_number in range(1, 7):
        print(guess_number)
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
                word_to_guess = "train"
                print('Alright, going again.')
                continue

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
                if len(word_list) <= 6 - guess_number:
                    game_running = False
                if score > highest_score:
                    best_word = word
                    highest_score = score


            if game_running and guess_number != 5:
                print(best_word)
                word_to_guess = best_word
            else:
                guessed = False
                for i in word_list:
                    print(i)
                    d = input('> ')


