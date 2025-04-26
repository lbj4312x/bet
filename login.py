import tkinter
import bet
import json
import os
username = os.getlogin()
try:
    os.mkdir(r"C:\Users\{}\AppData\Local\bet".format(username))
except:
    pass
root=tkinter.Tk()
def login():
    global b
    global a
    name=e.get()
    password=e1.get()
    if b==0:
        l=[name,password,1000]
        with open(r"C:\Users\{}\AppData\Local\bet\user.txt".format(username),"w") as f:
            json.dump(l,f)
        root.destroy()
    else:
        if a[0]==name and a[1]==password:
            root.destroy()
try:
    with open(r"C:\Users\{}\AppData\Local\bet\user.txt".format(username)) as f:
        a=json.load(f)
    b=1
except:
    b=0
if b==0:
    tkinter.Label(root,text="注册",font=(None,20)).grid(row=0,column=0)
    
else:
    tkinter.Label(root,text="登录",font=(None,20)).grid(row=0,column=0)
tkinter.Label(root,text="用户名",font=(None,20)).grid(row=1,column=0)
e=tkinter.Entry(root,font=(None,20))
e.grid(row=1,column=1)
tkinter.Label(root,text="密码",font=(None,20)).grid(row=2,column=0)
e1=tkinter.Entry(root,font=(None,20))
e1.grid(row=2,column=1)
button=tkinter.Button(root,text="确定",command=login,font=(None,20)).grid(row=3,column=0)
root.mainloop()
