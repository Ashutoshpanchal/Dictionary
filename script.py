from tkinter import *
import json
from difflib import get_close_matches


data = json.load(open("data.json"))
def serach():
    w=enter_text.get()
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


    text.insert(END,w)

root=Tk()
root.title("Dictionary")

label1=Label(text="Enter number")
label1.grid(row=0,column=0)
enter_text=StringVar()
entry=Entry(width=40,textvariable=enter_text)
entry.grid(row=0,column=1)

b=Button(text="SERACH",command=serach)
b.grid(row=0,column=2)

text=Text(width=15,height=10)
text.grid(row=1,column=0,columnspan=3,sticky=N+S+E+W)

root.mainloop()