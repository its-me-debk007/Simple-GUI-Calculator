from tkinter import *

window=Tk()
window.title("Calculator")
#window.iconbitmap("D:/Calculator_30001.ico")

e = Entry(window,borderwidth=6,width=50)
e.grid(row=0,column=0,columnspan=4)

def click(n):
    txt=e.get()
    if n=="c":
        if txt!="":
            txt=txt[:-1]
    else:
        txt=e.get()+str(n)
    e.delete(0,END)
    e.insert(0,txt)

def add():
    global first_num
    first_num = e.get()+"A"
    e.delete(0,END)

def sub():
    global first_num
    first_num = e.get()+"S"
    e.delete(0,END)

def mult():
    global first_num
    first_num = e.get()+"M"
    e.delete(0,END)

def div():
    global first_num
    first_num = e.get()+"D"
    e.delete(0,END)

def equal():
    second_num = int(e.get())
    e.delete(0,END)
    num=int(first_num[:-1])

    if first_num[-1]=="A":
        ans = num + second_num

    elif first_num[-1]=="S":
        ans = num - second_num

    elif first_num[-1]=="M":
        ans = num * second_num
    
    elif first_num[-1]=="D":
        
        if num%second_num ==0:
            ans=int(num/second_num)
        else:
            ans=num/second_num

    e.insert(0,ans)

bt7=Button(window,text="7",font=("Arial Bold",20),command=lambda:click(7)).grid(row=1,column=0)
bt8=Button(window,text="8",font=("Arial Bold",20),command=lambda:click(8)).grid(row=1,column=1)
bt9=Button(window,text="9",font=("Arial Bold",20),command=lambda:click(9)).grid(row=1,column=2)
bt4=Button(window,text="4",font=("Arial Bold",20),command=lambda:click(4)).grid(row=2,column=0)
bt5=Button(window,text="5",font=("Arial Bold",20),command=lambda:click(5)).grid(row=2,column=1)
bt6=Button(window,text="6",font=("Arial Bold",20),command=lambda:click(6)).grid(row=2,column=2)
bt1=Button(window,text="1",font=("Arial Bold",20),command=lambda:click(1)).grid(row=3,column=0)
bt2=Button(window,text="2",font=("Arial Bold",20),command=lambda:click(2)).grid(row=3,column=1)
bt3=Button(window,text="3",font=("Arial Bold",20),command=lambda:click(3)).grid(row=3,column=2)
bt0=Button(window,text="0",font=("Arial Bold",20),command=lambda:click(0)).grid(row=4,column=1)

btadd=Button(window,text="+",font=("Arial Bold",20),command=add).grid(row=1,column=3)
btsub=Button(window,text="-",font=("Arial Bold",20),command=sub).grid(row=2,column=3)
btmult=Button(window,text="*",font=("Arial Bold",20),command=mult).grid(row=3,column=3)
btdiv=Button(window,text="/",font=("Arial Bold",20),command=div).grid(row=4,column=3)
btdot=Button(window,text=".",font=("Arial Bold",20),command=lambda:click(".")).grid(row=4,column=2)
btcut=Button(window,text="c",font=("Arial Bold",20),command=lambda:click("c") ).grid(row=4,column=0)
bteq=Button(window,text="=",font=("Arial Bold",20),command=equal).grid(row=5,column=0)




window.mainloop()
