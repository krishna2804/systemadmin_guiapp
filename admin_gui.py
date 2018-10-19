#from functions import *
from tkinter import *
from subprocess import Popen,PIPE
import subprocess
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import pandas as  pd
import numpy as np

dirname = ''
files=''
CSV_name=""
batch_names=""
#------------------------------------------------
name = os.popen('whoami').read()

def terminal():
    subprocess.call(["ls","-a"])

def username():
    uname = simpledialog.askstring("Input", "enter username",parent=window)
    return uname

def password():
    passwd = simpledialog.askstring("Password","Enter your password",show="*",parent=window)
    return passwd

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
    password1=password()
    order=e1_order.get()
    print(order)
    command2="sudo update-grub"
    command="echo "+password1+" | sudo -S sed -i s/GRUB_DEFAULT=[0-9]*/GRUB_DEFAULT="+order+"/g /etc/default/grub"
    #subprocess.call(["echo \""+password1+"\" | ","sudo","-S","sed","-i","s/GRUB_DEFAULT=[0-9]*/GRUB_DEFAULT="+order+"/g","/etc/default/grub"],shell=True)
    subprocess.call(command,shell=True)
    subprocess.call(command2,shell=True)

    messagebox.showinfo("sucess", "default software  changed to")

def edittime():
       password1=password()
       timeer=e2_time.get()
       print(timeer)
       command2="sudo update-grub"
       command1="echo "+password1+" | sudo -S sed -i s/GRUB_TIMEOUT=[0-9]*/GRUB_TIMEOUT="+timeer+"/g /etc/default/grub"
       subprocess.call(command1,shell=True)
       subprocess.call(command2,shell=True)

       #subprocess.call(["echo \""+password1+"\" | ","sudo","-S","sed","-i","s/GRUB_TIMEOUT=[0-9]*/GRUB_TIMEOUT="+timeer+"/g","/etc/default/grub"],shell=True)
       messagebox.showinfo("sucess", "default TIMEOUT  changed ")

def openDirectory():
    files = filedialog.askopenfilenames(parent=root,initialdir='/home/', title='Select your pictures folder')
    file_name=files[0]
    password1=password()
    command1="echo "+password1+" | sudo -S sed -i '/GRUB_BACKGROUND/d' /etc/default/grub"
    subprocess.call(command1,shell=True)
    print("pass password1")
    #command2="echo "+password1+" | sudo -i"
    #command2="sudo -i"
    #print("pass password2")
    #subprocess.call(command2,shell=True)
    #command3="echo \"GRUB_BACKGROUND="+file_name+"\" >> /etc/default/grub"
    command3="echo "+password1+" | sudo -S sed -i '$ a GRUB_BACKGROUND="+file_name+"' /etc/default/grub"
    subprocess.call(command3,shell=True)
    #os.system(command3,shell=True)
    #command4="exit"
    #subprocess.call(command4,shell=True)
    command5="echo "+password1+" | sudo -S update-grub"
    subprocess.call(command5,shell=True)
    messagebox.showinfo("sucess", "default BACKGROUND ")
    #dirname = filedialog.askdirectory(parent=window, initialdir='/home/', title='Select your pictures folder')

def spalshscreen():
    passer=v.get()
    password1=password()

    command1="echo "+password1+" | sudo -S apt-get install plymouth-theme-breeze"

    command2="echo "+password1+" | sudo -S apt-get install plymouth-theme-ubuntustudio"

    command3="echo "+passer+" | sudo -S update-alternatives --config default.plymouth"

    command4="echo "+password1+" | sudo -S update-initramfs -u"
    #command1="echo "+password1+" | sudo -S sed -i s/GRUB_TIMEOUT=[0-9]*/GRUB_TIMEOUT="+timeer+"/g /etc/default/grub"
    subprocess.call(command1,shell=True)
    subprocess.call(command2,shell=True)
    subprocess.call(command3,shell=True)
    subprocess.call(command4,shell=True)
    messagebox.showinfo("sucess", "default SPLASH SCREEN is changed.REBOOT TO CHECK")

