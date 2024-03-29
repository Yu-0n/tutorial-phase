from email.mime import image
from msilib.schema import Icon
from stat import filemode
from tabnanny import verbose
from tkinter import *
from turtle import back, down, right, width
from time import *

# Widgets = GUI Elements: buttons, textboxes, labels, images etc.
# Windows = serves as a container to hold or contain those widgets

window = Tk() # instantiate an instance of a window
window.geometry("640x640") # size of window
window.title("Yua's first GUI") #window title
window.config(background="light blue") #change backgroudn color



photo = PhotoImage(file="GUI\\anime01.png")
resized_photo = photo.subsample(6,6)

giftimg = PhotoImage(file="GUI\\1301.png")
coupimg = PhotoImage(file="GUI\\1302.png")
snowimg = PhotoImage(file="GUI\\1303.png")
listImages = [giftimg, coupimg, snowimg]

#------------------------------------- Icon
'''
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
icon_ref = icon''' #doesn't work, file not found 

#----------------------------------------------------

#label = an area widget that holds text and/or an image within a window
'''
label = Label(window, text="Hello World",
              font=('Arial',40,'bold'),
                fg='red', bg="black",#foreground and background
                relief=RAISED, bd=10, #border width 10 and relief changes style
                padx=20, pady=20,
                image=resized_photo,
                compound="bottom") 
label.pack()'''
#label.place(x=100,y=100)

#----------------------------------------------------

#Buttons = you click it, then it does stuff
'''
count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button!")
button = Button(window,
                text="Click me",
                command=click,
                font=("Comic-Sans", 30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                #state=DISABLED disables button
                image=resized_photo,
                compound="bottom")
button.pack()
'''

#-----------------------------------------------

# entry widget = textbox that accepts a single line of user input
'''
def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED) #to disable box after entry

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END) # second to last, last character I only removes last char


entry = Entry(window,
              font=("Ariel",35),
              fg="red",
              bg="black",
              #show="*" only displays * basically hides the text
              )
entry.insert(0, 'Enter Username: ')
entry.pack(side=LEFT)


submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)
'''
# -----------------------------------------------------------

# Checkbox
'''
def display():
    if (x.get()==1):
        print("You agreed")
    else:
        print("You don't agree")
x = IntVar()
check_button = Checkbutton(window,
                           text="Yes",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='red', bg="black",
                           activeforeground='red', activebackground='black',
                           padx=25, pady=10,
                           image=resized_photo, compound="left")
check_button.pack()'''
#----------------------------------------------------------

# radio buttons =  similar to checkbox, but you can only select one from a group.
'''
x = IntVar()
food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered pizza.")
    elif(x.get() == 1):
        print("You ordererd a Hamburger")
    elif(x.get() == 2):
        print("You ordered a Hotdog")
    else:
        print("Huh?")

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                            text=food[index], # adds text to radio buttons
                            variable=x, # groups radibuttons together if they share the same variable
                            value=index, #this assigns each radiobutton a different value
                            padx=25, pady=10,
                            font=("Impact", 35),
                            image=listImages[index], compound="right", #Adds image to the radiobutton
                            indicatoron=0, #eliminate circle indicators
                            width = 375,
                            command=order #this sets the command for the radio buttons
                            )
    radiobutton.pack(anchor=W)'''
#-------------------------------------------------------------------
#sliding scale
'''
coldlabel = Label(image=snowimg)
coldlabel.pack()
def submit():
    print("The temp is "+ str(scale.get())+ "degrees C")
scale = Scale(window, 
              from_=100,
              to=0,
              length=500, # increases the scales lenght
              orient=VERTICAL, #sets the scale vertically up
              font=("Consolas",20),
              tickinterval=10, #adds numeric indicators for value
              showvalue=0, #hides current value on the slider itself
              resolution=5, #incremend of slider
              troughcolor='blue', #color of inner 
              fg='#FF1C00',
              bg='#111111'

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #makes it so the scale always starts in the middle
scale.pack()

giftlabel = Label(image=giftimg)
giftlabel.pack()


button = Button(window, text="submit",command=submit)
button.pack()'''

#---------------------------------------------------------------

# listbox = A listing of selectable text items within it's own container
'''
def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered: ")

    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()): #deletes from a reversed order to delete all selected indexes, because index change when one is deleted.
        listbox.delete(index)
    listbox.config(height=listbox.size())

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=('Constantia', 35),
                  width=12,
                  selectmode=MULTIPLE,)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size()) # dinamically changes size of list box

entrybox = Entry(window, 
                 )
entrybox.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()
deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()'''

#--------------------------------------------------

# messagebox 

#from tkinter import messagebox #import messagebox libary

#def click():
    #messagebox.showinfo(title="This is an info message box", message="You got a virus lol")
    #messagebox.showwarning(title="WARNING", message="You got a virus lol")
    #messagebox.showerror(title="ERROR", message="Something went wrong")

    #if messagebox.askokcancel(title="ask ok cancel", message="Do you want to slice tha kid?"):
        #print("You killed tha kidd")
    #else:
        #print("You canceld a thing")
