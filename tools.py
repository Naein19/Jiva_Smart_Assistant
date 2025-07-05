import os
import logging
import subprocess
import datetime
import psutil
import pywhatkit
import pytesseract
import pyautogui
from PIL import Image
from livekit.agents import function_tool, RunContext
from langchain_community.tools import DuckDuckGoSearchRun
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai
import datetime
import wikipedia

from dateutil import parser
from dateutil.parser import ParserError

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


@function_tool()
async def get_weather(context: RunContext, city: str) -> str:
    try:
        response = requests.get(f"https://wttr.in/{city}?format=3")
        return response.text.strip() if response.status_code == 200 else f"Couldn't get weather for {city}."
    except Exception as e:
        return f"Weather error: {e}"

@function_tool()
async def search_web(context: RunContext, query: str) -> str:
    try:
        return DuckDuckGoSearchRun().run(tool_input=query)[:300]
    except Exception as e:
        return f"Search error: {e}"

@function_tool()
async def send_email(context: RunContext, to_email: str, subject: str, message: str, cc_email: Optional[str] = None) -> str:
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.getenv("GMAIL_USER"), os.getenv("GMAIL_APP_PASSWORD"))
        msg = MIMEMultipart()
        msg['From'] = os.getenv("GMAIL_USER")
        msg['To'] = to_email
        msg['Subject'] = subject
        if cc_email:
            msg['Cc'] = cc_email
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(os.getenv("GMAIL_USER"), [to_email] + ([cc_email] if cc_email else []), msg.as_string())
        server.quit()
        return f"Email sent to {to_email}"
    except Exception as e:
        return f"Email error: {e}"

@function_tool()
async def ask_ai(context: RunContext, query: str) -> str:
    try:
        model_name = os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash")
        model = genai.GenerativeModel(model_name=model_name)

        print(f"🧠 Asking Gemini ({model_name}): {query}")
        response = model.generate_content(query)
        print("📤 Gemini Response:", response.text)

        return f"As you wish, Sir. \"{response.text}\""
    except Exception as e:
        print("❌ Gemini Error:", e)
        return "Apologies Sir, I couldn't retrieve the answer from my intelligence matrix."



@function_tool()
async def control_app(context: RunContext, action: str, app_name: str) -> str:
    try:
        if action.lower() == "open":
            subprocess.Popen(app_name)
            return f"Opened {app_name}."
        elif action.lower() == "close":
            for proc in psutil.process_iter():
                if app_name.lower() in proc.name().lower():
                    proc.kill()
                    return f"Closed {app_name}."
            return f"{app_name} not running."
        return "Action must be open or close."
    except Exception as e:
        return f"App control error: {e}"

@function_tool()
async def read_screen(context: RunContext) -> str:
    try:
        return pytesseract.image_to_string(pyautogui.screenshot()).strip()
    except Exception as e:
        return f"Screen read error: {e}"

@function_tool()
async def write_to_file(context: RunContext, file_path: str, content: str) -> str:
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Wrote to {file_path}."
    except Exception as e:
        return f"File write error: {e}"

@function_tool()
async def create_folder(context: RunContext, folder_path: str) -> str:
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder created at {folder_path}."
    except Exception as e:
        return f"Folder error: {e}"

@function_tool()
async def open_whatsapp(context: RunContext) -> str:
    try:
        subprocess.Popen("WhatsApp.exe")
        return "WhatsApp opened."
    except Exception as e:
        return f"WhatsApp open error: {e}"

@function_tool()
async def send_whatsapp_message(context: RunContext, recipient_number: str = "", message: str = "") -> str:
    try:
        if not recipient_number:
            recipient_number = await context.ask_user("Whom should I message?")
        if not message:
            message = await context.ask_user("What is the message?")
        pywhatkit.sendwhatmsg_instantly(recipient_number, message, wait_time=10)
        return f"Message sent to {recipient_number}"
    except Exception as e:
        return f"WhatsApp message error: {e}"





from dateutil import parser
from dateutil.parser import ParserError

@function_tool()
async def get_day_info(context: RunContext, date_str: Optional[str] = None) -> str:
    """
    Tells current date/time/day or provides info on a specific date.
    """
    try:
        now = datetime.datetime.now()

        # If no date given, respond with current info
        if not date_str:
            date_info = now.strftime("%A, %d %B %Y, %I:%M %p")
            return f"Today is {date_info} in Vijayawada, India. Would you like to know about any specific day or festival?"

        # Try parsing full date (with year)
        try:
            parsed_date = parser.parse(date_str, fuzzy=True)
        except ParserError:
            return "Sorry, I couldn't understand the date format. Try something like 'August 15' or 'January 26 1950'."

        # If no year is present in input, force it to current year
        if parsed_date.year == 1900:  # parser default when year not given
            parsed_date = parsed_date.replace(year=now.year)

        formatted_date = parsed_date.strftime("%B %-d")  # 'August 15'
        try:
            summary = wikipedia.summary(formatted_date, sentences=5, auto_suggest=False)
        except Exception:
            summary = "Couldn't find historical events for that date, Sir."

        return f"Here's what happened on {formatted_date}: {summary}"

    except Exception as e:
        return f"An error occurred while retrieving date info: {str(e)}"


