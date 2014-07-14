from tkinter import *
from kulturen import *
from rassen import *
from abstammungen import *
from collections import namedtuple
from operator import itemgetter
 
class Paketauswahl():
    def __init__(self, Pakettyp, Pakete):
        self.Auswahl = StringVar()
        self.Auswahl.set(Pakettyp + ' auswählen')
        self.dropdown = OptionMenu(button_frame, self.Auswahl, *sorted(list(Pakete.keys())))
        self.dropdown.pack(side=LEFT)
    
    def erstelleLabel(self):
        self.label = Label(root, textvariable = self.Auswahl)
        self.label.pack(side=LEFT)


root = Tk()
button_frame = LabelFrame(root, text='Pakete auswählen', width = 20)

Rassenpaket = Paketauswahl('Rasse', Rassen)
Kulturpaket = Paketauswahl('Kultur', Kulturen)
Abstammungspaket = Paketauswahl('Abstammung', Abstammungen)

button_frame.pack(side=TOP)

Rassenpaket.erstelleLabel()
Kulturpaket.erstelleLabel()
Abstammungspaket.erstelleLabel()

root.mainloop()