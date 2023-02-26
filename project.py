
# from tkinter import *



# parent = Tk()
# redbutton = Button(parent, text = "Red", fg = "red")  
# redbutton.pack( side = LEFT)  
# greenbutton = Button(parent, text = "Black", fg = "black")  
# greenbutton.pack( side = LEFT )  
# bluebutton = Button(parent, text = "Blue", fg = "blue")  
# bluebutton.pack( side = TOP )  
# blackbutton = Button(parent, text = "Green", fg = "green")  
# blackbutton.pack( side = BOTTOM)  
# parent.mainloop() 



# parent = Tk()
# name = Label(parent,text = "Name").grid(row = 0, column = 0)  
# e1 = Entry(parent).grid(row = 0, column = 1)  
# password = Label(parent,text = "Password").grid(row = 1, column = 0)  
# e2 = Entry(parent).grid(row = 1, column = 1)
# space = Label(parent,text = "              ").grid(row = 2, column = 3) 
# submit = Button(parent, text = "Submit").grid(row = 2, column = 4)  
# space = Label(parent,text = "              ").grid(row = 2, column = 3)
# parent.mainloop()



# top = Tk()
# top.geometry("1000x500")  
# name = Label(top, text = "Name").place(x = 30,y = 50)  
# email = Label(top, text = "Email").place(x = 30, y = 90)  
# password = Label(top, text = "Password").place(x = 30, y = 130)  
# e1 = Entry(top).place(x = 80, y = 50)  
# e2 = Entry(top).place(x = 80, y = 90)  
# e3 = Entry(top).place(x = 95, y = 130)  
# top.mainloop()


# top = Tk()
# top.geometry("200x100")
#
# def fun():
# 	print("hello")
# 	# messagebox.showinfo("Hello", "Red Button clicked")
#
# b1 = Button(top, text="Red", command=fun, activeforeground="red", activebackground="pink", pady=10)
# b2 = Button(top, text="Blue", activeforeground="blue", activebackground="pink", pady=10)
# b3 = Button(top, text="Green", activeforeground="green", activebackground="pink", pady=10)
# b4 = Button(top, text="Yellow", activeforeground="yellow", activebackground="pink", pady=10)
#
# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b3.pack(side=TOP)
# b4.pack(side=BOTTOM)
#
# top.mainloop()


# top = Tk()
# top.geometry("200x200")
#
# checkvar1 = IntVar()
# checkvar2 = IntVar()
# checkvar3 = IntVar()
#
# chkbtn1 = Checkbutton(top, text="C", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)
# chkbtn2 = Checkbutton(top, text="C++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)
# chkbtn3 = Checkbutton(top, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)
#
# chkbtn1.pack()
# chkbtn2.pack()
# chkbtn3.pack()
#
# top.mainloop()


# import tkinter as tk
# from functools import partial
#
#
# def call_result(label_result, n1, n2):
# 	num1 = (n1.get())
# 	num2 = (n2.get())
# 	result = int(num1) + int(num2)
# 	label_result.config(text="Result = %d" % result)
# 	number1.set("")
# 	return
#
#
# root = tk.Tk()
# root.geometry('400x200+100+200')
#
# root.title('Calculator')
#
# number1 = tk.StringVar()
# number2 = tk.StringVar()
#
# labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)
# labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)
# labelResult = tk.Label(root)
# labelResult.grid(row=7, column=2)
#
# entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
# entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
#
# call_result = partial(call_result, labelResult, number1, number2)
#
# buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
#
# root.mainloop()


# from tkinter import *
#
# top = Tk()
#
# top.geometry("200x250")
#
# menubutton = Menubutton(top, text="Language", relief=FLAT)
# menubutton.grid()
# menubutton.menu = Menu(menubutton)
# menubutton["menu"] = menubutton.menu
# menubutton.menu.add_checkbutton(label="Hindi", variable=IntVar())
# menubutton.menu.add_checkbutton(label="English", variable=IntVar())
# menubutton.pack()
#
# top.mainloop()


# from tkinter import *
# from tkinter import messagebox
#
# top = Tk()
# top.geometry("100x100")
# messagebox.askquestion("Confirm", "Are you sure?")
# top.mainloop()


print("dddd")