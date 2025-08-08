# 🤖 AutoReply ChatBot

AutoReply ChatBot is a Python-based automation tool that uses Google's **Gemini API** to generate smart replies based on copied chat conversations. The bot is designed to assist users in responding to messages quickly and intelligently.

---

## 🚀 Features

- ✅ Automatically detects the last message in a conversation
- 🤖 Uses **Gemini AI** (by Google) to generate context-aware responses
- 📋 Works with copied chat logs (e.g., from messaging apps)
- ⌨️ Can simulate typing and sending the generated message
- 🧠 Maintains continuity using previous conversation history

---

## 🧰 Tech Stack

- **Python**
- **Google Generative AI (Gemini API)**
- `pyautogui` – for keyboard and mouse automation
- `pyperclip` – to access clipboard content
- `dotenv` – for managing API keys securely

---

## ⚙️ How It Works

1. **Copy** the recent chat conversation.
2. The script captures the copied text and extracts the latest message.
3. It sends the context to **Gemini API** and receives a suitable response.
4. The response is typed and sent automatically using `pyautogui`.

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here


Getting Starded

# Clone the repo
git clone https://github.com/narukaavdesh2/AutoReply-Bot.git
cd AutoReply-Bot

# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
