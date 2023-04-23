from copy import copy
from struct import pack
from tokenize import String
import pyshorteners
from tkinter import *

#GUI
root = Tk()
root.geometry("600x300")
root.title("URL Shortner Application")
root.configure(bg="aqua")

#Define Variable for url
urlmain = StringVar()
urlshortmain = StringVar()


#Define Function
def urlShortner():
    urladdress = urlmain.get()
    urlshort = pyshorteners.Shortener().tinyurl.short(urladdress)
    urlshortmain.set(urlshort)



Label(root,text="URL Shortner App",font=('Serif 16 bold')).pack(pady=10)
Entry(root,textvariable=urlmain,width=50,font=('Serif 14')).pack(padx=10, pady=10)
Button(root,text="Generate Short URL",font=('Serif 11 bold'),command=urlShortner).pack(pady=7)
Entry(root,textvariable=urlshortmain,width=50,font=('Serif 14')).pack(padx=10, pady=10)
Label(root, text="Copy & Paste in Browser", font="Serif 12" ).pack(pady=10)


root.mainloop()