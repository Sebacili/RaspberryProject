import gpsd
from geopy.geocoders import Nominatim

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="myGeocoder")

# Connect to the local GPSD daemon
gpsd.connect()

try:
    while True:
        packet = gpsd.get_current()
        latitude = packet.lat
        longitude = packet.lon
        print(f"Latitude: {latitude}, Longitude: {longitude}")

        # Reverse geocode to get the address
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        address = location.address

        print("Address:", address)

except KeyboardInterrupt:
    print("GPS data acquisition stopped.")

# Disconnect from GPSD when done
gpsd.disconnect()