def addusers():
    password1=password()
    user_name=entry_username.get()
    user_id=entry_userid.get()
    user_pwd=entry_userpwd.get()
    print(user_pwd)
    user_shell=entry_usershell.get()
    print(user_shell)
    command1="echo "+password1+" | sudo -S apt install whois"
    print(command1)
    subprocess.call(command1,shell=True)
    command2="mkpasswd -m sha-512 "+user_pwd+""
    pipeer= Popen(command2, shell=True, stdout=PIPE).stdout
    output = pipeer.read()
    encry_pass=output.decode("utf-8")
    final_pass=encry_pass.rstrip()
    print(final_pass)
    if(user_id!="" and user_pwd!="" and user_name!="" and user_shell!=""):
        command3="echo "+password1+" | sudo -S groupadd -g \""+user_id+"\"  \""+user_name+"\""
        command4="sudo useradd -d \"/home/"+user_name+"\" -s \""+user_shell+"\" -u \""+user_id+"\" -g \""+user_id+"\" -p \""+final_pass+"\" \""+user_name+"\""
        #command4="sudo adduser -m "+user_name+" -u "+user_id+" -g "+user_id+" -p "+encry_pass+" -s "+user_shell+""
        print(command4)
        subprocess.call(command3,shell=True)
        subprocess.call(command4,shell=True)
        messagebox.showinfo("sucess", "user is created")
    else:
        messagebox.showwarning("warning","user details enter correctly")

def openCSV():
    files = filedialog.askopenfilenames(parent=window,initialdir='/home/', title='UPLOAD FILE')
    csv_file=files[0]
    global CSV_name
    CSV_name=csv_file

def batchcsv():
    files = filedialog.askopenfilenames(parent=window,initialdir='/home/', title='Select your csv file')
    batch_file=files[0]
    global batch_names
    batch_names=batch_file
    print(batch_names)

#-------------------------------------single user functions---------------------------------
def lockuser():
    username=single_user.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -L \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user is locked")

def setexpiry():
    username=single_user.get()
    expi_date=exp_date.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -e \""+expi_date+"\" \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user expirydate is set.")

def deleteuser():
    username=single_user.get()
    password1=password()
    command="echo "+password1+" | sudo -S userdel \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user is deleted")

def unlockuser():
    username=single_user.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -U \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user is unlocked")



    #sudo addgroup -gid 201551006 iiitv
    #sudo useradd -d "/home/mani" -U "201552079" -s "/bin/bash" -u "201552079" -g "201552079" -p "$a" "mani"

def changepasswd():
    password1=password()
    user_name=single_user.get()
    new_pwd=update_passwd.get()
    command1="echo "+password1+" | sudo -S apt install whois"
    subprocess.call(command1,shell=True)
    command2="mkpasswd -m sha-512 "+new_pwd+""
    pipeer= Popen(command2, shell=True, stdout=PIPE).stdout
    output = pipeer.read()
    encry_pass=output.decode("utf-8")
    final_pass=encry_pass.rstrip()
    if(new_pwd!="" and user_name!=""):
        command3="echo "+password1+" | sudo -S usermod -p \""+final_pass+"\"  \""+user_name+"\""
        #command4="sudo adduser -m "+user_name+" -u "+user_id+" -g "+user_id+" -p "+encry_pass+" -s "+user_shell+""
        subprocess.call(command3,shell=True)
        messagebox.showinfo("sucess", "users passwords are updated")
    else:
        messagebox.showwarning("warning","enter valid details")


def changeuser():
    username=single_user.get()
    newuser=new_user.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -l \""+newuser+"\" \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user is changed so now use updated username in columns")


def changeshell():
    username=single_user.get()
    newshell=update_shell.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -s \""+newshell+"\" \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user shell is changed")

def changeuserid():
    username=single_user.get()
    newuserid=up_useriduser.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -u \""+newuserid+"\" \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user UID is changed")

def addinformation():
    username=single_user.get()
    userinformat=information.get()
    password1=password()
    command="echo "+password1+" | sudo -S usermod -c \""+userinformat+"\" \""+username+"\""
    subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user information is added")

#----------------------------------BATCH USER FUNCtiONNS====================================

