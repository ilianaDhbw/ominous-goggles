# Spiel Tic-Tac-Toe

print("Tic-Tac-Toe Python Tutorial")
spiel_aktiv = True
spieler_aktuell = 'X'



spielfeld = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]


def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )




def spieler_eingabe():
    global spiel_aktiv #globale Variablen bleiben ueber Methodenaufrufe hinweg erhalten
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        # vorzeitiges Spielende durch Spieler
        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Eine Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == 'X' or spielfeld[spielzug] == 'O':
                    print("Das Feld ist bereits belegt - bitte wähle ein anderes !")
                else:
                    return spielzug
            else:
                print("Die Zahl muss zwischen 1 und 9 liegen")

def spieler_wechseln():
    global spieler_aktuell
    if spieler_aktuell == 'X':
        spieler_aktuell = 'O'
    else:
        spieler_aktuell = 'X'

spielfeld_ausgeben()
while spiel_aktiv:
    
    print ("Spieler " + spieler_aktuell + " ist am Zug")
    spielzug = spieler_eingabe()