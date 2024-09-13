from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from constants import GEOLOCATOR_CONFIG, US_STATE_ABBREV, ABBREV_TO_US_STATE, NEIGHBORING_STATES
import pandas as pd


def filter_by_distance(data, place_distance_is_from, max_distance):
    geolocator = Nominatim(user_agent=GEOLOCATOR_CONFIG['user_agent'])
    location = geolocator.geocode(place_distance_is_from)
    if not location:
        print(f"Error: Unable to locate {place_distance_is_from}")
        return data

    origin_coords = (location.latitude, location.longitude)

    def calculate_distance(row):
        if pd.notna(row['LATITUDE']) and pd.notna(row['LONGITUDE']):
            house_coords = (row['LATITUDE'], row['LONGITUDE'])
            return geodesic(origin_coords, house_coords).miles
        else:
            return None

    data['Distance'] = data.apply(calculate_distance, axis=1)
    data = data.dropna(subset=['Distance'])
    return data[data['Distance'] <= max_distance]


def get_state_abbrev(state):
    if state in US_STATE_ABBREV:
        return US_STATE_ABBREV[state]
    elif state in ABBREV_TO_US_STATE:
        return state
    else:
        raise ValueError(f"Invalid state: {state}")


def get_neighboring_states(state):
    try:
        state_abbr = get_state_abbrev(state)
        return NEIGHBORING_STATES.get(state_abbr, [])
    except ValueError:
        print(f"Warning: {state} is not a valid US state. Returning empty list for neighbors.")
        return []