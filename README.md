# Jarvis - A Voice-Controlled Python Assistant 

Jarvis is a lightweight Python-based voice assistant that can:
- Open websites
- Fetch news headlines
- Play your favorite music from YouTube
- Answer general queries using OpenAI's GPT
- Speak responses back to you

---

## Features

- **Speech Recognition**: Understands voice commands using `speech_recognition`.
- **Speech Output**: Responds via `pyttsx3` or `gTTS` + `pygame` audio.
- **Web Control**: Opens Google, YouTube, Facebook, LinkedIn, etc.
- **News Headlines**: Reads the latest news using NewsAPI.
- **AI Chat**: Uses OpenAI GPT for open-ended user queries.
- **Music Library**: Plays music from a predefined YouTube link library.

---

## Requirements

Install dependencies with:

```bash
pip install -r Requirements.txt
```

Usage

### 1. Clone the repo:

git clone https://github.com/YOUR_USERNAME/jarvis-voice-assistant.git
cd jarvis-voice-assistant

### 2. Update your own:

OpenAI API key in main.py

NewsAPI key in main.py

Customize your music links in musiclibrary.py



### 3. Run it:


```bash
python3 main.py

Speak Jarvis to activate the assistant.
```

---

###Example Commands

“Jarvis” → activates assistant

“Open Google”

“Play Legends Never Die”

“Give me the news”

“What is the capital of France?”



---

### Notes

Works best in a quiet environment with a decent mic.

Only supports predefined music names from musiclibrary.py.

You’ll need pygame, gTTS, speech_recognition, and openai.

### Author 
Made by - Shreya Kumari 