def addbatchusers():
    data=pd.read_csv(CSV_name)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()
            command1="echo "+password1+" | sudo -S apt install whois"
            print(command1)
            subprocess.call(command1,shell=True)
        user_name=str(data.loc[i][0])
        user_id=str(data.loc[i][1])
        user_pwd=str(data.loc[i][2])
        user_shell=str(data.loc[i][3])
        print(user_shell)
        command2="mkpasswd -m sha-512 "+user_pwd+""
        pipeer= Popen(command2, shell=True, stdout=PIPE).stdout
        output = pipeer.read()
        encry_pass=output.decode("utf-8")
        final_pass=encry_pass.rstrip()
        print(final_pass)
        if(user_id!="" and user_pwd!="" and user_name!="" and user_shell!=""):
            command3="echo "+password1+" | sudo -S groupadd -g \""+user_id+"\"  \""+user_name+"\""
            c
            ommand4="sudo useradd -d \"/home/"+user_name+"\" -s \""+user_shell+"\" -u \""+user_id+"\" -g \""+user_id+"\" -p \""+final_pass+"\" \""+user_name+"\""
            print(command4)
            subprocess.call(command3,shell=True)
            subprocess.call(command4,shell=True)
            if(i==(length-1)):
                messagebox.showinfo("sucess", "users is created")

        else:
            messagebox.showwarning("warning","user details enter correctly")

def deletebatchusers():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()
        user_name=str(data.loc[i][0])


        if(user_name!=""):
            command3="echo "+password1+" | sudo -S groupdel \""+user_name+"\""
            command4="echo "+password1+" | sudo -S userdel \""+user_name+"\""

            print(command4)
            subprocess.call(command3,shell=True)
            subprocess.call(command4,shell=True)
            if(i==(length-1)):
                messagebox.showinfo("sucess", "users is deleted")

        else:
            messagebox.showwarning("warning","user details enter correctly")

def lockbatchusers():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()
        username=str(data.loc[i][0])
        command="echo "+password1+" | sudo -S usermod -L \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "users is locked")



def unlockbatchusers():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()
        username=str(data.loc[i][0])
        command="echo "+password1+" | sudo -S usermod -U \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "users is unlocked")

def changebatchusers():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()

        username=str(data.loc[i][0])
        newuser=str(data.loc[i][1])
        command="echo "+password1+" | sudo -S usermod -l \""+newuser+"\" \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "users is changed so now use updated usernames")


def changebatchpasswd():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()
            command1="echo "+password1+" | sudo -S apt install whois"
            subprocess.call(command1,shell=True)


        user_name=str(data.loc[i][0])
        new_pwd=str(data.loc[i][1])
        command2="mkpasswd -m sha-512 "+new_pwd+""
        pipeer= Popen(command2, shell=True, stdout=PIPE).stdout
        output = pipeer.read()
        encry_pass=output.decode("utf-8")
        final_pass=encry_pass.rstrip()
        if(new_pwd!="" and user_name!=""):
            command3="echo "+password1+" | sudo -S usermod -p \""+final_pass+"\"  \""+user_name+"\""
        #command4="sudo adduser -m "+user_name+" -u "+user_id+" -g "+user_id+" -p "+encry_pass+" -s "+user_shell+""
            subprocess.call(command3,shell=True)
        else:
            messagebox.showwarning("warning","enter valid details")
    messagebox.showinfo("sucess", "users passwords is updated")


def expirybatchusers():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()

        username=str(data.loc[i][0])
        expi_date=str(data.loc[i][1])
        command="echo "+password1+" | sudo -S usermod -e \""+expi_date+"\" \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "user expirydate is set.")

def batchusershells():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()

        username=str(data.loc[i][0])
        newshell=str(data.loc[i][1])
        command="echo "+password1+" | sudo -S usermod -s \""+newshell+"\" \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "users shells is changed")

def uidbatchusers():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()
        username=str(data.loc[i][0])
        newuserid=str(data.loc[i][1])
        command="echo "+password1+" | sudo -S usermod -u \""+newuserid+"\" \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "users UID's is changed")


def addbatchinfo():
    data=pd.read_csv(batch_names)
    size=data.shape
    length=size[0]
    for i in range(length):
        if(i==0):
            password1=password()

        username=str(data.loc[i][0])
        userinformat=str(data.loc[i][1])
        password1=password()
        command="echo "+password1+" | sudo -S usermod -c \""+userinformat+"\" \""+username+"\""
        subprocess.call(command,shell=True)
    messagebox.showinfo("sucess", "users information is added")


#------------------------------------------------------------------------------------------

window = Tk()
window.configure(background='lavender')

window.title('SYSTEM ADMIN TOOL')
note = ttk.Notebook(window)

tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)
tab3 = ttk.Frame(note)

note.add(tab1, text = "assign1")
note.add(tab2, text = "user management")
note.add(tab3, text = "assign4")
note.pack(expand=1,fill="both")

