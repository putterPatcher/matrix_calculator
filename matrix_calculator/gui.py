from tkinter import *
from components.answer_widget import Answer
from components.matrix_widget import Input

root = Tk()
root.geometry("720x720")
root.title("Matrix Calculator")

matrix_frame = Frame(root, padx=5, pady=5)
matrix_input_frame = Frame(matrix_frame, padx=5, pady=5)
label = Label(matrix_frame, text="Matrix")
label.grid(row=0, column=0)

input = Input(matrix_input_frame, 5, 5)
output_frame = Frame(root, padx=5, pady=5)
answer = Answer(output_frame, 5, 5, values=[["" for _ in range(5)] for _ in range(5)])
def showMatrix():
    global answer
    answer.frame.destroy()
    answer = Answer(output_frame, 5, 5, values=[[input.variables[i][j].get() for j in range(5)] for i in range(5)])

show = Button(root, text="Show", command=showMatrix)
show.pack()

matrix_input_frame.grid(row=0, column=1)
matrix_frame.pack()
output_frame.pack()

root.mainloop()