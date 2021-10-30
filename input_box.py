import tkinter as tk


def write_slogan():
    print(__name__)


root = tk.Tk()

frame = tk.Frame(root)

tk.Label(root, text="Website/App").grid(row=0, padx=10)
tk.Label(root, text="e-mail address/login").grid(row=1, padx=10)
tk.Label(root, text="password").grid(row=2, padx=10)

e1 = tk.Entry(root, width=35)
e2 = tk.Entry(root, width=35)
e3 = tk.Entry(root, width=35)

e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)
e3.grid(row=2, column=1, padx=10, pady=10)

exit_button = tk.Button(root,
                        text="Exit",
                        width=15,
                        command=root.quit).grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
save_button = tk.Button(root,
                        text="Save",
                        width=15,
                        command=write_slogan).grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

root.mainloop()
