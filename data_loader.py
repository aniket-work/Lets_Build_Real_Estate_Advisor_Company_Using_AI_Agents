import pandas as pd
from constants import HOUSE_DATA_CONFIG


def load_house_data():
    try:
        house_data = pd.read_excel(HOUSE_DATA_CONFIG['file_path'])
        print("house data loaded successfully")
        return house_data
    except Exception as e:
        print(f"Error loading house data: {e}")
        return pd.DataFrame()