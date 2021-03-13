
import requests
import pandas
import argparse
import pandas as pd



def main(year, source, name, variables, state, county):

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

	data = pd.DataFrame(columns=response.json()[0], data=response.json()[1:])
	
	return print(data)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
    	"--year",
    	default='2018')
    parser.add_argument(
    	"--source",
    	default='acs')
    parser.add_argument(
    	"--name",
    	default='acs5')
    parser.add_argument(
    	"--variables",
        default=['B00001_001E'] )
    parser.add_argument(
    	"--state",
    	default='55')
    parser.add_argument(
    	"--county",
    	default='*')    
    args = parser.parse_args()

    main(
        year=args.year,
        source=args.source,
        name=args.name,
        variables=args.variables,
        state=args.state,
        county=args.county,
    )



