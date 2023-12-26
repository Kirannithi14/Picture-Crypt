from tkinter import * 
import tkinter.font as tkFont
import tkinter as tk

ws = Tk()
width= ws.winfo_screenwidth()
height= ws.winfo_screenheight()
ws.geometry("%dx%d" % (width, height))
ws.title('PythonGuides')
f = tkFont.Font ( family="Helvetica",size=24,weight="bold")
bckpath=r"C:\Users\GF\Downloads\sam.png"
bckimg=tk.PhotoImage(file=bckpath)
#print(width,height)
b_lbl=tk.Label(ws,image=bckimg)
b_lbl.place(x=0,y=0,relwidth=1,relheight=1)
def nextPage():
    ws.destroy()
    import first_page
    

def prevPage():
    ws.destroy()
    import second_page
    
Label(
    ws,
    text="AES Encryption",
    
    font=f,justify=CENTER,borderwidth=4,relief="solid",bg="grey",fg="#041016"
).place(x=630,y=80)
f2 = tkFont.Font( family = "Comic Sans MS", 
                                 size = 20, 
                                 weight = "bold",slant='italic')
f3=tkFont.Font(family="Arial",size=20)

Label(ws,text="Presented by",font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=730,y=540)
Label(ws,text='1.   Bharanidharan K(811721104019)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=630,y=590)
Label(ws,text='2.   Elayaraja R(811721104028)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=630,y=630)
Label(ws,text='3.   Kartheeban N(811721104044)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=630,y=670)
Label(ws,text='3.   Kirannithi R(811721104052)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=630,y=710)



Button(
    ws, 
    text="Image_Embedding", 
    font=f,borderwidth=4,relief="solid",bg="grey",fg="#041016",activeforeground='red',
    command=nextPage
    ).pack( expand =True,side=LEFT)

Button(
    ws, 
    text="Image_Detecting", 
    font=f,
    width=15 ,borderwidth=4,relief="solid",bg="grey",fg="#041016",activeforeground='red',
    command=prevPage
    ).pack(expand=TRUE, side=LEFT)
ws.configure()
ws.mainloop()
