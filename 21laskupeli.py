def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nHÄVISIT!")
    print("Parempi lysti seuraavalla kerralla!")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i-1]) != 1:
            return False
        i += 1
    return True

def start1():
    xyz = []
    last = 0
    while True:
        print("Paina 'F' ottakseen ensimmäisen mahdollisuuden.")
        print("Paina 'S' ottakseen toisen mahdollisuuden.")
        chance = input('> ')

        if chance.upper() == "F":
            while True:
                if last == 20:
                    lose1()
                print("\nSinun vuoro.")
                inp = int(input("Montako numeroa haluat syöttää? (1-3)\n"))
                if 1 <= inp <= 3:
                    comp = 4 - inp
                else:
                    print("Väärä syöte. Sinut on hylätty pelistä.")
                    lose1()

                print("Syötä numerot:")
                for _ in range(inp):
                    xyz.append(int(input('> ')))

                last = xyz[-1]

                if not check(xyz):
                    print("\nEt syöttänyt kokonaislukuja peräkkäin.")
                    lose1()
                if last == 21:
                    lose1()

                print("\nTietokoneen vuoro:")
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Numerot tietokoneen vuoron jälkeen:", xyz)
                last = xyz[-1]

        elif chance.upper() == "S":
            comp = 1
            last = 0
            while last < 20:
                print("\nTietokoneen vuoro:")
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Numerot tietokoneen vuoron jälkeen:", xyz)
                if xyz[-1] == 20:
                    lose1()

                print("\nSinun vuoro.")
                inp = int(input("Montako numeroa haluat syöttää? (1-3)\n"))
                print("Syötä numerot:")
                for _ in range(inp):
                    xyz.append(int(input('> ')))
                last = xyz[-1]

                if not check(xyz):
                    print("\nEt syöttänyt kokonaislukuja peräkkäin.")
                    lose1()

                near = nearestMultiple(last)
                comp = near - last
                if comp == 4:
                    comp = 3

            print("\n\nONNEKSI OLKOON!!!")
            print("SINÄ VOITIT!")
            exit(0)

        else:
            print("Väärä valinta. Paina joko F tai S.")

game = True
while game:
    print("\nPelaaja 2 on Tietokone.")
    ans = input("Haluatko pelata 21 numeropeliä? (Yes / No)\n> ")
    if ans.lower() == "yes":
        start1()
    else:
        nex = input("Haluatko poistua pelistä? (Yes / No)\n> ")
        if nex.lower() == "yes":
            print("Poistutaan pelistä...")
            exit(0)
        elif nex.lower() == "no":
            print("Jatketaan peliä...")
        else:
            print("Väärä valinta")