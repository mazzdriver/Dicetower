from modules import *


def get_number(start, stop):
	number = random.randint(start, stop)
	return number
	
	
def main():
	print(get_number(1, 6))


if __name__== "__main__":
    main()