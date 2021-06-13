# Simple AI virtual assistant code in python
# Part 1 - Import statememt
import wolframalpha
client = wolframalpha.Client('UA687L-9RRVL6VTJ8')
import PySimpleGUI as sg
import wikipedia
import pyttsx3
# Object creations:
engine = pyttsx3.init()
# voice control(0 female, 1 male)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# Part 2 - The Layout
# Define the window's contents
sg.theme('dark blue')
layout = [[sg.Text("Enter your command!")], [sg.InputText()],
          [sg.Button('Ok')], [sg.Button('Cancel')]]

# Create the window
window = sg.Window('Alexa', layout)

# Part 3 Event loop and handling excpetions:
while True:
    event, values = window.read()
    if event in (None, "Cancel"):
        break
    try:
        wolfram_res = next(client.query(values[0]).results).text
        # engine.say(wolfram_res)
        wiki_res = wikipedia.summary(values[0], sentences=1)
        engine.say(wolfram_res)
        sg.popup_non_blocking("Wolfram Result: " + wolfram_res, "Wiki Result " + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.popup_non_blocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=1)
        engine.say(wiki_res)
        sg.popup_non_blocking(wiki_res)
    engine.runAndWait()
    print (values[0])
# Do something with the information gathered
# sg.popup(next(res.results).text)
# part 4: closing the window
window.close()