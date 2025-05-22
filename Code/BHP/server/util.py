import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Load columns.json
    artifacts_path = os.path.join(os.path.dirname(__file__), 'artifacts')
    columns_path = os.path.join(artifacts_path, 'columns.json')
    model_path = os.path.join(artifacts_path, 'banglore_home_prices_model.pickle')

    try:
        with open(columns_path, "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    except FileNotFoundError:
        print(f"Error: '{columns_path}' not found.")
        __data_columns = []
        __locations = []

    # Load model
    try:
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)
    except FileNotFoundError:
        print(f"Error: '{model_path}' not found.")
        __model = None

    print("loading saved artifacts...done")


def get_estimated_price(location, sqft, bhk, bath):
    if __data_columns is None or __model is None:
        print("Artifacts not loaded properly.")
        return None

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # unknown location
    print(get_estimated_price('Ejipura', 1000, 2, 2))   # unknown location
