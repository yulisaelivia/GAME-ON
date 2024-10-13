import random


def kiesJeSpel():
        while True:
            choice = input("Kies een spel(1: Raad het nummer, 2: Galgje,): ")
            if choice == "1":
                guess_the_number()
                break
            elif choice == "2":
                galgje()
                break
            else:
                print("Dat is geen geldige keuze. Probeer het opnieen.")
                continue


def guess_the_number():
    # Instellingen
    min_tries = 1  # Minimale poging
    max_tries = 12  # Aantal pogingen
    max_number = 25  # Maximale waarde van het getal

    # Genereer een random integer
    number_to_guess = random.randint(min_tries, max_tries)

    print(f"Leuk dat je er bent!, Welkom bij 'Raad het Getal'!")
    print(f"Je hebt {max_tries} pogingen om het getal tussen 1 en {max_number} te raden.")

    for attempt in range(max_tries):
        try:
            guess = int(input(f"Poging {attempt + 1}: Voer je gok in: "))
        except ValueError:
            print("Dat is geen geldig getal. Probeer het opnieuw.")
            continue

        if guess < 1 or guess > max_number:
            print(f"Het getal moet tussen 1 en {max_number} liggen. Probeer het opnieuw.")
            continue

        if guess < number_to_guess:
            print("Het getal is hoger.")
        elif guess > number_to_guess:
            print("Het getal is lager.")
        else:
            print(f"Gefeliciteerd! Je hebt het getal {number_to_guess} geraden.")
            break
    else:
        print(f"Jammer, je hebt het getal niet geraden. Het juiste getal was {number_to_guess}.")


def toon_galg(pogingen):
    states = [
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / 
           |
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |
           |
        ''',
        '''
           -----
           |   |
           |   O
           |   |
           |
           |
        ''',
        '''
           -----
           |   |
           |   O
           |
           |
           |
        ''',
        '''
           -----
           |   |
           |
           |
           |
           |
        ''',
        '''
           -----
           |   |
           |
           |
           |
           |
        '''
    ]
    print(states[pogingen])

def galgje():
    
    woordenlijst = ['python', 'codering', 'galgje', 'laptop', 'software', 'utrecht', 'bushalte']
    woord = random.choice(woordenlijst)
    geraden_letters = []
    pogingen = 5

    print("Leuk dat je er bent! Welkom bij Galgje!")

    while pogingen > 0:
        toon_galg(pogingen)
        weergave = ''.join(letter if letter in geraden_letters else '_' for letter in woord)
        print("\nHuidige stand: ", weergave)
        print(f"Pogingen over: {pogingen}")

        geraden_letter = input("Raad een letter: ").lower()

        if geraden_letter in geraden_letters:
            print("Denk na, je hebt deze letter al geraden!")
            continue

        geraden_letters.append(geraden_letter)

        if geraden_letter in woord:
            print("Lekker bezig! Goed gedaan! Het letter zit in het woord.")
        else:
            pogingen -= 1
            print("Helaas, die letter zit niet in het woord.")

        if all(letter in geraden_letters for letter in woord):
            print(f"Gefeliciteerd! Je hebt het woord '{woord}' geraden!")
            break
    else:
        toon_galg(pogingen)
        print(f"Helaas, je hebt verloren. Het woord was '{woord}'.")



