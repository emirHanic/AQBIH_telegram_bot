import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables using os.environ
RHMZRS = os.environ.get('RHMZRS')

api_url = RHMZRS + str(time.time())

class AirQualityData:
    def __init__(self):
        self.data = response = requests.get(api_url).json()

    def get_pm_data(self):
        pm_data = []
        if self.data:
            for key, value in self.data.items():
                for station in value:
                    station_id = station['StationID']
                    pm10_value = station['PM10']
                    pm25_value = station['PM25']

                    pm_data.append({
                        'StationID': station_id,
                        'PM10': pm10_value,
                        'PM25': pm25_value,
                    })
        return pm_data


# # Create an instance of AirQualityData
# air_quality = AirQualityData()

# # # Fetch data from the API
# # air_quality.fetch_data()

# # # Get PM data
# pm_data = air_quality.get_pm_data()

# # Process or print the PM data as needed
# for entry in pm_data:
#     if entry['StationID']=='BanjaLuka':
#         print(f"Station ID: {entry['StationID']}, PM10: {entry['PM10']}, PM25: {entry['PM25']}")
