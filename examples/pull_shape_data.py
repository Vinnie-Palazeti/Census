
from GPS.TIGER.fns import *
from GPS.ACS.utils import *

def main():

	i = 0
	length = len(state_codes)
	for state in state_codes:
		i + 1

		print()
		print(f"overall query {(i / length)*100}% complete ")
		print()
		print(f'state code:{state}')
		get_state_shape(state)
		print()

if __name__ == "__main__":
	 main()








