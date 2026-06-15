import random

print("Hei! Tervetuloa Numeronarvauspeliin!\nSinulla on 7 mahdollisuutta arvata numero. Aloitetaan!")

low = int(input("Syötä alin numeroraja: "))
high = int(input("Syötä korkein numeroraja: "))

print(f"\nSinulla on 7 mahdollisuutta arvata numero {low} ja {high} välistä. Aloitetaan!")

num = random.randint(low, high)
# Sallitut mahdollisuudet yhteensä
ch = 7
# Arvaus laskuri (montako arvausta pelaaja käyttää)
gc = 0

while gc < ch:
    gc += 1
    # Pelaaja syöttää numeron
    guess = int(input('Syötä arvauksesi: '))

    # Peli ohi, voitto
    if guess == num:
        print(f'Aivan oikein! Numero on {num}. Arvasit sen {gc} mahdollisuudessa.')
        break

    # Peli ohi, ei voittoa
    elif gc >= ch and guess != num:
        print(f'Pahoittelut! Numero oli {num}. Parempi onni seuraavalla kerralla.')

    # Pelaaja arvaa liian korkean luvun vastauksesta
    elif guess > num:
        print('Liian korkea! Kokeile pienempää numeroa.')

    # Pelaaja arvaa liian pienen luvun vastauksesta
    elif guess < num:
        print('Liian pieni! Kokeile korkeampaa numeroa.')