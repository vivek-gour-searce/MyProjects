__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2013, Searce'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Vivek.Gour@searce.com'
__status__ = 'Development'

import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()