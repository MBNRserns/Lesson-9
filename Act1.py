from tkinter import *
from tkinter import messagebox
import time

root=Tk()
root.geometry("500x500")
root.title("Stopwatch")

hour=StringVar()
min=StringVar()
sec=StringVar()
hour.set("00")
min.set("00")
sec.set("00")


hourEntry = Entry(root,width=3,font=("Arial",18,"bold"),textvariable=hour)
hourEntry.place(x=80, y=20)
minEntry = Entry(root,width=3,font=("Arial",18,"bold"),textvariable=min)
minEntry.place(x=120, y=20)
secEntry = Entry(root,width=3,font=("Arial",18,"bold"),textvariable=sec)
secEntry.place(x=160, y=20)

def submit():
    try:
        temp = int(hour.get())*3600 + int(min.get())*60 + int(sec.get())
    except:
        print("Please Input the right value")

    while temp >-1:
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp, 60)
        hours = 00
        if mins > 60:
            hours,mins= divmod(mins,60)
        hour.set("{00:2d}".format(hours))
        min.set("{00:2d}".format(mins))
        sec.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 00):
            messagebox.showinfo("Time Countdown", "TImes Up")

        temp -=1

    


btn=Button(root, text="Set Time", command=submit)
btn.place(x=110, y=70)


root.mainloop()