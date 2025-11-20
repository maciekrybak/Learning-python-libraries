import tkinter as tk
from pydoc import visiblename
from tkinter import messagebox
import re

class SignUp:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('800x400')
        self.root.title('Sign Up')


        self.label = tk.Label(self.root,text='Sign Up\nValidation',font=('Arial',20))
        self.instruction_title = tk.Label(self.root,font=('Arial',15),text='Instruction')
        self.instruction_description = tk.Label(self.root,font=('Arial',10),text=
                                                   '* Login contains 3-7 characters starting with '
                                                   'atleast one letter. No symbols allowed\n'
                                                   '* E-Mail contains such a pattern like'
                                                   ' <username>@<domain>.com Where <username> and domain'
                                                   'is lowercase.\n'
                                                   '* Password contains 8-16 characters',justify='left')

        self.entry_frame = tk.Frame(self.root)
        self.login_text = tk.Label(self.entry_frame,text='Login :')
        self.login_entry = tk.Entry(self.entry_frame)

        self.email_text = tk.Label(self.entry_frame, text='E-Mail :')
        self.email_entry = tk.Entry(self.entry_frame)

        self.password_text = tk.Label(self.entry_frame, text='Password :')
        self.password_entry = tk.Entry(self.entry_frame,show='*')
        self.password_visibility_button_value = tk.IntVar()
        self.password_visibility_button = tk.Checkbutton(self.entry_frame,variable=self.password_visibility_button_value,command=self.checkbox)
        self.password_visibility_button_text = tk.Label(self.entry_frame,text='Show password')

        self.validate_button = tk.Button(self.root,text='Validate',font=('Arial',12),padx=30,pady=10
                                         ,command=self.validate)

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

    def validate(self):
        login_text = self.login_entry.get()
        email_text = self.email_entry.get()
        password_text = self.password_entry.get()

        # ✅ Improved regex patterns
        login_pattern = r'^[A-Za-z][A-Za-z0-9]{2,6}$'  # starts with letter, total 3–7 chars
        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$'  # must end with .com
        password_pattern = (
            r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>\/?]).{8,16}$'
        )  # 8–16 chars, one uppercase, number, and symbol

        # ✅ Validation flags
        login_flag = bool(re.match(login_pattern, login_text))
        email_flag = bool(re.match(email_pattern, email_text))
        password_flag = bool(re.match(password_pattern, password_text))

        # ✅ Feedback messages
        messages = []
        if not login_flag:
            messages.append("❌ Bad login (must start with a letter, 3–7 chars)")
        if not email_flag:
            messages.append("❌ Bad email (use format like user@domain.com)")
        if not password_flag:
            messages.append(
                "❌ Bad password (8–16 chars, must include uppercase, number & symbol)"
            )

        if not messages:
            messagebox.showinfo("Validation", "✅ All fields are correct!")
        else:
            messagebox.showinfo("Validation errors", "\n".join(messages))

    def checkbox(self):
        if self.password_visibility_button_value.get() == 1:
            self.password_entry.config(show='')
            print('cry')

        else:
            self.password_entry.config(show='*')
            print('hide')


        #traz robic pattern dla email i haslo w message boxie zlaczyc warunki co jest poprawne a co nie
        # i funckjinalsosc dla check boxa



SignUp()