'''
    if messagebox.askretrycancel(title="ask ok retry cancel", message="Do you want to retry?"):
        print("You retried a thing")
    else:
        print("You canceled a thing")'''
    
    #if messagebox.askyesno(title="Ask yes or no", message="Do you want to eat tha cake?"): #returns a bool value
        #print("YOu ate tha cake")
    #else:
        #print("I guess no cake today")
'''
    answer = messagebox.askquestion(title="Ask question", message="Do you like pie?") #returns a string with yes / no
    if(answer == 'yes'):
        print('Pie pie pie pie')
    else:
        print("no pie ):")'''
    
    #answer = messagebox.askyesnocancel(title="Ask yes no cancel", message="Do you like to code?",icon='warning') #returns True, False or None

    #if(answer==True):
        #print("I like to code too")
    #elif(answer==False):
        #print("Burn tha witch")
    #else:
        #print("You dodged me ):")
'''
button = Button(window, command=click, text="Click me")
button.pack()
'''

#------------------------------------------------------

# Colorchooser
'''
from tkinter import colorchooser #submodule

def click():
    window.config(colorchooser.askcolor()[1]) #changes background color

button = Button(window,
                text="click me",
                command=click,
                )
button.pack()
'''
#----------------------------------------------------

# Text Area

# text widget = functions like a text area, you can enter multiple linse of text
'''
def submit():
    input = text.get("1.0", END)
    print(input)

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple"
            )
text.pack()

button = Button(window, command=submit, text="submit")
button.pack()'''

#-----------------------------------------------

# File dialouge, open and read files
'''
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:tutorial-phase\\GUI",
                                          title="Open file",
                                          filetypes= (("text files", "*.txt"),
                                          ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()
window = Tk()


button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()'''
# -------------------------------------- 1H 50M
'''
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\tutorial-phase\\GUI",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file" ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text="Open", command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()'''

# -------------------------------------- 2H

# Menubar
'''
menubar = Menu(window)
window.config(menu=menubar)

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("You cut")
def copy():
    print("You copied")
def paste():
    print("You pasted")

fileMenu = Menu(menubar, tearoff=0 # line to seperate section
                , font=("MV Boli", 15)
                )
menubar.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile, image=snowimg, compound=LEFT)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar,tearoff=0, font=("MV Boli", 15))

menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)'''
# -------------------------------------- 2H 10M

# frame = rectangular container to grop and hold widgets
'''
frame = Frame(window,bg="black",bd=5,relief=RAISED)
#frame.pack(side=BOTTOM)
frame.place(x=50,y=100) #places frame at exact location and it will stay there
Button(frame, text="W", font=("Consolas", 20), width=3).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 20), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 20), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 20), width=3).pack(side=LEFT)
'''
# -------------------------------------- 2H 16M

# open new window
'''
def create_window():
    new_window = Toplevel() #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    # new_window = Tk() # would create a complete new independent window
    wind.destroy() #close out of old window
wind = Toplevel()
Button(window, text="Create new window", command=create_window).pack()
wind.mainloop()'''
# -------------------------------------- 2H 20M

# Set new Tabs
'''
from tkinter import ttk #gives access to several widgets

wind = Tk()

notebook = ttk.Notebook(wind) # widget that manages a collection of windows/displays

tab1 = Frame(notebook) # new frame for tab 1
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both") # expand = expand to fill any space not otherwise used.
                                        #fill = fill space on x and y axis
Label(tab1, text="Hello, this is tab#1!", width=50, height=25).pack()
Label(tab2, text="Hello, this is tab#2!", width=50, height=25).pack()
wind.mainloop()'''
# -------------------------------------- 2H 26M

# Grid geometry manager

# grid() = geometry manager that organizes widgets in a table-like structure in a parent
# column width is dependent on biggest widget in that colmn
'''
titleLabel = Label(window, text="Enter ur info", font=("Ariel", 20)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

LastNameLabel = Label(window, text="Last name: ",bg="green").grid(row=2,column=0)
LastNameEntry = Entry(window).grid(row=2,column=1)

EmailLabel = Label(window, text="Email: ",width=30).grid(row=3,column=0)
EmailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window, text="Submit").grid(row=4,column=0,columnspan=2#spans over more than one column
                                                  )'''
# -------------------------------------- 2H 35M

# Progress bar
'''
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed =  1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" tasks complted")
        window.update_idletasks() #updates window after each iteration of while loop

percent = StringVar()
text = StringVar()
bar = Progressbar(window, orient=HORIZONTAL, length=200)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window,text="download", command=start).pack()
'''
# -------------------------------------- 2H 45M

# canvas = widget that is used to draw graphs, plots, images in a window
'''
points = [250,0,500,500,0,500,]
canvas = Canvas(window, height=500, width=500)
canvas.create_line(0,0,500,500, fill="blue",width=10)
canvas.create_line(500,0,0,500, fill="red",width=10) # starting x/y ending x/y
canvas.create_rectangle(50,50,250,250, fill="purple")
#canvas.create_polygon(250,0,500,500,0,500, fill="yellow",outline="black", width=5) #x, y, x, y, x, y,
canvas.create_polygon(points, fill="yellow",outline="black", width=5)
canvas.create_arc(0,0,500,500, fill="green", style=CHORD#draws a line or do ARC for no line
                  , start=180# sets degrees
                  , extent=100 # how far does it extend
                  )
#pokeball
canvas.create_arc(0,0,500,500,fill="red",extent=180, width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180, start=180,width=10)
canvas.create_oval(190,190,310,310, fill="white",width=10)
canvas.pack()'''
# -------------------------------------- 2H 56M

