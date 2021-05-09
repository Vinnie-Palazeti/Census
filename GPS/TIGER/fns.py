import requests
import pandas as pd
import geopandas as gpd
import zipfile
import io
import shutil
import pickle


def get_state_shape(state_code):

    url = f"https://www2.census.gov/geo/tiger/TIGER2018/TRACT/tl_2018_{state_code}_tract.zip"
    temp_path = "tmp/"
    print("Downloading shapefile...")
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    print("Done")
    
    z.extractall(path=temp_path)
    filenames = [
        y
        for y in sorted(z.namelist())
        for ending in ["dbf", "prj", "shp", "shx"]
        if y.endswith(ending)
    ]

    dbf, prj, shp, shx = [filename for filename in filenames]
    state = gpd.read_file(temp_path + shp)

    state = (
        state[["GEOID", "STATEFP", "NAMELSAD", "geometry"]]
        .explode()
        .reset_index(drop=True)
    )

    with open(f"./data/storage/shape_state_data/state_{state_code}.pkl", "wb") as file:
        pickle.dump(state, file)

    try:
        shutil.rmtree(temp_path)
    except OSError as e:
        print("Error: %s : %s" % (temp_path, e.strerror))


def get_US_shape():

    url = "https://www2.census.gov/geo/tiger/TIGER2018/STATE/tl_2018_us_state.zip"
    temp_path = "tmp/"

    print("Downloading shapefile...")
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    print("Done")

    z.extractall(path=temp_path)
    filenames = [
        y
        for y in sorted(z.namelist())
        for ending in ["dbf", "prj", "shp", "shx"]
        if y.endswith(ending)
    ]

    dbf, prj, shp, shx = [filename for filename in filenames]
    state = gpd.read_file(temp_path + shp)

    state = state[~state["STUSPS"].isin(["VI", "MP", "GU", "AS", "PR"])]

    state = (
        state[["NAME", "GEOID", "STUSPS", "geometry"]].explode().reset_index(drop=True)
    )

    with open("./data/storage/shape_US_data/us_states.pkl", "wb") as file:
        pickle.dump(state, file)

    try:
        shutil.rmtree(temp_path)
    except OSError as e:
        print("Error: %s : %s" % (temp_path, e.strerror))
