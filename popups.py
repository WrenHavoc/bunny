import os
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.withdraw()
bunny_text = str(open("./bunny.txt").read())

for i in range(0,999):
    bunny = tk.Toplevel(root)
    bunny.title("Get Pwned")
    bunny.resizable(False, False)
    ttk.Label(bunny, text=bunny_text, background="#000", foreground="#0f0", font=("Mono")).pack()
    ttk.Button.config(bunny, background="#000", pady=10)
    ttk.Button(bunny, text = " UH OH! ", command = bunny.destroy).pack(side=tk.BOTTOM)

root.mainloop()

