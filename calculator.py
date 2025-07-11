from tkinter import *
root=Tk()
root.title("Simple Calculator")
entry=StringVar()
def on_click(button_text):
    current_text = entry.get()

    if button_text =='=':
            result = eval(current_text)
            entry.delete(0,END)
            entry.insert(END,str(result))
    elif button_text =='C':
        entry.delete(0,END)
    elif button_text=='x^2':
        entry.delete(0,END)
        entry.insert(END,f"{current_text}**2")
    elif button_text=='del':
       entry.delete(len(entry.get())-1,END)
       
       
    else:
        entry.insert(END,button_text)

root.title("Simple Calculator")
root.resizable(0,0)
# Entry widget for displaying and entering the input
entry =Entry(root, width=20,font=('Arial', 30))
entry.grid(row=0, column=0, columnspan=4)

#list of tuples
buttons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),('(',5,0),(')',5,1),('x^2',5,2),('del',5,3)]

for (text, row,col) in buttons:
    button =Button(root, text=text, width=5, height=2, font=('Arial', 14),bg="yellow",command=lambda t=text: on_click(t))
    button.grid(row=row, column=col)
root.mainloop()

