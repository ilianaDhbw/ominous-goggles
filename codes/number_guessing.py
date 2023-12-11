import random
nummer = random.randint(1, 5)

name = input("Hallo,wie lautet dein Name? ")
number_of_guesses = 0
print('Nice to meet you {}! Errate meine Zahl, welche zwischen 1 und 5 liegt \nDu hast nur 3 Versuche:'.format(name))

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < nummer:
        print('Deine Zahl ist zu klein, versuch es nochmal!')
    if guess > nummer:
        print('Deine Zahl ist zu hoch, versuch es nochmal!')
    if guess == nummer:
        break
if guess == nummer:
    print( 'Gratuliere {}, du hast die Zahl mit {} Versuchen erraten!'.format(name, number_of_guesses))
else:
    print('Leider hast du die Zahl nicht gefunden \nDie Zahl lautet {}.'.format(nummer))