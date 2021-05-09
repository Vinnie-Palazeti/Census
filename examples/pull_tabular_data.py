import pandas as pandas
import requests
import time

from GPS.ACS.fns import *
from GPS.ACS.utils import *


def main(state_codes,vars_struct):

	for state in state_codes:
		print(state)
		print()
		print('API Query Start...')
		query_data(state, vars_struct)
		print('API Query Complete')
		time.sleep(30)


if __name__ == "__main__":
    main(state_codes, vars_struct)
