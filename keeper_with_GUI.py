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

        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')
        self.root.title('Password Manager')
        self.root.config(bg='#CCCCCC')

        self.frame = tk.Frame(self.root)
        self.frame.grid(padx=10, pady=10)

        tk.Label(self.root, text="Website/App", bg='#CCCCCC').grid(row=0)
        tk.Label(self.root, text="E-mail address\nor login", bg='#CCCCCC').grid(row=1)
        tk.Label(self.root, text="Password", bg='#CCCCCC').grid(row=2)

        self.source_entry = tk.Entry(self.root, width=40)
        self.source_entry.focus()
        self.source_entry.grid(row=0, column=1, padx=10, pady=10)
        self.username_entry = tk.Entry(self.root, width=40)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root, width=40)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.export_button = tk.Button(self.root,
                                       text="Export to database",
                                       command=self.on_export,
                                       width=15,
                                       bg='#666666',
                                       fg='White',
                                       activebackground='White',
                                       activeforeground='Black'
                                       )
        self.export_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.exit_button = tk.Button(self.root,
                                     text="Exit",
                                     width=15,
                                     command=self.root.quit,
                                     bg='#666666',
                                     fg='White',
                                     activebackground='White',
                                     activeforeground='Black')
        self.exit_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

        self.save_button = tk.Button(self.root,
                                     text="Save",
                                     width=15,
                                     command=self.input_validation,
                                     bg='#666666',
                                     fg='White',
                                     activebackground='White',
                                     activeforeground='Black')
        self.save_button.grid(row=3, column=0, padx=5, pady=5)

        self.root.mainloop()

    def store_values(self):
        self.source = self.source_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        return [self.source, self.username, self.password]

    def add_data(self):
        self.__passes.append(self.store_values())
        return self.__passes

    def clear_entries(self):
        self.source_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.source_entry.focus()

    def addition(self):
        self.__passes = []
        self.add_data()
        with open('passes.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.__passes)
        tk_mess.showinfo("Info", "Data saved.")
        self.clear_entries()

    def input_validation(self):
        for index, entry in enumerate(self.store_values(), start=1):
            if ' ' in entry and len(entry) > 0:
                tk_mess.showerror('Incorrect character', f'Space char is not allowed!\nRemove it from field {index}.')
                raise ValueError("Space char in input.")
        if not all(self.store_values()):
            tk_mess.showerror('Missing data!', 'Fields can\'t be empty!')
        else:
            self.addition()

    def on_export(self):
        if os.stat('passes.csv').st_size > 0:
            db_creator.export_to_db()
            tk_mess.showinfo("Success!", f"Data successfully exported to database!")
            with open('passes.csv', 'w'):
                pass
        else:
            tk_mess.showwarning('File error', 'File is empty. There is no data to export to database.')
            raise FileEmpty("Empty file.")
        self.clear_entries()


keeper = Keeper()
