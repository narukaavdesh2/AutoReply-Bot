import pyautogui
import time
import pyperclip
import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

def get_last_sender(chat_log):
    lines = chat_log.strip().splitlines()
    for line in reversed(lines):
        if "]" in line and ":" in line:
            try:
                sender = line.split("]")[1].split(":")[0].strip()
                return sender
            except IndexError:
                continue
    return None

# ✅ Step 1: One-time click to open Chrome
pyautogui.click(1431, 1056)  # Your Chrome icon
time.sleep(2)

last_chat = ""

while True:
    time.sleep(5)

    # ✅ Step 2: Select chat area and copy
    pyautogui.moveTo(857, 225)
    pyautogui.dragTo(1551, 992, duration=2.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # ✅ Step 3: Retrieve chat content
    chat_history = pyperclip.paste()
    print("Chat:\n", chat_history)

    sender = get_last_sender(chat_history)
    print("Last sender:", sender)

    if sender != "avdesh Singh" and chat_history.strip() != last_chat.strip():
        last_chat = chat_history

        # ✅ Step 4: Generate response
        response = model.generate_content([
            "You are a person named avdesh who speaks Hindi as well as English. You are from India. You analyze chat history and reply them in a friendly way. Output should be the next chat response (text message only) but reply should be small.",
            chat_history
        ]).text

        print("Generated response:", response)
        pyperclip.copy(response)

        # ✅ Step 5: Click input box every time
        pyautogui.click(962, 932)  # Focus WhatsApp message box
        time.sleep(1)

        # ✅ Step 6: Paste and send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
    else:
        print("No new message or message sent by you.")
