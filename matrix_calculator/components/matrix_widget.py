from tkinter import *

class Input:
    def __init__(self, parent, rows, columns):
        self.frame = Frame(parent, padx=5, pady=5, borderwidth=2, bg="green")
        variables = []
        for i in range(rows):
            vars = []
            for j in range(columns):
                var = StringVar(self.frame)
                border_frame = Frame(self.frame, bg="green", padx=1, pady=1)
                entry = Entry(border_frame, textvariable=var, width=15)
                entry.pack()
                border_frame.grid(row=i, column=j)
                vars.append(var)
            variables.append(vars)
        self.variables = variables
        self.frame.pack()
