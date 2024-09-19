from tkinter import *

#T1: how to make basic window
def tutorial1():
    root = Tk()
    thelabel = Label(root, text="howdy yall")
    thelabel.pack()
    root.mainloop()
    return

#T2: organizing layout
def tutorial2():
    root = Tk()
    topframe = Frame(root)
    topframe.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    button1 = Button(topframe, text="button1", fg="purple")
    button2 = Button(topframe, text="button2", fg="red")
    button3 = Button(topframe, text="button3", fg="blue")
    button4 = Button(bottomframe, text="button4", fg="green")
    button1.pack(side=LEFT)
    button2.pack(side=RIGHT)
    button3.pack(side=BOTTOM)
    button4.pack(side=BOTTOM)

    root.mainloop()
    return

#T3: fitting widgets in layout
def tutorial3():
    root = Tk()
    one = Label(root, text="One", bg="purple", fg="white")
    one.pack()
    two = Label(root, text="Two", bg="green", fg="black")
    two.pack(fill=X)
    three = Label(root, text="Three", bg="blue", fg="white")
    three.pack(side=LEFT, fill=Y)
    root.mainloop()
    return

#T4: grid layout
def tutorial4():
    root = Tk()
    label_1 = Label(root, text="Name")
    label_2 = Label(root, text="Password")
    entry_1 = Entry(root)
    entry_2 = Entry(root)
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    c = Checkbutton(root, text="Keep me logged in")
    c.grid(columnspan=2)
    root.mainloop()
    return

#T5: more grid layout stuff, binding function to widget
def printname():
    print("Hello my name is Allison!")
    return

def differentfcn(event):
    print("Hello world!")

def tutorial5():
    root = Tk()
    button_1 = Button(root, text="Print my name", command=printname)
    button_1.pack()
    button_2 = Button(root, text="Print a name", command=differentfcn)
    button_2.bind("<Button-1>", differentfcn)
    button_2.pack()
    root.mainloop()
    return

#T6: mouse click events
def leftclick(event):
    print("Left")

def middleclick(event):
    print("Middle")

def rightclick(event):
    print("Right")

def tutorial6():
    root = Tk()
    frame = Frame(root, width=300, height=250)
    frame.bind("<Button-1>", leftclick)
    frame.bind("<Button-2>", middleclick)
    frame.bind("<Button-3>", rightclick)
    frame.pack()
    root.mainloop()
    return

#T7: using classes
class AllisonsButtons:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text="Print Message", command=self.printmessage)
        self.printButton.pack(side=LEFT)
        self.quitbutton = Button(frame, text="Quit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("Wow this actually worked!")

def tutorial7():
    root = Tk()
    b = AllisonsButtons(root)
    root.mainloop()
    return

#T8: creating drop down menus and toolbars
def doNothing():
    print("okay okay i won't ...")

def tutorial8():
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Project...", command=doNothing)
    subMenu.add_cascade(label="Now ...", menu=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=doNothing)
    editmenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editmenu)
    editmenu.add_command(label="Redo", command=doNothing)
    root.mainloop()
    return


#uncomment tutorial calls below to run each tutorial
#tutorial1()
#tutorial2()
#tutorial3()
#tutorial4()
#tutorial5()
#tutorial6()
#tutorial7()
#tutorial8()