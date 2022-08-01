# This is simple program to that will say a personalised message to a user.
# We make use of the gTTS(Google Text to speech) library here.


import tkinter
import playsound
import os
from gtts import gTTS
# We create a function that can say a personalised welcome message with an input text
def TTS(text1):
    texttoSpeech = gTTS("Welcome " + text1)                  # gTTS function converts the text into speech
    texttoSpeech.save("Speech1.mp3")                         # We save the file as an mp3 file
    playsound.playsound('type in the address to which Speech1 is stored', True)  # Specify the address and use the playsound function to play the saved file
    os.remove('Speech1.mp3')                                 # The os.remove function is used to remove the file path


mywindow= tkinter.Tk()               # The tkinter library is used to create a window where we can display a message.
mywindow.title("Greeting Window")
mywindow.geometry('550x350')

tkinter.Label(mywindow,text="Greetings Window ",font =("Arial",16)).place(x=170,y=10)
tkinter.Label(mywindow,text="Please Enter Your Name: ",font =("Arial",16)).place(x=0,y=100)
name = tkinter.Entry(mywindow,font =("Arial",16),width=30)
name.place(x=250,y=100)

    
# Here we create a function that will be called for the enter button we are about t create.
def submit():
    text1 = name.get()
    TTS(text1)

mybutton = tkinter.Button(mywindow,text="Enter",font =("Arial",16), command = submit).place(x=200,y=150)


mywindow.mainloop()     # This function tells python to keep the tkinter window running until it is closed.
