# This is simple program to that will say a personalised message to a user.
# We make use of the gTTS(Google Text to speech) library here.


import tkinter
import playsound
import os
from gtts import gTTS

mywindow= tkinter.Tk()               # The tkinter library is used to create a window where we can display a message.
mywindow.title("Greeting Window")
mywindow.geometry('550x350')

tkinter.Label(mywindow,text="Greetings Window ",font =("Arial",16)).place(x=170,y=10)
tkinter.Label(mywindow,text="Please Enter Your Name: ",font =("Arial",16)).place(x=0,y=100)
name = tkinter.Entry(mywindow,font =("Arial",16),width=30)
name.place(x=250,y=100)
def TTS(text1):
    texttoSpeech = gTTS("Welcome " + text1)
    texttoSpeech.save("Speech1.mp3")
    playsound.playsound('C:/Users/asus/Desktop/Srishti Robotics/2. Python/Speech1.mp3', True)
    os.remove('Speech1.mp3')
    

def submit():
    text1 = name.get()
    TTS(text1)

mybutton = tkinter.Button(mywindow,text="Enter",font =("Arial",16), command = submit).place(x=200,y=150)


mywindow.mainloop() 
