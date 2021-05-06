from random import choice
from time import sleep

with open("wordlist.txt", "r", encoding="UTF-8") as file:
    words = file.readlines()

word = choice(words)[:-1]

allowed_mistakes = 7
guesses = []
guesses_str = ""
done = False

while not done:

    print("A palavra é a seguinte: ")
    # Prints the word in the console
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end =" ")
    sleep(1)
    print("\n##################################################")
    print(f"Tentativas restantes: {allowed_mistakes}")
    guesses_str = ", ".join(guesses)
    print(f"Letras já sugeridas: {guesses_str}")
    print("##################################################")
    sleep(1)
    guess = input("Digite uma letra: ")

    # checks if the user inputted a correct letter
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_mistakes -= 1
        # if they run out of allowed mistakes, then they lost the game.
        if allowed_mistakes == 0:
            break

    done = True

    # checks if there's still some letters to be discovered.
    # we could use here a variable to inform the user how much letters
    # there are still to be discovered. But this would make the game easier so...
    # we won't do it now. Maybe
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"UHUU VOCÊ ACERTOU E SALVOU O ZÉZINHO! A palavra era: {word}")
else:
    print(f"VOCÊ DEIXOU O ZÉZINHO MORRER, SEU MALDITO!!\nA PALAVRA ERA: {word}")
