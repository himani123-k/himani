from tkinter import messagebox
from tkinter import Scrollbar
import os
import tkinter as tk

def register_student():
    first_name = fname_var.get()
    last_name = lname_var.get()
    data = first_name + ":" + last_name + "\n"
    f = open("student_data.txt", "a+")
    f.write(data)
    f.close()

    fname_var.set("")
    lname_var.set("")

def fetch_display_from_file():

    f = open("student_data.txt", "a+")
    a = os.path.getsize("student_data.txt")
    f.close()
    if a != 0:
        New_Window = tk.Toplevel()
        New_Window.geometry("400x100+500+200")
        New_Window.title("Student Information")
        scrollbar_v = Scrollbar(New_Window, orient="vertical")
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        txt = tk.Text(New_Window, wrap="none", width=60, height=30,padx=5, pady=5, spacing1=10, spacing2=10, spacing3=10)
        txt["yscrollcommand"] = scrollbar_v
        scrollbar_v.config(command=txt.yview)
        stringdisplay = "%20s"%("First Name") + "%20s" %("Last Name") +"\n"
        txt.insert(tk.INSERT, stringdisplay)
        txt.pack()
        f = open("student_data.txt", "r")
        file_data = f.readlines()
        for data in file_data:
            names = data.strip()
            sep_name = names.split(':');
            NameText = "%20s" %(sep_name[0]) + "%20s" %(sep_name[1]);
            txt.insert(tk.INSERT, (NameText) + "\n")
        New_Window.mainloop()
    else:
        warning = messagebox.showinfo("NO DATA IN FILE", "There is no student registered in the program")

root = tk.Tk()
root.title("Student Record")
root.geometry("300x80+200+200")
fname_var = tk.StringVar()
lname_var = tk.StringVar()
fname_label = tk.Label(root, text='First Name', font=('calibre', 10, 'bold'))
fname_label.grid(row=0, column=0)
fname_entry = tk.Entry(root, textvariable=fname_var, font=('calibre', 10, 'normal'))
fname_entry.grid(row=0, column=1)
lname_label = tk.Label(root, text='Last Name', font=('calibre', 10, 'bold'))
lname_label.grid(row=1, column=0)
lname_entry = tk.Entry(root, textvariable=lname_var, font=('calibre', 10, 'normal'))
lname_entry.grid(row=1, column=1)
submit_btn = tk.Button(root, text='Get Student Information',fg='black', bg="aqua", command=register_student)
submit_btn.grid(row=2, column=0)
display_btn = tk.Button(root, text='Display Student Information',fg='black', bg="aqua", command=fetch_display_from_file)
display_btn.grid(row=2, column=1)

root.mainloop()