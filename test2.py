from tkinter import *
import tkinter.messagebox as MessageBox

class App(Toplevel):

    def __init__(self,master):
        super(App, self).__init__(master)#this is Python 3, don't know about Python 2
        self.elements = [Zahl('Eins','Eine Eins'), Zahl('Zwei','Eine Zwei'), Zahl('Drei','Eine Drei')]
        self.zahl_var = StringVar()#you should google "tkinter variables" if you don't know about these yet
        self.generiereButtons()

    def generiereButtons(self):
        button_frame = LabelFrame(self, text='Click a button!')
        for element in self.elements:
            r = Radiobutton(button_frame, text=element.name, variable=self.zahl_var, value=element.Beschreibung, command=self.show_selection)
            r.pack()
        button_frame.pack()

    def show_selection(self):
        selection = self.zahl_var.get()
        MessageBox.showinfo(message='You selected '+selection)


class Zahl():
    def __init__(self, name, Beschreibung):
        self.name = name
        self.Beschreibung = Beschreibung


if __name__ == '__main__':

    root = Tk()
    app = App(root)
    root.mainloop()