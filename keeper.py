import csv
import tkinter as tk


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


keeper = Keeper()


root = tk.Tk()
root.title('Password Manager')
root.config(bg='#CCCCCC')

frame = tk.Frame(root).grid(padx=10, pady=10)

tk.Label(root, text="Website/App", bg='#CCCCCC').grid(row=0)
tk.Label(root, text="E-mail address\nor login", bg='#CCCCCC').grid(row=1)
tk.Label(root, text="Password", bg='#CCCCCC').grid(row=2)

source_entry = tk.Entry(root, width=35)
source_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry = tk.Entry(root, width=35)
username_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry = tk.Entry(root, width=35)
password_entry.grid(row=2, column=1, padx=10, pady=10)


save_button = tk.Button(root,
                        text="Save",
                        width=15,
                        command=keeper.addition,
                        bg='#666666',
                        fg='White',
                        activebackground='White',
                        activeforeground='Black').grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

exit_button = tk.Button(root,
                        text="Exit",
                        width=15,
                        command=root.quit,
                        bg='#666666',
                        fg='White',
                        activebackground='White',
                        activeforeground='Black').grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)


root.mainloop()




