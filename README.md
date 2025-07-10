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
pip install -r requirements.txt
