#some import lines in this program are unwanted and not used inside the program.

import time
import sys
import os
from tkinter import *
import openai
import tkinter as tk
import time as sleep2
import subprocess
import pyautogui
import pygetwindow as gw
import datetime
from tkinter import Tk, Label
# Here the there will be a todo / given as the prompt to the API then the response will displayed using tkinter window as a pop-up

#The below code is the main window UI Design functionalities due to lack of API GPT4.This is just a local deployment of Personal TO-DO list AI
def loop():
    window = Tk()
    def writer():
        with open("logs.txt",'r')as Reader:
            global readlines
            readlines=Reader.readlines()
            boom=str(readlines)
            if(readlines==""):
                    msg="EMPTY"
            else:
                    msg="TODO"
                    nologstag=Label(window,text=msg,font=('Terminal',8),
                                        fg="green",bg="#2B2B2B")
                    nologstag.place(x=190,y=218)
                    if(len(readlines)>=1):
                        global yPosition
                        global indexVal
                        yPosition=235
                        indexVal=0
                        for i in range(len(readlines)):
                            if(indexVal<=len(readlines)):
                                loginwindow=Label(window,text=readlines[indexVal],font=('Times',8),
                                    fg="white",bg="#2B2B2B")
                                loginwindow.place(x=0,y=yPosition)
                                indexVal+=1
                                yPosition+=17
    writer()
    #this part of program will read the existing local file and depending on that it returns 2 workaples for tkinter window
    def title():
        with open("logs.txt",'r')as Reader2:
                global readlinesMain
                readlinesMain=Reader2.readlines()
                if(len(readlinesMain)<=0):
                    msg="EMPTY"
                else:
                    msg="TODO"
                nologstag=Label(window,text=msg,font=('Terminal',8),
                                fg="green",bg="#2B2B2B")
                nologstag.place(x=190,y=218)
    def on_entry_click(event):
        if entry.get() == "Give a TO-DO name":
            entry.delete(0, END)
            entry.config(fg='white')  # Change text color to black

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, "Give a TO-DO name")
            entry.config(fg='grey')  # Change text color to grey
    entry = Entry(window, font=("Arial", 10), fg='grey')
    entry.insert(0, "Give a TO-DO name")
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focus_out)
    entry.config(fg='grey',bg='black')  # Set default text color to grey
    
    def onclick_run():#this onclick() function will run if a user taps on submit button on the window
        global submit
        submit =tk.Button(window, text="Done", font=("Comic Sans", 10), fg="#00FF00", bg="black",
                    activebackground="#00FF00", activeforeground="black", command=on_submit)
        submit.place(x=160, y=95)
        global delete
        delete = tk.Button(window, text="Cancel", font=("Comic Sans", 10), fg="#00FF00", bg="black",
                    activebackground="#00FF00", activeforeground="black", command="")
        delete.place(x=210, y=95)
        entry.place(x=150, y=70)    

    window.title("TO-DO Ai")#Design and looks of window of tkinter framework
    window.geometry("420x420")

    window.config(background="#2B2B2B")

    label = Label(window, text="Hi geek, create your TO-DO's. We make your life easier", font=('Arial', 10, 'bold'),
                fg="white", bg="#2B2B2B")
    label.place(x=0, y=0)
    title()
    seperator=Label(window,text="------------------------------------------------------------",font=('Arial',15),
                    fg="blue",bg="#2B2B2B")
    #seperator.place(x=0,y=10)


    button = Button(window, text="New", font=("Comic Sans", 10), fg="#00FF00", bg="black",
                    activebackground="#00FF00", activeforeground="black", command=onclick_run, state=ACTIVE)
    button.place(x=200, y=35)
    global due_date
    global due_time
    from tkinter import simpledialog
    from tkinter import messagebox as ms
    global epudra 
    epudra=235
    with open("logs.txt",'r')as reader20:
        global reader2
        reader2=reader20.readlines()
        increase=17  
        epudra+=increase*len(reader2)
    def on_submit():
        global entryvalue
        global epudra
        entryvalue=entry.get()
        title()
        if entryvalue=="Give a TO-DO name":
            ms.showerror(title="Empty todo",message="Please give a name first")
        else:
            due_date = simpledialog.askstring("Input", "Enter the due date (YYYY-MM-DD):", parent=window)
            due_time = simpledialog.askstring("Input", "Enter the due time (HH:MM):", parent=window)
            submit.destroy()
            delete.destroy()
            entry.place_forget()
            
            with open("logs.txt",'a')as file:
                
                global todoscale
                todoscale=entryvalue+" "+due_date+" "+due_time
                file.write(todoscale+"\n")
                todo=entry.get()
            
                indexVal=0
                if(indexVal<=len(readlines)):
                    loginwindow=Label(window,text=todoscale,font=('Times',8),
                        fg="white",bg="#2B2B2B")
                    loginwindow.place(x=0,y=epudra)
                    indexVal+=1
                    epudra+=17
    def popup():
        window.deiconify()
        window.lift()
    
    seperator.place(x=0,y=190)

    def insert_newline_after_n_words(text, n):
            words = text.split()
            result = []
            for i, word in enumerate(words, start=1):
                result.append(word)
                if i % n == 0:
                    result.append('\n')
            return ' '.join(result)

    def insert_text_with_line_breaks(text, n):
            # Open Notepad
            process = subprocess.Popen(["notepad.exe"])
            time.sleep(0.5)
            notepad_window = gw.getWindowsWithTitle("Untitled - Notepad")[0]
            window=notepad_window
            window.resizeTo(500,500)

            # Type the text with newline after every n words
            text_with_newline = insert_newline_after_n_words(text, n)
            pyautogui.write(text_with_newline, interval=0.01)

            # Set the window size
            # Set your desired width and height

        
        # window.mainloop()

    def gptrunner(Uprompt,timetorun): #this function call the writing function of GPT output in a specific time using conditional statements
        sec=1
        while True:
            sleep2.sleep(1)
            now = datetime.datetime.now()
            time=str((now.strftime('%H:%M')))
            if time==timetorun:
                insert_text_with_line_breaks(Uprompt, 8)
                loop()
            else:
                print("processing..",sec)
                sec+=1
    def openOnTime():
        with open("logs.txt",'r') as opentimeread:
            line = opentimeread.readlines(1)
            logtime=""
            sorted=""
            str1=str(line)
            for i in str1:
                if i.isnumeric():
                    logtime=str1[str1.index(i)+11:-4]
                    break
            for i in range(len(str1)):
                    if str1[i].isnumeric():
                        break
                    else:
                        sorted+=str1[i]
            while True:
                if sorted!=""and logtime!="":
                    
                    gptrunner(responseoftodoify,logtime)
    window.after(5000,popup)
    window.mainloop()
     print("Requesting Openai.servers")
     sleep2.sleep(1)
     print("Fetching APIs")
     sleep2.sleep(1)
     print("Connected..wait please don't interrupt with your keyboard or any HID device")
     with open("logs.txt",'r')as sortedword:
          wordline=sortedword.readlines(1)
          message=""
          for i in range(len(wordline)):
                         if wordline[i].isnumeric():
                             break
                         else:
                             message+=wordline[i]
          openai.api_key = '' #USE YOUR API KEY HERE.it costs around $5.90(varies depending on your region of purchase)
          messages=[{"role":"system","content":
                "you are a teacher"}]
         # Define the prompt you want to send to the model
          if message:
             messages.append(
                         {"role":"user","content":"How to make in 5 steps"+message},
                     )
             chat=openai.ChatCompletion.create(
                         model="gpt-3.5-turbo",messages=messages
                     )
             global responseoftodoify
             responseoftodoify=chat.choices[0].message.content
     print("OpenAI response received successfully...")
     sleep2.sleep(2)
    openOnTime()
loop()
