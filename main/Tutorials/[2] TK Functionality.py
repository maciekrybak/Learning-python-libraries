import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar,tearoff=0) # no dashline at top
        self.filemenu.add_command(label='Close',command=exit)

        self.menubar.add_cascade(menu=self.filemenu,label="File")
        self.root.config(menu=self.menubar)


        self.root.geometry('800x500')
        self.root.title('Greetings')

        self.label = tk.Label(self.root,text="Welcome in my APP",font=('Arial',18))
        self.label.pack()

        self.textbox = tk.Text(self.root,font=('Arial',16),height=2)
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(pady=50,padx=100)

        self.check_value = tk.IntVar() # dla checka dostajemy mozliwosc value
        self.check = tk.Checkbutton(self.root,text="Do you want to display?",font=('Arial',14),variable=self.check_value)
        self.check.pack()

        self.button = tk.Button(self.root,text='Click!',font=('Arial',14),command=self.show_message)
        self.button.pack()

        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_value.get() == 1: # value z tego bierzemy z get
            if self.textbox.get('1.0',tk.END).strip() == '': # tutaj tez aby uzyskac str get
                messagebox.showinfo(title='Bad Entry',message='Enter a proper message!')
                self.root.destroy()
            else:
                messagebox.showinfo(title='Yo bro tweakin',message=self.textbox.get('1.0',tk.END))
                print(self.textbox.get('1.0',tk.END))
        else:
            print(self.textbox.get('1.0', tk.END))

    def shortcut(self,event):
        actual_value = self.check_value.get() # tu podobnie get

        if str(event.keysym) == 'd' and str(event.state) == '12': # event z bindu textboxa i tam on jest
            if actual_value == 1:
                self.check_value.set(0) # set pozwala narzucic checka
            else:
                self.check_value.set(1)

    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="Want to quit?"):
            self.root.destroy()


MyGUI()