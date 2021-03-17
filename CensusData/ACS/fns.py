
import requests
import pandas as pd



def get_data(year, source, name, variables, state, county):

	dyear = year
	dsource = source 
	dname = name
	variables += ['NAME']
	cols = variables
	state_name = state
	county_name = county

	base_url = f'https://api.census.gov/data/{dyear}/{dsource}/{dname}/'

	data_url = f'{base_url}?get={",".join(cols)}&for=county:{county_name}&in=state:{state_name}'

	response = requests.get(data_url)
	
	return pd.DataFrame(columns=response.json()[0], data=response.json()[1:])