#-----------------------------tab1 content---------------------------------------
frame1 = LabelFrame(tab1, text="CHANGE DEFAULT OS",width=500, height=50,bd=3,fg="red",bg="")
#frame2 = LabelFrame(tab1,text="CHANGE DEFAULT TIMEOUT",width=500, height=50)
frame3 = LabelFrame(tab1, text="BRUG INSTALLATION",bg='lavender',width=500, height=80,bd=3,fg="red")
frame4 = LabelFrame(tab1,text="BOOTSPLASH AND LOGO CHANGE", width=500, height=50,bd=3,fg="red")
frame5 = LabelFrame(tab1, text="SCHEDULE FOR SHUTDOWN OR REBOOT OF SYSTEM",width=500, height=50,bd=3,fg="red")
frame6 = Frame(tab1, width=500, height=50)

frame1.grid(row=3,padx=8, pady=4)
#frame2.grid(row=5,padx=8, pady=4)
frame3.grid(row=7,padx=8, pady=4)
frame4.grid(row=9,padx=8, pady=4)
frame5.grid(row=11,padx=8, pady=4)
frame6.grid(row=13,padx=8, pady=4)

model_label = Label(frame1, text='enter default os for your system',padx=10, pady=1)
e1_order=StringVar()
e1=Spinbox(frame1, from_=0, to=10,textvariable=e1_order)
b1=Button(frame1,text="CHANGE",width=12,command=editorder,padx=5, pady=1)

model_label.grid(row=4, column=1,padx=10,columnspan=2)
e1.grid(row=5,column=1,padx=10, pady=1)
b1.grid(row=6,column=1,columnspan=2,padx=15, pady=1)

model_label1 = Label(frame1, text='enter default TIMEOUT for your system',padx=10, pady=1)
e2_time=StringVar()
e2=Entry(frame1,textvariable=e2_time)
b2=Button(frame1,text="CHANGE",width=12,command=edittime,padx=5, pady=1)

model_label1.grid(row=4, column=4,padx=10,columnspan=2)
e2.grid(row=5,column=4,padx=10, pady=1)
b2.grid(row=6,column=4,columnspan=2,padx=15, pady=1)

model_burg = Label(frame3, text='1-open terminal', pady=1,bd=2,fg="blue")
model_burg1= Label(frame3, text='2-sudo add-apt-repository ppa:n-muench/burg => use this command and then type password',pady=1,bd=2,fg="blue")
model_burg2= Label(frame3, text='3-use the command =>> sudo apt-get update', pady=1,bd=2,fg="blue")
model_burg3= Label(frame3, text='4-sudo apt-get install burg burg-themes => command for install the burg bootloader', pady=1,bd=2,fg="blue")
model_burg4= Label(frame3,text='5-options are displayed ehilr installation and press tab to switch to OK button and hit Enter',pady=1,bd=2,fg="blue")
model_burg5= Label(frame3, text='6-select the path for the bootloader to install with space and hit tab and press enter',pady=1,bd=2,fg="blue")
model_burg6= Label(frame3, text='7-sudo burg-emu => command to load to burg',pady=1,bd=2,fg="blue")
#model_burger.grid(row=0)
model_burg.grid(row=1,column=0,pady=1,sticky="w")
model_burg1.grid(row=2,column=0,pady=1,sticky="w")
model_burg2.grid(row=3,column=0,pady=1,sticky="w")
model_burg3.grid(row=4,column=0,pady=1,sticky="w")
model_burg4.grid(row=5,column=0,pady=1,sticky="w")
model_burg5.grid(row=6,column=0,pady=1,sticky="w")
model_burg6.grid(row=7,column=0,pady=1,sticky="w")


model_image = Label(frame4, text='change grub background image :',padx=15)
b4=Button(frame4,text = 'select image ', fg = 'black', command= openDirectory,padx=15)
# layout the widgets in the top frame
model_image.grid(row=4, column=2,padx=15)
b4.grid(row=4,column=3,padx=10,columnspan=2,pady=5)

v = StringVar()

model_image2 = Label(frame4, text='change splash screen for grub :',padx=7)

model_image2.grid(row=5, column=2,padx=5)
Radiobutton(frame4,text="default",padx = 5,variable=v,value=2,command=spalshscreen).grid(row=5,column=3,padx=1)
Radiobutton(frame4,text="change",padx = 5,variable=v,value=3,command=spalshscreen).grid(row=5,column=4,padx=1)

