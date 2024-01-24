beerAmount = int(input('Enter number of bottles: '))

def bottlesOfBeer(numberOfBottles):
    while numberOfBottles != 1:
        print(f'{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer. Take one down pass it around, {numberOfBottles - 1} bottles of beer on the wall')
        numberOfBottles = numberOfBottles -1 

    if numberOfBottles == 1:
        print(f'{numberOfBottles} bottle of beer on the wall, {numberOfBottles} bottle of beer. Take one down pass it around, {numberOfBottles - 1} bottle of beer on the wall')


bottlesOfBeer(beerAmount)