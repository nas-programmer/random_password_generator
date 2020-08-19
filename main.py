import random
from pyperclip import copy
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Entry, Canvas, IntVar, Radiobutton, PhotoImage, END
from tkinter.ttk import Combobox

#colors
color = '#00b894'
fg = '#dfe6e9'
color2 = '#55efc4'

#Images


#GUI Window
root = Tk()
root.title('Password Generator')
root.geometry("640x480+500+100")
root.config(borderwidth = 0)
p1 = PhotoImage(file = 'Images/5.png') 
root.iconphoto(False, p1)
root.resizable(height = False, width = False)

#Vars
var = IntVar() 
var1 = IntVar() 

#BackGround
bg = Image.open('Images/2.png')
photoBg = ImageTk.PhotoImage(bg)
labelBg = Label(root, bg= '#00060a', bd=0, highlightthickness=0, width= 640, height= 480)
labelBg.pack()

#Logo
logo= Image.open('Images/3.png')
photoLogo = ImageTk.PhotoImage(logo)
labelLogo = Label(root, image= photoLogo, bd=0, highlightthickness=0)
labelLogo.place(x= 256, y= 30)

#Options
radio_low = Radiobutton(root, text="Only LowerCase", variable=var, value=1, bg= '#00060a', fg= fg, activebackground= '#00060a', activeforeground= fg) 
radio_low.place(x= 105, y= 122)
radio_middle = Radiobutton(root, text="Only UpperCase", variable=var, value=0, bg= '#00060a', fg= fg, activebackground= '#00060a', activeforeground= fg) 
radio_middle.place(x= 105, y= 144)
radio_strong = Radiobutton(root, text="LowerCase and UpperCase", variable=var, value=3, bg= '#00060a', fg= fg, activebackground= '#00060a', activeforeground= fg) 
radio_strong.place(x= 105, y= 165)
radio_middle = Radiobutton(root, text="LowerCase, UpperCase and Special Characters", variable=var, value=4, bg= '#00060a', fg= fg, activebackground= '#00060a', activeforeground= fg) 
radio_middle.place(x= 105, y= 186)
radio_strong = Radiobutton(root, text="LowerCase, UpperCase, Special Characters and Numbers", variable=var, value=5, bg= '#00060a', fg= fg, activebackground= '#00060a', activeforeground= fg) 
radio_strong.place(x= 105, y= 208)



#Length
c_label = Label(root, text="Length:", bg= '#00060a', fg= fg) 
c_label.place(x=270, y= 250)
combo = Combobox(root, textvariable=var1, width= 5) 
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.place(x=320, y= 250)

#Password
r_pwd = Label(root, text= 'Password:', fg= fg, bd=0, highlightthickness=0, bg= '#00060a')
r_pwd.place(x= 155, y= 300)
entry = Entry(labelBg, bg= '#636e72') 
entry.place(x=250, y= 296) 

#Random Password Generator Function
def rnd_pwd():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz "
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    upper_lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    spl = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !@#$%^&*()"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    if var.get() == 1:
        for i in range(length):
            password += random.choice(lower)
        return password
    elif var.get() == 0:
        for i in range(length):
            password += random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(length):
            password += random.choice(upper_lower)
        return password
    elif var.get() == 4:
        for i in range(length):
            password += random.choice(spl)
        return password
    elif var.get() == 5:
        for i in range(length):
            password += random.choice(digits)
        return password
    else:
        print("Select an option")
    
# Function for generation of password
def generate():
	password1 = rnd_pwd()
	entry.insert(10, password1)

# Function for copying password to clipboard
def copy1():
	random_password = entry.get()
	copy(random_password)

#Buttons
cpy_btn = Button(labelBg, text="Copy to Clipboard", bg= color, activebackground= color2, borderwidth=0, command=copy1) 
cpy_btn.place(x= 105, y= 368) 
gnrt_btn = Button(labelBg, text="Generate Password", bg= color, activebackground= color2, borderwidth=0, command=generate) 
gnrt_btn.place(x= 418, y= 368)

root.mainloop()


