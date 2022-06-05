from modules import *


def beginning():
	print(text.throw_it)
	

def get_number(start, stop):
	number = random.randint(start, stop)
	return number


def get_sides():
	yes_side = False 
	while not yes_side:
		sides = input(text.sides)
		if sides.isdigit() and int(sides) > 0:
			yes_side = True
		else:
			print(text.num_need)
	return int(sides)

def get_dices():
	yes_dice = False 
	while not yes_dice:
		dices = input(text.dices)
		if dices.isdigit() and int(dices) > 0:
			yes_dice = True
		else:
			print(text.num_need)
	return int(dices)
	
	
def throw(amount_of_dices:int, amount_of_sides:int):
	numbers = []
	for _ in range(amount_of_dices):
		numbers.append(get_number(1, amount_of_sides))
	if amount_of_sides != 6:
		return numbers
	else:
		six.six_sided(numbers)
		return numbers


def try_again():
	user_input = input(text.throw_again)
	if 'y' in user_input.lower():
		return True
	else:
		return False
	
	
def main():
	beginning()
	ready = True
	while ready:
		print(*(throw(get_dices(), get_sides())), sep=' ')
		ready = try_again()

if __name__== "__main__":
    main()
    