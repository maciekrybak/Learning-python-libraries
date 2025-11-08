import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.geometry('320x500')

        self.label = tk.Label(self.root,text='calculator',font=('Arial',18))
        self.label.pack(pady=10)

        self.value_box = []
        self.entry = tk.Text(self.root,height=1)
        self.entry.pack(padx=10)
        self.entry.bind('<KeyPress>', self.key_input)



        self.history_label = tk.Label(self.root,text='operation history')
        self.history_label.pack()
        self.history = tk.Text(self.root,height=1)
        self.history.pack(padx=20)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.sym_count = 0
        self.num_count = 0

        self.button0 = tk.Button(self.frame, text='0', command=lambda: self.write_num('0'))
        self.button10 = tk.Button(self.frame, text='.', command=lambda: self.write_num('.'))
        self.button9 = tk.Button(self.frame, text='9', command=lambda: self.write_num('9'))
        self.button8 = tk.Button(self.frame, text='8', command=lambda: self.write_num('8'))
        self.button7 = tk.Button(self.frame, text='7', command=lambda: self.write_num('7'))
        self.button6 = tk.Button(self.frame, text='6', command=lambda: self.write_num('6'))
        self.button5 = tk.Button(self.frame, text='5', command=lambda: self.write_num('5'))
        self.button4 = tk.Button(self.frame, text='4', command=lambda: self.write_num('4'))
        self.button3 = tk.Button(self.frame, text='3', command=lambda: self.write_num('3'))
        self.button2 = tk.Button(self.frame,text='2',command=lambda:self.write_num('2'))
        self.button1 = tk.Button(self.frame, text='1',command=lambda:self.write_num('1'))
        self.buttonO1 = tk.Button(self.frame, text='+',command=lambda:self.write_num('+'))
        self.buttonO2 = tk.Button(self.frame, text='-', command=lambda: self.write_num('-'))
        self.buttonO3 = tk.Button(self.frame, text='*', command=lambda: self.write_num('*'))
        self.buttonO4 = tk.Button(self.frame, text='/', command=lambda: self.write_num('/'))
        self.buttonO5 = tk.Button(self.frame, text='x²', command=lambda: self.write_num('**2'))
        self.buttonO6 = tk.Button(self.frame, text='^', command=lambda: self.write_num('**'))
        self.buttonO7 = tk.Button(self.frame, text='√', command=lambda: self.write_num('**0.5'))

        self.buttonOR = tk.Button(self.frame, text='=',command=self.get_result)
        self.buttonOC = tk.Button(self.frame, text='CLEAR', command=self.clear)

        self.button10.grid(row=5, column=2, sticky=tk.W + tk.E)
        self.button9.grid(row=2, column=2, sticky=tk.W + tk.E)
        self.button8.grid(row=2, column=1, sticky=tk.W + tk.E)
        self.button7.grid(row=2, column=0, sticky=tk.W + tk.E)
        self.button6.grid(row=3, column=2, sticky=tk.W + tk.E)
        self.button5.grid(row=3, column=1, sticky=tk.W + tk.E)
        self.button4.grid(row=3, column=0, sticky=tk.W + tk.E)
        self.button3.grid(row=4, column=2, sticky=tk.W + tk.E)
        self.button2.grid(row=4,column=1,sticky=tk.W+tk.E)
        self.button1.grid(row=4, column=0,sticky=tk.W+tk.E)
        self.button0.grid(row=5, column=1, sticky=tk.W + tk.E)

        self.buttonO1.grid(row=3, column=3,sticky=tk.W+tk.E)
        self.buttonO2.grid(row=2, column=3, sticky=tk.W + tk.E)
        self.buttonO3.grid(row=1, column=3, sticky=tk.W + tk.E)
        self.buttonO4.grid(row=0, column=3, sticky=tk.W + tk.E)
        self.buttonO5.grid(row=0, column=2, sticky=tk.W + tk.E)
        self.buttonO6.grid(row=1, column=2, sticky=tk.W + tk.E)
        self.buttonO7.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.buttonOR.grid(row=4, column=3,sticky=tk.W+tk.E)
        self.buttonOC.grid(row=0, column=0, sticky=tk.W + tk.E)



        self.frame.pack(fill='x',pady=5)


        self.root.mainloop()

    def write_num(self, value):
        current = self.entry.get("1.0", tk.END).strip()

        if str(value) in ['+', '-', '*', '/']:
            if value == '-' and (self.num_count == 0 or current.endswith(('+', '-', '*', '/'))):
                self.value_box.append(value)
                self.entry.insert(tk.END, value)
                return

            if current.endswith(('+', '-', '*', '/')):
                return

            self.value_box.append(value)
            self.entry.insert(tk.END, value)
            self.sym_count = 1

        else:
            # liczba
            self.value_box.append(value)
            self.entry.insert(tk.END, value)
            self.num_count += 1

    def get_result(self):
        expression = ''.join(self.value_box)
        try:
            result = eval(expression)
            self.history.delete('1.0', tk.END)
            self.history.insert('1.0', expression)
            self.entry.delete('1.0', tk.END)
            self.entry.insert('1.0', str(result))
            self.value_box = [str(result)]
            self.sym_count = 0
            self.num_count = 1
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")

    def clear(self):
        self.value_box = []
        self.entry.delete('1.0',tk.END)
        self.history.delete('1.0',tk.END)

    def key_input(self,event):
        print(event)
        if event.char in '0123456789.+-*/':
            self.write_num(event.char)

        elif event.keysym == r'Return':
            self.get_result()

        elif event.keysym == r'BackSpace':
            self.clear()
        return 'break'







Calculator()