import random
import datetime
import calendar
import os
import pytesseract
import cv2
import webbrowser
import smtplib
import wikipedia
import pyjokes

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good morning, how may I help you?"
    elif 12 <= hour < 16:
        return "Good afternoon, how may I help you?"
    else:
        return "Good evening, how may I help you?"

def get_today_date():
    now = datetime.datetime.now()
    week_day = calendar.day_name[now.weekday()]
    month = now.strftime("%B")
    day = now.day
    return f'Today is {week_day}, {month} {day}.'

def chatbot_response(input_text):
    responses = {
        "hello": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm good, thanks!", "I'm doing well.", "I'm fine."],
        "date": [get_today_date()],
        "time": [f"It is {datetime.datetime.now().strftime('%I:%M %p')}.", "The time is now {datetime.datetime.now().strftime('%I:%M %p')}."],
        "joke": [pyjokes.get_joke()],
        # Add more responses and features based on user input
    }

    input_text = input_text.lower()
    if input_text in responses:
        return random.choice(responses[input_text])
    elif "search" in input_text:
        search_query = input_text.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return f"I've opened a Google search for '{search_query}'."
    elif "email" in input_text:
        # Implement email sending logic here
        return "Sorry, email functionality is not implemented in this version."
    elif "open" in input_text:
        app_mapping = {
            "chrome": "Google Chrome",
            "word": "Microsoft Word",
            "excel": "Microsoft Excel",
            "vs code": "Visual Studio Code",
            "brave": "Brave Browser",
        }
        app_name = input_text.split("open")[1].strip()
        if app_name in app_mapping:
            os.system(f"start {app_mapping[app_name]}")
            return f"Opening {app_name}..."
        else:
            return f"Sorry, I don't know how to open {app_name}."
    else:
        return "I'm not sure how to respond to that."

print("Chatbot: " + greet())
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
