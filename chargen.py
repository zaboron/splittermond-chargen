from tkinter import *
import tkinter.messagebox as MessageBox


class App(Toplevel):
    def __init__(self,master):
        super(App, self).__init__(master)#this is Python 3, don't know about Python 2
        self.Rassen = [Rasse('Alb','Ein Elf'),  Rasse('Gnom','Ein Gnom'), Rasse('Varg','Ein Wolf')]
        self.zahl_var = StringVar()#you should google "tkinter variables" if you don't know about these yet
        self.generiereButtons()
        
   
        
    def generiereButtons(self):
        button_frame = LabelFrame(self, text='Click a button!')
        label = Label(button_frame,textvariable = self.zahl_var)
        for element in self.Rassen:  
            Radiobutton(button_frame, text=element.name,  variable=self.zahl_var, value="You selected the option " + element.name,
                     command=self.sel(element, label),indicatoron=0).pack( anchor = W )
        
        label.pack()
        button_frame.pack()
        self.sel(self.Rassen[1],label)
        
    def sel(self, element, label):
        selection = "You selected the option " + element.Beschreibung
        self.zahl_var.set(selection)
        label.config(text = self.zahl_var) 
        MessageBox.showinfo(message='You selected '+selection)
        #root.update_idletasks()

    
class Rasse():
    def __init__(self, name, Beschreibung):
        self.name = name
        self.Beschreibung = Beschreibung
        

if __name__ == '__main__':

    root = Tk()
    app = App(root)
    root.mainloop()





