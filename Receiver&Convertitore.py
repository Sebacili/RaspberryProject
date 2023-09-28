#GPS receiver

import gpsd
from geopy.geocoders import Nominatim
from gtts import gTTS
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


# Messaggio di testo da convertire in audio
testo = "ciao, è avvenuto un incidente nella seguente via:" +address + " vi preghiamo di verificare l' incidente, grazie"

# Crea un oggetto gTTS con il messaggio di testo
tts = gTTS(text=testo, lang='it')  # 'it' sta per la lingua italiana, puoi cambiarla secondo le tue preferenze

# Salva l'audio in un file MP3
tts.save("messaggio.mp3")


# Disconnect from GPSD when done
gpsd.disconnect()
