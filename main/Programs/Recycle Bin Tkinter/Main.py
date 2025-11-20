import tkinter as tk
from tkinter import messagebox
import shutil
import os
import re


class RecycleBin():
    def __init__(self):
        self.root = tk.Tk()

        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "DesktopFiles")
        self.trash_path = os.path.join(os.path.expanduser("~"), "Desktop", "TrashCan")

        os.makedirs(self.desktop_path, exist_ok=True)
        os.makedirs(self.trash_path, exist_ok=True)

        self.root.geometry('800x500')
        self.root.title('Recycle Bin')

        self.contrast_frame1 = tk.Frame(self.root)

        self.desktop_files_label = tk.Label(self.contrast_frame1,text='Available desktop files :')
        self.desktop_files_list = []
        self.desktop_files = tk.Label(self.contrast_frame1,text=', '.join(self.desktop_files_list))

        self.bin_files_label = tk.Label(self.contrast_frame1, text='Available recycle bin files :')
        self.bin_files_list = []
        self.bin_files = tk.Label(self.contrast_frame1, text=', '.join(self.bin_files_list))


        self.contrast_frame2 = tk.Frame(self.root)

        self.creation_file_label = tk.Label(self.contrast_frame2, text='Create File')
        self.creation_file_input = tk.Entry(self.contrast_frame2)
        self.creation_file_commit = tk.Button(self.contrast_frame2,text='Commit',command=self.create_desktop_file)

        self.throw_file_label = tk.Label(self.contrast_frame2,text='Throw file to bin')
        self.throw_file_input = tk.Entry(self.contrast_frame2)
        self.throw_file_commit = tk.Button(self.contrast_frame2, text='Commit',command=self.delete_desktop_file)

        self.buttons_frame = tk.Frame(self.root)
        self.recycle = tk.Button(self.buttons_frame,text='Recycle Files',command=self.recycle)
        self.restore = tk.Button(self.buttons_frame,text='Restore Files',command=self.restore)


        self.contrast_frame1.pack()

        self.desktop_files_label.grid(row=0,column=0,padx=20,pady=20)
        self.desktop_files.grid(row=1,column=0,padx=20)

        self.bin_files_label.grid(row=0,column=1,padx=20,pady=20)
        self.bin_files.grid(row=1,column=1,padx=20)

        self.contrast_frame2.pack(pady=10)

        self.creation_file_label.grid(row=1,column=0,padx=20,pady=10)
        self.creation_file_input.grid(row=1,column=1,padx=20,pady=10)
        self.creation_file_commit.grid(row=1,column=2,padx=20,pady=10)

        self.throw_file_label.grid(row=1,column=3,padx=20,pady=10)
        self.throw_file_input.grid(row=1,column=4,padx=20,pady=10)
        self.throw_file_commit.grid(row=1,column=5,padx=20,pady=10)

        self.buttons_frame.pack()
        self.recycle.grid(row=0,column=0,padx=20,pady=20)
        self.restore.grid(row=0,column=1,padx=20,pady=20)

        self.root.mainloop()
        shutil.rmtree(self.trash_path)
        shutil.rmtree(self.desktop_path)

    def create_desktop_file(self):
        file_name = self.creation_file_input.get()
        if file_name not in self.desktop_files_list:
            if re.match(r'^[a-z]+[.]{1}[a-z]+$',file_name):
                file_path = os.path.join(self.desktop_path, file_name)
                with open(file_path, 'w') as file:
                    file.write(file_name)  # or file.write(file_name)
                self.desktop_files_list.append(file_name)
                self.desktop_files.config(text=', '.join(self.desktop_files_list))
                self.desktop_files.grid(row=1, column=0, padx=20)
            else:
                tk.messagebox.showinfo('Bad Input','Please entry : <file_name>.<extension>')
        else:
            tk.messagebox.showinfo('File exists','This file already exists')

    def delete_desktop_file(self):
        file_name = self.throw_file_input.get()
        if re.match(r'^[a-z]+[.]{1}[a-z]+$', file_name):
                if file_name in self.desktop_files_list:
                    source = os.path.join(self.desktop_path, file_name)
                    destination = os.path.join(self.trash_path, file_name)
                    shutil.move(source,destination)
                    self.desktop_files_list.remove(file_name)
                    self.bin_files_list.append(file_name)
                    self.bin_files.config(text=', '.join(self.bin_files_list))
                    self.bin_files.grid(row=1, column=1, padx=20)

                    self.desktop_files.grid(row=1, column=0, padx=20)
                    self.desktop_files.config(text=', '.join(self.desktop_files_list))
                else:
                    tk.messagebox.showinfo(f'Bad File Entry',f'No such file as {file_name}')
        else:
            tk.messagebox.showinfo('Bad Input', 'Please entry : <file_name>.<extension>')

    def recycle(self):
        for file_name in self.bin_files_list:
            path = os.path.join(self.trash_path, file_name)
            if os.path.exists(path):
                os.remove(path)

        self.bin_files_list = []
        self.bin_files.config(text=', '.join(self.bin_files_list))

    def restore(self):
        for file_name in self.bin_files_list:
            source = os.path.join(self.trash_path, file_name)
            destination = os.path.join(self.desktop_path, file_name)
            shutil.move(source, destination)
        for file in self.bin_files_list:
            self.desktop_files_list.append(file)
        self.bin_files_list = []
        self.bin_files.config(text=', '.join(self.bin_files_list))

        self.desktop_files.config(text=', '.join(self.desktop_files_list))








RecycleBin()

