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



def score_anzeigen():

    if len(score_list) == 0:
        print("Kein Score vorhanden")

    else:
        for scores in score_list:
            print(scores)



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

    elif wahl == "4":
        score_anzeigen()

    elif wahl == "5":
        print("Spiel beendet")
        save_spieler_list()
        break

