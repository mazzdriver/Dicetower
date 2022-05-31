sides = [' -----\n|     |\n|  o  |\n|     |\n -----', ' -----\n|    o|\n|     |\n|o    |\n -----', ' -----\n|    o|\n|  o  |\n|o    |\n -----', ' -----\n|o   o|\n|     |\n|o   o|\n -----', ' -----\n|o   o|\n|  o  |\n|o   o|\n -----', ' -----\n|o o o|\n|     |\n|o o o|\n -----']


def six_sided(numbers:list):
	for num in numbers:
		print(sides[num-1], end='\n\n')