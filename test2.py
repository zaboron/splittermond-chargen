from tkinter import *

from collections import namedtuple
from operator import itemgetter

Rasse = namedtuple('Rasse', 'name Beschreibung')
Rassen = [Rasse('Alb','Ein Elf'),  Rasse('Gnom','Ein Gnom'), Rasse('Varg','Ein Wolf'), Rasse('Mensch','Ein Mensch')]


Kultur = namedtuple('Kultur', 'name Beschreibung')
Kulturen = [Kultur('Zwingard','Ein Zwingarder'),  Kultur('Seealb','Ein Seealb')]

class App(Frame): # an extended Frame
    def __init__(self, parent=None):
        Frame.__init__(self, parent) # do superclass )
        self.pack()
        self.data = 42

    

class RadioSelektion(App):
    def __init__(self, entries, parent=None):
        App.__init__(self, parent)
        self.zahl_var = StringVar() #you should google "tkinter variables" if you don't know about these yet
        self.zahl_var.set("You selected the option " + Rassen[0].Beschreibung)
        self.buttonwidth = max(len(entry.name) for entry in entries)
        self.generiereButtons(entries)
        self.make_widgets() # attach widgets to self
        
    def make_widgets(self):
        widget = Button(self, text='Next', command=self.message)
        widget.pack(side=LEFT)
        
    def message(self):
        self.master.withdraw()
   
    def generiereButtons(self,entries):
        button_frame = LabelFrame(self, text='Click a button!', width = 20)
        label = Label(button_frame,textvariable = self.zahl_var)
        for element in entries:  
            OptionMenu(button_frame, text=element.name,  variable=self.zahl_var, value="You selected the option " + element.Beschreibung,
                     command=self.sel,indicatoron=0, width = self.buttonwidth).pack( anchor = W )
        label.pack()
        button_frame.pack()
        self.sel()
        
    def sel(self):
        selection = self.zahl_var.get()
        #root.update_idletasks()  
        
class test(App):
    def __init__(self, parent=None):
        App.__init__(self, parent)
        
    def make_widgets(self):
        widget = Button(self, text='Next', command=self.message)
        widget.pack(side=LEFT)
        
    def message(self):
        self.master.withdraw()
   
    def generiereButtons(self,entries):
        button_frame = LabelFrame(self, text='Click a button!', width = 20)
        label = Label(button_frame,textvariable = self.zahl_var)
        for element in entries:  
            OptionMenu(button_frame, text=element.name,  variable=self.zahl_var, value="You selected the option " + element.Beschreibung,
                     command=self.sel,indicatoron=0, width = self.buttonwidth).pack( anchor = W )
        label.pack()
        button_frame.pack()
        self.sel()
        
    def sel(self):
        selection = self.zahl_var.get()
        #root.update_idletasks()  
    

if __name__ == '__main__': RadioSelektion(Rassen).mainloop()