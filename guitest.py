from tkinter import *
from tkinter import filedialog
from datetime import date

todays_date = date.today().strftime('%Y%m%d')
directory_path = ""

window = Tk()
window.config(padx=20, pady=20)

def open_wow_directory():
    file_path = filedialog.askdirectory()
    wow_directory_entry.insert(END, string=file_path)
    return

def open_backup_directory():
    global directory_path
    directory_path = filedialog.askdirectory()
    backup_directory_entry.delete(0, END)    

    if naming_option.get() == 1:
        backup_directory_entry.insert(END, directory_path+'/'+todays_date)
    elif naming_option.get() == 2:
        custom_name = backup_name_entry.get()
        backup_directory_entry.insert(END, directory_path+'/'+custom_name)
    return

def naming_option_date():
    print("Naming option changed to date: "+todays_date)
#    backup_name_entry.delete(0, END)
    backup_name_entry.config(state=DISABLED)
    backup_directory_entry.delete(0, END)
    backup_directory_entry.insert(END, directory_path+'/'+todays_date)
    return

def naming_option_custom():
    print("Naming option changed to custom: "+backup_name_entry.get())
    backup_name_entry.config(state=NORMAL)
    backup_directory_entry.delete(0, END)
    backup_directory_entry.insert(END, directory_path+'/'+backup_name_entry.get())
    return

def apply_custom_name():
    backup_directory_entry.delete(0, END)
    backup_directory_entry.insert(END, directory_path+'/'+backup_name_entry.get())
    return

window.title('WoW Backup Script')
window.minsize(width=700, height=300)

header = Label(text="World of Warcraft Backup Script v1.0", font=("Arial", 12, "bold"))
header.grid(column=1, row=0, columnspan=4)

author = Label(text="By GibsonSWE")
author.grid(column=1, row=1, columnspan=4)


# WoW Directory

wow_directory_text = Label(text="Game directory:")
wow_directory_text.grid(column=0, row=4, sticky="E")

wow_directory_entry = Entry(width=60)
wow_directory_entry.grid(column=1, row=4, columnspan=4, sticky="W")

wow_browse_button = Button(text="...", command=open_wow_directory)
wow_browse_button.grid(column=5, row=4, sticky="W")


# Backup Directory

backup_directory_text = Label(text="Backup directory:")
backup_directory_text.grid(column=0, row=5, sticky="E")

backup_directory_entry = Entry(width=60)
backup_directory_entry.grid(column=1, row=5, columnspan=4, sticky="W")

backup_browse_button = Button(text="...", command=open_backup_directory)
backup_browse_button.grid(column=5, row=5, sticky="W")


# Backup Naming

naming_option_label = Label(text="Name of Backup:")
naming_option_label.grid(column=0, row=6, sticky="E")

naming_option = IntVar()
naming_option.set(1)
backup_string = StringVar()


backup_name_selector1 = Radiobutton(text="Date:", value=1, variable=naming_option, command=naming_option_date)
backup_name_selector1.grid(column=1, row=6, sticky="W")

date_label = Label(text='../'+todays_date)
date_label.grid(column=2, row=6)

backup_name_selector2 = Radiobutton(text="Custom Name: ../", value=2, variable=naming_option, command=naming_option_custom)
backup_name_selector2.grid(column=3, row=6, sticky="W")

backup_name_entry = Entry(width=20, textvariable=backup_string, state=DISABLED)
backup_name_entry.grid(column=4, row=6, sticky="W")

 
backup_directory_entry.delete(0, END)
backup_directory_entry.insert(END, directory_path+'/'+str(backup_string))
#author.config(text=custom_name)

run = Button(text="Apply", command=apply_custom_name)
run.grid(column=5,row=6)

run = Button(text="BACKUP", font=("Arial", 15, "bold"))
run.grid(column=1,row=10, columnspan=4)

window.mainloop()