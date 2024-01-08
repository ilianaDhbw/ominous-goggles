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

def kontrolle_win():

    # wenn alle 3 Felder gleich sind,hat der Spieler gewonnen
    # Reihen
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    # Spalten
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    # Diagonalen
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[5]
    if spielfeld[7] == spielfeld[5] == spielfeld[3]:
        return spielfeld[5]

def kontrolle_unentschieden():
    if (spielfeld[1] == 'X' or spielfeld[1] == 'O') \
      and (spielfeld[2] == 'X' or spielfeld[2] == 'O') \
      and (spielfeld[3] == 'X' or spielfeld[3] == 'O') \
      and (spielfeld[4] == 'X' or spielfeld[4] == 'O') \
      and (spielfeld[5] == 'X' or spielfeld[5] == 'O') \
      and (spielfeld[6] == 'X' or spielfeld[6] == 'O') \
      and (spielfeld[7] == 'X' or spielfeld[7] == 'O') \
      and (spielfeld[8] == 'X' or spielfeld[8] == 'O') \
      and (spielfeld[9] == 'X' or spielfeld[9] == 'O'):
        return ('unentschieden')

spielfeld_ausgeben()
while spiel_aktiv:
    
    print ("Spieler " + spieler_aktuell + " ist am Zug")
    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        spielfeld_ausgeben()

        #gewonnen?1
        
        gewonnen = kontrolle_win()
        if gewonnen:
            print ("Spieler " + gewonnen + " hat gewonnen!")
            spiel_aktiv = False
            break
        # unentschieden?
        unentschieden = kontrolle_unentschieden()
        if unentschieden:
            print ("Spiel ist unentschieden ausgegangen")
            spiel_aktiv = False
        spieler_wechseln()