Uganda Air Pollution Monitoring
This is a Python script for monitoring air pollution levels in Uganda's districts. It uses air pollution data from a CSV file and displays information about the air quality in the district based on user-provided coordinates. Additionally, it can send notifications about air quality to a Pushbullet account.

Prerequisites
Before using this code, ensure that you have the following libraries and dependencies installed:

Python 3.x
pandas
geopandas
folium
random
streamlit
geopy
pushbullet (You will need a Pushbullet API key)
You can install these dependencies using pip:

bash
Copy code
pip install pandas geopandas folium streamlit geopy pushbullet.py
Usage
Data Files: Make sure you have the following data files in the same directory as this script:

global.csv: Air pollution data in CSV format.
uganda_districts.geojson: GeoJSON file containing Uganda's district boundaries.
Pushbullet API Key: Replace the placeholder API key in the send_notifications function with your Pushbullet API key.

District Names: Replace the example district names in the generate_random_data function with the names of the districts you want to monitor.

Run the Application:

Run the application by executing the script:

bash
Copy code
python your_script_name.py
Input Coordinates: Enter the latitude and longitude coordinates when prompted. The script will determine the district based on the coordinates.

View Results: The script will display air pollution data for the detected district and send notifications if pollution thresholds are met.

Map: A map displaying your location will also be shown using Folium.

Important Notes
Ensure that you have a stable internet connection to use geocoding services for location detection.

This script is a basic example and can be extended for more districts and enhanced features.

Acknowledgments
This script uses data from the Global Air Pollution Database.

Notifications are sent using Pushbullet's service.

Feel free to customize and extend this code to fit your specific air pollution monitoring needs in Uganda or any other location.