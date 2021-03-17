
import requests
import pandas
import argparse
import pandas as pd
from CensusData.ACS.fns import get_data
from CensusData.ACS.utils import var_dict 




def main(year, source, name, variables, state, county):

    return print(get_data(year,source,name,variables,state,county))

if __name__ == "__main__":
    variable_codes = list(var_dict.values())
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
        default=variable_codes)
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



