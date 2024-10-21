import sounddevice as sd
import numpy as np
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import pyperclip
import threading
import msvcrt

# Load Whisper Large V3 Turbo model and processor
model_dir = "./whisper-large-v3-turbo"
model = AutoModelForSpeechSeq2Seq.from_pretrained(model_dir)
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained(model_dir)

# Set up the pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    device=device
)

# Initialize variables for recording
sampling_rate = 16000  # Whisper works best with 16kHz
recording = []
is_recording = False
recording_thread = None

def record_audio():
    global recording
    def callback(indata, frames, time, status):
        if is_recording:
            recording.append(indata.copy())

    with sd.InputStream(samplerate=sampling_rate, channels=1, callback=callback):
        while is_recording:
            sd.sleep(100)

def start_recording():
    global is_recording, recording_thread
    is_recording = True
    recording.clear()  # Reset recording buffer
    print("Recording started...")
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

def stop_recording():
    global is_recording, recording_thread
    is_recording = False
    if recording_thread:
        recording_thread.join()
    print("Recording stopped.")
    
    # Convert the recording to a numpy array
    audio_data = np.concatenate(recording, axis=0).flatten()
    
    # Perform transcription directly on raw audio data
    result = pipe(audio_data)["text"]

    # Print the result to the console
    print("Transcribed Text:", result)
    
    # Copy the result to the clipboard
    pyperclip.copy(result)
    print("Transcription copied to clipboard.")

def main():
    global is_recording
    print("Press 'r' to start/stop recording, 'q' to quit:")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'r':
                if not is_recording:
                    start_recording()
                else:
                    stop_recording()
            elif key == 'q':
                if is_recording:
                    stop_recording()
                print("Exiting...")
                break

if __name__ == "__main__":
    main()