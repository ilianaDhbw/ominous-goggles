<!-- https://github.com/skills/communicate-using-markdown -->

-->WISSEN IST MACHT

# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->
# Algorithmus beschreibung
![Dieser Algorithmus beschreibt die Logik zur Reduzierung des Punktestands. Wenn der Punktestand größer als 1 ist, wird er um 1 reduziert und das entsprechende GUI-Element aktualisiert. Diese Operation wird alle 2 Sekunden wiederholt.](image-100.png)
# - Datentypen
![Hier werden verschiedene Datentypen verwendet: player_name_var und player_name_label sind Zeichenketten, während key und imported_questions vermutlich Listen oder Dictionaries sind, je nach dem, wie sie in der Funktion get_random_questions() zurückgegeben werden.](image101.png)
# - E/A-Operationen und Dateiverarbeitung
![Hier wird eine Bilddatei ("img/start.PNG") geöffnet und ihre Größe geändert, bevor sie in der GUI verwendet wird.](image-102.png)
# - Operatoren
![Dieser Ausdruck verwendet den Zuweisungsoperator (=) und den Additionoperator (+), um den Wert der Variablen index um 1 zu erhöhen.](image-103.png)
# - Kontrollstrukturen
![Hier wird eine bedingte Anweisung verwendet, um zu überprüfen, ob die vom Benutzer eingegebene Antwort korrekt ist. Je nachdem, ob die Bedingung erfüllt ist oder nicht, werden unterschiedliche Funktionen aufgerufen.](image-104.png)
# - Funktionen
![Hier wird eine Funktion scanner() definiert, die die vom Benutzer eingegebene Antwort überprüft und dann je nach Ergebnis andere Funktionen aufruft.alt text](image-105.png)
# - Stringverarbeitung
![In diesem Beispiel werden Zeichenkettenmanipulationen verwendet, um den Spielernamen zu speichern und an die GUI zu übergeben.](image-106.png)
# - Strukturierte Datentypen
![Hier wird auf einen strukturierten Datentyp (wahrscheinlich ein Dictionary) zugegriffen, um die richtige Antwort auf eine Frage zu erhalten. Die Verwendung von Schlüsseln (key[index]) ermöglicht den Zugriff auf bestimmte Einträge im Dictionary.](image-107.png)
# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
![move window, center, hide titelbar](200.png)
![blackbar](201.png)
![Funktionen an Ereignisse binden](202.png)
Dass tkinter-Fenster wird immer in der Mitte des Bildschirms erstellt wird, indem die Funktion "center" den Seitenabstand des Bildschirms berechnet. Mit der Funktion "start_move" wird die Mausposition auf der "black_bar" gespeichert und sichergestellt, dass das Fenster von dieser Mausposition aus mit der Funktion "move_window" verschoben wird. Dann werden die verscheidenen Funktionen an die Ereignisse gebunden. Die Blackbar wird mit der Funktion "start_move" und der Funktion "move_window verbunden, um das Fenster durch gedrückhalten der Maustaste auf einem Punkt der Blackbar von dort aus verschieben zu können. Dann wird das Fenster noch mit der Funktion hide_titelbar verbunden um die Standart-Titelleiste dieses tkinter-Fensters zu entfernen. 
Dadurch haben wir gelernt, wie man Funktionen an bestimmt Ereignisse binden kann und wie man einen eigene individuelle Titelleiste erstellen kann. Außerdem haben wir gelernt wie man anhand der Bildschirmgröße berechenen kann, dass das geöffnete Fenster mittig auf dem Bildschirm erscheint.
	

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
https://github.com/emmanuelyoussefyoussef/Wissen-ist-Macht/graphs/commit-activity
![Code frequency](image-305.png)
![Commits](imgage-306.png)
![Beispiel Lars](image-310.png)
![Besipiel Youssef](image-311.png)
![Beispiel Iliana](image-312.png)
# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->

![dictionary für Fragen im Projekt](203.png)
![neues Dictionary mit 10 random Fragen](204.png)
Um unser Quiz mit Fragen zu versorgen haben wir eine Dictionary erstellt. Aus dieser Dictionary werden bei jedem Spielstart 10 Fragen zufällig ausgesucht und
durch die nummerierung (eindeutige keys) in einer neuen dictionary gespeichert. Diese wird dann an die Hauptdatei übergeben, in der dann die Frage, die 
Antwortmöglichkeiten und evtl. auch die Kategorie einer Frage verwendet werden können.



## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->
<!-- VSC -->
![VSC als IDE verwendet für die Organisation vom Code und für die Commits](image-108.png)

<!-- zB -->
<!-- GIT -->
![Github verwendet für das zusammenfügen vom Code und zum Commiten](image-109.png)
![Github Commithistory](image-110.png)
<!-- Copilot -->

<!-- other -->
![Used the tool ChatGPT to get some help and inspiration and to solve some coding problems](image-111.png)



## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
![Bei Fragen und Problemen haben wir uns weitergeholfen. Dafür hatten wir einen Discord-Channel, indem wir uns ausgetauscht, geupdatet und geholfen haben.Bsp.1:](image-300.png)
![Bsp.2:](image-301.png)
![Bsp.3:](image-302.png)
![Bsp.4:](image-303.png)
![Bsp.5:](image-304.png)

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->
![Der Code könnte in verschiedenen dateien programmiert werden anstatt in nur eine große Datei da der Überblick dann beibehalten wird.](image-112.png)
![Die Variablen wurden in 2 verschiedene Sprachen gecoded und das sollte man vermeiden](image-113.png)
![die namen für die Variablen können auch besser gestaltet sein](image-114.png)
# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
verschiedene libaries:
![tkinter](image-307.png)
![Discord.py,dotenv](image-308.png)
![random](image-309.png)

<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->
![wir wollten dass unser spiel auf 2 verschiede weisen gestartet werden kann einmal durch die IDE und durch Discord, dies war ein großes Problem und wir sind sehr stolz drauf dass wir fremde Plattformen einbringen konnten und uns außerhalb der IDE einbringen konnten](image-115.png)
![Starten durch Discord](image-116.png)



## Kenntnisse in prozeduraler Programmierung:
^^siehe oben Frage 1
# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen


