# 🎓 Voice Assistant

## Overview

Welcome to the Voice Assistant project, a sophisticated and innovative solution designed to facilitate interaction through voice commands. Utilizing OpenAI's ChatGPT, this assistant processes and responds to user queries in audio format, integrating advanced technologies for voice recognition and audio playback. Our goal is to provide a seamless and intuitive interface for users to access information and perform tasks using natural language.

## 🌐 Features

- **🎙 Voice Recording**: Harnesses microphone technology to capture user voice inputs, incorporating dynamic silence detection to ascertain the completion of queries.
- **📝 Speech Recognition**: Utilizes state-of-the-art speech-to-text models to transcribe voice inputs accurately, converting spoken language into textual data.
- **💡 ChatGPT Integration**: Employs the robust capabilities of the ChatGPT API to interpret transcribed texts and generate relevant responses.
- **🔎 Response Shortening**: Implements intelligent algorithms to condense ChatGPT responses, ensuring brevity and relevance within the constraints of audio playback.
- **🗣 Text-to-Speech**: Transforms text responses into spoken words through a high-fidelity text-to-speech engine, enhancing the auditory experience for users.
- **🔊 Audio Playback**: Delivers the generated audio response, completing the interactive communication loop with the user.

## 📋 How It Works

1. **🎤 Record Audio**: Activates audio recording via the microphone, ceasing automatically upon detecting prolonged silence to signify the end of a query.
2. **📝 Transcribe Audio**: Processes the audio file through a speech recognition model, transcribing the vocal input into textual form.
3. **💡 Process Query**: Forwards the transcribed text to the ChatGPT API, which formulates a response grounded in the context of the query.
4. **🔎 Shorten Response**: Applies response shortening techniques as needed, ensuring the output is succinct and suitable for audio delivery.
5. **🗣 Generate Audio**: Converts the processed response into audio, utilizing a text-to-speech engine for natural voice output.
6. **🔊 Play Audio**: Executes the playback of the generated audio file, culminating the user interaction cycle.

## 🛠 Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Microphone access
- An OpenAI API key for ChatGPT access

### Setup Instructions

1. **📥 Clone the Repository**: Obtain the project's codebase by cloning this repository to your local machine.
    ```bash
    git clone https://github.com/uladkaminski/local-assistant-gpt.git
    ```
2. **🔧 Install Dependencies**: Transition to the project's directory and install the requisite Python packages.
    ```bash
    pip install -r requirements.txt
    ```
3. **🔑 Environment Variables**: Generate a `.env.dev` file at the project root and populate it with your OpenAI API key.
    ```plaintext
    OPENAI_API_KEY=your_api_key_here
    ```
4. **🎤 Verify Microphone Access**: Ensure your system grants microphone access to Python scripts, adjusting privacy settings if necessary.

5. **🚀 Test Installation**: Execute a preliminary test to verify the setup's integrity, such as recording and playing back a brief audio clip.
    ```bash
    python main.py --test
    ```
6. **📢 Usage**: Initiate the voice assistant by running the `main.py` script and interact through voice commands.
    ```bash
    python main.py
    ```

## 📜 License

This project is distributed under the MIT License. For more details, refer to the LICENSE file.
