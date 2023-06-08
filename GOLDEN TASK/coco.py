import speech_recognition as aa 
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)

machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "coco" in instruction:
                instruction = instruction.replace("coco"," ")
                print("instruction")
 
    except:
        pass
    return instruction

def play_coco():
    global instruction
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play',"")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%P')
        talk('current time' + time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%y') 
        talk("Today's Date" + date)

    elif "what is your name" in instruction:
        talk("My name is coco, what can i do for you?")

    elif "how are you" in instruction:
        talk("i'm fine, what about you?")

    elif "who is" in instruction:
        human = instruction.replace("who is", " ")
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)

    else:
        talk("please repeat")

play_coco()