# Virtual Assistant

Virtual Assistant is a program that lets users address their requests and automate their desired functions. It is a Python 3 based project, but developers using all programming language are welcome here to contribute their work towards its development.

It is a voice controlled virtual assistant with just Python, yet 
developers can use any language to integrate new features into it.

Its functionality involves:

- The virtual assistant would only accept futher tasks after getting the correct password (i.e., it is password protected).

- Firstly, it greets you according to time of execution and could also tell you the current time (if asked for).

- Following this, you can do web scraping to grab data from:

    1. Wikipedia 
    2. YouTube
    3. Google search 
    etc.

- You can send mails by voice control or by texting it to the virtual assistant.

- You can directly perform simple mathematical calculations in it.

- You can translate your content to different languages

- You can listen to your favourite music (it redirects you to Spotify)

- You can quit it anytime by saying 'bye', 'logout' or 'deactivate'.

## Using the code

To use the code locally, you'll firstly need to have Python v3 installed. You can download it from [https://www.python.org/downloads/], if it isn't already in your system.

Then, you'll need to run the following command to ensure that all the related dependencies are configured into your system.

     python -m pip install pyttsx3 speech_recognition wikipedia smtplib googletrans difflib

**NOTE**: In Ubuntu and Mac OS, use `python3` instead of `python`, if both _Python 2_ as well as _Python 3_ have come installed in your system.

Then, you can simply execute the script using any Python interpreter, or by using the following command into your terminal: 

     python "virtual assistant.py"

That's it! Now, you can relax, and let the code help you out! 😉
