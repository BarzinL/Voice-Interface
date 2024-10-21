# Voice Interface for Speech-to-Text Transcription

This script is a simple voice interface that allows you to record from your microphone with a keypress, the transcription for which is created via the Whisper Large V3 Turbo model, and automatically copy the transcribed material to the clipboard.

The intended use of this is to enable the user to paste their speech as text into the ChatGPT web application which at the moment of this writing still does not have voice capability.

## Features
- Real-time speech recording with a sampling rate of 16kHz.
- Transcription of recorded audio using Whisper Large V3 Turbo.
- Auto-copy the transcribed text to the system clipboard.
- Keyboard controls to start/stop recording and quit the program.

## Prerequisites

Before running the code, ensure that you have the following dependencies installed:

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for managing the environment.
- Python 3.12.7 or higher.
- The necessary Python libraries, as listed below.

## Installation

### Step 1: Set Up a Conda Environment

Create a new Conda environment and activate it:

```bash
conda create --name voice-interface python=3.12.7
conda activate voice-interface
```

### Step 2: Install Dependencies

Run the following command to install the required libraries:

```bash
pip install sounddevice numpy torch transformers pyperclip
```

### Step 3: Download Whisper Large V3 Turbo Model

The Whisper Large V3 Turbo model should be placed in the `/whisper-large-v3-turbo` directory. You can find the model file [here](https://huggingface.co/openai/whisper-large-v3-turbo/blob/main/model.safetensors).

Ensure the downloaded model file is located at `./whisper-large-v3-turbo/model.safetensors`.

## Running the Code

After setting up the environment and placing the model file in the correct directory, you can run the script:

```bash
python main.py
```

### Keyboard Controls

- Press **`r`** to start or stop recording.
- Press **`q`** to quit the application.

The transcribed text will be printed to the console and copied to your clipboard for easy use.

## Notes

- The transcription pipeline uses the Whisper Large V3 Turbo model, which works best with a 16kHz sampling rate.
- The application automatically detects if a CUDA-enabled GPU is available and will utilize it for faster processing if available.
- Audio input is recorded using the system's default microphone.

## License

This project is licensed under the terms of the MIT license.