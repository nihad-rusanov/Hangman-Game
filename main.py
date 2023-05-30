import random

words = ["apple", "caar", "phonee"]
running = True
life = 3


word = random.choice(words)

print(word)

display = []

for _ in range(len(word)):
    display.append("_")

print(display)

while running:
    # Get a guess
    guess = input("what is your guess: ")

    # Check guess
    if guess in word:
        for index in range(len(word)):
            if guess == word[index]:
                display[index] = guess
    else:
        life -= 1

    # Check game
    if "_" not in display:
        print("You WIN")
        running = False

    if life == 0:
        print("You LOST")
        running = False

    print(display)

