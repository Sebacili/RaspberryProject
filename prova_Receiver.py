#Ricevere il segnale gps e convertirlo in un indirizzo di via
import serial

# Configura la porta seriale
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

try:
    while True:
        # Leggi una linea dalla porta seriale
        line = ser.readline().decode('utf-8').strip()
        if line.startswith('$GPRMC'):
            # Se la linea inizia con "$GPRMC", è una riga di dati GPS
            data = line.split(',')
            if len(data) >= 7 and data[2] == 'A':
                # Estrai la latitudine e la longitudine
                latitude = data[3]
                longitude = data[5]
                print(f'Latitudine: {latitude}, Longitudine: {longitude}')
except KeyboardInterrupt:
    # Interrompi il programma con CTRL+C
    ser.close()

    #python gps.py per eseguire