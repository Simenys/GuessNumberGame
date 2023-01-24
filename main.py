from tkinter import*
root = Tk()

import random

start_from = 1
range_to = int(input("įveskite spėjamo skaičiaus diapazoną: "))
range_min = start_from
range_max = range


random_number = random.randint(start_from, range_to)
count_numbers = 0

while True:
    print(f"Spėjimo diapazonas: nuo {range_min} iki {range_max}")
    guess = int(input("Spėkite skaičių: "))
    if guess >= range_max or guess < range_min:
        print(f"Pasirinkote skaičių už diapazono ribų")
        continue

    count_numbers += 1

    if guess > random_number:
        print("Mažiau")
        range_max = guess
    if guess < random_number:
        print("Daugiau")
        range_min = guess
    if guess == random_number:
        print(f"Atspėjote skaičių {random_number}!")
        break

print(f"Žaidimas baigtas. Jums prireikė {count_numbers} spėjimų")

