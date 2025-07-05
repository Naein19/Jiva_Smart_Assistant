# Jiva_Smart_Assistant
# 🧠 Jiva - AI Voice Assistant

**Jiva** is a smart, voice-based personal assistant inspired by J.A.R.V.I.S. from Iron Man — with an Indian soul.  
It helps you perform intelligent tasks via voice or web interface:

- 🔍 Web search  
- 📬 Send emails via Gmail  
- ☁️ Get real-time weather reports  
- 🤖 Ask questions (powered by Gemini AI)  
- 📆 Get date, time, day, and India-specific festivals or events  
- 💬 Open and message via WhatsApp Desktop  
- 💻 Open apps on your PC  
- 📝 Create folders and files via voice  
- 🖥️ Beautiful web UI using Gradio

---

## 🗂️ Project Structure

jiva/
├── agent.py
├── tools.py
├── prompts.py
├── test_gemini.py
├── app.py
├── requirements.txt
├── .env

## 🔐 .env Example

```env
GOOGLE_API_KEY=your_google_gemini_key
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_SECRET=your_livekit_secret
LIVEKIT_URL=wss://your-livekit-url
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
MY_WHATSAPP_NUMBER=+91XXXXXXXXXX
```

---

## 📦 Installation

1. Clone the repo and `cd` into the project folder.
2. Create your `.env` file with correct keys.
3. Install required dependencies:

```bash
pip install -r requirements.txt
```


## ▶️ Usage

### Start voice assistant via terminal:
```bash
python agent.py
```

### Test Gemini AI separately:
```bash
python test_gemini.py
```

### Launch Gradio web interface:
```bash
python app.py
```

---

## 🧪 Sample Commands

- “What’s the weather in Mumbai?”
- “Send an email to test@example.com with subject Hello and message Let’s meet.”
- “Open WhatsApp”
- “Send WhatsApp message to +91xxxxxxxxxx saying I’ll call you at 4.”
- “What happened on August 15?”
- “Tell me today’s date and time”
- “What is Artificial Intelligence?”


## ⚠️ Notes

- ✅ Be logged into WhatsApp Desktop (for messaging)
- ✅ Use Gmail **App Password**, not your login password
- 🌐 Gemini models may hit free-tier limits – `gemini-1.5-flash` is best for free use
- 📍 Festival/day info defaults to: `India`, city: `Vijayawada`

---

## 🛡️ Security

Never expose `.env` files or commit credentials to public repositories.  
Add `.env` and `__pycache__/` to `.gitignore`.

---

## 👨‍💻 Author

Created by :Tadaka Naveen  
Powered by:

- [Google Gemini AI](https://ai.google.dev/)
- [LiveKit Agents](https://livekit.io/)
- [Gradio](https://gradio.app/)
- [DuckDuckGo Search](https://duckduckgo.com)

---

## 📌 Future Upgrades

- GPT-4 or Claude fallback
- PDF/file summarizer
- Auto meeting scheduler
- Task automation memory
- Voice command logging and history

---
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
