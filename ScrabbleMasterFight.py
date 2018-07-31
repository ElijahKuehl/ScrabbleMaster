# TODO: make a while loop for quit == false to let the user quit.
from random import randint
from itertools import permutations


def scrabble_master():
    # Makes your input a list of letters, and the same list but without brackets, then finds the length of the word.
    total = 0
    print "\nWelcome to ScrabbleMaster!"
    letters = raw_input("Type your letters here, with no separations. ")
    letters = letters.upper()
    letter_list = list(letters)
    # compact = sorted(letter_list) would just put the letters in an alphabetical order
    compact = ", ".join(letter_list)
    length = len(letters)
    if length > 9:
        print "\nThis word may be too long, it could take forever to get all the outputs. Proceed with caution.\n"

    length, pvalue, do_pts = find_length(length, letter_list)

    scramble(compact, letters, pvalue, total, letter_list, length, do_pts)


def find_length(length, letter_list):
    # TODO: Make it get multiple lengths at once, compare results to english words(Natural language processing)
    # Choices: Random, max and min, original, set, all(Maybe?)
    # Asks the user how long they want their outputs to be, and provides many options.
    choice = raw_input("Same length(L), Random length(R), or Set length(S) in results, or check its Point value(P)? ")
    choice = choice.lower()
    pvalue = 0
    do_pts = False
    if choice == "r":
        length = random_length(length)
    elif choice == "s":
        # TODO: make an error() here, it has to be an integer
        length = input("How long do you need your word to be?")
    elif choice == "p":
        pvalue = points_value(letter_list)
        do_pts = True
    elif choice != "l":
        error()  # choice, "'L','R','S', or 'P'")
        scrabble_master()
    # 'L' will run normally
    return length, pvalue, do_pts


def random_length(length):
    rand_choice = raw_input("Would you like a truly random length(T) or a random length from a range(R)?")
    rand_choice = rand_choice.lower()
    if rand_choice == "t":
        # makes a random output from 2 to the max length.
        if length > 10:
            length = 9
        length = randint(2, length)
    elif rand_choice == "r":
        # Lets the user decide the range they want the random length to be.
        # Note this will only result in one length, not outputs for all the lengths in the range.
        min_rand = input("Type the lowest number in your range.")
        max_rand = input("Type the highest number in your range.")
        if (min_rand > max_rand) or (min_rand < 0) or (min_rand > length):
            error()  # "a min larger than the max, smaller than 0, or larger than your word's length", "a logical min")
            scrabble_master()
        else:
            length = randint(min_rand, max_rand)
    else:
        error()  # rand_choice, "'T' or 'R'")
        scrabble_master()
    return length


def points_value(letters):
    # Calculates the point value the word will have if you play it in Scrabble.
    points = 0
    print ""
    for i in letters:
        if i in ["E", "A", "O", "T", "I", "N", "R", "S", "L", "U"]:
            points += 1
            value = "1"
        elif i in ["D", "G"]:
            points += 2
            value = "2"
        elif i in ["C", "M", "B", "P"]:
            points += 3
            value = "3"
        elif i in ["H", "F", "W", "Y", "V"]:
            points += 4
            value = "4"
        elif i in ["K"]:
            points += 5
            value = "5"
        elif i in ["J", "X"]:
            points += 8
            value = "8"
        elif i in ["Q", "Z"]:
            points += 10
            value = "10"
        else:
            value = "0"
        tile_name = i, " tile! +", value
        tile = "".join(tile_name)
        raw_input(tile)
    return points


def scramble(compact, letters, pvalue, total, letter_list, length, do_pts):
    # Scrambles your input to all possible combinations.
    print "\nYour letters were:", compact
    if do_pts is True:
        print letters, "has a point value of", pvalue, "!\n"
    else:
        print "Scrambling...\n"
        for word in permutations(letter_list, length):
            print ''.join(word)
            total += 1
        print "\nScrambled!"
        print "Length: ", length
        print "Total results:", total
        print "Hopefully you got some words!\n"
    retry = raw_input("Would you  like to put in a new word? Yes(Y) or no(N)?")
    retry = retry.lower()
    if retry == "y":
        print ""
        scrabble_master()
    else:
        print "\nThank you for using ScrabbleMaster. Please come back another time!"


# Normal error here:
# def error(typed, expect):
#     # Old ScrabbleMasterFight used to be here. Now tells you what you did wrong
#     print "\nERROR, INVALID INPUT."
#     print "You typed", typed, "when we expected", expect, "."
#     raw_input("")
#     scrabble_master()


def error():
    # Will begin the secret boss fight when an input doesn't make sense.
    raw_input("\nERROR> INVALID SYNTAX>")
    raw_input("PREPARE FOR BATTLE>")
    raw_input("\nScrabble Master, The Final Boss has been summoned!")
    raw_input("\n   YOU CANNOT DEFEAT ME!\n")
    action()


def action():
    print "What would you like to do?"
    actions = raw_input("Attack   Item   Run")
    actions = actions.lower()

    if actions in ["a", "attack"]:
        attack()
    elif actions in ["i", "item"]:
        item()
    elif actions in ["r", "run"]:
        run()
    else:
        print "\n   What... what are you trying to do?\n"
        action()


