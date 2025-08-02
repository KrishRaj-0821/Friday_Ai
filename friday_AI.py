import pyttsx3  # Text-to-speech library
import speech_recognition as sr  # Speech recognition library
import datetime  # For working with date and time
import wikipedia  # To get information from Wikipedia
import requests  # To make HTTP requests (e.g., for weather)
import subprocess  # Import subprocess
import time  # Import time
import re  # Import regular expressions

# Step 3: Initialize the Text-to-Speech Engine
engine = pyttsx3.init()

# Optional: Change voice (if available)
voices = engine.getProperty('voices')
# 0 for male, 1 for female
engine.setProperty('voice', voices[1].id)  # Change to 1 for female voice if available


# Step 4: Create a Function for the Assistant to Speak
def speak(text):
    """
    This function makes the assistant speak the given text.
    """
    engine.say(text)
    engine.runAndWait()


# Step 5: Create a Function to Listen for User Input
def take_command():
    """
    This function listens to the user's voice, converts it to text,
    and returns the text.  It handles potential errors during speech recognition.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # Reduced pause threshold (default is 0.8)
        r.phrase_time_limit = 5  # Add phrase time limit.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        start_time = time.time()  # start time
        query = r.recognize_google(audio, language='en-in')  # Use 'en-in' for Indian English
        end_time = time.time()  # end time
        print(f"User said: {query}\n")
        print(f"Recognition took {end_time - start_time:.2f} seconds")  # print the time taken

    except sr.WaitTimeoutError:  # handle timeout error
        print("No speech detected.  Please try again.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")  # Print the specific error message
        print("Say that again please...")  # More user-friendly
        return "None"  # Important: Return "None" on error
    return query


def get_weather(city_name):
    """
    Fetches weather information for a given city using the OpenWeatherMap API.
    Replace 'YOUR_API_KEY' with your actual API key.
    """
    api_key = "YOUR_API_KEY"  # Replace with your API key from OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"  # Get in Celsius
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        #  Make sure the city was found
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = data["weather"][0]["description"]
        weather_report = (
            f"The temperature in {city_name} is {temperature} degrees Celsius, "
            f"with {humidity}% humidity. The weather is described as {description}."
        )
        return weather_report
    else:
        return "Sorry, I couldn't find weather information for that city."


def get_day_of_week():
    """
    Gets the current day of the week.
    """
    now = datetime.datetime.now()
    day_name = now.strftime("%A")  # Full day name (e.g., "Friday")
    return day_name


def perform_calculation(expression):
    """
    Safely performs basic arithmetic calculations from a string expression.
    Uses a whitelist of allowed operators and digits to prevent arbitrary code execution.
    """
    # Whitelist of allowed characters and operators.  This is CRITICAL for security.
    allowed_chars = r"[0-9+\-*/(). ]"  # Include space
    if not re.match(r"^" + allowed_chars + "*$", expression):
        return "Error: Invalid characters in expression."
    try:
        # Use eval, but it's now much safer because of the input filtering
        result = eval(expression)
        return str(result)  # Convert the result to a string before returning
    except Exception:
        return "Error: Calculation failed."

# Step 6: Implement Friday-Related Functionality
if __name__ == "__main__":
    # Attempt to fix the distutils error at the start.
    try:
        from packaging import version
    except ImportError:
        print("Required 'packaging' module not found. Installing...")
        subprocess.check_call(['pip', 'install', 'packaging'])
        from packaging import version

    # Example version check (optional)
    if version.parse("3.12") <= version.parse("3.13"):
        print("Warning: distutils module is deprecated in your Python version.")

    day_of_week = get_day_of_week()  # get the day
    if day_of_week == "Friday":
        speak(f" Hello bose! It's {day_of_week} today. How can I help you today?")
    else:
        speak(f" Hello bose! It's {day_of_week} today. How can I help you today?")
    while True:
        query = take_command().lower()

        if 'time' in query:
            now = datetime.datetime.now().strftime("%I:%M %p")  # Get time in 12-hour format
            speak(f"The current time is {now}")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)  # Get a 2-sentence summary
                speak("According to Wikipedia...")
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find that page on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Wikipedia found multiple possible pages. Could you be more specific?")
                print(e)  # print the options

        elif 'weather' in query:
            speak("Please tell me the city name")
            city = take_command().lower()
            if city != "None":
                weather_report = get_weather(city)
                speak(weather_report)

        elif 'calculate' in query or 'Do calculation' in query:
            speak("Please tell me the expression you want me to calculate.")
            expression = take_command()
            if expression != "None":
                result = perform_calculation(expression)
                speak(f"The result is {result}")

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Have a great day!")
            break

        elif query != "None":
            speak("Sorry, I didn't understand that.")
        # else: # removed this else, so it doesn't speak when query is None
        # speak("I am waiting for your command") # Removed this line. It was causing too much chatter.