model_label21 = Label(frame5, text='IMMEDIATE REBOOT OF SYSTEM', pady=3)

e5_hour=StringVar()
e5_minitue=StringVar()
e5_hour.set(0)
e5_minitue.set(1)
e5label=Label(frame5,text="hours",padx=2, pady=3)
e5=Spinbox(frame5, from_=0, to=23,textvariable=e5label)
e51label=Label(frame5,text="minutes",padx=4, pady=3)
e51=Spinbox(frame5, from_=0, to=59,textvariable=e51label)

b5=Button(frame5,text="SHUTDOWN",width=12,command=timeshut,padx=5, pady=2)
b51=Button(frame5,text="REBOOT",width=12,command=timerestart,padx=5, pady=2)
b52=Button(frame5,text="cancel shutdown",width=12,command=shutdowncancel,padx=5, pady=2)



model_label21.grid(row=6, column=2,padx=10,columnspan=2)

e5label.grid(row=4,column=1,padx=5, pady=2)
e5.grid(row=4,column=2,padx=5, pady=2)
e51label.grid(row=4,column=3,padx=5, pady=2)
e51.grid(row=4,column=4,padx=10, pady=2)
b5.grid(row=4,column=5,padx=2, pady=2)
b51.grid(row=6,column=4,columnspan=2,padx=2, pady=2)
b52.grid(row=4,column=6,columnspan=2,padx=2, pady=2)

b6=Button(frame6,text="CLOSE",width=12,command=window.destroy ,bg="red",padx=5, pady=2)
b6.grid(row=1,column=4,padx=8, pady=2)

#----------------------------------TAB2--------------------------------------------------------

tab2_frame1 =LabelFrame(tab2,text="SINGLE USER MODE",bd=5,width=500, height=80)
tab2_frame1.grid(row=0, column=3, rowspan=8, columnspan=2,padx=100,pady=14)

tab2_frame2 =LabelFrame(tab2,text="SINGLE USER FUNCTIONS",bd=5,width=500, height=80)
tab2_frame2.grid(row=10, column=3, rowspan=8, columnspan=2,padx=100,pady=14)

#------------------single user name--------------------------------
username=Label(tab2_frame1,text="USERNAME",padx=15,pady=1)
userid=Label(tab2_frame1,text="USERID",padx=15,pady=1)
userpwd=Label(tab2_frame1,text="PASSWORD",padx=15,pady=1)
usershell=Label(tab2_frame1,text="SHELLTYPE",padx=15,pady=1)
username.grid(row=2,column=2,columnspan=3,padx=15,pady=2)
userid.grid(row=4,column=2,columnspan=3,padx=15,pady=2)
userpwd.grid(row=6,column=2,columnspan=3,padx=15,pady=2)
usershell.grid(row=8,column=2,columnspan=3,padx=15,pady=2)

entry_username=StringVar()
entry_userid=StringVar()
entry_userpwd=StringVar()
entry_usershell=StringVar()

username_entry=Entry(tab2_frame1,textvariable=entry_username)
userid_entry=Entry(tab2_frame1,textvariable=entry_userid)
userpwd_entry=Entry(tab2_frame1,textvariable=entry_userpwd,show="*")
#usershell_entry=Entry(tab2_frame1,textvariable=entry_usershell)
Radiobutton(tab2_frame1,text="sh",padx = 5,variable=entry_usershell,value="/bin/sh").grid(row=8,column=5,padx=1)
Radiobutton(tab2_frame1,text="bash",padx = 5,variable=entry_usershell,value="/bin/bash").grid(row=8,column=6,padx=1)

username_entry.grid(row=2,column=5,columnspan=3,padx=5,pady=2)
userid_entry.grid(row=4,column=5,columnspan=3,padx=5,pady=2)
userpwd_entry.grid(row=6,column=5,columnspan=3,padx=5,pady=2)
#usershell_entry.grid(row=8,column=4,columnspan=3,padx=5,pady=2)

submit=Button(tab2_frame1,text="submit",width=12,bg="yellow",padx=5,pady=2,command=addusers)
submit.grid(row=10,column=4,columnspan=2,padx=8, pady=2)

#-------------------------single mode user operations-------------------------------------
single_user=StringVar()
new_user=StringVar()
update_passwd=StringVar()
information=StringVar()
update_shell=StringVar()
exp_date=StringVar()
new_passwd=StringVar()
up_userid=StringVar()

