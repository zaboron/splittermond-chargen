from tkinter import *
import tkinter.messagebox as MessageBox
from collections import namedtuple
from operator import itemgetter

Rasse = namedtuple('Rasse', 'name Beschreibung')
Rassen = [Rasse('Alb','Ein Elf'),  Rasse('Gnom','Ein Gnom'), Rasse('Varg','Ein Wolf'), Rasse('Mensch','Ein Mensch')]

class App(Toplevel):
    def __init__(self,master, entries):
        super(App, self).__init__(master)#this is Python 3, don't know about Python 2
        self.entries = entries
        self.zahl_var = StringVar() #you should google "tkinter variables" if you don't know about these yet
        self.zahl_var.set("You selected the option " + self.entries[0].Beschreibung)
        self.buttonwidth = max(len(entry.name) for entry in entries)
        self.generiereButtons()
   
        
    def generiereButtons(self):
        button_frame = LabelFrame(self, text='Click a button!')
        label = Label(button_frame,textvariable = self.zahl_var)
        for element in self.entries:  
            Radiobutton(button_frame, text=element.name,  variable=self.zahl_var, value="You selected the option " + element.Beschreibung,
                     command=self.sel(),indicatoron=0, width = self.buttonwidth).pack( anchor = W )
        label.pack()
        button_frame.pack()
        self.sel()
        
    def sel(self):
        selection = self.zahl_var.get()
        #root.update_idletasks()
        
class Rasse(App):
     def sel(self):
        selection = self.zahl_var.get()
        #root.update_idletasks()
    
        

if __name__ == '__main__':

    root = Tk()
    app = App(root, Rassen)
    root.mainloop()





