from appJar import gui
from itertools import permutations


def press(button):
    if button == "Scramble":
        value()

    elif button == "Stop value":
        app.showScale("Stop at: ")
        app.showButton("Close")
        app.hideButton("Stop value")
    elif button == "Close":
        app.hideScale("Stop at: ")
        app.hideButton("Close")
        app.showButton("Stop value")

    elif button == "Length":
        app.showScale("Length: ")
        app.showButton("Close ")
        app.hideButton("Length")
    elif button == "Close ":
        app.hideScale("Length: ")
        app.hideButton("Close ")
        app.showButton("Length")

    elif button == "Reset":
        app.hideScale("Length: ")
        app.showButton("Length")
        app.hideScale("Stop at: ")
        app.showButton("Stop value")
        app.hideButton("Close")
        app.hideButton("Close ")
        app.setScale("Length: ", 0)
        app.setScale("Stop at: ", 10000)
        app.clearTextArea("Scrambled")
        app.clearEntry("Letters: ")
        app.setLabel("pts", "")
        app.setLabel("Total", "")

    elif button == "Quit":
        app.stop()


def value():
    letters = app.getEntry("Letters: ")
    longer = len(letters)
    letters = letters.upper()
    letter_list = list(letters)
    length = app.getScale("Length: ")
    length = int(length)
    points = 0
    total = 0
    stop = app.getScale("Stop at: ")
    app.clearTextArea("Scrambled")

    if length > longer:
        app.setTextArea("Scrambled", "Error: Length is longer than the provided letters. Set Length to 0 for max length")

    else:
        if length == 0:
            length = longer
        for word in permutations(letter_list, length):
            results = ''.join(word)
            app.setTextArea("Scrambled", results)
            app.setTextArea("Scrambled", "\n")
            if total == stop and stop != 0:
                limit = ["Stopped at", str(stop), "results."]
                limit = " ".join(limit)
                app.setTextArea("Scrambled", limit)
                break
            total += 1
        total_txt = ["Total results: ", str(total)]
        total_txt = ' '.join(total_txt)
        app.setLabel("Total", total_txt)
        app.showLabel("Total")
        points = str(points_value(points, letter_list))
        points_txt = ['"', letters, '" has a point value of ', points, '.']
        compact = "".join(points_txt)
        app.setLabel("pts", compact)
        app.showLabel("pts")


def points_value(points, letters):
    for i in letters:
        if i in ["E", "A", "O", "T", "I", "N", "R", "S", "L", "U"]:
            points += 1
        elif i in ["D", "G"]:
            points += 2
        elif i in ["C", "M", "B", "P"]:
            points += 3
        elif i in ["H", "F", "W", "Y", "V"]:
            points += 4
        elif i in ["K"]:
            points += 5
        elif i in ["J", "X"]:
            points += 8
        elif i in ["Q", "Z"]:
            points += 10
    points = str(points)
    return points


app = gui("Scrabble Master", "700x550")
app.setBg("#E0D6A3")
app.setFont(18)

app.addLabel("title", "Welcome to ScrabbleMaster")
app.setLabelBg("title", "#297929")

app.addLabelEntry("Letters: ")
app.setFocus("Letters: ")
app.setEntryBg("Letters: ", "#FFFFE3")

app.addLabelScale("Length: ")
app.setScaleRange("Length: ", 0, 50)
app.showScaleIntervals("Length: ", 5)
app.setScaleBg("Length: ", "#99D6EB")
app.hideScale("Length: ")

app.addLabelScale("Stop at: ")
app.setScaleRange("Stop at: ", 0, 50000, curr=10000)
app.showScaleIntervals("Stop at: ", 10000)
app.hideScale("Stop at: ")
app.setScaleBg("Stop at: ", "#FF8484")

app.addButtons(["Close ", "Close"], press)
app.hideButton("Close")
app.setButtonBg("Close", "#FF8484")
app.hideButton("Close ")
app.setButtonBg("Close ", "#99D6EB")

app.addButtons(["Length", "Stop value"], press)
app.setButtonBg("Stop value", "#FF8484")
app.setButtonBg("Length", "#99D6EB")

app.addButtons(["Reset", "Scramble", "Quit"], press)
app.setButtonBg("Reset", "#FF5050")
app.setButtonBg("Scramble", "#FFFFE3")
app.setButtonBg("Quit", "#0099CC")

app.addLabel("pts", "")

app.addLabel("Total", "")

app.addScrolledTextArea("Scrambled")
app.setTextAreaFont("Scrambled", size=18)
app.setTextAreaBg("Scrambled", "#F0EBB8")

app.addLabel("Buffer", "")

app.go()
