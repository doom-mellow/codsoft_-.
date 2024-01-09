from tkinter import*

window=Tk()
window.geometry("490x750")
window.title("Calculator By Mahearsh")
window.configure(background="white")
window.iconbitmap(r'calc.ico')


v=StringVar()
v.set("")

e=Entry(window,textvar=v,font="lucida 40 bold")
e.pack(fill=X,ipadx=8,ipady=8,padx=8)


def click(event):
    global v
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if v.get().isdigit():
            value=int(v.get())
        else:
            value=eval(e.get())
        v.set(value)
        e.update()
        pass
    elif text=="C":
        v.set("")
        e.update
        pass
    else:
        v.set(v.get()+text)
        e.update()


f1=Frame(window,bg="white")
b1=Button(f1,text="7",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold ")
b1.bind("<Button-1>",click)
b1.pack(side=LEFT,padx=5,pady=5)
b1=Button(f1,text="8",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b1.bind("<Button-1>",click)
b1.pack(side=LEFT,padx=5,pady=5)
b1=Button(f1,text="9",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b1.bind("<Button-1>",click)
b1.pack(side=LEFT,padx=5,pady=5)
b1=Button(f1,text="+",padx=17,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b1.bind("<Button-1>",click)
b1.pack(side=LEFT,padx=5,pady=5)
f1.pack()



f2=Frame(window,bg="white")
b2=Button(f2,text="4",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b2.bind("<Button-1>",click)
b2.pack(side=LEFT,padx=5,pady=5)
b2=Button(f2,text="5",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b2.bind("<Button-1>",click)
b2.pack(side=LEFT,padx=5,pady=5)
b2=Button(f2,text="6",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b2.bind("<Button-1>",click)
b2.pack(side=LEFT,padx=5,pady=5)
b2=Button(f2,text="-",padx=21,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b2.bind("<Button-1>",click)
b2.pack(side=LEFT,padx=5,pady=5)
f2.pack()



f3=Frame(window,bg="white")
b3=Button(f3,text="1",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b3.bind("<Button-1>",click)
b3.pack(side=LEFT,padx=5,pady=5)
b3=Button(f3,text="2",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b3.bind("<Button-1>",click)
b3.pack(side=LEFT,padx=5,pady=5)
b3=Button(f3,text="3",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b3.bind("<Button-1>",click)
b3.pack(side=LEFT,padx=5,pady=5)
b3=Button(f3,text="*",padx=19,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b3.bind("<Button-1>",click)
b3.pack(side=LEFT,padx=5,pady=5)
f3.pack()



f4=Frame(window,bg="white")
b4=Button(f4,text="C",padx=14,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b4.bind("<Button-1>",click)
b4.pack(side=LEFT,padx=5,pady=5)
b4=Button(f4,text="0",padx=18,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b4.bind("<Button-1>",click)
b4.pack(side=LEFT,padx=5,pady=5)
b4=Button(f4,text="=",padx=17,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b4.bind("<Button-1>",click)
b4.pack(side=LEFT,padx=5,pady=5)
b4=Button(f4,text="/",padx=21,pady=18,bg="#d9d9d9",font="lucida 35 bold")
b4.bind("<Button-1>",click)
b4.pack(side=LEFT,padx=5,pady=5)
f4.pack()



window.mainloop()
