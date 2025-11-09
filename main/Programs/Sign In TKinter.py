import tkinter as tk

class SignUp:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('600x400')
        self.root.title('Sign Up')


        self.label = tk.Label(self.root,text='Sign Up\nValidation',font=('Arial',20))
        self.instruction_title = tk.Label(self.root,font=('Arial',15),text='Instruction')
        self.instruction_description = tk.Label(self.root,font=('Arial',10),text=
                                                   '* Login contains 3-12 characters starting with '
                                                   'atleast one letter. No symbols allowed\n'
                                                   '* E-Mail contains such a pattern like'
                                                   ' <username>@<domain>.com\n'
                                                   '* Password contains 8-16 characters atleast one'
                                                   'symbol,number and uppercase letter',justify='left')

        self.entry_frame = tk.Frame(self.root)
        self.login_text = tk.Label(self.entry_frame,text='Login :')
        self.login_entry = tk.Entry(self.entry_frame)

        self.email_text = tk.Label(self.entry_frame, text='E-Mail :')
        self.email_entry = tk.Entry(self.entry_frame)

        self.password_text = tk.Label(self.entry_frame, text='Password :')
        self.password_entry = tk.Entry(self.entry_frame)
        self.password_visibility_button = tk.Checkbutton(self.entry_frame)
        self.password_visibility_button_text = tk.Label(self.entry_frame,text='Show password')

        self.validate_button = tk.Button(self.root,text='Validate',font=('Arial',12),padx=30,pady=10)

        #column configuration

        # LAYOUT [UPPER]
        # upper labels
        self.label.pack(pady=5)
        self.instruction_title.pack(pady=10)
        self.instruction_description.pack(pady=5)

        #LAYOUT [LOWER]
        #login
        self.entry_frame.pack()
        self.login_text.grid(row=0,column=0)
        self.login_entry.grid(row=0,column=1)
        #email
        self.email_text.grid(row=1, column=0)
        self.email_entry.grid(row=1, column=1)
        #password

        self.password_text.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1)
        self.password_visibility_button.grid(row=2, column=2)
        self.password_visibility_button_text.grid(row=2,column=3)

        self.validate_button.pack(side='bottom',pady=50)

        self.root.mainloop()

SignUp()
print('nice')