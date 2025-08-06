import tkinter as tk
def on_click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="pink")
entry = tk.Entry(root, bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=65, ipady=15, pady=10)
buttons = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'0', '.', '=', '+',
'(', ')', 'C'
]
row = 1
col = 0
for btn_text in buttons:
    btn_color = "#f0f0f0"
    if btn_text == '=':
        btn_color = "#80e27e"
    elif btn_text == 'C':
        btn_color = "#ef5350"
    elif btn_text == '+':
        btn_color = "blue"
    elif btn_text == '-':
        btn_color = "blue"
    elif btn_text == '*':
        btn_color = "blue"
    elif btn_text == '/':
        btn_color = "blue"
    elif btn_text == '(':
        btn_color = "blue"
    elif btn_text == ')':
        btn_color = "blue"
    button = tk.Button(root, text=btn_text, font=("Arial", 18), width=6, height=2,bg=btn_color, relief=tk.RAISED, bd=3)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()