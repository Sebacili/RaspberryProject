from gtts import gTTS

# Messaggio di testo da convertire in audio
testo = "Ciao, questo è un messaggio di prova che verrà trasformato in un file audio MP3."

# Crea un oggetto gTTS con il messaggio di testo
tts = gTTS(text=testo, lang='it')  # 'it' sta per la lingua italiana, puoi cambiarla secondo le tue preferenze

# Salva l'audio in un file MP3
tts.save("messaggio.mp3")
