import pyautogui
import time
from PIL import ImageGrab
import sys
import subprocess
words_list = []

#WordGuessr
#x = [740, 833, 920, 1013, 1100]
#y = [350, 430, 510, 590, 660, 740]
#white = (0, 0, 0)
#green = (0, 124, 0)
#yellow = (255, 165, 0)

#Squabble
x = [805, 884, 957, 1010, 1087]
y = [404, 477, 555, 624, 700, 773]
white = (155, 93, 247)
green = (46, 216, 60)
yellow = (214, 190, 0)

word_starter = "forts"

#pyautogui.keyDown('alt')
#time.sleep(.1)
#pyautogui.press('tab')
#time.sleep(.1)
#pyautogui.keyUp('alt')

for i in open("words.txt", "r").read().split('\n'):
    if len(i) == 5:
        words_list.append(i)


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
    word_to_guess = word_starter

    final_guess_number = 0
    guessing_stage = 0 # 0 is guessing, 1 is definitive, 2 is guessed

    while guessing_stage != 2:
        guess_number += 1
        if guessing_stage == 1:
            print('> ' + word_list[final_guess_number])
            pyautogui.write(word_list[final_guess_number])
            pyautogui.press('enter')
            time.sleep(1)
            color_data = ''
            final_guess_number += 1
            time.sleep(1)
            im = ImageGrab.grab()
            for color_x in x:
                clr = im.getpixel((color_x,y[guess_number-1]))
                print(clr)
                if clr == white:
                    color_data += 'b'
                if clr == yellow:
                    color_data += 'y'
                if clr == white:
                    color_data += 'b'
            print(color_data)
            new_color_info = color_data
            if new_color_info == 'ggggg':
                possible_letters = []
                definitive_letters = ['','','','','']
                negative_letters = []
                guessed_letters = []
                game_running = True
                guessing_number = 0
                final_guess_number = 0
                word_to_guess = word_starter
                print(f'Alright, going again. Got it in {guess_number} guesses!')
                guessing_stage = 2
        else:
            if guess_number == 1:
                print(word_to_guess)
                pyautogui.write(word_to_guess)
                pyautogui.press('enter')
            if guess_number == 6:
                print(word_list[0])
                pyautogui.write(word_list[0])
                pyautogui.press('enter')
            else:
                word_list = []
                new_word_info = word_to_guess
                color_data = ''
                time.sleep(1)
                im = ImageGrab.grab()
                #agars
                # im.show()
                for color_x in x:
                    clr = im.getpixel((color_x,y[guess_number-1]))
                    if clr == white:
                        color_data += 'b'
                    if clr == green:
                        color_data += 'g'
                    if clr == yellow:
                        color_data += 'y'
                new_color_info = color_data

                print(new_color_info)
                if new_color_info == 'ggggg':
                    possible_letters = []
                    definitive_letters = ['','','','','']
                    negative_letters = []
                    guessed_letters = []
                    game_running = True
                    word_to_guess = word_starter
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
                
                if len(word_list) == 1:
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
                    pyautogui.write(best_word)
                    pyautogui.press('enter')
                    word_to_guess = best_word
                
                


