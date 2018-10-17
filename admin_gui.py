from tkinter import *

import subprocess
import os
from tkinter import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#def bash_command(cmd):
#    subprocess.Popen(cmd, shell=True, executable='/bin/bash')

dirname = ''
files=''

name = os.popen('whoami').read()

def terminal():
    #bash_command('a="Apples and oranges" && echo "${a/oranges/grapes}"')
    subprocess.call(["ls","-a"])

def shutdown():
       subprocess.call(["shutdown", "-h", "now"])
       messagebox.showinfo("msg","SHUTDOWN starts in 60sec")
def shutdowncancel():
       subprocess.call(["shutdown", "-c"])
       messagebox.showinfo("msg","SHUTDOWN starts in 60sec")

def timeshut():
       time=e5_hour.get()+":"+e5_minitue.get()
       subprocess.call(["shutdown "+time])
       messagebox.showinfo("msg","SHUTDOWN is scheduled")

def timerestart():
       time=e5_hour.get()+":"+e5_minitue.get()
       subprocess.call(["shutdown", "-r", "now"])
       messagebox.showinfo("msg","RESTAR starts in 60sec")

def editorder():
    messagebox.showinfo("password", "enter password in terminal")
    order=e1_order.get()
    print(order)
    subprocess.call(["sudo","sed","-i","s/GRUB_DEFAULT=[0-9]*/GRUB_DEFAULT="+order+"/g","/etc/default/grub"])
    messagebox.showinfo("sucess", "default software  changed to")

def edittime():
       messagebox.showinfo("password", "enter password in terminal")
       timeer=e2_time.get()
       #print(timeer)
       subprocess.call(["sudo","sed","-i","s/GRUB_TIMEOUT=[0-9]*/GRUB_TIMEOUT="+timeer+"/g","/etc/default/grub"])
       messagebox.showinfo("sucess", "default TIMEOUT  changed to",timeer)

def openDirectory():
    files = filedialog.askopenfilenames(parent=root,initialdir='/home/', title='Select your pictures folder')
    #dirname = filedialog.askdirectory(parent=window, initialdir='/home/', title='Select your pictures folder')



root = Tk()
root.title('Model Definition')
header=Label(root,text="SYSTEM ADMIN TOOL",bg="lightyellow",bd=20,width=80,font=65)
header.grid(rowspan=2,columnspan=8,padx=5, pady=2)
# create all of the main containers
#frame1 = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1,bg='lavender', width=400, height=60, pady=3)
frame1 = Frame(root, width=500, height=80, pady=1)
frame2 = Frame(root, width=500, height=80, pady=1)
frame3 = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1,bg='lavender',width=500, height=80, pady=1)
frame4 = Frame(root, width=500, height=80, pady=1)
frame5 = Frame(root, width=500, height=80, pady=1)
frame6 = Frame(root, width=500, height=80, pady=1)

# layout all of the main containers
#root.grid_rowconfigure(1, weight=1)
#root.grid_columnconfigure(0, weight=1)

frame1.grid(row=3,padx=5, pady=3)
frame2.grid(row=5,padx=5, pady=3)
frame3.grid(row=7,padx=5, pady=3)
frame4.grid(row=9,padx=5, pady=3)
frame5.grid(row=11,padx=5, pady=3)
frame6.grid(row=13,padx=5, pady=3)


w = Canvas(root,width=600,height=20)
w.grid(row=2,padx=5, pady=5)
w.create_line(0, 20, 600, 20, fill="#476042")

w1= Canvas(root,width=600,height=20)
w1.grid(row=4,padx=5, pady=3)
w1.create_line(0, 20, 600, 20, fill="#476042")

w2= Canvas(root,width=600,height=20)
w2.grid(row=6,padx=5, pady=3)
w2.create_line(0, 20, 600, 20, fill="#476042")

w3= Canvas(root,width=600,height=20)
w3.grid(row=8,padx=5, pady=3)
w3.create_line(0, 20, 600, 20, fill="#476042")

w4= Canvas(root,width=600,height=20)
w4.grid(row=10,padx=5, pady=3)
w4.create_line(0, 20, 600, 20, fill="#476042")

# create the widgets for the top frame
model_label = Label(frame1, text='enter default os for your system',padx=10, pady=3)
e1_order=StringVar()
#e1=Entry(frame1,textvariable=e1_order)
e1=Spinbox(frame1, from_=0, to=10,textvariable=e1_order)
b1=Button(frame1,text="CHANGE",width=12,command=editorder,padx=5, pady=3)

