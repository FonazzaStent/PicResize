"""PicResize 1.0.2 - A simple image resizer
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import sys
import os
from tkinter import simpledialog
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image

def init():
    global setdimflag
    setdimflag=False

def create_window():
    global width_entry
    global height_entry
    global resize_button
    global root
    global top
    global im
    global ratiow
    global ratioh
    global widthvar
    global heightvar
    global imgfile

    imgfile=str(sys.argv[1])
    #print (imgfile)
    im=Image.open(imgfile)
    w,h=im.size
    ratiow=h/w
    ratioh=w/h

    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TpVKqghYUcchQneyiIo6likWwUNoKrTqYXPohNGlIUlwcBdeCgx+LVQcXZ10dXAVB8APE1cVJ0UVK/F9SaBHjwXE/3t173L0DhEaFqWZXDFA1y0gn4mIuvyIGXhFAH4IYwJDETD2ZWcjCc3zdw8fXuyjP8j735+hVCiYDfCJxjOmGRbxOPLNp6Zz3icOsLCnE58QTBl2Q+JHrsstvnEsOCzwzbGTTc8RhYrHUwXIHs7KhEk8TRxRVo3wh57LCeYuzWqmx1j35C0MFbTnDdZqjSGARSaQgQkYNG6jAQpRWjRQTadqPe/hHHH+KXDK5NsDIMY8qVEiOH/wPfndrFqcm3aRQHOh+se2PMSCwCzTrtv19bNvNE8D/DFxpbX+1Acx+kl5va5EjoH8buLhua/IecLkDDD/pkiE5kp+mUCwC72f0TXlg8BYIrrq9tfZx+gBkqaulG+DgEBgvUfaax7t7Onv790yrvx9vNXKlrv1EmQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+cHDgoYFu4ygmcAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAADTUlEQVRIx41WvW4cNxD+vjlyJUCJEJfyGaqsh7H1AvEL5ABVgt5D5QE+V/4p9TYSnDQCYhtQ4QgqEivNkdxxQS6X3J+DptjlcocznG9+GYIHiJoUYHw8gXbzyeivIkmfFNWvFQooqPPSlYCMTrJ7stvXKTUk5m9SsEohdEys/3KKmcUNBhciOgVPJx2cH5hVeCSxmYG3jIk79H47ZRkVY9BZ66jUlxbQdtIBtaaZQY0TwqcDAQAQOiKFJIUSF+TNzY1QMlEWIuWnkGlRbVNEGEJoQwghSGGTAjHq0i0+vP9QwhEjpvQAO2y6Hwk/1cKWbMH19TVrCvkakdow3AkhBD/4Xq/XpITg46/eBycnJyV06/W6isA+CHUmizXaZY0B+0ySHHkHBwevX71yPtFqtYpH9vb3NpvNzkQp1grT2CIhiGxj9FFeZx8KRSiXl5dDrGZos3lLkSS2DYIhEADUua13zvutc+7Pvz6DOD8/B/Dl7y8T7ACZahMA70MJoYDKPhxQFKJktffBOQfQGPvy5GVmOj09vbi4SOlqrG1MnWPMeeBLWOYMTzlCISW04eHhIUba4+P/t7e3GdAYRSLiO7GmcpROeVGxXC6V9M6lyy7M2827s7Ozb9++Hv76i/PeOWcb65xLdVzTSQXNAMpxcbu/v//+z3e3dXHDB2cWZrX6w3sH0FprjPXel0KY6gljP9AeONVxEB4dPf/08RPZAxvFWdsAcM6Rte0K7Yuu9h1Niy6SWa2xJN68+X1Qrb33qnj227Ooo4TXWFMEGmWIT/HTGqvQGEI68o3z7sfj49XVVd8eAQBNY4s4LPqBan9BAgp13u2oyiR88F2dq1Jai01TtZDubYyNVZVQBZleGg+zmzj6IjoKj8gL0HTStXxsveOTBxOMigETQlVPZh5XWIpjHb7USVU6/2nyBWOwvVguF4vF8fHx4eGhtVZVW9ViCNP//v3RtqHZawBxbtu2LUkFzGKxv79vjbm7uytDgiGk2mStrfq2Fsh2kJdwMs9Eqiw4I28OkF5BL2ZqmMh262hc2e0eGU07mBrodC5eOVvFsgKi9itnJrgdo0qd/bUyKerPVCuBjttigdakJu6YrqdGuWmo+glsXIPLEz8BhZUtlEFRgV8AAAAASUVORK5CYII='


    root= tk.Tk()
    top= root
    top.geometry("300x150")
    top.resizable(1,1)
    top.title("Image Resize")

    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

    widthvar=StringVar()
    width_label=Label(top,justify="right")
    width_label.place(x=15,y=15,width=50,height=30)
    width_label.configure(text="Width")

    heightvar=StringVar()    
    height_label=Label(top,justify="right")
    height_label.place(x=15,y=55,width=50,height=30)
    height_label.configure(text="Height")

    width_entry=Entry(top, textvariable=widthvar)
    width_entry.place(x=65,y=15,width=180,height=30)
    width_entry.bind("<Return>",widthset)
    width_entry.focus() 

    height_entry=Entry(top,textvariable=heightvar)
    height_entry.place(x=65, y=55,width=180,height=30)
    height_entry.bind("<Return>",heightset)
    

    resize_button=Button(top)
    resize_button.place(x=125,y=95,width=50,height=30)
    resize_button.configure(text="Resize")
    resize_button.bind ("<Button-1>",resize)

    set_height_button=Button(top)
    set_height_button.place(x=255,y=55,width=30,height=30)
    set_height_button.configure(text="Set")
    set_height_button.bind ("<Button-1>",heightset)

    set_width_button=Button(top)
    set_width_button.place(x=255,y=15,width=30,height=30)
    set_width_button.configure(text="Set")
    set_width_button.bind ("<Button-1>",widthset)

def widthset(event):
    global setdimflag
    global width
    global height
    width=width_entry.get()
    #print (width)
    if width!='' and width.isdigit()==True:
        #print ('ok')
        width=int(width)
        height=int(width*ratiow)
        if height<1:
            height=1    
        heightvar.set(height)
        height_entry.configure(text=heightvar)
        setdimflag=True

def heightset(event):
    global setdimflag
    global height
    global width
    height=height_entry.get()
    #print (height)
    if height!='' and height.isdigit()==True:
        height=int(height)
        width=int(height*ratioh)
        if width<1:
            width=1
        widthvar.set(width)
        width_entry.configure(text=widthvar)
        setdimflag=True

def resize(event):
    global setdimflag
    global imgfile
    global width
    global height
    #print (setdimflag)
    if setdimflag==True:    
        im2=im.resize((width,height),Image.Resampling.BICUBIC)
        imgfile=os.path.splitext(imgfile)[0]
        filename=imgfile+" "+str(width)+"x"+str(height)+".png"
        im2.save(filename)
        
init()
create_window()
root.mainloop()
