import tkinter as tk              
import tkcalendar as cale
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import BOTH, END, LEFT 
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Menu
from tkinter import Label
import pandas as pd
import sys
import mysql.connector as sql
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import random
import webbrowser as wb
import statistics as st
window=tk.Tk()
window.geometry("2000x2000")
window.title("Home Page")
width=2000
height=2000
image = Image.open("hospital.png")
resize_image = image.resize((width, height))
img = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(image=img)
label1.image = img
label1.pack()
greeting=tk.Label(text="AVM Multispeciality Hospital",font=("Times New Roman",24))
greeting.place(x=575,y=5)
label=tk.Label(text="Healthcare Services",fg="red",bg="white",font=("Times New Roman",36))
label.place(x=575,y=350)
txtfld1=tk.StringVar()
txtfl2=tk.StringVar()
txtfl3=tk.StringVar()
txtfld1a=tk.StringVar()
txtfld2a=tk.StringVar()
txtfld3a=tk.StringVar()     
txtfld4a=tk.StringVar()
txtfld5a=tk.IntVar()
txtfld7=tk.StringVar()
txtfld4=tk.StringVar()
det=[]
cbc=0
hemo=0
ppbs=0
fbs=0
serum=0
thyroid=0
lipid=0
vitD=0
amino=0
amylase=0
cholse=0
vitB12=0
cpk=0
bg=0
covid=0
mg=0
prolactin=0
Ca=0
K=0
lft=0
un=""
option=""
test_cost=0
n1= tk.StringVar()
n2= tk.StringVar()
n3= tk.StringVar()
n4= tk.StringVar()
n5= tk.StringVar()
n6= tk.StringVar()
n7= tk.StringVar()
n8= tk.StringVar()
n9= tk.StringVar()
n10= tk.StringVar()
response=[]
hist1= tk.StringVar()
hist2= tk.StringVar()
hist3= tk.StringVar()
hist4= tk.StringVar()
def open1a():
    global top
    global un
    #top.destroy()
    messagebox.showinfo("Welcome!","Hello "+un)
    topA=tk.Toplevel(window)                  #homepage-mainscreen
    topA.geometry("2000x2000")
    topA.title("Main screen")
    width=2000
    height=2000
    image = Image.open("hospital3.png")
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(topA,image=img)
    label1.image = img
    lbl4=tk.Label(topA,text="Welcome Back",fg="black",font=("Times New Roman",32))
    lbl4.place(x=600,y=20)
    label1.pack()
    def open3():#opens appointment window
        topC=tk.Toplevel(topA)
        topC.geometry("2000x2000")
        topC.title("Appointment")
        width=2000
        height=2000
        image = Image.open("hospital4alt.jpg")     #add image
        resize_image = image.resize((width, height))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(topC,image=img)
        label1.image = img           #add extra stuff in screen
        label1.pack() 
        b1=tk.Button(topC,text="View schedule",width=20,height=4,bg="red",fg="yellow",font=("Times New Roman",20))
        b1.place(x=400,y=600)
        def open3a():
            topI=tk.Toplevel(topC)
            topI.geometry("2000x2000")
            topI.title("View Schedule")
            width=1700
            height=1000
            image = Image.open("hospital10.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(topI,image=img)
            label1.image = img
            label1.pack()
            l1=tk.Label(topI,text="Show full schedule:",fg="blue",font=("Times New Roman",20))
            l1.place(x=5,y=100)
            l2=tk.Label(topI,text="Filter by : morning availability",fg="blue",font=("Times New Roman",20))
            l2.place(x=5,y=300)
            l3=tk.Label(topI,text="Filter by : evening availability",fg="blue",font=("Times New Roman",20))
            l3.place(x=5,y=500)
            def open3a1():
                topJ=tk.Toplevel(topI)
                topJ.geometry("2000x2000")
                topJ.title("View full Schedule")
                width=1700
                height=1000
                filename = "D:\Python\docdata1.xlsx"
                df1 = pd.read_excel(filename, sheet_name = "Tables", engine='openpyxl')
                data1=pd.DataFrame(df1, columns= ['Chief_Doctors','Speciality','From','To'])
                txt = tk.Text(topJ) 
                txt.pack() 
                class PrintToTXT1(object): 
                    def write(self, s): 
                        txt.insert(END, s)
                sys.stdout = PrintToTXT1() 
                print(data1)
            def open3a2():
                topK=tk.Toplevel(topI)
                topK.geometry("2000x2000")
                topK.title("View Schedule filtered by timing")
                width=1700
                height=1000
                filename = "D:\Python\docdata1.xlsx"
                df2 = pd.read_excel(filename, sheet_name = "Tables", engine='openpyxl')
                data2=pd.DataFrame(df2, columns= ['Chief_Doctors','Speciality','From','To'])
                txt = tk.Text(topK) 
                txt.pack() 
                class PrintToTXT2(object): 
                    def write(self, s): 
                        txt.insert(END, s)
                sys.stdout = PrintToTXT2() 
                print(data2.head(4))
            def open3a3():
                topM=tk.Toplevel(topI)
                topM.geometry("2000x2000")
                topM.title("View Schedule filtered by timing")
                width=1700
                height=1000
                filename = "D:\Python\docdata1.xlsx"
                df3 = pd.read_excel(filename, sheet_name = "Tables", engine='openpyxl')
                data3=pd.DataFrame(df3, columns= ['Chief_Doctors','Speciality','From','To'])
                txt = tk.Text(topM) 
                txt.pack() 
                class PrintToTXT3(object): 
                    def write(self, s): 
                        txt.insert(END, s)
                sys.stdout = PrintToTXT3() 
                print(data3.tail(8))
            b1=tk.Button(topI,text="Select",width= 5,height=1,fg="green",
                         bg="white",font=("Times New Roman",24),command=open3a1)
            b1.place(x=545,y=90)
            b2=tk.Button(topI,text="Select",width= 5,height=1,fg="green",
                         bg="white",font=("Times New Roman",24),command=open3a2)
            b2.place(x=545,y=290)
            b3=tk.Button(topI,text="Select",width= 5,height=1,fg="green",
                         bg="white",font=("Times New Roman",24),command=open3a3)
            b3.place(x=545,y=490)    
        b1=tk.Button(topC,text="View schedule",width=20,height=4,bg="red",fg="yellow",font=("Times New Roman",20),command=open3a)
        b1.place(x=400,y=600)
        def open3c():
            topL=tk.Toplevel(topC)
            topL.geometry("2000x2000")
            topL.title("Book Appointment")
            width=1700
            height=1000
            image = Image.open("hospital10.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(topL,image=img)
            label1.image = img           #add extra stuff in screen
            lbl=tk.Label(topL,text="Please select speciality from above",
                         fg="black",font=("Times New Roman",32))
            lbl.place(x=100,y=20)
            style= ttk.Style()
            style.theme_use("clam") #clam,alt,default,classic
            topL.option_add("*TCombobox*Listbox*selectBackground", "grey")
            topL.option_add("*TCombobox*Listbox*Background", "gold")
            doc_name=""
            cost=0
            
            #app_date=     #####
            def bookdoc(n):
                global text
                global option
                global cost
                global doc_name
                global un
                option=n.get()
                print(option)
                mydb = sql.connect(host='localhost',
                   database='avm',
                   username='root',
                   password='Vishvak03$'# change password acc to computer
                   )
                cursor=mydb.cursor()
                ins="insert into bookdoc1(username,doc_name,cost,app_date,time) values (%s,%s,%s,%s,%s)"
                data=(un,doc_name,cost,text,option)
                print(data)
                cursor.execute(ins,data)
                mydb.commit()
                mydb.close()
            def my_upd(cal,l1):              #dob entry
                global text
                text=cal.get_date()
                l1.config(text=cal.get_date())
            def General():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width=23,values=["9:00 to 10:00","10:00 to 11:00","11:00 to 12:00"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name="Dr. Monishraj"
                cost= 75
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Paediatrician():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["8:00 to 9:00","9:00 to 10:00"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Naren"
                cost= 35
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Cardiologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x =400 , y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["18:00 to 19:00","19:00 to 20:00"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name="Dr. Manavh"
                cost= 70
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",bg="blue",
                              font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Anaesthetist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black',
                              font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["17:00 to 18:00","18:00 to 19:00"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name="Dr. Vignesh"
                cost= 45
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Dermatologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,
                                      values = ["18:30 to 19:30","19:30 to 20:30","20:30 to 21:30"],textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Jaideep"
                cost=35
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Ophthalmologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,
                                      values = ["10:00 to 11:00","11:00 to 12:00","12:00 to 13:00"],textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Varsha"
                cost= 40
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Oncologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["15:30 to 16:30","16:30 to 17:30"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Harini"
                cost= 35
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Virologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["19:30 to 20:30","20:30 to 21:30"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Chirag"
                cost= 55
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Radiologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["17:30 to 18:30","18:30 to 19:30"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Shreya"
                cost= 60
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def ENT_specialist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["9:30 to 10:30","10:30 to 11:30","11:30 to 12:30"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Pranav"
                cost= 35
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Neurologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,
                                      values = ["18:30 to 19:30","19:30 to 20:30","20:30 to 21:30"],textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Gem"
                cost= 70
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def Pulmonologist():
                global option
                global doc_name
                global cost
                name1 = Label(topL, text="Slots are", fg='black', font=("Helvetica", 10))
                name1.place(x = 400, y = 100)
                n = tk.StringVar() 
                option = ttk.Combobox(topL, width = 23,values = ["19:00 to 20:00","20:00 to 21:00"],
                                      textvariable = n)
                option.place(x = 400, y = 125)
                option['state'] = 'readonly'
                cal=cale.DateEntry(topL,fg="red",bg="yellow")
                cal.place(x=400,y=360)
                l1=tk.Label(topL,text='data',bg='yellow')  
                l1.place(x=800,y=360) 
                b0=tk.Button(topL,text='Read', command=lambda:my_upd(cal,l1))     #####
                b0.place(x=600,y=360)
                doc_name= "Dr. Darshan"
                cost= 40
                bt1=tk.Button(topL, text= "Confirm", width = 5 , fg="yellow",
                              bg="blue", font=("Helvetica", 10),command=lambda:bookdoc(n))
                bt1.place(x=600,y=700)
            def window_setup():
                 menu = Menu(topL, background = "black", activebackground = "gold")
                 topL.config(menu = menu)
                 gen = Menu(menu, background = "gold", activebackground = "grey") #General 
                 menu.add_cascade(label='General', menu = gen)
                 gen.add_command(label='Dr. Monishraj', command = General)
                 peds = Menu(menu, background = "gold", activebackground = "grey") #Paediatrician 
                 menu.add_cascade(label='Paediatrician', menu = peds)
                 peds.add_command(label='Dr. Naren', command = Paediatrician)
                 cardio = Menu(menu, background = "gold", activebackground = "grey") #Cardiologist 
                 menu.add_cascade(label='Cardiologist', menu = cardio)
                 cardio.add_command(label='Dr. Manavh', command = Cardiologist)
                 ana = Menu(menu, background = "gold", activebackground = "grey") #Anaesthetist 
                 menu.add_cascade(label='Anaesthetist', menu = ana)
                 ana.add_command(label='Dr. Vignesh', command = Anaesthetist)
                 derm = Menu(menu, background = "gold", activebackground = "grey") #Dermatologist 
                 menu.add_cascade(label='Dermatologist', menu = derm)
                 derm.add_command(label='Dr. Jaideep', command = Dermatologist)
                 opth = Menu(menu, background = "gold", activebackground = "grey") #Ophthalmologist 
                 menu.add_cascade(label='Ophthalmologist', menu = opth)
                 opth.add_command(label='Dr. Varsha', command = Ophthalmologist)
                 on = Menu(menu, background = "gold", activebackground = "grey") #Oncologist 
                 menu.add_cascade(label='Oncologist', menu = on)
                 on.add_command(label='Dr. Harini', command = Oncologist)
                 viro = Menu(menu, background = "gold", activebackground = "grey") #Virologist 
                 menu.add_cascade(label='Virologist', menu = viro)
                 viro.add_command(label='Dr. Chirag', command = Virologist)
                 rad = Menu(menu, background = "gold", activebackground = "grey") #Radiologist 
                 menu.add_cascade(label='Radiologist', menu = rad)
                 rad.add_command(label='Dr. Shreya', command = Radiologist)
                 ent = Menu(menu, background = "gold", activebackground = "grey") #ENT_specialist 
                 menu.add_cascade(label='ENT_specialist', menu = ent)
                 ent.add_command(label='Dr. Pranav', command = ENT_specialist)
                 neuro = Menu(menu, background = "gold", activebackground = "grey") #Neurologist 
                 menu.add_cascade(label='Neurologist', menu = neuro)
                 neuro.add_command(label='Dr. Gem', command = Neurologist)
                 plum = Menu(menu, background = "gold", activebackground = "grey") #Pulmonologist 
                 menu.add_cascade(label='Pulmonologist', menu = plum)
                 plum.add_command(label='Dr. Darshan', command = Pulmonologist)
            window_setup()
            label1.pack()
        b2=tk.Button(topC,text="Book Appointment",width=20,height=4,bg="red",
                     fg="yellow",font=("Times New Roman",20),command=open3c)
        b2.place(x=400,y=200)
        def cbc_count():
            global test_cost
            global cbc
            cbc+=1
            test_cost+=390
            print(cbc)
        def hemo_count():
            global test_cost
            global hemo
            hemo+=1
            test_cost+=300
            print(hemo)
        def ppbs_count():
            global test_cost
            global ppbs
            ppbs+=1
            test_cost+=300
        def fbs_count():
            global test_cost
            global fbs
            fbs+=1
            test_cost+=350
        def serum_count():
            global test_cost
            global serum
            serum+=1
            test_cost+=400
        def thyroid_count():
            global test_cost
            global thyroid
            thyroid+=1
            test_cost+=530
        def lipid_count():
            global test_cost
            global lipid
            lipid+=1
            test_cost+=330
        def vitD_count():
            global test_cost
            global vitD
            vitD+=1
            test_cost+=240
        def amino_count():
            global test_cost
            global amino
            amino+=1
            test_cost+=400
        def amylase_count():
            global test_cost
            global amylase
            amylase+=1
            test_cost+=360
        def cholse_count():
            global test_cost
            global cholse
            cholse+=1
            test_cost+=470
        def vitB12_count():
            global test_cost
            global vitB12
            vitB12+=1
            test_cost+=450
        def cpk_count():
            global test_cost
            global cpk
            cpk+=1
            test_cost+=430
        def bg_count():
            global test_cost
            global bg
            bg+=1
            test_cost+=420
        def covid_count():
            global test_cost
            global covid
            covid+=1
            test_cost+=100
        def mg_count():
            global test_cost
            global mg
            mg+=1
            test_cost+=320
        def prolactin_count():
            global test_cost
            global prolactin
            prolactin+=1
            test_cost+=380
        def Ca_count():
            global test_cost
            global Ca
            Ca+=1
            test_cost+=400
        def K_count():
            global test_cost
            global K
            K+=1
            test_cost+=400
        def lft_count():
            global test_cost
            global lft
            lft+=1
            test_cost+=300
        def book_test():########
            global test_cost
            global un
            global cbc
            global hemo
            global ppbs
            global fbs
            global serum
            global thyroid
            global lipid
            global vitD
            global amino
            global amylase
            global cholse
            global vitB12
            global cpk
            global bg
            global covid
            global mg
            global prolactin
            global Ca
            global K
            global lft
            mydb = sql.connect(host='localhost',
                   database='avm',
                   username='root',
                   password='Vishvak03$'# change password acc to computer
                   )
            cursor=mydb.cursor()
            ins="insert into booktests(username,cbc,hemo,ppbs,fbs,serum,thyroid,lipid,vitD,amino,amylase,cholse,vitB12,cpk,bg,covid,mg,prolactin,Ca,K,lft,cost) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data=(un,cbc,hemo,ppbs,fbs,
                  serum,thyroid,lipid,vitD,
                  amino,amylase,cholse,vitB12,
                  cpk,bg,covid,mg,prolactin,
                  Ca,K,lft,test_cost)
            print(data)
            cursor.execute(ins,data)
            mydb.commit()
            mydb.close()
        def open3b1(): #opens book tests window
            topH=tk.Toplevel(topC)
            topH.geometry("2000x2000")
            topH.title("Book Tests page 1 of 2")
            scrollbar=tk.Scrollbar(topH)
            scrollbar.pack( side = tk.RIGHT,  fill = tk.Y )
            mylist = tk.Listbox(topH, yscrollcommand = scrollbar.set )
            width=2000
            height=2000
            image = Image.open("hospitalbooktests.jpg")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(topH,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            l1=tk.Label(topH,text="Complete Blood Count / Hemogram (CBC)",fg="blue",font=("Times New Roman",20))
            l1.place(x=5,y=100)
            l2=tk.Label(topH,text="Hemoglobin",fg="blue",font=("Times New Roman",20))
            l2.place(x=5,y=200)
            l3=tk.Label(topH,text="Post Prandial Blood Sugar (PPBS)",fg="blue",font=("Times New Roman",20))
            l3.place(x=5,y=300)
            l4=tk.Label(topH,text="Fasting Blood Sugar (FBS)",fg="blue",font=("Times New Roman",20))
            l4.place(x=5,y=400)
            l5=tk.Label(topH,text="Serum Electrolytes",fg="blue",font=("Times New Roman",20))
            l5.place(x=5,y=500)
            l6=tk.Label(topH,text="Thyroid Profile",fg="blue",font=("Times New Roman",20))
            l6.place(x=700,y=100)
            l7=tk.Label(topH,text="Lipid Profile",fg="blue",font=("Times New Roman",20))
            l7.place(x=700,y=200)
            l8=tk.Label(topH,text="Vitamin D Total",fg="blue",font=("Times New Roman",20))
            l8.place(x=700,y=300)
            l9=tk.Label(topH,text="Amino Acid Profile",fg="blue",font=("Times New Roman",20))
            l9.place(x=700,y=400)
            l10=tk.Label(topH,text="Amylase",fg="blue",font=("Times New Roman",20))
            l10.place(x=700,y=500)
            b1=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=cbc_count)
            b1.place(x=545,y=90)
            b2=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=hemo_count)
            b2.place(x=545,y=190)
            b3=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=ppbs_count)
            b3.place(x=545,y=290)
            b4=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=fbs_count)
            b4.place(x=545,y=390)
            b5=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=serum_count)
            b5.place(x=545,y=490)
            b6=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=thyroid_count)
            b6.place(x=1200,y=90)
            b7=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=lipid_count)
            b7.place(x=1200,y=190)
            b8=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=vitD_count)
            b8.place(x=1200,y=290)
            b9=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                         activebackground='#00ff00',font=("Times New Roman",24),command=amino_count)
            b9.place(x=1200,y=390)
            b10=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=amylase_count)
            b10.place(x=1200,y=490)
            b21=tk.Button(topH,text="BACK",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=topH.destroy)
            b21.place(x=545,y=600)
            b22=tk.Button(topH,text="NEXT",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=open3b2)
            b22.place(x=1200,y=600)
        def open3b2():
            topH=tk.Toplevel(topC)
            topH.geometry("2000x2000")
            topH.title("Book Tests page 2 of 2")
            scrollbar=tk.Scrollbar(topH)
            scrollbar.pack( side = tk.RIGHT,  fill = tk.Y )
            mylist = tk.Listbox(topH, yscrollcommand = scrollbar.set )
            width=2000
            height=2000
            image = Image.open("hospitalbooktests.jpg")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(topH,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            l11=tk.Label(topH,text="Total Cholesterol",fg="blue",font=("Times New Roman",20))
            l11.place(x=5,y=100)
            l12=tk.Label(topH,text="Vitamin B12",fg="blue",font=("Times New Roman",20))
            l12.place(x=5,y=200)
            l13=tk.Label(topH,text="CPK (Muscle / Brain)",fg="blue",font=("Times New Roman",20))
            l13.place(x=5,y=300)
            l14=tk.Label(topH,text="Blood Group",fg="blue",font=("Times New Roman",20))
            l14.place(x=5,y=400)
            l15=tk.Label(topH,text="Covid IgG Antibody Test",fg="blue",font=("Times New Roman",20))
            l15.place(x=5,y=500)
            l16=tk.Label(topH,text="Magnesium",fg="blue",font=("Times New Roman",20))
            l16.place(x=700,y=100)
            l17=tk.Label(topH,text="Prolactin",fg="blue",font=("Times New Roman",20))
            l17.place(x=700,y=200)
            l18=tk.Label(topH,text="Calcium (Ca)",fg="blue",font=("Times New Roman",20))
            l18.place(x=700,y=300)
            l19=tk.Label(topH,text="Potassium (K+)",fg="blue",font=("Times New Roman",20))
            l19.place(x=700,y=400)
            l20=tk.Label(topH,text="Liver Function Test (LFT)",fg="blue",font=("Times New Roman",20))
            l20.place(x=700,y=500)
            b11=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=cholse_count)
            b11.place(x=545,y=90)
            b12=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=vitB12_count)
            b12.place(x=545,y=190)
            b13=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=cpk_count)
            b13.place(x=545,y=290)
            b14=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=bg_count)
            b14.place(x=545,y=390)
            b15=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=covid_count)
            b15.place(x=545,y=490)
            b16=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=mg_count)
            b16.place(x=1200,y=90)
            b17=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=prolactin_count)
            b17.place(x=1200,y=190)
            b18=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=Ca_count)
            b18.place(x=1200,y=290)
            b19=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=K_count)
            b19.place(x=1200,y=390)
            b20=tk.Button(topH,text="Select",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=lft_count)
            b20.place(x=1200,y=490)
            b21=tk.Button(topH,text="BACK",width= 5,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=topH.destroy)
            b21.place(x=545,y=600)
            b22=tk.Button(topH,text="CONFIRM",width= 7,height=1,fg="green",bg="white",
                          activebackground='#00ff00',font=("Times New Roman",24),command=book_test)
            b22.place(x=1200,y=600)
        b3=tk.Button(topC,text="Book tests",width=20,height=4,bg="red",fg="yellow",
                     font=("Times New Roman",20),command=open3b1)
        b3.place(x=800,y=200)
    b1=tk.Button(topA,text="Appointments",width=10,height=2,bg="yellow",
                 fg="red",font=("Times New Roman",18),command=open3)
    b1.place(x=400,y=600)
    def open4():   #self check window
        topD=tk.Toplevel(topA)
        topD.geometry("2000x2000")
        topD.title("Self Check")
        width=1500
        height=800
        image = Image.open("hospitalselfcheck.png")     #add image
        resize_image = image.resize((width, height))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(topD,image=img)
        label1.image = img           #add extra stuff in screen
        label1.pack()
        l1=tk.Label(topD,text="To assess your condition, click the button below:",
                    fg="purple",bg="yellow",font=("Times New Roman",24))
        l1.place(x=100,y=100)
        l2=tk.Label(topD,text="To take up a quiz on safety precautions, click the button below:",
                    fg="purple",bg="yellow",font=("Times New Roman",24))
        l2.place(x=100,y=400)
        def quesfinish():
            global response
            q11=tk.Toplevel(topD)
            q11.geometry("2000x2000")
            q11.title("Self Test - End")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q11,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lb1=tk.Label(q11,text="Results based on the answers to the previous 10 questions:",
                         width=100,height=2,fg="black",font=("Times New Roman",14))
            lb1.place(x=5, y=20)
            if int(response[0])<8:
                if int(response[0])<5:
                    lbl1=tk.Label(q11,text="Unhealthy",width=100,height=2,fg="black",font=("Times New Roman",14))
                    lbl1.place(x=50, y=100)
                else:
                    lbl2=tk.Label(q11,text="Healthy, keep track of your health",
                                  width=100,height=2,fg="black",font=("Times New Roman",14))
                    lbl2.place(x=50, y=100)
            else:
                lbl6=tk.Label(q11,text="Healthy",width=100,height=2,fg="black",font=("Times New Roman",14))
                lbl6.place(x=50, y=100)
            if response[1] in ['Several days','More days than not','Nearly every day']:
                if response[1]!="Nearly every day":
                    lbl3=tk.Label(q11,text="Try to talk about your anxieties to someone.",
                                  width=100,height=2,fg="black",font=("Times New Roman",14))
                    lbl3.place(x=50, y=175)
                else:
                    lbl8=tk.Label(q11,text="Consult a therapist immedietely",
                                  width=100,height=2,fg="black",font=("Times New Roman",14))
                    lbl8.place(x=50, y=175)
            else:
                lbl7=tk.Label(q11,text="Mentally Healthy",width=100,
                              height=2,fg="black",font=("Times New Roman",14))
                lbl7.place(x=50, y=175)
            if response[2] in ['1','2','3','4','5']:
                if int(response[2])<3:
                    lbl4=tk.Label(q11,text="Exercise Regularly",width=100,
                                  height=2,fg="black",font=("Times New Roman",14))
                    lbl4.place(x=50, y=250)
                else:
                    lbl5=tk.Label(q11,text="Continue Exercising Regularly",width=100,height=2,
                                  fg="black",font=("Times New Roman",14))
                    lbl5.place(x=50, y=250)
            else:
                lbl9=tk.Label(q11,text="Continue Exercising Regularly, keep up the good physical work :)",
                              width=100,height=2,fg="black",font=("Times New Roman",14))
                lbl9.place(x=50, y=250)
            bt1=tk.Button(q11,text="Return to homepage",width=100,height=2,fg="black",
                          font=("Times New Roman",14),command=q11.destroy)
            bt1.place(x=200,y=500)
        def nn10(n10):
            global response
            an10=n10.get()
            response.append(an10)
        def next10():
            global n10
            q10=tk.Toplevel(topD)
            q10.geometry("2000x2000")
            q10.title("Question 10")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q10,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q10,
                         text="10. On how many of the last 7 days did you engage in moderate to strenuous exercise (like a brisk walk)?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q10, width = 27, textvariable = n10) 
            a1['values'] = ('0','1','2','3','4','5','6','7')  
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q10,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[quesfinish(),nn10(n10)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q10,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[next9(),q10.destroy()])
            bt2.place(x=800,y=660)
        def nn9(n9):
            an9=n9.get()
        def next9():
            global n9
            q9=tk.Toplevel(topD)
            q9.geometry("2000x2000")
            q9.title("Question 9")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q9,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q9,
                         text="9. How often do you have trouble taking medicines the way you have been told to take them?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q9, width = 27, textvariable = n9) 
            a1['values'] = ('I do not have to take medicine',
                            'I always take them as prescribed',
                            'Sometimes I take them as prescribed',
                            'I seldom take them as prescribed')  
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q9,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next10(),q9.destroy(),nn9(n9)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q9,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next8(),q9.destroy()])
            bt2.place(x=800,y=660)
        def nn8(n8):
            an8=n8.get()
        def next8():
            global n8
            q8=tk.Toplevel(topD)
            q8.geometry("2000x2000")
            q8.title("Question 8")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q8,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q8,
                         text="8. Over the past 2 weeks, how often have you felt little interest or pleasure in doing things?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q8, width = 27, textvariable = n8) 
            a1['values'] = ('Not at all','Several days','More days than not','Nearly every day')  
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q8,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next9(),q8.destroy(),nn8(n8)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q8,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next7(),q8.destroy()])
            bt2.place(x=800,y=660)
        def nn7(n7):
            global response
            an7=n7.get()
            response.append(an7)
        def next7():
            global n7
            q7=tk.Toplevel(topD)
            q7.geometry("2000x2000")
            q7.title("Question 7")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q7,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q7,
                         text="7. Over the past 2 weeks, how often have you felt down, depressed, or hopeless?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q7, width = 27, textvariable = n7) 
            a1['values'] = ('Not at all','Several days','More days than not','Nearly every day')  
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q7,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next8(),q7.destroy(),nn7(n7)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q7,text="Back",width=10,height=2,
                          fg="black",font=("Times New Roman",14),command=lambda:[next6(),q7.destroy()])
            bt2.place(x=800,y=660)
        def nn6(n6):
            an6=n6.get()
        def next6():
            global n6
            q6=tk.Toplevel(topD)
            q6.geometry("2000x2000")
            q6.title("Question 6")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q6,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q6,text="6. Over the past 2 weeks, how often have you felt nervous, anxious, or on edge?",fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q6, width = 27, textvariable = n6) 
            a1['values'] = ('Not at all','Several days','More days than not','Nearly every day') #values:It specifies the list of values to display in the drop-down listbox. 
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q6,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[next7(),q6.destroy(),nn6(n6)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q6,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[next5(),q6.destroy()])
            bt2.place(x=800,y=660)
        def nn5(n5):
            an5=n5.get()
        def next5():
            global n5
            q5=tk.Toplevel(topD)
            q5.geometry("2000x2000")
            q5.title("Question 5")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q5,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q5,text="5. Do you have any hereditary conditions/diseases?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q5, width = 27, textvariable = n5) 
            a1['values'] = ('High blood pressure','Diabetes','Hemophilia','Thalassemia','Huntington','Other')   
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q5,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[next6(),q5.destroy(),nn5(n5)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q5,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[next4(),q5.destroy()])
            bt2.place(x=800,y=660)
        def nn4(n4):
            an4=n4.get()
        def next4():
            global n4
            q4=tk.Toplevel(topD)
            q4.geometry("2000x2000")
            q4.title("Question 4")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q4,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q4,text="4. Do you have any chronic diseases?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q4, width = 27, textvariable = n4) 
            a1['values'] = ('Yes','No') 
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q4,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next5(),q4.destroy(),nn4(n4)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q4,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next3(),q4.destroy()])
            bt2.place(x=800,y=660)
        def nn3(n3):
            an3=n3.get()
        def next3():
            global n3
            q3=tk.Toplevel(topD)
            q3.geometry("2000x2000")
            q3.title("Question 3")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q3,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q3,text="3. What do you say about your overall health?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q3, width = 27, textvariable = n3) 
            a1['values'] = ('Having Good Physical Health','Moderately physically impaired',
                            'Severely physically impaired','Totally physically impaired')   
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q3,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next4(),q3.destroy(),nn3(n3)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q3,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next2(),q3.destroy()])
            bt2.place(x=800,y=660)
        def nn2(n2):
            global response
            an2=n2.get()
            response.append(an2)
        def next2():
            global n2
            q2=tk.Toplevel(topD)
            q2.geometry("2000x2000")
            q2.title("Question 2")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q2,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q2,text="2. How often do you get a health checkup?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q2, width = 27, textvariable = n2) 
            a1['values'] = ('Once in 3 months','Once in 6 months',
                            'Once a year','Only when needed','Never get it done')     
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q2,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next3(),q2.destroy(),nn2(n2)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q2,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next1(),q2.destroy()])
            bt2.place(x=800,y=660)
        def nn1(n1):
            global response
            an1=n1.get()
            response.append(an1)
        def next1():
            global n1
            q1=tk.Toplevel(topD)
            q1.geometry("2000x2000")
            q1.title("Question 1")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q1,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q1,text="1. How healthy do you consider yourself on a scale of 1 to 10?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            a1= ttk.Combobox(q1, width = 27, textvariable = n1) 
            a1['values'] = ('1','2','3','4','5','6','7','8','9','10')  
            a1.current()
            a1.place(x=340,y=380)
            bt1=tk.Button(q1,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[next2(),q1.destroy(),nn1(n1)])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q1,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=q1.destroy)
            bt2.place(x=800,y=660)
        b1=tk.Button(topD,text="Start",width=10,height=4,bg="yellow",
                     fg="red",font=("Times New Roman",20),command=next1)
        b1.place(x=400,y=200)
        b1=tk.Button(topD,text="Start",width=10,height=4,bg="yellow",
                     fg="red",font=("Times New Roman",20),command=next1)
        b1.place(x=400,y=200)
        def sel():
            global var
            selection = "You selected the option " + var.get()
            label.config(text = selection)
        def qzfinish():
            global var
            q11=tk.Toplevel(topD)
            q11.geometry("2000x2000")
            q11.title("Qustions - End")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q11,image=img)
            label1.image = img           
            label1.pack()
            lb1=tk.Label(q11,text="Results:",width=10,height=2,fg="black",font=("Times New Roman",14))
            lb1.place(x=5, y=20)
            bt1=tk.Button(q11,text="Return to homepage",width=20,height=2,
                          fg="black",font=("Times New Roman",14),command=q11.destroy)
            bt1.place(x=200,y=500)
        def qz10():
            global var
            q10=tk.Toplevel(topD)
            q10.geometry("2000x2000")
            q10.title("Question 10")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q10,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q10,text="10. If someone near you has been electrocuted, when should that person see a doctor?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel10():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is B. Electrocution victims should ALWAYS see a doctor.")
            R1 = tk.Radiobutton(q10, text="A. If the electrocution was bad enough to cause burns",
                                fg="blue",font=("Times New Roman",24), variable=var, value="A",command=sel10)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q10, text="B. Electrocution victims should ALWAYS see a doctor.",
                                fg="blue",font=("Times New Roman",24), variable=var, value="B",command=sel10)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q10, text="C. Electrocution victims never have to see a doctor",
                                fg="blue",font=("Times New Roman",24), variable=var, value="C",command=sel10)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q10, text="D. If the electrocution causes tremors or confusion",
                                fg="blue",font=("Times New Roman",24), variable=var, value="D",command=sel10)
            R4.place(x=100,y=400)
            label1 = tk.Label(q10,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q10,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q10,text="Next",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[qzfinish(),q10.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q10,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=lambda:[qz9(),q10.destroy()])
            bt2.place(x=800,y=660)
        def qz9():
            global var
            q9=tk.Toplevel(topD)
            q9.geometry("2000x2000")
            q9.title("Question 9")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q9,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q9,
                         text="9. You are at a pool party, and a friend gets stuck under water. When he is pulled out of the water, he is unconscious. What should you do before you start CPR or mouth-to-mouth resuscitation?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel9():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is B. Put your ear to the person's nose to check if he or she is breathing.")
            R1 = tk.Radiobutton(q9, text="A. Poke the person's toe with a needle to check for reflexes",
                                fg="blue",font=("Times New Roman",24), variable=var, value="A",command=sel9)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q9,
                                text="B. Put your ear to the person's nose to check if he or she is breathing.",
                                fg="blue",font=("Times New Roman",24), variable=var, value="B",command=sel9)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q9,
                                text="C. Pinch the person's face to bring back consciousness",
                                fg="blue",font=("Times New Roman",24), variable=var, value="C",command=sel9)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q9, text="D. Splash the person's face with water to shock him awake",
                                fg="blue",font=("Times New Roman",24), variable=var, value="D",command=sel9)
            R4.place(x=100,y=400)
            label1 = tk.Label(q9,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q9,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q9,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz10(),q9.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q9,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz8(),q9.destroy()])
            bt2.place(x=800,y=660)
        def qz8():
            global var
            q8=tk.Toplevel(topD)
            q8.geometry("2000x2000")
            q8.title("Question 8")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q8,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q8,
                         text="8. If someone you know becomes disoriented or loses alertness, which of these questions should you NOT ask him or her?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel8():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is D. What is the square root of 164,752?.")
            R1 = tk.Radiobutton(q8, text="A. How old are you?",fg="blue",font=("Times New Roman",24),
                                variable=var, value="A",command=sel8)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q8, text="B. What is the date?",fg="blue",
                                font=("Times New Roman",24), variable=var, value="B",command=sel8)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q8, text="C. What is your name?",fg="blue",font=("Times New Roman",24),
                                variable=var, value="C",command=sel8)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q8, text="D. What is the square root of 164,752?.",fg="blue",
                                font=("Times New Roman",24), variable=var, value="D",command=sel8)
            R4.place(x=100,y=400)
            label1 = tk.Label(q8,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q8,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q8,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz9(),q8.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q8,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz7(),q8.destroy()])
            bt2.place(x=800,y=660)
        def qz7():
            global var
            q7=tk.Toplevel(topD)
            q7.geometry("2000x2000")
            q7.title("Question 7")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q7,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q7,text="7. How do you help a choking person?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel7():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is B. Begin back blows.")
            R1 = tk.Radiobutton(q7, text="A. Make them sit properly",fg="blue",
                                font=("Times New Roman",24), variable=var, value="A",command=sel7)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q7, text="B. Begin back blows.",fg="blue",font=("Times New Roman",24),
                                variable=var, value="B",command=sel7)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q7, text="C. Call 911",fg="blue",font=("Times New Roman",24),
                                variable=var, value="C",command=sel7)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q7, text="D. Make them sleep",fg="blue",
                                font=("Times New Roman",24), variable=var, value="D",command=sel7)
            R4.place(x=100,y=400)
            label1 = tk.Label(q7,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q7,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q7,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz8(),q7.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q7,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz6(),q7.destroy()])
            bt2.place(x=800,y=660)
        def qz6():
            global var
            q6=tk.Toplevel(topD)
            q6.geometry("2000x2000")
            q6.title("Question 6")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q6,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q6,text="6. What determines you to use CPR?",fg="purple",
                         bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel6():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is C. If someone is not breathing normally.")
            R1 = tk.Radiobutton(q6, text="A. When a person is not moving",fg="blue",
                                font=("Times New Roman",24), variable=var, value="A",command=sel6)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q6, text="B. When a person is low in energy",fg="blue",
                                font=("Times New Roman",24), variable=var, value="B",command=sel6)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q6, text="C. If someone is not breathing normally.",
                                fg="blue",font=("Times New Roman",24), variable=var, value="C",command=sel6) 
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q6, text="D. All of the above",fg="blue",font=("Times New Roman",24),
                                variable=var, value="D",command=sel6)
            R4.place(x=100,y=400)
            label1 = tk.Label(q6,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q6,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q6,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz7(),q6.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q6,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz5(),q6.destroy()])
            bt2.place(x=800,y=660)
        def qz5():
            global var
            q5=tk.Toplevel(topD)
            q5.geometry("2000x2000")
            q5.title("Question 5")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q5,image=img)
            lbl=tk.Label(q5,text="5. Which of these is not a sign of heatstroke?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel5():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is A. Nose bleeding.")
            R1 = tk.Radiobutton(q5, text="A. Nose bleeding.",fg="blue",font=("Times New Roman",24),
                                variable=var, value="A",command=sel5)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q5, text="B. Muscle cramps",fg="blue",font=("Times New Roman",24),
                                variable=var, value="B",command=sel5)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q5, text="C. Nausea or vomiting",fg="blue",font=("Times New Roman",24),
                                variable=var, value="C",command=sel5)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q5, text="D. None of the above",fg="blue",font=("Times New Roman",24),
                                variable=var, value="D",command=sel5)
            R4.place(x=100,y=400)
            label1 = tk.Label(q5,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q5,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q5,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz6(),q5.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q5,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz4(),q5.destroy()])
            bt2.place(x=800,y=660)
        def qz4():
            global var
            q4=tk.Toplevel(topD)
            q4.geometry("2000x2000")
            q4.title("Question 4")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     #add image
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q4,image=img)
            label1.image = img           #add extra stuff in screen
            label1.pack()
            lbl=tk.Label(q4,
                         text="4. Which of the following is a common sign or symptom of a patient experiencing a diabetic emergency?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel4():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is B. Pale, clammy skin.")
            R1 = tk.Radiobutton(q4, text="A. Slow pulse",fg="blue",font=("Times New Roman",24),
                                variable=var, value="A",command=sel4)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q4, text="B. Pale, clammy skin.",fg="blue",font=("Times New Roman",24),
                                variable=var, value="B",command=sel4)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q4, text="C. Elevated blood pressure",fg="blue",font=("Times New Roman",24),
                                variable=var, value="C",command=sel4)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q4, text="D. Decreased respiratory rate",fg="blue",font=("Times New Roman",24),
                                variable=var, value="D",command=sel4)
            R4.place(x=100,y=400)
            label1 = tk.Label(q4,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q4,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q4,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz5(),q4.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q4,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz3(),q4.destroy()])
            bt2.place(x=800,y=660)
        def qz3():
            global var
            q3=tk.Toplevel(topD)
            q3.geometry("2000x2000")
            q3.title("Question 3")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q3,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q3,
                         text="3. The victim has pale or bluish skin color, cold skin, and dull or sunken eyes. These are symptoms of which health emergency?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel3():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is B. Shock.")
            R1 = tk.Radiobutton(q3, text="A. High fever",fg="blue",font=("Times New Roman",24),
                                variable=var, value="A",command=sel3)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q3, text="B. Shock.",fg="blue",font=("Times New Roman",24),
                                variable=var, value="B",command=sel3)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q3, text="C. Heart attack",fg="blue",font=("Times New Roman",24),
                                variable=var, value="C",command=sel3)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q3, text="D. None of the above",fg="blue",
                                font=("Times New Roman",24), variable=var, value="D",command=sel3)
            R4.place(x=100,y=400)
            label1 = tk.Label(q3,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q3,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q3,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz4(),q3.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q3,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz2(),q3.destroy()])
            bt2.place(x=800,y=660)
        def qz2():
            global var
            q2=tk.Toplevel(topD)
            q2.geometry("2000x2000")
            q2.title("Question 2")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q2,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q2,text="2. If a person has a bleeding wound, what should you do?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel2():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is D. B and C.")
            R1 = tk.Radiobutton(q2, text="A. Apply a tourniquet right away",fg="blue",
                                font=("Times New Roman",24), variable=var, value="A",command=sel2)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q2, text="B. Cover the wound with a clean cloth",fg="blue",
                                font=("Times New Roman",24), variable=var, value="B",command=sel2)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q2, text="C. Put continuous pressure on the wound with the palm of your hand",
                                fg="blue",font=("Times New Roman",24), variable=var, value="C",command=sel2) 
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q2, text="D. B and C.",fg="blue",font=("Times New Roman",24),
                                variable=var, value="D",command=sel2)
            R4.place(x=100,y=400)
            label1 = tk.Label(q2,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q2,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q2,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz3(),q2.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q2,text="Back",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz1(),q2.destroy()])
            bt2.place(x=800,y=660)
        def qz1():
            global var
            q1=tk.Toplevel(topD)
            q1.geometry("2000x2000")
            q1.title("Question 1")
            width=1500
            height=800
            image = Image.open("hospitalselfcheck.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(q1,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(q1,text="1. If you need to call 911 in an emergency, what should you tell the dispatcher?",
                         fg="purple",bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            var = tk.StringVar()
            def sel1():
                s=var.get()
                selection = "You selected the option " + s
                label1.config(text = selection)
                label2.config(text = "The correct option is D. All of the above.")
            R1 = tk.Radiobutton(q1, text="A. Describe the emergency",fg="blue",font=("Times New Roman",24),
                                variable=var, value="A",command=sel1)
            R1.place(x=100,y=100)
            R2 = tk.Radiobutton(q1, text="B. Give your name and the telephone number of the phone you are using to make the call",
                                fg="blue",font=("Times New Roman",24), variable=var, value="B",command=sel1)
            R2.place(x=100,y=200)
            R3 = tk.Radiobutton(q1, text="C. Give the exact address where the emergency occurred",
                                fg="blue",font=("Times New Roman",24), variable=var, value="C",command=sel1)
            R3.place(x=100,y=300)
            R4 = tk.Radiobutton(q1, text="D. All of the above.",fg="blue",font=("Times New Roman",24),
                                variable=var, value="D",command=sel1)
            R4.place(x=100,y=400)
            label1 = tk.Label(q1,fg="purple",font=("Times New Roman",18))
            label1.place(x=100,y=500)
            label2 = tk.Label(q1,fg="purple",font=("Times New Roman",18))
            label2.place(x=100,y=550)
            bt1=tk.Button(q1,text="Next",width=10,height=2,fg="black",font=("Times New Roman",14),
                          command=lambda:[qz2(),q1.destroy()])
            bt1.place(x=340,y=660)
            bt2=tk.Button(q1,text="Back",width=10,height=2,fg="black",
                          font=("Times New Roman",14),command=q1.destroy)
            bt2.place(x=800,y=660)
        b2=tk.Button(topD,text="Start",width=10,height=4,bg="yellow",fg="red",
                     font=("Times New Roman",20),command=qz1)
        b2.place(x=400,y=500)
        b3=tk.Button(topD,text="return to \nhome page",width=20,height=4,bg="yellow",
                     fg="red",font=("Times New Roman",16),command=topD.destroy)
        b3.place(x=800,y=600)
    b2=tk.Button(topA,text="Self Check",width=10,height=2,bg="yellow",fg="red",
                 font=("Times New Roman",18),command=open4)
    b2.place(x=800,y=600)
    def open5():         #about us screen
        def graph():
            def graphnxt():
                plt.style.use('seaborn')
                topEnxt=tk.Tk()
                topEnxt.geometry("2000x2000")
                topEnxt.title("graph")
                width=2000
                height=2000
                matplotlib.use('TkAgg')
                f = Figure(figsize=(5,5), dpi=100)
                a = f.add_subplot(111)
                dates = [
                    datetime(2020, 2, 1),
                    datetime(2020, 3, 1),
                    datetime(2020, 4, 1),
                    datetime(2020, 5, 1),
                    datetime(2020, 6, 1),
                    datetime(2020, 7, 1),
                    datetime(2020, 8, 1),
                    datetime(2020, 9, 1),
                    datetime(2020, 10, 1),
                    datetime(2020, 11, 1),
                    datetime(2020, 12, 1),
                    datetime(2021, 1, 1),
                    datetime(2021, 2, 1),
                    datetime(2021, 3, 1),
                    datetime(2021, 4, 1),
                    datetime(2021, 5, 1),
                    datetime(2021, 6, 1),
                    datetime(2021, 7, 1),
                    datetime(2021, 8, 1),
                    datetime(2021, 9, 1),
                    datetime(2021, 10, 1),
                    datetime(2021, 11, 1),
                    datetime(2021, 12, 1),
                    datetime(2022, 1, 1),
                    datetime(2022, 2, 1),
                    datetime(2022, 3, 1),
                    datetime(2022, 4, 1),
                    datetime(2022, 5, 1),
                    datetime(2022, 6, 1),
                    datetime(2022, 7, 1),
                    datetime(2022, 8, 1),
                    datetime(2022, 9, 1),
                    datetime(2022, 10, 1),
                ]

                y = [3,20,120,430,
                     880,2000,2500,7000,
                     8000,9300,16000,16400,
                     12000,15000,23500,41000,
                     53000,73000,40000,30000,
                     20000,10000,5000,100000,
                     350000,75000,5000,2500,
                     20000,2000,5000,2500,
                     500
                     ]
                temp2=y
                figure = Figure(figsize=(6, 4), dpi=100)
                figure_canvas = FigureCanvasTkAgg(figure, topEnxt)
                NavigationToolbar2Tk(figure_canvas, topEnxt)
                axes = figure.add_subplot()
                axes.plot(dates,y)
                axes.plot(dates, y,linestyle='solid')
                plt.gcf().autofmt_xdate()
                date_format=mpl_dates.DateFormatter('%b,%m,%Y')
                axes.set_title('Covid 19 deaths average per month in India')
                axes.set_ylabel('deaths')
                figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                def stat():
                    nonlocal temp1
                    nonlocal temp2
                    topEst=tk.Toplevel(topE)
                    topEst.geometry("2000x2000")
                    topEst.title("About us")
                    width=2000
                    height=2000
                    image = Image.open("hospital6.png")     
                    resize_image = image.resize((width, height))
                    img = ImageTk.PhotoImage(resize_image)
                    label1 = tk.Label(topEst,image=img)
                    label1.image = img           #add extra stuff in screen
                    label1.pack()
                    st1=st.mean(temp1)   #### case avg
                    st2=st.mean(temp2)
                    lb1=tk.Label(topEst,text="Average Covid case per month:",fg="yellow",
                                 bg="black",font=("Times New Roman",18))
                    lb1.place(x=5,y=100)
                    lbl1=tk.Label(topEst,text=st1,fg="yellow",bg="black",font=("Times New Roman",18))
                    lbl1.place(x=5,y=200)
                    lb2=tk.Label(topEst,text="Average Number of deaths due to covid per month:",
                                 fg="yellow",bg="black",font=("Times New Roman",18))
                    lb2.place(x=5,y=300)
                    lbl2=tk.Label(topEst,text=st2,fg="yellow",bg="black",font=("Times New Roman",18))
                    lbl2.place(x=5,y=300)
                    bt=tk.Button(topEst,text="Close",width=5,height=3,fg="green",bg="white",
                                 font=("Times New Roman",18),command=topEst.destroy())
                    bt.place(x=5,y=500)
                button=tk.Button(topEnxt,text="next",width=5,height=1,bg="green",fg="yellow",
                                 font=("Times New Roman",20),command=lambda:[topEnxt.destroy(),stat()])
                button.place(x=1400,y=600)
            plt.style.use('seaborn')
            topE5=tk.Tk()
            topE5.geometry("2000x2000")
            topE5.title("graph")
            width=2000
            height=2000
            matplotlib.use('TkAgg')
            f = Figure(figsize=(5,5), dpi=100)
            a = f.add_subplot(111)
            dates = [
                datetime(2020, 2, 1),
                datetime(2020, 3, 1),
                datetime(2020, 4, 1),
                datetime(2020, 5, 1),
                datetime(2020, 6, 1),
                datetime(2020, 7, 1),
                datetime(2020, 8, 1),
                datetime(2020, 9, 1),
                datetime(2020, 10, 1),
                datetime(2020, 11, 1),
                datetime(2020, 12, 1),
                datetime(2021, 1, 1),
                datetime(2021, 2, 1),
                datetime(2021, 3, 1),
                datetime(2021, 4, 1),
                datetime(2021, 5, 1),
                datetime(2021, 6, 1),
                datetime(2021, 7, 1),
                datetime(2021, 8, 1),
                datetime(2021, 9, 1),
                datetime(2021, 10, 1),
                datetime(2021, 11, 1),
                datetime(2021, 12, 1),
                datetime(2022, 1, 1),
                datetime(2022, 2, 1),
                datetime(2022, 3, 1),
                datetime(2022, 4, 1),
                datetime(2022, 5, 1),
                datetime(2022, 6, 1),
                datetime(2022, 7, 1),
                datetime(2022, 8, 1),
                datetime(2022, 9, 1),
                datetime(2022, 10, 1),
            ]

            y = [3,20,600,2400,
                 8800,20000,52000,78000,
                 80000,39000,36000,16000,
                 12000,15000,92000,400000,
                 130000,45000,40000,30000,
                 20000,10000,5000,100000,
                 350000,75000,5000,2500,
                 20000,2000,5000,2500,
                 500
                 ]
            temp1=y
            figure = Figure(figsize=(6, 4), dpi=100)
            figure_canvas = FigureCanvasTkAgg(figure, topE5)
            NavigationToolbar2Tk(figure_canvas, topE5)
            axes = figure.add_subplot()
            axes.plot(dates,y)
            axes.plot(dates, y,linestyle='solid')
            plt.gcf().autofmt_xdate()
            date_format=mpl_dates.DateFormatter('%b,%m,%Y')
            axes.set_title('Covid 19 daily case average per month in India')
            axes.set_ylabel('Cases')
            figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            button=tk.Button(topE5,text="next",width=5,height=1,bg="green",fg="yellow",
                             font=("Times New Roman",20),command=lambda:[topE5.destroy(),graphnxt()])
            button.place(x=1400,y=600)
        def faclt():
            fac=tk.Toplevel(topE)
            fac.geometry("2000x2000")
            fac.title("About us")
            width=2000
            height=2000
            image = Image.open("hospital6.png")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(fac,image=img)
            label1.image = img           
            label1.pack()
            def next1():
                fac1=tk.Toplevel(fac)
                fac1.geometry("2000x2000")
                fac1.title("About us")
                width=2000
                height=2000
                image = Image.open("hospital4.jpg")     
                resize_image = image.resize((width, height))
                img = ImageTk.PhotoImage(resize_image)
                label1 = tk.Label(fac1,image=img)
                label1.image = img           
                label1.pack()
                def next2():
                    fac2=tk.Toplevel(fac1)
                    fac2.geometry("2000x2000")
                    fac2.title("About us")
                    width=2000
                    height=2000
                    image = Image.open("hospital18.jpg")     
                    resize_image = image.resize((width, height))
                    img = ImageTk.PhotoImage(resize_image)
                    label1 = tk.Label(fac2,image=img)
                    label1.image = img           
                    label1.pack()
                    b3=tk.Button(fac2,text="Back",width=4,height=4,bg="white",
                                 fg="green",font=("Times New Roman",20),command=fac2.destroy)
                    b3.place(x=700,y=700)
                b2=tk.Button(fac1,text="Next",width=4,height=4,bg="white",
                             fg="green",font=("Times New Roman",20),command=next2)
                b2.place(x=700,y=700)
                b4=tk.Button(fac1,text="Back",width=4,height=4,bg="white",
                             fg="green",font=("Times New Roman",20),command=fac1.destroy)
                b4.place(x=400,y=700)
            b1=tk.Button(fac,text="Next",width=4,height=4,bg="white",
                         fg="green",font=("Times New Roman",20),command=next1)
            b1.place(x=700,y=700)
            b4=tk.Button(fac,text="Back",width=4,height=4,bg="white",
                         fg="green",font=("Times New Roman",20),command=fac.destroy)
            b4.place(x=400,y=700)
        def doc1():
            url="https://www.askapollo.com/physical-appointment"
            wb.open_new_tab(url)
        def fb():
            url="https://www.apollohospitals.com/apollo-hospitals-reviews/"
            wb.open_new_tab(url)
        def awards():
            url="https://www.apollohospitals.com/corporate/awards-accolades/management/"
            wb.open_new_tab(url)
        topE=tk.Toplevel(topA)
        topE.geometry("2000x2000")
        topE.title("About us")
        width=2000
        height=2000
        image = Image.open("hospital6.png")     #add image
        resize_image = image.resize((width, height))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(topE,image=img)
        label1.image = img           #add extra stuff in screen
        label1.pack()
        b1=tk.Button(topE,text="Distinguished doctors",width=20,height=3,
                     bg="white",fg="green",font=("Times New Roman",20),command=doc1)
        b1.place(x=200,y=100)
        b2=tk.Button(topE,text="Awards",width=20,height=3,bg="white",
                     fg="green",font=("Times New Roman",20),command=awards)
        b2.place(x=600,y=100)
        b3=tk.Button(topE,text="Facilities",width=20,height=3,bg="white",
                     fg="green",font=("Times New Roman",20),command=faclt)
        b3.place(x=200,y=500)
        b4=tk.Button(topE,text="People who trust us",width=20,height=3,bg="white",fg="green",font=("Times New Roman",20),command=fb)
        b4.place(x=600,y=500)
        b5=tk.Button(topE,text="Statistics",width=20,height=3,bg="white",
                     fg="green",font=("Times New Roman",20),command=graph)
        b5.place(x=1000,y=500)
    b3=tk.Button(topA,text="About Us",width=10,height=2,bg="yellow",
                 fg="red",font=("Times New Roman",18),command=open5)
    b3.place(x=800,y=400)
    def open6():         
        topF=tk.Toplevel(topA)
        topF.geometry("2000x2000")
        topF.title("My details")
        width=2000
        height=2000
        image = Image.open("hospital7.jpg")     
        resize_image = image.resize((width, height))
        img = ImageTk.PhotoImage(resize_image)
        label1 = tk.Label(topF,image=img)
        label1.image = img           
        label1.pack()
        def histsub():
            global un
            mydb = sql.connect(host='localhost',
                   database='avm',
                   username='root',
                   password='Vishvak03$'
                   )
            cursor=mydb.cursor()
            hd=hist1.get()
            cd=hist2.get()
            alg=hist3.get()
            vc=hist4.get()
            ins="insert into pahistory (username,hd,cd,allergies,vaccine) values (%s,%s,%s,%s,%s)"
            data=(un,hd,cd,alg,vc)
            cursor.execute(ins,data)
            mydb.commit()
            mydb.close()
        def history():
            hist=tk.Toplevel(topF)
            hist.geometry("2000x2000")
            hist.title("My details")
            width=2000
            height=2000
            image = Image.open("hospital7.jpg")     
            resize_image = image.resize((width, height))
            img = ImageTk.PhotoImage(resize_image)
            label1 = tk.Label(hist,image=img)
            label1.image = img           
            label1.pack()
            lbl=tk.Label(hist,text="Enter the following details:",fg="purple",
                         bg="yellow",font=("Times New Roman",32))
            lbl.place(x=5, y=20)
            lbl1=tk.Label(hist,
                          text="If you have any hereditary diesease\nplease enter:",
                          fg="blue",font=("Times New Roman",32))
            lbl1.place(x=5,y=150)
            txtfld1=tk.Entry(hist,bd=5,width=50,textvariable = hist1,font=("Times New Roman",24))
            txtfld1.place(x=650,y=150)
            lbl2=tk.Label(hist,text="If you have any chronic disease\nplease enter:",
                          fg="blue",font=("Times New Roman",32))
            lbl2.place(x=5,y=280)
            txtfld2=tk.Entry(hist,bd=5,width=50,textvariable = hist2,font=("Times New Roman",24))
            txtfld2.place(x=650,y=280)
            lbl3=tk.Label(hist,text="If you have any allergies\nplease Enter:",
                          fg="blue",font=("Times New Roman",32))
            lbl3.place(x=5,y=410)
            txtfld3=tk.Entry(hist,bd=5,width=50,textvariable = hist3,font=("Times New Roman",24))
            txtfld3.place(x=650,y=410)
            lbl4=tk.Label(hist,text="Are you vaccinated for Covid 19?:",
                          fg="blue",font=("Times New Roman",32))
            lbl4.place(x=5,y=540)
            txtfld4=tk.Entry(hist,bd=5,width=50,textvariable = hist4,font=("Times New Roman",24))
            txtfld4.place(x=650,y=540)
            but=tk.Button(hist,
                          text="submit",width=10,height=4,bg="blue",
                          fg="yellow",font=("Times New Roman",32),
                          command=lambda:[histsub(),hist.destroy()])
            but.place(x=750,y=670)
        b1=tk.Button(topF,text="My History",width=20,height=4,bg="blue",
                     fg="yellow",font=("Times New Roman",20),command=history)
        b1.place(x=200,y=100)
        b2=tk.Button(topF,text="Return to Homepage",width=20,height=4,bg="blue",
                     fg="yellow",font=("Times New Roman",20),command=topF.destroy)
        b2.place(x=200,y=600)
    b4=tk.Button(topA,text="My Details",width=10,height=2,bg="yellow",fg="red",
                 font=("Times New Roman",18),command=open6)
    b4.place(x=400,y=400)
    bclose=tk.Button(topA,text="Back",width=10,height=2,bg="yellow",fg="red",
                     font=("Times New Roman",18),command=topA.destroy)
    bclose.place(x=400,y=200)
    topA.mainloop()
def submit2(n):
    global top
    global det
    cond=txtfld4.get()
    c=n.get()
    mydb = sql.connect(host='localhost',
                   database='avm',
                   username='root',
                   password='Vishvak03$'
                   )
    cursor=mydb.cursor()
    cursor.execute("select * from client;")
    data=cursor.fetchall()
    li=data[0]     
    cid=0
    while True:
        cid=random.randint(0,1000)
        if cid in li:
            continue
        else:
            break
    det.append(cid)
    det.append(c)
    det.append(cond)
    mydb.close()
    txtfld4.set("")
def redirect():
    global window
    screen=tk.Toplevel(window)
    screen.geometry("2000x2000")
    width=2000
    height=2000
    screen.title("Redirect page")
    image = Image.open("hospital.png")
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(screen,image=img)
    label1.image = img
    label1.pack()
    label2=tk.Label(screen,
                    text="To browse the facilities of the application, click BROWSE below\n To book appointments, close the applicaion and SIGN IN:",
                    fg="yellow",bg="black",font=("Times New Roman",18))
    label2.place(x=200,y=300)
    bt=tk.Button(screen,text="CLOSE",width=10,height=5,fg="yellow",bg="black",
                 font=("Times New Roman",18),command=window.destroy)
    bt.place(x=500,y=500)
    bt1=tk.Button(screen, text="BROWSE",width=10,height=5,fg="yellow",bg="black",
                  font=("Times New Roman",18),command=open1a)
    bt1.place(x=700,y=500)
def open1b():
    global un
    global top
    un=txtfld2a.get()
    topB=tk.Toplevel(window)
    topB.geometry("2000x2000")
    topB.title("Sign up: page 2")
    width=2000
    height=2000
    image = Image.open("hospital.png")
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(topB,image=img)
    label1.image = img
    label1.pack()
    lbl1=tk.Label(topB,text="Enter medical details:",fg="purple",
                  bg="yellow",font=("Times New Roman",32))
    lbl1.place(x=5, y=20)
    lbl2=tk.Label(topB,text="Gender:",fg="blue",font=("Times New Roman",32))
    lbl2.place(x=5,y=100)
    def sel():
        global det
        s=var1.get()
        selection = "You selected the option " + s
        s=s[0]
        label.config(text = selection)
        det.append(s)
    var1 = tk.StringVar()
    R1 = tk.Radiobutton(topB, text="Male",fg="blue",font=("Times New Roman",24),
                        variable=var1, value="Male",command=sel)
    R1.place(x=340,y=100)
    R2 = tk.Radiobutton(topB, text="Female",fg="blue",font=("Times New Roman",24),
                        variable=var1, value="Female",command=sel)
    R2.place(x=600,y=100)
    label = tk.Label(topB,fg="purple",font=("Times New Roman",18))
    label.place(x=340,y=180)
    lbl3=tk.Label(topB,text="Blood Group:",fg="blue",font=("Times New Roman",32))
    lbl3.place(x=5,y=260)
    n = tk.StringVar() 
    bldg = ttk.Combobox(topB, width = 27, textvariable = n)  
    bldg['values'] = ('A+','O+','B+','AB+','A-','O-','B-','AB-') 
    bldg.place(x=340,y=280)
    lbl4=tk.Label(topB,text="Enter specific \nmedical condition \n(if any):",
                  fg="blue",font=("Times New Roman",32))
    lbl4.place(x=5,y=360)
    txtfld1=tk.Entry(topB,bd=5,width=50,textvariable = txtfld4,
                     font=("Times New Roman",24))
    txtfld1.place(x=340,y=400)
    bt1=tk.Button(topB,
                  text="Confirm",width=10,height=2,fg="black",
                  font=("Times New Roman",14),command=lambda:[redirect(),submit2(n)])
    bt1.place(x=400,y=660)
    bt2=tk.Button(topB,text="Back",width=10,height=2,
                  fg="black",font=("Times New Roman",14),command=topB.destroy)
    bt2.place(x=800,y=660)
    topB.mainloop()
def pwinc():  
    global top
    messagebox.showerror("password incorrect!","Password incorrect! Try again!")
    top.destroy()
def usernotfound():
    global top
    messagebox.askretrycancel("not found","Username not found. Please go SIGN UP")
    top.destroy()
def submit():       
    mydb = sql.connect(host='localhost',
                   database='avm',
                   username='root',
                   password='Vishvak03$'
                   )
    global un
    cursor=mydb.cursor()
    name=txtfl2.get()
    password=txtfl3.get()
    cursor.execute("select * from client;")
    data=cursor.fetchall()
    for i in data:
        if name == i[2]:
            print("Username found")
            if password == i[3]:
                print("logged in successfully")
                un=name
                open1a()
            else:
                print("password incorrect")
                pwinc()
            break
        elif name != i[2]:
            continue
    else:
        print("Username not registered")
        usernotfound()
    mydb.close()
    txtfl2.set("")
    txtfl3.set("")
def open1():#login 
    global top
    top=tk.Toplevel(window)
    top.geometry("2000x2000")
    top.title("Sign in")
    width=2000
    height=2000
    image = Image.open("hospital.png")
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(top,image=img)
    label1.image = img
    label1.pack()
    lbl1=tk.Label(top,text="Enter credentials:",fg="purple",
                  bg="yellow",font=("Times New Roman",32))
    lbl1.place(x=5, y=20)
    lbl2=tk.Label(top,text="Enter Username:",fg="blue",
                  font=("Times New Roman",32))
    lbl2.place(x=5,y=100)
    txtfld2=tk.Entry(top,textvariable = txtfl2,bd=5,width=50,
                     font=("Times New Roman",24))
    txtfld2.place(x=340,y=100)
    lbl3=tk.Label(top,text="Enter Password:",fg="blue",
                  font=("Times New Roman",32))
    lbl3.place(x=5,y=180)
    txtfld3=tk.Entry(top,textvariable = txtfl3,bd=5,width=50,
                     show="*",font=("Times New Roman",24))
    txtfld3.place(x=340,y=180)
    bt1=tk.Button(top,text="Confirm",width=10,height=2,fg="black",
                  font=("Times New Roman",14),command=submit)
    bt1.place(x=340,y=260)
    bt2=tk.Button(top,text="Back",width=10,height=2,fg="black",
                  font=("Times New Roman",14),command=top.destroy)
    bt2.place(x=800,y=260)
    top.mainloop()
def submit1(m):
    global det
    email=txtfld1a.get()
    username=txtfld2a.get()
    password=txtfld3a.get()
    mydb = sql.connect(host='localhost',
                   database='avm',
                   username='root',
                   password='Vishvak03$'
                   )
    cursor=mydb.cursor()
    fname=txtfld4a.get()
    mob=txtfld5a.get()
    city=m.get()
    det.append(email)
    det.append(username)
    det.append(password)
    det.append(fname)
    det.append(mob)
    det.append(city)
    print(det)
    ins="insert into client(cust_id,email_id,username,paswrd,dob,fullname,mob,city,gender,bloodgrp,special) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(det[2],det[5],det[6],det[7],det[0],
          det[8],det[9],det[10],det[1],
          det[3],det[4])
    cursor.execute(ins,data)
    mydb.commit()
    mydb.close()
    txtfld1a.set("")
    txtfld2a.set("")
    txtfld3a.set("")
    txtfld4a.set("")
    txtfld5a.set(0)
