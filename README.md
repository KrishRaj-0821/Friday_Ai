# Friday_Ai

# 🤖 Friday – Your Personal Python Voice Assistant

Friday is a **voice-controlled AI assistant** built with Python. It listens to your commands, talks back with a natural voice, and can perform tasks like telling the time, fetching Wikipedia info, checking the weather, and doing calculations – all hands-free!


✨ Features

✅ **Voice Commands:** Speak naturally; Friday understands and responds.
✅ **Day-Based Greeting:** Greets you with the current day of the week.
✅ **Time Updates:** Asks “What’s the time?” to get the current time instantly.
✅ **Weather Reports:** Live weather updates using the OpenWeatherMap API.
✅ **Wikipedia Search:** Get quick 2-line summaries for any topic.
✅ **Voice Calculator:** Perform basic math calculations via voice.
✅ **Interactive Exit:** Say “quit”, “exit”, or “bye” to close the assistant.

📦 Tech Stack

* 🗣️ **speech\_recognition** – For capturing and converting your voice to text
* 🔊 **pyttsx3** – Offline Text-to-Speech engine for voice replies
* 🌐 **requests** – To fetch live weather data
* 📚 **wikipedia** – For Wikipedia summaries
* 🧮 **re** – Secure math evaluation with regex
* 
## 🛠️ Installation

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/your-username/friday-assistant.git
cd friday-assistant
```

2️⃣ **Install required packages:**

```bash
pip install pyttsx3 speechrecognition wikipedia requests
```

3️⃣ **(Optional)** Install `pyaudio` for better microphone support:

* Windows: `pip install pyaudio`
* Linux: `sudo apt-get install python3-pyaudio`

4️⃣ **Add your OpenWeatherMap API Key:**

* Open `friday_assistant.py`
* Replace `"YOUR_API_KEY"` with your API key in the `get_weather()` function.

---

▶️ Usage

Run Friday from your terminal:

```bash
python friday_assistant.py
```

🎤 **Sample Commands:**

* “What’s the time?”
* “Tell me the weather”
* “Search Wikipedia for Albert Einstein”
* “Calculate 25 \* 6”
* “Bye”

🔮 Future Improvements

* 🧠 Add conversation memory
* 🗂️ Open apps and control PC with voice
* 🤖 Integrate GPT-based AI for smarter responses
* 🎶 Play music or fetch news

---

📜 License

MIT License – Feel free to fork and modify.

---

⭐ Star this repo if you like Friday!


Do you want me to also make a **fancy GitHub tagline + badges (e.g., Python version, open source, license)** at the top, so it looks professional like popular repos?

