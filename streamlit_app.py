import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
# from pushbullet import Pushbullet
import folium

# # Load air pollution data from global.csv
air_pollution_data = pd.read_csv('global.csv')

# Function to get the district name from coordinates
def get_district_name(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
    address = location.raw['address']
    district_name = address.get('county', '')  # Use 'county' instead of 'country' to get district name
    return district_name

# Function to send notifications based on air pollution levels
def send_notifications(district_name, pollution_value):
    pb = Pushbullet('YOUR_PUSHBULLET_API_KEY')  # Replace with your Pushbullet API key
    if pollution_value > 80:
        alert_message = f"High Pollution rates in {district_name}! Please move to a new area or put on a mask."
        pb.push_note(f"Air Quality Alert in {district_name}", alert_message)
    elif pollution_value < 20:
        alert_message = f"The air in {district_name} is now safe to breathe. Feel at home!"
        pb.push_note(f"Air Quality Improvement in {district_name}", alert_message)

# Main Streamlit app
# ... [rest of the imports and functions]

def main():
    st.title("Uganda Air Pollution Monitoring")

    # Get user's location coordinates with an action button
    latitude = st.number_input("Enter Latitude:")
    longitude = st.number_input("Enter Longitude:")
    
    if st.button('Submit Coordinates'):
        # Convert coordinates to district name
        district_name = get_district_name(latitude, longitude)
        st.write(f"You are in {district_name}.")

        # Generate and display air pollution data for the district
        district_pollution = air_pollution_data[air_pollution_data['Country'] == district_name]
        st.subheader("Air Pollution Data for Your District")
        st.write(district_pollution)

        # Display a map with the user's location
        m = folium.Map(location=[latitude, longitude], zoom_start=10)
        folium.Marker([latitude, longitude], tooltip="Your Location").add_to(m)
        
        # Save folium map to an HTML file
        m.save('map.html')
        with open("map.html", "r") as f:
            html = f.read()
        
        st.components.v1.html(html, width=800, height=450)

if __name__ == "__main__":
    main()


# import pandas as pd
# import geopandas as gpd
# import folium
import random
# import streamlit as st
# from geopy.geocoders import Nominatim
# # from pushbullet import Pushbullet

# Function to get the district name from coordinates


# import pandas as pd
# import geopandas as gpd
# import folium
# import random
# import streamlit as st
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderTimedOut
# # from pushbullet import Pushbullet
# import time

# # Function to get the district name from coordinates with retry
# def get_district_name_with_retry(latitude, longitude, max_retries=3):
#     retries = 0
#     while retries < max_retries:
#         try:
#             geolocator = Nominatim(user_agent="geoapiExercises")
#             location = geolocator.reverse(f"{latitude}, {longitude}", exactly_one=True)
#             address = location.raw['address']
#             district_name = address.get('county', '')  # Modify this based on the location data structure
#             return district_name
#         except GeocoderTimedOut:
#             retries += 1
#             time.sleep(1)  # Wait for a second before retrying
#     return "Unknown"  # Return a default value if retries are exhausted

# # Function to generate random air pollution data for districts
# def generate_random_data():
#     districts = ['District1', 'District2', 'District3']  # Replace with your district names
#     air_pollution_values = [random.uniform(0, 100) for _ in districts]
#     data = {'district_name': districts, 'air_pollution_value': air_pollution_values}
#     return pd.DataFrame(data)

# # Function to send notifications based on air pollution levels
# def send_notifications(district_name, pollution_value):
#     pb = Pushbullet('o.61fA5UUNB8HmBRCHUSoys6O6OFw4G7wJ')  # Replace with your Pushbullet API key

#     if pollution_value > 80:
#         alert_message = f"High Pollution rates in {district_name}! Please move to a new area or put on a mask."
#         pb.push_note(f"Air Quality Alert in {district_name}", alert_message)
#     elif pollution_value < 20:
#         alert_message = f"The air in {district_name} is now safe to breathe. Feel at home!"
#         pb.push_note(f"Air Quality Improvement in {district_name}", alert_message)

# # Main Streamlit app
# def main():
#     st.title("Uganda Air Pollution Monitoring")

#     # Get user's location coordinates
#     latitude = st.number_input("Enter Latitude:")
#     longitude = st.number_input("Enter Longitude:")

#     # Convert coordinates to district name with retry
#     district_name = get_district_name_with_retry(latitude, longitude)
#     st.write(f"You are in {district_name}.")

#     while True:
#         # Generate and display air pollution data for the district
#         air_pollution_data = generate_random_data()
        
#         # Filter the data for the user's district
#         district_pollution = air_pollution_data[air_pollution_data['district_name'] == district_name]
        
#         # Check if there are rows in district_pollution
#         if not district_pollution.empty:
#             # Send notifications if pollution thresholds are met
#             pollution_value = district_pollution.iloc[0]['air_pollution_value']
#             send_notifications(district_name, pollution_value)
            
#             # Create a map with the user's location
#             st.subheader("Map Showing Your Location")
#             m = folium.Map(location=[latitude, longitude], zoom_start=10)
#             folium.Marker([latitude, longitude], tooltip="Your Location").add_to(m)
            
#             # Add district boundaries and highlight areas with high pollution
#             uganda_districts = gpd.read_file('uganda_districts.geojson')
#             merged_data = uganda_districts.merge(air_pollution_data, on='district_name')

#             # Customize the map style and colors based on pollution levels
#             for _, row in merged_data.iterrows():
#                 district = row['district_name']
#                 pollution = row['air_pollution_value']

#                 color = 'green' if pollution < 20 else 'red' if pollution > 80 else 'orange'

#                 folium.GeoJson(
#                     row['geometry'],
#                     name=district,
#                     style_function=lambda x, color=color: {'fillColor': color, 'color': 'black', 'weight': 1}
#                 ).add_to(m)

#             folium.LayerControl().add_to(m)
#             st.write(m)

#         # Sleep for 60 seconds before generating data again
#         time.sleep(1)

# if __name__ == "__main__":
        
#     main()