password_frame=LabelFrame(tab2_frame2,text="changepassword",bd=1,padx=5,pady=2)
password_frame.grid(row=1,column=1,padx=5,pady=2)
oldpasswd_user=Label(password_frame,text="username",padx=5,pady=2)
oldpasswd_user.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
olduser_enter=Entry(password_frame,textvariable=single_user)
olduser_enter.grid(row=1,column=3,columnspan=2,padx=8, pady=2)
passwd_change=Label(password_frame,text="change password",padx=5,pady=2)
passwd_change.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
passwd_enter=Entry(password_frame,textvariable=update_passwd,show="*")
passwd_enter.grid(row=2,column=3,columnspan=2,padx=8, pady=2)
change_pass=Button(password_frame,text="change",width=15,bg="yellow",padx=5,pady=2,command=changepasswd)
change_pass.grid(row=3,column=2,columnspan=2,padx=8, pady=2)


lock_frame=LabelFrame(tab2_frame2,text="lock user",bd=1,padx=5,pady=2)
lock_frame.grid(row=2,column=5,padx=5,pady=2)
username_single=Label(lock_frame,text="enter username",padx=5,pady=2)
username_single.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
username_enter=Entry(lock_frame,textvariable=single_user)
username_enter.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
lock_user=Button(lock_frame,text="lock_user",width=15,bg="yellow",padx=5,pady=2,command=lockuser)
lock_user.grid(row=3,column=1,columnspan=2,padx=8, pady=2)

unlock_frame=LabelFrame(tab2_frame2,text="unlock user",bd=1,padx=5,pady=2)
unlock_frame.grid(row=1,column=5,padx=5,pady=2)
username_unlock=Label(unlock_frame,text="enter username",padx=5,pady=2)
username_unlock.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
usernameunlock_enter=Entry(unlock_frame,textvariable=single_user)
usernameunlock_enter.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
unlock_user=Button(unlock_frame,text="unlock_user",width=15,bg="yellow",padx=5,pady=2,command=unlockuser)
unlock_user.grid(row=3,column=1,columnspan=2,padx=8, pady=2)

usershell_frame=LabelFrame(tab2_frame2,text="change user shell",bd=1,padx=5,pady=4)
usershell_frame.grid(row=2,column=1,padx=5,pady=2)
usershell_name=Label(usershell_frame,text="username:",padx=5,pady=2)
usershell_name.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
usershell_enter=Entry(usershell_frame,textvariable=single_user)
usershell_enter.grid(row=1,column=3,columnspan=2,padx=8, pady=2)
shell_name=Label(usershell_frame,text="newshell name",padx=5,pady=2)
shell_name.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
shell_enter=Entry(usershell_frame,textvariable=update_shell)
shell_enter.grid(row=2,column=3,columnspan=2,padx=8, pady=2)
change_shell=Button(usershell_frame,text="change shell",width=15,bg="yellow",padx=5,pady=2,command=changeshell)
change_shell.grid(row=3,column=2,rowspan=2,columnspan=2,padx=8, pady=2)



changeuser_frame=LabelFrame(tab2_frame2,text="change user",bd=1,padx=5,pady=4)
changeuser_frame.grid(row=1,column=4,padx=5,pady=2)
usershell_name=Label(changeuser_frame,text="old username:",padx=5,pady=2)
usershell_name.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
usershell_enter=Entry(changeuser_frame,textvariable=single_user)
usershell_enter.grid(row=1,column=3,columnspan=2,padx=8, pady=2)
shell_name=Label(changeuser_frame,text="new name",padx=5,pady=2)
shell_name.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
shell_enter=Entry(changeuser_frame,textvariable=new_user)
shell_enter.grid(row=2,column=3,columnspan=2,padx=8, pady=2)
change_shell=Button(changeuser_frame,text="change user",width=15,bg="yellow",padx=5,pady=2,command=changeuser)
change_shell.grid(row=3,column=2,rowspan=2,columnspan=2,padx=8, pady=2)



