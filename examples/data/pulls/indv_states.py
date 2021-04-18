
import requests
import pandas as pd
import pickle
import shutil
import zipfile
import io
import geopandas as gpd
import os


def main():

	url = 'https://www2.census.gov/geo/tiger/TIGER2018/STATE/tl_2018_us_state.zip'
	temp_path = 'tmp/'

	print('Downloading shapefile...')
	r = requests.get(url)
	z = zipfile.ZipFile(io.BytesIO(r.content))
	print("Done")

	z.extractall(path=temp_path) 
	filenames = [y for y in sorted(z.namelist()) for ending in ['dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)] 
	print(filenames)

	dbf, prj, shp, shx = [filename for filename in filenames]
	state = gpd.read_file(temp_path + shp)


	state= state[~state['STUSPS'].isin(['VI','MP','GU','AS','PR'])]

	state = state[['NAME','GEOID','STUSPS','geometry']]

	with open(os.path.abspath(os.getcwd()).replace('data_pulls','data') + '/us_states.pkl','wb') as file:
	    pickle.dump(state,file)

	try:
		shutil.rmtree(temp_path)
	except OSError as e:
		print("Error: %s : %s" % (temp_path, e.strerror))


if __name__ == "__main__":
	 main()








