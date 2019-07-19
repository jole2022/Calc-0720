import tkinter
from tkinter import ttk

root = tkinter.Tk()
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0)

CE_button = ttk.Button(main_frame, text="CE")
CE_button.grid(row=1, column=0, padx=5, pady=5)

for i in range(3):
    for j in range(3):
        button = ttk.Button(main_frame, text=3*i + j + 1)
        button.grid(row=4 - i, column=j, padx=5, pady=5)

zero_button = ttk.Button(main_frame, text="0")
zero_button.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()