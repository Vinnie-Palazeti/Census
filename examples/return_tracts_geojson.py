import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import argparse

def main(lat,lon):
	# GPS point input
	p = Point(lat,lon)

	# create circle
	p_buff = p.buffer(.1)

	# put point into df
	point_frame = gpd.GeoDataFrame(pd.DataFrame({
	    'input' : ['point'],
	    'geometry' : p_buff 
	}))
	      
	# set point CRS
	point_frame = point_frame.set_crs(epsg=4269)

	# Read in USA frame
	usa = pd.read_pickle('/Users/vinniepalazeti/Desktop/github/GPS/examples/data/storage/shape_US_data/us_states.pkl')
	usa = usa.set_crs(epsg=4269)

	# find states
	states = gpd.sjoin(usa, point_frame,op='intersects')['GEOID'].values

	# iterate through states returned from spatial join
	state_data = []
	for code_number in states:
	    read_in = pd.read_pickle(f"/Users/vinniepalazeti/Desktop/github/GPS/examples/data/storage/shape_state_data/state_{code_number}.pkl")
	    state_data.append(read_in)
    
    # create single pandas frame
	state_data = pd.concat(state_data,axis=1)

	# spatial join with state data
	joined = gpd.sjoin(state_data, point_frame,op='intersects')
	joined = joined.drop(columns = ['index_right','input'])

	print(joined)
	
	return joined

if __name__ == "__main__":
    
    args = parser.parse_args()
    main(
        lat=args.lat,
        lon=args.lon
        )









