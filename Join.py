import subprocess,os,tkinter
from tkinter.ttk import Label,Button,Entry
def start():
    T.destroy()
    os.chdir(os.getcwd()+'/batch/')
    global IP
    IP=IP.get().replace('tcp://','')
    IP=IP.replace(':',' ')
    cmd=['cmd','/c','telnet '+IP]
    output=subprocess.run(cmd).stdout
T=tkinter.Tk()
T.title('EZNC - Join')
IP=tkinter.StringVar()
a=Label(T,text='Please enter the IP you want to join.')
b=Label(T,text='IP')
c=Entry(T,textvariable=IP)
d=Button(T,text='Start!',command=start)
a.grid(row=0,column=0,columnspan=2)
b.grid(row=1,column=0)
c.grid(row=1,column=1)
d.grid(row=2,column=0)
T.mainloop()