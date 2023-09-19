from geopy.geocoders import Nominatim

# Inizializza il geocoder Nominatim
geolocator = Nominatim(user_agent="myGeocoder")

# Specifica le coordinate (latitudine e longitudine)
latitude = 45.51135 # Esempio: latitudine di New York City
longitude = 9.130027 # Esempio: longitudine di New York City,

# Ottieni l'indirizzo dalla latitudine e longitudine
location = geolocator.reverse((latitude, longitude), exactly_one=True)

# Estrai l'indirizzo
address = location.address

# Stampalo
print("Coordinate ({}, {}):".format(latitude, longitude))
print("Indirizzo:", address)