def attack():
    # Takes the word you type, and converts it to Scrabble points.
    points = 0
    count = 0
    attack_word = raw_input("\nWhat word do you want to attack Scrabble Master with?")
    attack_word = attack_word.upper()
    attack_list = list(attack_word)
    print "You fire the word", attack_word, "in the form of Scrabble tiles at Scrabble Master."
    raw_input("")
    for i in attack_list:
        if i in ["E", "A", "O", "T", "I", "N", "R", "S", "L", "U"]:
            points += 1
            value = "1"
        elif i in ["D", "G"]:
            points += 2
            value = "2"
        elif i in ["C", "M", "B", "P"]:
            points += 3
            value = "3"
        elif i in ["H", "F", "W", "Y", "V"]:
            points += 4
            value = "4"
        elif i in ["K"]:
            points += 5
            value = "5"
        elif i in ["J", "X"]:
            points += 8
            value = "8"
        elif i in ["Q", "Z"]:
            points += 10
            value = "10"
        else:
            value = "0"
        tile_name = i, " tile! +", value
        tile = "".join(tile_name)
        raw_input(tile)
        count += 1
    print "\nIt has a strength of", points
    # Only specific words can defeat scrabblemaster, like 'SCRABBLEMASTER' or 'SCRABBLEBEGONE.'
    if 21 < points < 24 and count == 14:
        raw_input("It was enough to defeat Scrabble Master!")
        print""
        win()
    else:
        # Scrabble Master retaliates by doing the purpose of the program.
        raw_input("It wasn't enough to defeat Scrabble Master!")
        raw_input("\n   WHAT WAS THAT? IT WAS PATHETIC!")
        raw_input("   NO MATTER, IT'S MY TURN TO ATTACK!")
        counter()
        raw_input("\nScrabble Master decided to fire all of the outputs you wanted, at maximum settings.")
        raw_input("\n   GO MY SCRAMBLERS!\n")
        for word in permutations(attack_list):
            words = ''.join(word)
            print words, "+", points, "\n"
        while count > 0:
            points *= count
            count -= 1
        print "Point value:", points, "\n"
        if points > 10:
            raw_input("   HOPEFULLY YOU GOT SOME WORDS! HAHAHAHA!")
            raw_input("\nScrabble Master has defeated you.")
            retry = raw_input("Would you like to try again? (Y)es or (N)o?")
            retry = retry.lower()
            if retry in ["y", "yes"]:
                error()
            else:
                print "Goodbye."
        else:
            raw_input("   WHAT? IT WASN'T ENOUGH?")
            raw_input("   BAH, IT DOESN'T MATTER.\n")
            action()


def item():
    # Ends quickly, didn't know what else to happen.
    raw_input("\nYou pick up a letter tile to consume. It's hard, and hurts to bite, as it is made of plastic.")
    raw_input("\n   OH SO IT'S TILES YOU WANT? WELL I HAVE PLENTY!")
    counter()
    raw_input("   IF I LEAVE, YOU CAN'T DEFEAT ME!")
    raw_input("\nScrabble Master just went away.")
    raw_input("You didn't technically lose, but you didn't technically win either.")
    retry = raw_input("Would you like to chase after him? Yes(Y) or no(N)?")
    retry = retry.lower()
    if retry == ["n", "no"]:
        print "Goodbye."
    elif retry in ["y", "yes"]:
        print "\n   OH YOU WANT MORE THEN? WELL HAVE AT IT!\n"
        action()
    else:
        error()


def run():
    # Will put you on an infinite loop until you type 'SCRABBLEBEGONE.'
    luck = 777
    raw_input("\n   YOU CANNOT ESCAPE!")
    counter()
    while True:
        loop = randint(1, 1000)
        if loop < 100:
            loop_break = raw_input("\n\n   IT'S AN INFINITE LOOP!")
            luck -= 1
        elif 101 < loop < 200:
            loop_break = raw_input("\n\n   HAHAHA!")
            luck -= 1
        elif 201 < loop < 300:
            loop_break = raw_input("\n\n   YOU CANNOT RUN!")
            luck -= 1
        elif 301 < loop < 400:
            loop_break = raw_input("\n\n   IT WILL NEVER BE YOUR TURN!")
            luck -= 1
        elif 777 < loop < luck:
            # This hint is more likely to appear the more blank spaces you get.
            print "   JUST DON'T TYPE 'SCRABBLEBEGONE'"
            loop_break = raw_input("\n\n\n\n\n\n\n\n\n")
        else:
            loop_break = raw_input("")
            luck += 1

        if loop_break.lower() == "scrabblebegone":
            win()
            break


def counter():
    raw_input("   GO MY TILES!")
    raw_input("\nTiles fly at you. They are a minor annoyance.")
    raw_input("\n   BAH! THIS ISN'T WORKING!")
    raw_input("   AH! I KNOW!")


def win():
    raw_input("   NOOOOO! HOW IS THIS POSSIBLE!")
    raw_input("   HOW COULD I BE DEFEATED!")
    raw_input("   I ONCE AGAIN RETURN TO MY REALM!")
    raw_input("   TRAPPED FOR AN ETERNITY!")
    raw_input("   NOOOOOOOOOOOOoooo....")
    raw_input("\nCongratulations! You have defeated Scrabble Master!")
    yorn = raw_input("Would you like to try again? (Y)es or (N)o?")
    if yorn.lower in ["y", "yes"]:
        raw_input("Just try not to summon him again, okay?")
        scrabble_master()
    else:
        raw_input("Thank you for playing ScrabbleMaster! Please come back another time!")
        quit()


if __name__ == "__main__":
    scrabble_master()