# layout the widgets in the top frame
model_label.grid(row=4, column=1,padx=10,columnspan=2)
e1.grid(row=4,column=3,padx=10, pady=5)
b1.grid(row=4,column=4,columnspan=2,padx=15, pady=3)


model_label1 = Label(frame2, text='enter default TIMEOUT for your system',padx=10, pady=3)
e2_time=StringVar()
e2=Entry(frame2,textvariable=e2_time)
b2=Button(frame2,text="CHANGE",width=12,command=edittime,padx=5, pady=3)

# layout the widgets in the top frame
model_label1.grid(row=4, column=1,padx=10,columnspan=2)
e2.grid(row=4,column=3,padx=10, pady=3)
b2.grid(row=4,column=4,columnspan=2,padx=15, pady=3)

model_burger = Label(frame3, text='BURG configuration/installation',font=10,pady=2)
model_burg = Label(frame3, text='1-open terminal',padx=10, pady=2)
model_burg1= Label(frame3, text='2-sudo add-apt-repository ppa:n-muench/burg => use this command and then type password ',padx=10, pady=2)
model_burg2= Label(frame3, text='3-use the command sudo apt-get update',padx=10, pady=2)
model_burg3= Label(frame3, text='4-sudo apt-get install burg burg-themes => command for install the burg bootloader',padx=10, pady=2)
model_burg4 = Label(frame3, text='5-options are displayed ehilr installation and press tab to switch to OK button and hit Enter',padx=10, pady=2)
model_burg5= Label(frame3, text='6-select the path for the bootloader to install with space and hit tab and press enter',padx=10, pady=2)
model_burg6= Label(frame3, text='7-sudo burg-emu => command to load to burg',padx=10, pady=2)
model_burger.grid(row=0)
model_burg.grid(row=1,pady=2)
model_burg1.grid(row=2,pady=2)
model_burg2.grid(row=3,pady=2)
model_burg3.grid(row=4,pady=2)
model_burg4.grid(row=5,pady=2)
model_burg5.grid(row=6,pady=2)
model_burg6.grid(row=7,pady=2)



# layout the widgets in the top frame
model_label1.grid(row=4, column=1,padx=10,columnspan=2)


model_image = Label(frame4, text='select image as background for grub',padx=5, pady=3)
b4=Button(frame4,text = 'Select pictures ', fg = 'black', command= openDirectory)
# layout the widgets in the top frame
model_image.grid(row=4, column=1,padx=10,columnspan=2)
b4.grid(row=4,column=4,padx=5, pady=3)

model_label2 = Label(frame5, text='SCHEDULE FOR SHUTDOWN OR REBOOT OF SYSTEM', pady=3)
model_label21 = Label(frame5, text='IMMEDIATE REBOOT OF SYSTEM', pady=3)

e5_hour=StringVar()
e5_minitue=StringVar()
e5_hour.set(0)
e5_minitue.set(1)
e5label=Label(frame5,text="hours",padx=2, pady=3)
e5=Entry(frame5,textvariable=e5_hour)
e51label=Label(frame5,text="minutes",padx=4, pady=3)
e51=Entry(frame5,textvariable=e5_minitue)

#e5=OptionMenu(frame5, e5_hour , textvariable=e5_hour)
#e51=OptionMenu(frame5, e5_minitue ,minutes.values() ,textvariable=e5_minitue)
b5=Button(frame5,text="SHUTDOWN",width=12,command=timeshut,padx=5, pady=2)
b51=Button(frame5,text="REBOOT",width=12,command=timerestart,padx=5, pady=2)
b52=Button(frame5,text="cancel shutdown",width=12,command=shutdowncancel,padx=5, pady=2)


# layout the widgets in the top frame
model_label2.grid(row=3, column=2,padx=10,columnspan=2)
model_label21.grid(row=6, column=2,padx=10,columnspan=2)

e5label.grid(row=4,column=2,padx=5, pady=2)
e5.grid(row=4,column=3,padx=5, pady=2)
e51label.grid(row=4,column=4,padx=5, pady=2)
e51.grid(row=4,column=5,padx=10, pady=2)
b5.grid(row=4,column=6,padx=2, pady=2)
b51.grid(row=6,column=4,columnspan=2,padx=2, pady=2)
b52.grid(row=6,column=6,columnspan=2,padx=2, pady=2)

b6=Button(frame6,text="CLOSE",width=12,command=root.destroy ,bg="red",padx=5, pady=2)
b6.grid(row=1,column=4,padx=8, pady=2)



root.mainloop()
