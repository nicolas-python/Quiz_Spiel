#Quiz spiel

spieler = None
score = 0
spieler_list = []
score_list = []

# score und spieler speichern und laden
def load_spieler_list():
    spieler_list.clear()
    with open("spieler_list.txt", "r") as file:
        for save in file:
            spieler_list.append(save)

    return spieler_list

def load_score_list():
    with open("score_list.txt", "r") as file:
        score_list.clear()
        for save in file:
            score_list.append(save)

    return score_list

def save_spieler_list():
    with open("spieler_list.txt", "w") as file:
        for save in spieler_list:
            file.write(save)

def save_score_list():
    with open("score_list.txt", "w") as file:
        for save in score_list:
            file.write(save)

# fragen
fragen = [

    ("Was ist Python?",
     ["Ein Programm", "Ein Nahrungsergänzungsmittel", "Eine Automarke", "Ein Promi"],
     "1"),

    ("Wie definiert man eine Funktion in Python?",
     ["def", "func", "define","funktion"],
     "1"),

    ("Wie überprüfe ich ob etwas gleich 10 ist?",
     ["=", "==", "!=", "==="],
     "2"),

    ("Was fängt Fehler in Python ab?",
     ["try/except", "error/handle", "try/catch", "if/else"],
     "1"),

    ("Welche Variable ist korrekt geschrieben?",
     ["2name = 'Max'", "name_2 = 'Max'", "name - 'Max'", "name 2 = 'Max'"],
     "2"),

    ("Welcher Befehl gibt Text in Phyton aus ?",
     ["echo","print","write","show"],
     "2"),

    ("Wie schreibt man einen Kommentar in Python ?",
     ["//","!?","#","*"],
     "3"),

    ("Wie oft läuft die Schleife? for i in range(5)",
     ["3","4","5","6"],
     "3"),

    ("Welche Schleife wird verwendet, um durch alle Elemente einer Liste zu gehen?",
    ["while","for","loop","repeat"],
    "2"),

    ("Welche Funktion wird verwendet, um Benutzereingaben zu lesen?",
    ["scan()","input()","read()","enter()"],
    "2"),]

# menü
def menue():
    choice = None

    while choice not in ["1", "2", "3","4","5"]:
        print("1 : Spieler Erstellen")
        print("2 : Spieler wählen")
        print("3 : Spielen")
        print("4 : score anzeigen")
        print("5 : Beenden")

        choice = input("Wähle eine Option:")
        print("Du hast gewählt:", choice)

        if choice not in ["1", "2", "3","4","5"]:
            print("Ungültige Option, bitte erneut zwischen 1,2,3,4,5  wählen.")

    return choice



def spieler_erstellen():
    global score
    name = input("Spieler erstellen:")
    print("Du hast den Namen:",name,"gewählt")
    score = 0
    spieler_list.append(name + "\n")

    return name



def spieler_waehlen():

    print("Wähle einen Benutzer")
    lines = load_spieler_list()

    for user in lines:
        print(user.strip())             #das\n wieder weggeht

    benutzer = input("Welchen Benutzer ?")
    print("Du hast den Spieler:",benutzer, "gewählt")

    return benutzer



def quiz_spiel():
    global score

    for frage, antworten, richtig in fragen:
        print(frage)

        for i in range(len(antworten)):
            print(i+1,":",antworten[i])         #i steht für die position in der liste

        eingabe = input("Deine Antwort: ")

        if eingabe == richtig:
            print("Richtig")
            score += 1

        else:
            print("leider falsch")
            print("richtig wäre",antworten[int(richtig)-1])

    print("Dein Score:",score)

    score_list.append(spieler + "=" +str(score) + "\n")
    save_spieler_list()
    save_score_list()



def score_anzeigen():
    load_score_list()

    if len(score_list) == 0:
        print("Kein Score vorhanden")

    else:
        for score in score_list:
            print(score)



def umwandeln_txt(lines):
    speichern = {}
    for line in lines:
        line = line.strip()

        try:
            if line == "":
                continue

            spieler, score = line.split("=")

            speichern[spieler] = int(score)

        except ValueError:
            continue

    return speichern



while True:
    wahl = menue()

    if wahl == "1":
        print("Benutzer erstellen")
        spieler = spieler_erstellen()

    elif wahl == "2":
        print("Spieler wählen ")
        spieler = spieler_waehlen()

    elif wahl == "3":
        print("Spielen")

        if spieler is None:
            print("Namen erstellen")

        else:
            print("Spieler:", spieler)
            quiz_spiel()

    elif wahl == "4":
        score_anzeigen()

    elif wahl == "5":
        print("Spiel beendet")
        save_spieler_list()
        save_score_list()
        break