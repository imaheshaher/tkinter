from tkinter import *
import string
import time
tasks=[]
class App:
    def __init__(self,master):
        def listtodo():
            tasks=[]
            for todo in tasks:
                data=todo
                todolist.insert(END,data)

        listtodo()

window=Tk()
window.title("todo list")
window.geometry("409x566")
window.resizable(False,False)
todolist=Listbox(width=50,height=30)
todolist.grid(row=0,column=0,columnspan=2,sticky="we")
add=Button(text="add",command = lambda : addfun(addtextbox.get()))
add.grid(row=1,column=0,sticky="we")
delete=Button(text="delete",command =lambda : deletefunc(todolist))
delete.grid(row=1,column=1,sticky="we")

addtextbox=Entry()
addtextbox.grid(row=2,column=0,columnspan=2,sticky="we")
addtextbox.focus()

def listtodo():
    
    for todo in tasks:
        data=todo
        todolist.insert(END,data)

def addfun(i):
    todolist.delete(0,END)
    addtextbox.delete(0,'end')
    if i:
        addtodo=tasks.append(i)
    print(tasks)
    listtodo()
window.bind('<Return>',lambda i: addfun(addtextbox.get()))
def deletefunc(l):
    selection=l.curselection()
    if selection:
        idfirst=l.get(selection)
        id=tasks.index(idfirst)
        del[tasks[id]]
        l.delete(selection)


app=App(window)

mainloop()
