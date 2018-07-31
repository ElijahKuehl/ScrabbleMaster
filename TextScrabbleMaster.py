
# TODO: make a while loop for quit == false to let the user quit. appJar has gui, try it out!
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
        # TODO: make an error() here
        length = input("How long do you need your word to be?")
    elif choice == "p":
        pvalue = points_value(letter_list)
        do_pts = True
    elif choice != "l":
        error(choice, "'L','R','S', or 'P'")
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
            error("a min larger than the max, smaller than 0, or larger than your word's length", "a logical min")
            scrabble_master()
        else:
            length = randint(min_rand, max_rand)
    else:
        error(rand_choice, "'T' or 'R'")
        scrabble_master()
    return length


def points_value(letters):
    # TODO: DOCTEST
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


def error(typed, expect):
    # Old ScrabbleMasterFight used to be here. Now tells you what you did wrong
    print "\nERROR, INVALID INPUT."
    print "You typed", typed, "when we expected", expect, "."
    raw_input("")
    scrabble_master()


if __name__ == "__main__":
    scrabble_master()
