
import requests
import pandas as pd



def get_data(year, source, name, variables, state, county):

	dyear = year
	dsource = source ## this shit should be in a function from censusdata.
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



variables = {
    'Total Population' : "B01003_001E",
    'Population - Race': {
        "White Population" : "B02001_002E",
        "Black Population" : 'B02001_003E',
        "Hispanic or Latino": "B03003_003E",
        #"Arab Population": 'B04004_006E',
        "American Indiana & Alaska Native": 'B02001_004E'
        "Asian Population" : 'B02001_005E',
        "Hawaiian & Pacific Islander": "B02001_006E"
    },
    'Population - Sex': {
        'Male Population' : 'B01001_002E',
        "Female Population" : 'B01001_026E'
    },
    'Population - Age' : {
    	'Male': {
    		'0-5':'B01001_003E',
    		'5-9':'B01001_004E',
    		'10-14':'B01001_005E',
    		'15-17':'B01001_006E',
    		'18-19':'B01001_007E',
    		'20':'B01001_008E',
    		'21':'B01001_009E',
    		'22-24':'B01001_010E',
    		'25-29':'B01001_011E',
    		'30-34':'B01001_012E',
    		'35-39':'B01001_013E',
    		'40-44':'B01001_014E',
    		'45-49':'B01001_015E',
    		'50-54':'B01001_016E',
    		'55-59':'B01001_017E',
    		'60-61':'B01001_018E',
    		'62-64':'B01001_019E',
    		'65-66':'B01001_020E',
    		'67-69':'B01001_021E',
    		'70-74':'B01001_022E',
    		'75-79':,'B01001_023E'
    		'80-84':'B01001_024E',
    		'85+': 'B01001_025E'

    	},
    	'Female': {
    		'0-5':'B01001_027E',
    		'5-9':'B01001_028E',
    		'10-14':'B01001_029E',
    		'15-17':'B01001_030E',
    		'18-19':'B01001_031E',
    		'20':'B01001_032E',
    		'21':'B01001_033E',
    		'22-24':'B01001_034E',
    		'25-29':'B01001_035E',
    		'30-34':'B01001_036E',
    		'35-39':'B01001_037E',
    		'40-44':'B01001_038E',
    		'45-49':'B01001_039E',
    		'50-54':'B01001_040E',
    		'55-59':'B01001_041E',
    		'60-61':'B01001_042E',
    		'62-64':'B01001_043E',
    		'65-66':'B01001_044E',
    		'67-69':'B01001_045E',
    		'70-74':'B01001_046E',
    		'75-79':'B01001_047E',
    		'80-84':'B01001_048E',
    		'85+':'B01001_049E',
    }
}
 



