import random
from collections import Counter

# Sanalista
someWords = '''omena banaani mango mansikka appelsiini rypäle ananas aprikoosi 
sitruuna kookos vesimeloni kirsikka marja persikka mustikka'''

someWords = someWords.split(' ')
# Hirsipuun tasot, 6 yritystä
stages = [
    '''
  -----
  |   |
      |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
  |   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
'''
]

# Arpoo satunnaisen sanan listalta
word = random.choice(someWords)

if __name__ == '__main__':

    print('Arvaa sana! VINKKI: sana on joko marja tai hedelmä')

    for _ in word:
        print('_', end=' ')
    print()

    letterGuessed = ''
    wrong_guesses = 0
    max_chances = len(stages) - 1
    flag = 0

    try:
        while wrong_guesses < max_chances and flag == 0:

            print()
            guess = input('Syötä arvattava kirjain: ').lower()

            # Jos ei laita kirjainta
            if not guess.isalpha():
                print('Syötä joku kirjain tähän!')
                continue

            # Jos yrittää laittaa enemmän kun yhden kirjaimen
            elif len(guess) > 1:
                print('Syötä vain yksi kirjain kerrallaan!')
                continue

            # Kirjainta on jo käytetty arvauksessa
            elif guess in letterGuessed:
                print('Olet kokeilut arvata tällä kirjaimella jo!')
                continue

            # Mikäli arvattu kirjain on oikein. Lisätään arvattu kirjain muistiin.
            if guess in word:
                letterGuessed += guess * word.count(guess)
            else:
                wrong_guesses += 1
                print(stages[wrong_guesses])

            # Korvaa alaviivan oikealla arvatulla kirjaimella. Jos kirjain ei ole oikein, ei tehdä mitään
            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')

            # Pelaaja voittaa
            if Counter(letterGuessed) == Counter(word):
                print("\nOnneksi olkoon! Arvasit sanan:", word)
                flag = 1
                break

            # Pelaaja ei voita
        if wrong_guesses == max_chances:
            print('\nHävisit pelin! Sana olisi ollut:', word)

    except KeyboardInterrupt:
        print('\nPeli keskeytetty. Nähdään!')