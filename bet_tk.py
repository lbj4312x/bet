import tkinter
from bet import *
import login
root=tkinter.Tk()
g=Game(False,1000)

def dzj():


    def dzj1():
        
        try:
            m=g.game(10,int(e.get()))
        except:
            l1.config(text="请输入数字!")
        if m!=False:
            if m>0:
                l1.config(text="你获得了"+str(m)+"元。")

                l.config(text=g.money)
        elif m==0:
            l1.config(text="你没得钱。")
            l.config(text=g.money)
        else:
            l1.config(text="你没钱了!")
    a=tkinter.Tk()
    tkinter.Label(a,text="金额",font=(None,20)).grid(row=0,column=0)
    e=tkinter.Entry(a,font=(None,20))
    e.grid(row=0,column=1)
    tkinter.Button(a,text="开始",command=dzj1,font=(None,20)).grid(row=1,column=1)
    l1=tkinter.Label(a,font=(None,20),text=" ")
    l1.grid(row=2,column=1)
def lhj():  


    def lhj1():
        
        try:
            m=g.lhj(int(e.get()))
        except:
            l1.config(text="请输入数字!")
        else:
            if m!=False:
                if m>0:
                    l1.config(text="你获得了"+str(m)+"元。")

                    l.config(text=g.money)
                l2.config(text=g.show)
            elif m==0:
                l1.config(text="你没得钱。")
                l.config(text=g.money)
                l2.config(text=g.show)
            else:
                l1.config(text="你没钱了!")
    a=tkinter.Tk()
    tkinter.Label(a,text="金额",font=(None,20)).grid(row=0,column=0)
    e=tkinter.Entry(a,font=(None,20))
    e.grid(row=0,column=1)
    tkinter.Button(a,text="开始",command=lhj1,font=(None,20)).grid(row=1,column=1)
    l1=tkinter.Label(a,font=(None,20),text=" ")
    l1.grid(row=3,column=1)
    l2=tkinter.Label(a,font=(None,20),text=" ")
    l2.grid(row=2,column=1)
tkinter.Label(root,text="剩余资金:",font=(None,20)).pack()
l=tkinter.Label(root,text=g.money,font=(None,20))
l.pack()
tkinter.Button(root,text="弹珠机",command=dzj,font=(None,20)).pack()
tkinter.Button(root,text="老虎机",command=lhj,font=(None,20)).pack()
root.mainloop()
