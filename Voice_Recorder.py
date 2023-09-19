#python -m pip install sounddevice
#pip install scipy
#sudo apt-get install libportaudio2
#pip install pipwin
#pipwin install pyaudio
import sounddevice
from scipy.io.wavfile import write

record_voice = sounddevice.rec( int( second * fs ) , samplerate = fs , channels = 2 )
sounddevice.wait()
record_voice= sounddevice.rec(second* fs, dtype='float64')
sounddevice.query_devices()
sounddevice.default.device = 'digital output'
write("out.wav", fs , record_voice )


import sounddevice
from scipy.io.wavfile import write
fs= 44100
second =  int(input("Enter time duration in seconds: "))
print("Recording.....n")
record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
sounddevice.wait()
write("out.wav",fs,record_voice)
print("Finished.....nPlease check your output file")