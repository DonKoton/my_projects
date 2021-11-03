import os
import csv
import tkinter as tk
import tkinter.messagebox as tk_mess
import db_creator


class FileEmpty(Exception):
    pass


class Keeper:
    def __init__(self):
        self.__passes = None
        self.source = None
        self.username = None
        self.password = None

    def store_values(self):
        self.source = source_entry.get()
        self.username = username_entry.get()
        self.password = password_entry.get()
        return [self.source, self.username, self.password]

    def add_data(self):
        self.__passes.append(self.store_values())
        return self.__passes

    def addition(self):
        self.__passes = []
        self.add_data()
        with open('passes.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.__passes)
        tk_mess.showinfo("Info", "Data saved.")
        clear_entries()


keeper = Keeper()


root = tk.Tk()
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.title('Password Manager')
root.config(bg='#CCCCCC')

frame = tk.Frame(root).grid(padx=10, pady=10)

tk.Label(root, text="Website/App", bg='#CCCCCC').grid(row=0)
tk.Label(root, text="E-mail address\nor login", bg='#CCCCCC').grid(row=1)
tk.Label(root, text="Password", bg='#CCCCCC').grid(row=2)

source_entry = tk.Entry(root, width=40)
source_entry.focus()
source_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry = tk.Entry(root, width=40)
username_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry = tk.Entry(root, width=40)
password_entry.grid(row=2, column=1, padx=10, pady=10)


def clear_entries():
    source_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    source_entry.focus()


def input_validation():
    entries = keeper.store_values()
    for index, entry in enumerate(entries, start=1):
        if ' ' in entry and len(entry) > 0:
            tk_mess.showerror('Incorrect character', f'Space char is not allowed!\nRemove it from field {index}.')
            raise ValueError("Space char in input.")
    if not all(entries):
        tk_mess.showerror('Missing data!', 'Fields can\'t be empty!')
    else:
        keeper.addition()


save_button = tk.Button(root,
                        text="Save",
                        width=15,
                        command=input_validation,
                        bg='#666666',
                        fg='White',
                        activebackground='White',
                        activeforeground='Black').grid(row=3, column=0, padx=5, pady=5)


def on_export():
    if os.stat('passes.csv').st_size > 0:
        db_creator.export_to_db()
        tk_mess.showinfo("Success!", f"Data successfully exported to database!")
        with open('passes.csv', 'w'):
            pass
    else:
        tk_mess.showwarning('File error', 'File is empty. There is no data to export to database.')
        raise FileEmpty("Empty file.")
    clear_entries()


export_button = tk.Button(root,
                          text="Export to database",
                          command=on_export,
                          width=15,
                          bg='#666666',
                          fg='White',
                          activebackground='White',
                          activeforeground='Black'
                          ).grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

exit_button = tk.Button(root,
                        text="Exit",
                        width=15,
                        command=root.quit,
                        bg='#666666',
                        fg='White',
                        activebackground='White',
                        activeforeground='Black').grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)


root.mainloop()
