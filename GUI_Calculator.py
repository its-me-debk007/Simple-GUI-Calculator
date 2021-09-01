from tkinter import *
from math import *

window=Tk()
window.title("Calculator")
window.configure(bg="black")

e = Entry(window, borderwidth=10, width=14, fg="white", bg="black", font=("Arial",20))
e.grid(row=0, column=0, columnspan=4, pady = 1)

flag=0

def click(n):
    global flag
    if flag:
        e.delete(0,END)
        flag=0

    txt=e.get()
    if n=="c":
        if txt!="":
            txt=txt[:-1]
    else:
        txt=e.get()+str(n)
    
    e.delete(0,END)
    e.insert(0,txt)


def power():
    global first_num
    first_num = e.get() + "P"
    e.delete(0,END)


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


def root():
    num=float(e.get())
    e.delete(0,END)
    if num < 0:
        e.insert(0,"Error")
    else:
        ans = sqrt(num)
        if(ans - int(ans) == 0):
            ans = int(ans)
        e.insert(0, ans)
    
    global flag
    flag=1

def absolute():
    num = float(e.get())
    e.delete(0,END)
    
    if num<0:
        num = abs(num)
    else:
        num = -num
    
    if not num - int(num):
        num = int(num)

    e.insert(0, num)

def equal():
    second_num = float(e.get())
    e.delete(0,END)
    num=float(first_num[:-1])

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

    elif first_num[-1] == "P":
        ans = pow(num, second_num)

    if(ans - int(ans) == 0):
        ans = int(ans)

    e.insert(0,ans)
    global flag
    flag=1


bt7=Button(window,text="7",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(7))
bt7.grid(row=2,column=0)
window.bind("7", lambda event: click(7))

bt8=Button(window,text="8",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(8))
bt8.grid(row=2,column=1)
window.bind("8", lambda event: click(8))

bt9=Button(window,text="9",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(9))
bt9.grid(row=2,column=2)
window.bind("9", lambda event: click(9))

bt4=Button(window,text="4",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(4))
bt4.grid(row=3,column=0)
window.bind("4", lambda event: click(4))

bt5=Button(window,text="5",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(5))
bt5.grid(row=3,column=1)
window.bind("5", lambda event: click(5))

bt6=Button(window,text="6",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(6))
bt6.grid(row=3,column=2)
window.bind("6", lambda event: click(6))

bt1=Button(window,text="1",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(1))
bt1.grid(row=4,column=0)
window.bind("1", lambda event: click(1))

bt2=Button(window,text="2",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(2))
bt2.grid(row=4,column=1)
window.bind("2", lambda event: click(2))

bt3=Button(window,text="3",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(3))
bt3.grid(row=4,column=2)
window.bind("3", lambda event: click(3))

bt0=Button(window,text="0",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click(0))
bt0.grid(row=5,column=1)
window.bind("0", lambda event: click(0))

btadd=Button(window,text="+",font=("Arial",20),fg="white",bg="black",width=3,command=add)
btadd.grid(row=4,column=3)
window.bind("+", lambda event: add())

btsub=Button(window,text="-",font=("Arial",20),fg="white",bg="black",width=3,command=sub)
btsub.grid(row=3,column=3)
window.bind("-", lambda event: sub())

btmult=Button(window,text="*",font=("Arial",20),fg="white",bg="black",width=3,command=mult)
btmult.grid(row=2,column=3)
window.bind("*", lambda event: mult())

btdiv=Button(window,text="/",font=("Arial",20),fg="white",bg="black",width=3,command=div)
btdiv.grid(row=1,column=3)
window.bind("/", lambda event: div())

btdot=Button(window,text=".",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click("."))
btdot.grid(row=5,column=0)
window.bind(".", lambda event: click("."))

btroot = Button(window, text="√", font=("Arial",20),command=root,fg="white",bg="black",width=3).grid(row=1,column=0)

btcut=Button(window,text="c",font=("Arial",20),fg="white",bg="black",width=3,command=lambda:click("c") )
btcut.grid(row=1,column=2)
window.bind("<BackSpace>", lambda event: click("c"))

btpow = Button(window, text = "^", font = ("Arial",20), fg = "white", bg = "black",width = 3, command = power)
btpow.grid(row = 1, column = 1)
window.bind("^", lambda event: power())

bteq=Button(window,text="=",font=(" Arial",20),fg="white",bg="black",width=3,command=equal)
window.bind("<Return>", lambda event: equal())
bteq.grid(row=5,column=3)

btabs = Button(window, text = "+/-", fg = "white", bg = "black", font = ("Arial",20), command = absolute, width = 3).grid(row = 5, column = 2)




window.mainloop()
