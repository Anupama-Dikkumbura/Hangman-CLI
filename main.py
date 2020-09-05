import sys
import random

while True:
    file = open('words.txt', 'r').read().split('\n')

    word = file[random.randint(0, len(file))]
    guessing = '*' * len(word)
    attempts = 3

    while attempts > 0:
        print("==========================")
        print(f"word: {guessing}")
        print(f"Attempts left: {attempts}")
        print("==========================")
        guess = input("Guess: ")

        for i in range(len(word)):
            if word[i] == guess:
                if guessing[i] == '*':
                    temp = list(guessing)
                    temp[i] = guess
                    guessing = "".join(temp)
                    break
        else:
            attempts -= 1
            failed_attempts = 1
        if guessing.find('*') == -1:
            cont1 = input(f"Your won !! word is '{guessing}'. Play Again? (y/n)")
            if cont1.lower() == 'y':
                break
            else:
                sys.exit()
    else:
        cont = input(f"You Failed! word is '{word}'. Try again?(y/n) ")
        if cont.lower() == 'n':
            print("Bye.....!!!")
            sys.exit()
