from tkinter import *
import random
import string

windowScreen = Tk()
windowScreen.title("Title of Window Screen")
windowScreen.geometry('600x500')
windowScreen['bg'] = '#117799'

def printValue():
    uname = userName.get()
    Label(windowScreen, text=f'{uname}, Registered!', pady=20, bg='#ffaadd').place(relheight=0.1, relwidth= 0.3, relx=0.3, rely=0.4)
    print(str(uname))

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

empNum = int("999" + id_generator(3, string.digits))
Label(windowScreen, text="User ID: ", pady=5, bg='#ffaadd').place(relheight=0.1, relwidth= 0.1, relx=0.1, rely=0.1) 
uid = Label(windowScreen, text=empNum, pady=5)
uid.place(relheight=0.1, relwidth= 0.1, relx=0.2, rely=0.1)
print(uid['text'])

Label(windowScreen, text="Enter Username: ", pady=5, bg='#ffaadd').place(relheight=0.1, relwidth= 0.2, relx=0.3, rely=0.1)
userName = Entry(windowScreen)
userName.place(relheight=0.1, relwidth= 0.2, relx=0.5, rely=0.1)

Button(
    windowScreen,
    text="Add User to Database", 
    padx=10, 
    pady=5,
    bg='#00DDAA',
    command=printValue).place(relheight=0.1, relwidth= 0.4, relx=0.1, rely=0.2)
Button(
    windowScreen,
    text="Quit",
    padx=30, 
    pady=5,
    bg='#00DDAA',
    command=windowScreen.destroy).place(relheight=0.1, relwidth= 0.2, relx=0.5, rely=0.2)
windowScreen.mainloop()