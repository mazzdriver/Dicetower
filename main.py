from modules import *


def beginning():
	print(text.throw_it)
	

def get_number(start, stop):
	number = random.randint(start, stop)
	return number


def get_sides():
	sides = int(input(text.sides))
	return sides


def get_dices():
	dices = int(input(text.dices))
	return dices
	
	
def main():
	beginning()
	amount_of_dices = get_dices()
	amount_of_sides = get_sides()
	for _ in range(amount_of_dices):
		print(get_number(1, amount_of_sides), end=' ')


if __name__== "__main__":
    main()