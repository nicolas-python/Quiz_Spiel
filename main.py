#Quiz spiel

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
        save_speichern()
        break