# key events
'''
def doSomething(event):
    #print("It worked"+event.keysym) #displays keysymbol
    label.config(text=event.keysym)
window.bind("<Key>", doSomething) #do <Key> for all keys

label = Label(window, font=("Helvetica", 100))
label.pack()'''
# -------------------------------------- 3H 1M

# mouse events
'''
def doSomething(event):
    print("Mouse coordinates"+str(event.x)+str(event.y))#event.x gives me the x coordinate, same for y

window.bind('<Button-1>',doSomething) #event, function / left mouse button
window.bind('<Button-2>',doSomething) if pressed middle mouse button
window.bind('<Button-3>', doSomething) right click
window.bind('<ButtonRelease>', doSomething) #activates when mouse button released
window.bind('<Enter>', doSomething) # enter the window
window.bind('<Leave>', doSomething) # leave the window
window.bind('<Motion>', doSomething) # Where the mouse moved
'''
# -------------------------------------- 3H 6M

# drag & drop widgets

'''
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget #makes it compatible with every widget
    x = widget.winfo_x() - widget.startX + event.x # x = top left corner - place where we click within label + coord where we drag
    y = widget.winfo_y() - widget.startY + event.y # Sets new coordinates

    widget.place(x=x, y=y)
    

label = Label(window,bg="Red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="Blue",width=10,height=5)
label2.place(x=100,y=50)

label.bind("<Button-1>",drag_start)#(event, function)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)#(event, function)
label2.bind("<B1-Motion>",drag_motion)'''
# -------------------------------------- 3H 14M

# move images
'''
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10) 
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
#arrow keys
window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

resized_photo = resized_photo.subsample(4,4)
label = Label(window, image=resized_photo)
label.place(x=0,y=0)'''

#move images on canvas
'''
def move_up(event):
    canvas.move(myimage,0,-10) # 3 arguments (var, x,y)
def move_down(event):
    canvas.move(myimage,0,+10)
def move_right(event):
    canvas.move(myimage,+10,0)
def move_left(event):
    canvas.move(myimage,-10,0)

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
#arrow keys
window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

resized_photo = resized_photo.subsample(4,4)
myimage = canvas.create_image(0,0, image=resized_photo, anchor=NW)
'''
# -------------------------------------- 3H 25M

# 2D Animations

#imported time
'''
WIDTH = 500 #constants
HEIGHT = 500
#velocities
xVelocity = 2
yVelocity = 3
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

resized_photo = resized_photo.subsample(4,4)
myimage = canvas.create_image(0,0, image=resized_photo, anchor=NW)


background = canvas.create_image(0,0,image=snowimg,anchor=NW) 

image_width = resized_photo.width()
image_height = resized_photo.height()

while True:
    coordinates = canvas.coords(myimage) #gets the coordinates of myimage
    print(coordinates)
    if(coordinates[0]>= (WIDTH-image_width) or coordinates[0]<0): #x value
        xVelocity = -xVelocity
    if(coordinates[1]>= (HEIGHT-image_height) or coordinates[1]<0): #y value
        yVelocity = -yVelocity
    canvas.move(myimage, xVelocity,yVelocity)# 3 arguments, what, x, y # moves it 
    window.update()
    time.sleep(0.03)'''

# -------------------------------------- 3H 39M

# Animate multiple objects

'''
from classforTut import *
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1,1, "red")
tennis_ball = Ball(canvas, 0, 0, 40, 3,4, "blue")
bigger_ball = Ball(canvas, 0, 0, 150, 0.5,0.7, "white")
deez_Balls = Ball(canvas, 0, 0, 85, 1.2,1.5, "black")

while True:
    volley_ball.move() #function in classforTut
    tennis_ball.move()
    bigger_ball.move()
    deez_Balls.move()
    window.update()
    time.sleep(0.03)'''

# -------------------------------------- 3H 51M

# Clock program
# https://docs.python.org/3/library/time.html#time.strftime
'''
def update():
    time_string = strftime("%I:%M:%S %p", gmtime())
    time_label.config(text=time_string)

    day_string = strftime("%A", gmtime())
    day_label.config(text=day_string)

    date_String = strftime("%B %d, %Y", gmtime())
    date.config(text=date_String)

    wind.after(1000, update) #milisceonds, function


wind = Tk()

time_label = Label(wind,font=("Arial", 50), fg="Green", bg="black")
time_label.pack()

day_label = Label(wind,font=("Arial", 25))
day_label.pack()

date = Label(wind,font=("Arial", 15))
date.pack()

update()

wind.mainloop()
'''
# -------------------------------------------------------------------------------
#Finished
window.mainloop() #place window on computer screen, listen for events