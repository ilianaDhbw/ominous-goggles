# Spiel Tic-Tac-Toe

print("Tic-Tac-Toe Python Tutorial")
spiel_aktiv = True
spieler_aktuell = 'X'



spielfeld = [" ",
             " "," "," ",
             " "," "," ",
             " "," "," "]


def spielfeld_ausgeben():
    print (spielfeld[1] + "_|_" + spielfeld[2] + "_|_" + spielfeld[3] )
    print (spielfeld[4] + "_|_" + spielfeld[5] + "_|_" + spielfeld[6] )
    print (spielfeld[7] + "_|_" + spielfeld[8] + "_|_" + spielfeld[9] )




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
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        spielfeld_ausgeben()
        spieler_wechseln()