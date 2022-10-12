import subprocess,os,tkinter
from tkinter.ttk import Label,Button,Entry
def start():
    T.destroy()
    os.chdir(os.getcwd()+'/batch/')
    os.system('start game "'+ppath.get()+'"')
    cmd=['cmd','/c','ngrok tcp 1000 --authtoken '+token.get()]
    output=subprocess.run(cmd).stdout
T=tkinter.Tk()
T.title('EZ NetCon - Host')
ppath=tkinter.StringVar()
token=tkinter.StringVar()
a=Label(T,text='Please enter your NGROK token and Game Directory')
b=Label(T,text='NGROK Token')
c=Entry(T,textvariable=token,show='*')
d=Label(T,text='Game Dir')
e=Entry(T,textvariable=ppath)
f=Button(T,text='Start!',command=start)
a.grid(row=0,column=0,columnspan=2)
b.grid(row=1,column=0)
c.grid(row=1,column=1)
d.grid(row=2,column=0)
e.grid(row=2,column=1)
f.grid(row=3,column=0)
T.mainloop()