def my_upd(cal,l1):              
    global text
    global det
    text=cal.get_date()
    l1.config(text=cal.get_date())
    det.append(text)
def open2():         
    top1=tk.Toplevel(window)
    top1.geometry("2000x2000")
    top1.title("Sign up")
    width=2000
    height=2000
    image = Image.open("hospital.png")
    resize_image = image.resize((width, height))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(top1,image=img)
    label1.image = img
    label1.pack()
    lbl=tk.Label(top1,text="To create an account, enter the following details:",
                 fg="purple",bg="yellow",font=("Times New Roman",32))
    lbl.place(x=5, y=20)
    lbl1=tk.Label(top1,text="Enter Email id:",fg="blue",
                  font=("Times New Roman",32))
    lbl1.place(x=5,y=100)
    txtfld1=tk.Entry(top1,bd=5,width=50,textvariable = txtfld1a,
                     font=("Times New Roman",24))
    txtfld1.place(x=340,y=100)
    lbl2=tk.Label(top1,text="Enter Username:",fg="blue",
                  font=("Times New Roman",32))
    lbl2.place(x=5,y=180)
    txtfld2=tk.Entry(top1,bd=5,width=50,textvariable = txtfld2a,
                     font=("Times New Roman",24))
    txtfld2.place(x=340,y=180)
    lbl3=tk.Label(top1,text="Enter Password:",fg="blue",
                  font=("Times New Roman",32))
    lbl3.place(x=5,y=260)
    txtfld3=tk.Entry(top1,bd=5,width=50,show="*",textvariable = txtfld3a,
                     font=("Times New Roman",24))
    txtfld3.place(x=340,y=260)
    lbl4=tk.Label(top1,text="Enter Date of Birth:",fg="blue",
                  font=("Times New Roman",32))
    lbl4.place(x=5,y=340)
    cal=cale.DateEntry(top1,fg="red",bg="yellow")
    cal.place(x=400,y=360)
    l1=tk.Label(top1,text='data',bg='yellow')  
    l1.place(x=800,y=360) 
    b0=tk.Button(top1,text='Read', command=lambda:my_upd(cal,l1))
    b0.place(x=600,y=360)
    lbl5=tk.Label(top1,text="Enter Full Name:",fg="blue",
                  font=("Times New Roman",32))
    lbl5.place(x=5,y=420)
    txtfld5=tk.Entry(top1,bd=5,width=50,textvariable = txtfld4a,
                     font=("Times New Roman",24))
    txtfld5.place(x=340,y=420)
    lbl6=tk.Label(top1,text="Enter mobile no:",fg="blue",
                  font=("Times New Roman",32))
    lbl6.place(x=5,y=500)
    txtfld6=tk.Entry(top1,bd=5,width=50,textvariable = txtfld5a,
                     font=("Times New Roman",24))
    txtfld6.place(x=340,y=500)
    lbl7=tk.Label(top1,text="Enter city:",fg="blue",
                  font=("Times New Roman",32))
    lbl7.place(x=5,y=580)
    m = tk.StringVar() 
    city= ttk.Combobox(top1, width = 27, textvariable = m) 
    city['values'] = ('Chennai','Mumbai','Delhi',
                      'Bangalore','Kolkata','Hyderabad',
                      'Ahmedabad','Kochin','Pune','Lucknow')  
    city.current()
    city.place(x=340,y=580)
    bt1=tk.Button(top1,text="Next",width=10,height=2,fg="black",
                  font=("Times New Roman",14),
                  command=lambda:[open1b(),submit1(m)])
    bt1.place(x=340,y=660)
    bt2=tk.Button(top1,text="Back",width=10,height=2,fg="black",
                  font=("Times New Roman",14),command=top1.destroy)
    bt2.place(x=800,y=660)
    top1.mainloop()
button=tk.Button(window,text="SIGN IN",width= 25,height=10,
                 fg="green",bg="white",font=("Times New Roman",24),
                 command=open1)
button.place(x=80,y=200)
bt=tk.Button(window,text="SIGN UP",width= 25,height=10,
             fg="green",bg="white",font=("Times New Roman",24),
             command=open2)
bt.place(x=1000,y=200)
window.mainloop()
