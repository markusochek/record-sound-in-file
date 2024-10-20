import serial
import wave

ser = serial.Serial('COM9', 115200)  # Укажите правильный COM-порт
output_file = "recorded_audio.wav"

audio = []
try:
    print("Recording... Press Ctrl+C to stop.")
    while True:
        audio.append(ord(ser.read(1)))
except KeyboardInterrupt:
    print("Recording stopped.")

with wave.open(output_file, 'wb') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(1)
    wav_file.setframerate(8000)
    wav_file.writeframes(bytearray(audio))

print(f"Audio saved to {output_file}")