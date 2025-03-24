import character as ch
import rooms as r

if __name__ == '__main__':
    # Start game
    username = input("Enter a name: ")
    main_character = ch.Character(username, 10)

    # Room 1

    r.room1(main_character)

    # Room 2
    r.room2(main_character)

    # Room 3
    r.room3(main_character)

    if main_character.health > 0:
        print("Nice job, you made it out alive!")
        print("You made it out keeping your sanity!")

