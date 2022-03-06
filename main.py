from tkinter import *

def submit():
    print("A Temperatura é de: "+str(scale.get())+ " graus C")

#Testing branches
#2022/03
window = Tk()
#window.geometry("420x420")
window.title("A minha primeira Janela Python")

icon = PhotoImage(file='estrela.png')
window.iconphoto(True,icon)
window.config(bg="white")

scale =Scale(window,
             from_=100,
             to=0,
             length=600,
             orient=VERTICAL,
             font=('Consolas',20),
             tickinterval=10,
             showvalue=0,
             resolution=2)
scale.pack()

button=Button(window,text="submit",command=submit)
button.pack()

window.mainloop()