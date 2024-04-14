import pyaudio
import wave

p = pyaudio.PyAudio() # Initializes pyaudio object
audio = wave.open("file_example.wav") # Opens the wav audio file

data = audio.readframes(1024)
print("Audio Sample Rate: ", audio.getframerate())

stream = p.open(
    format=p.get_format_from_width(audio.getsampwidth()),
    channels=audio.getnchannels(),
    rate = 2 * 160000, # Change this to play audio at different sample rates
    output=True
)

while data:
    stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()

