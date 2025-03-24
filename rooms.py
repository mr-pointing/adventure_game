import random
import character as ch


def roll():
    return random.randint(1, 20)


def room1(character):
    print(f"\nWelcome to room 1 {character.name}")
    # get words to scramble
    words = ['python', 'classes', 'object', 'floats', 'dunder']

    # choose a word to scramble
    word = random.choice(words)

    # scramble the word
    scrambled = ''.join(random.sample(word, len(word)))

    # present to the user and allow to guess
    solved = False
    while character.health > 0 and solved is False:
        print(f"Scrambled: {scrambled}")
        print(character)
        user_guess = input("What do you think the word is? ")
        if user_guess == word:
            print(f"You guessed the word correctly!")
            character.add_to_score(1 * character.health)
            solved = True
        elif user_guess != scrambled:
            character.dec_health(1)
            print("Not it!")
    if character.health == 0:
        print(f"You lost!")
        exit()



def room2(character):
    print(f"\nWelcome to room 2 {character.name}")
    random_num = random.randint(1, 10)
    solved = False
    while character.health > 0 and solved is False:
        print(character)
        user_guess = int(input("Enter a number to guess: "))
        if user_guess < random_num:
            print("Too low!")
            character.dec_health(2)
        elif user_guess > random_num:
            print("Too high!")
            character.dec_health(2)
        elif user_guess == random_num:
            print("You guess the number correctly!")
            character.add_to_score(1 * character.health)
            solved = True
    if character.health == 0:
        print(f"You lost!")
        exit()


def room3(character):
    print(f"\nWelcome to room 3 {character.name}")
    print("There is an evil wizard in the room. You must defeat him to pass on.")
    wizard = ch.Character("Wizard", 100)

    # Battle Loop Starts
    turn = 1
    while character.health > 0 and wizard.health > 0:
        print(character)
        print(wizard)
        print(f"Turn: {turn}")
        user_turn = input("What do you want to do?\nRoll\nInventory")
        if user_turn == "Roll":
            user_roll = input("Ready to roll? (y/n) ")
            if user_roll == 'y':
                num = roll()
                if num == 20:
                    print("Perfect roll! Killed the wizard in one shot")
                    wizard.dec_health(100)
                    character.add_to_score(1 * character.health)
                    break
                elif 20 > num >= 15:
                    print("Nice roll! Hit the wizard for 20 damage")
                    wizard.dec_health(20)
                    character.add_to_score(20)
                    turn += 1
                elif 14 > num >= 9:
                    print("Good roll! Hit the wizard for 10 damage")
                    wizard.dec_health(10)
                    character.add_to_score(20)
                    turn += 1
                else:
                    print("Bad roll! Wizard hits you for 3 damage")
                    character.dec_health(3)
                    turn += 1

    if character.health <= 0:
        print(f"You lost!")
        exit()


def room4(character):
    print(f"\nWelcome to room 4 {character.name}")

    zodiacs = {
        'taurus': "Stubborn Bull",
        'capricorn': 'Quiet, but calculating'
    }

    for zodiac in zodiacs:
        print(zodiac)

    user_f = input("Pick a word to retrieve your zodiac sign: ")

    if user_f in zodiacs:
        print(zodiacs[user_f])