userinfo_frame=LabelFrame(tab2_frame2,text="Add user information",bd=1,padx=5,pady=4)
userinfo_frame.grid(row=2,column=4,padx=5,pady=2)
userinfo_lab=Label(userinfo_frame,text="enter user info",padx=5,pady=2)
userinfo_lab.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
userinfo_enter=Entry(userinfo_frame,textvariable=single_user)
userinfo_enter.grid(row=1,column=3,columnspan=2,padx=8, pady=2)
info_lab=Label(userinfo_frame,text="information",padx=5,pady=2)
info_lab.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
info_enter=Entry(userinfo_frame,textvariable=information)
info_enter.grid(row=2,column=3,columnspan=2,padx=8, pady=2)
update_user=Button(userinfo_frame,text="add information",width=12,bg="yellow",padx=5,pady=2,command=addinformation)
update_user.grid(row=3,column=2,columnspan=2,padx=8, pady=2)

expiry_frame=LabelFrame(tab2_frame2,text="Add expirydate",bd=1,padx=5,pady=4)
expiry_frame.grid(row=3,column=1,padx=5,pady=2)
userexpiry_name=Label(expiry_frame,text="enter the username:",padx=5,pady=2)
userexpiry_name.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
userexpiry_enter=Entry(expiry_frame,textvariable=single_user)
userexpiry_enter.grid(row=1,column=3,columnspan=2,padx=8, pady=2)
expirydate_name=Label(expiry_frame,text="enter date[yyyy-mm-dd]",padx=5,pady=2)
expirydate_name.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
expirydate_enter=Entry(expiry_frame,textvariable=exp_date)
expirydate_enter.grid(row=2,column=3,columnspan=2,padx=8, pady=2)
set_expiry=Button(expiry_frame,text="set date",width=15,bg="yellow",padx=5,pady=2,command=setexpiry)
set_expiry.grid(row=3,column=2,rowspan=2,columnspan=2,padx=8, pady=2)

delete_frame=LabelFrame(tab2_frame2,text="delete",bd=1,padx=5,pady=4)
delete_frame.grid(row=3,column=5,padx=5,pady=2)
userdel_lab=Label(delete_frame,text="username to delete",padx=5,pady=2)
userdel_lab.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
userdel_entry=Entry(delete_frame,textvariable=single_user)
userdel_entry.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
lock_user=Button(delete_frame,text="delete user",width=15,bg="yellow",padx=5,pady=2,command=deleteuser)
lock_user.grid(row=3,column=1,columnspan=2,padx=8, pady=2)

userid_frame=LabelFrame(tab2_frame2,text="change userid",bd=1,padx=5,pady=4)
userid_frame.grid(row=3,column=4,padx=5,pady=2)
userinfo_lab=Label(userid_frame,text="enter username",padx=5,pady=2)
userinfo_lab.grid(row=1,column=1,columnspan=2,padx=8, pady=2)
userid_enter=Entry(userid_frame,textvariable=single_user)
userid_enter.grid(row=1,column=3,columnspan=2,padx=8, pady=2)
info_lab=Label(userid_frame,text="enter new userid",padx=5,pady=2)
info_lab.grid(row=2,column=1,columnspan=2,padx=8, pady=2)
info_enter=Entry(userid_frame,textvariable=up_userid)
info_enter.grid(row=2,column=3,columnspan=2,padx=8, pady=2)
update_user=Button(userid_frame,text="update UID",width=12,bg="yellow",padx=5,pady=2,command=changeuserid)
update_user.grid(row=3,column=2,columnspan=2,padx=8, pady=2)


###########------------------------------------------------tab3------------------------------------

tab2_frame1 =LabelFrame(tab3,text="BATCH USER MODE",bd=5,width=500, height=80)
tab2_frame1.grid(row=0, column=3, rowspan=8, columnspan=2,padx=100,pady=14)

fileupload=Button(tab2_frame1,text="file",width=12,bg="yellow",padx=5,pady=2,command=openCSV)
fileupload.grid(row=10,column=4,columnspan=2,padx=8, pady=2)
fileupload2=Button(tab2_frame1,text="UPLOAD",width=12,bg="yellow",padx=5,pady=2,command=addbatchusers)
fileupload2.grid(row=10,column=6,columnspan=2,padx=8, pady=2)


#-------------------------BATCH mode user operations-------------------------------------

tab2_frame2 =LabelFrame(tab3,text="BATCH USER FUNCTIONS",bd=5,width=500, height=80)
tab2_frame2.grid(row=10, column=3, rowspan=8, columnspan=2,padx=100,pady=14)

