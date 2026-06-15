import random

# Pelaajan nimi
name = input("Mikä on nimesi? ")
print("Onni lykkyyn!", name)

# Sanalista
words = [
    'sateenkaari', 'tietokone', 'tiede', 'ohjelmointi',
    'python', 'matematiikka', 'pelaaja', 'kunto',
    'päinvastainen', 'vesi', 'lankku', 'nörtti'
]

# Valitsee satunnaisen sanan luettelosta
word = random.choice(words)

print("\nArvaa kirjaimet")

# Tallentaa arvatut kirjaimet
guesses = ''

# Yrityksien määrä
turns = 12

# Pääpelin silmukka
while turns > 0:

    failed = 0

    # Näyttää arvatut kirjaimet ja piiloitetut kirjaimet
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # Tarkista jos sana on arvattu
    if failed == 0:
        print("Voitit Pelin")
        print("Sana on:", word)
        break

    # Ota käyttäjän syöte
    guess = input("Arvaa kirjain: ").lower()

    # Vahvista syötteen pituus
    if len(guess) != 1:
        print("Ole hyvä ja syötä yksittäinen kirjain.")
        continue

    # Tarkista jos kirjain on jo arvattu
    if guess in guesses:
        print("Olet jo arvanut tämän kirjaimen.")
        continue

    # Tallenna arvaus
    guesses += guess

    # Hallita väärät arvaukset
    if guess not in word:
        turns -= 1
        print("Väärin")
        print("Sinulla on", turns, "arvausta jäljellä")

        # Tarkista jos pelaaja on hävinnyt pelin
        if turns == 0:
            print("Hävisit Pelin")
            print("Sana on:", word)