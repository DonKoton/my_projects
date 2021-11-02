import csv
import tkinter as tk
import tkinter.messagebox as tk_mess


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
        with open('passes.csv', 'w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.__passes)
        tk_mess.showinfo("Info", "Data saved.")


keeper = Keeper()


root = tk.Tk()
root.title('Password Manager')
root.config(bg='#CCCCCC')

frame = tk.Frame(root).grid(padx=10, pady=10)

tk.Label(root, text="Website/App", bg='#CCCCCC').grid(row=0)
tk.Label(root, text="E-mail address\nor login", bg='#CCCCCC').grid(row=1)
tk.Label(root, text="Password", bg='#CCCCCC').grid(row=2)

source_entry = tk.Entry(root, width=40)
source_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry = tk.Entry(root, width=40)
username_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry = tk.Entry(root, width=40)
password_entry.grid(row=2, column=1, padx=10, pady=10)


save_button = tk.Button(root,
                        text="Save",
                        width=15,
                        command=keeper.addition,
                        bg='#666666',
                        fg='White',
                        activebackground='White',
                        activeforeground='Black').grid(row=3, column=0, padx=5, pady=5)


def on_export():
    tk_mess.showinfo("Success!", "Data successfully exported to database!")


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