password_frame=LabelFrame(tab2_frame2,text="changepassword",bd=1,padx=5,pady=2)
password_frame.grid(row=1,column=1,padx=5,pady=2)
fileadd=Button(password_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=2,columnspan=2,padx=4, pady=2)
change_pass=Button(password_frame,text="change",width=15,bg="yellow",padx=5,pady=2,command=changebatchpasswd)
change_pass.grid(row=3,column=2,columnspan=2,padx=8, pady=2)


lock_frame=LabelFrame(tab2_frame2,text="lock user",bd=1,padx=5,pady=2)
lock_frame.grid(row=2,column=5,padx=5,pady=2)
fileadd=Button(lock_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=3,columnspan=2,padx=4, pady=2)
lock_user=Button(lock_frame,text="lock_user",width=15,bg="yellow",padx=5,pady=2,command=lockbatchusers)
lock_user.grid(row=3,column=3,columnspan=2,padx=8, pady=2)

unlock_frame=LabelFrame(tab2_frame2,text="unlock user",bd=1,padx=5,pady=2)
unlock_frame.grid(row=1,column=5,padx=5,pady=2)
fileadd=Button(unlock_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=1,columnspan=2,padx=4, pady=2)
unlock_user=Button(unlock_frame,text="unlock_user",width=15,bg="yellow",padx=5,pady=2,command=unlockbatchusers)
unlock_user.grid(row=3,column=1,columnspan=2,padx=8, pady=2)

usershell_frame=LabelFrame(tab2_frame2,text="change user shell",bd=1,padx=5,pady=4)
usershell_frame.grid(row=2,column=1,padx=5,pady=2)
fileadd=Button(usershell_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=2,columnspan=2,padx=4, pady=2)
change_shell=Button(usershell_frame,text="change shell",width=15,bg="yellow",padx=5,pady=2,command=batchusershells)
change_shell.grid(row=3,column=2,rowspan=2,columnspan=2,padx=8, pady=2)



changeuser_frame=LabelFrame(tab2_frame2,text="change user",bd=1,padx=5,pady=4)
changeuser_frame.grid(row=1,column=4,padx=5,pady=2)
fileadd=Button(changeuser_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=2,columnspan=2,padx=4, pady=2)
change_shell=Button(changeuser_frame,text="change user",width=15,bg="yellow",padx=5,pady=2,command=changebatchusers)
change_shell.grid(row=3,column=2,rowspan=2,columnspan=2,padx=8, pady=2)



userinfo_frame=LabelFrame(tab2_frame2,text="Add user information",bd=1,padx=5,pady=4)
userinfo_frame.grid(row=2,column=4,padx=5,pady=2)
fileadd=Button(userinfo_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=2,columnspan=2,padx=4, pady=2)
update_user=Button(userinfo_frame,text="add information",width=12,bg="yellow",padx=5,pady=2,command=addbatchinfo)
update_user.grid(row=3,column=2,columnspan=2,padx=8, pady=2)


expiry_frame=LabelFrame(tab2_frame2,text="Add expirydate",bd=1,padx=5,pady=4)
expiry_frame.grid(row=3,column=1,padx=5,pady=2)
fileadd=Button(expiry_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=2,columnspan=2,padx=4, pady=2)
set_expiry=Button(expiry_frame,text="set date",width=15,bg="yellow",padx=5,pady=2,command=expirybatchusers)
set_expiry.grid(row=3,column=2,rowspan=2,columnspan=2,padx=8, pady=2)


delete_frame=LabelFrame(tab2_frame2,text="delete",bd=1,padx=5,pady=4)
delete_frame.grid(row=3,column=5,padx=5,pady=2)
fileadd=Button(delete_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=1,columnspan=2,padx=4, pady=2)
lock_user=Button(delete_frame,text="delete user",width=15,bg="yellow",padx=5,pady=2,command=deletebatchusers)
lock_user.grid(row=3,column=1,columnspan=2,padx=8, pady=2)


userid_frame=LabelFrame(tab2_frame2,text="change userid",bd=1,padx=5,pady=4)
userid_frame.grid(row=3,column=4,padx=5,pady=2)
fileadd=Button(userid_frame,text="file",width=8,bg="yellow",padx=5,pady=2,command=batchcsv)
fileadd.grid(row=2,column=2,columnspan=2,padx=4, pady=2)
update_user=Button(userid_frame,text="update UID",width=12,bg="yellow",padx=5,pady=2,command=uidbatchusers)
update_user.grid(row=3,column=2,columnspan=2,padx=8, pady=2)



window.mainloop()
exit()
