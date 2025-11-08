import tkinter as tk

root = tk.Tk() # Baza projektu

root.geometry("800x500") # < W x H >
root.title("untitled data app") # Deklaruje tytuł

label = tk.Label(root,text="good morning",font=('Arial',18)) # tworzy label gdzie jest czescia roota
label.pack(padx=50,pady=50) # padding podobnie jak w FE

buttonframe = tk.Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

button1 = tk.Button(buttonframe, text="7",font=('Arial',18))
button1.grid(row=0,column=0,sticky=tk.W+tk.E)

button2 = tk.Button(buttonframe, text="8",font=('Arial',18))
button2.grid(row=0,column=1,sticky=tk.W+tk.E)

button3 = tk.Button(buttonframe, text="9",font=('Arial',18))
button3.grid(row=0,column=2,sticky=tk.W+tk.E)

button4 = tk.Button(buttonframe, text="4",font=('Arial',18))
button4.grid(row=1,column=0,sticky=tk.W+tk.E)

button5 = tk.Button(buttonframe, text="5",font=('Arial',18))
button5.grid(row=1,column=1,sticky=tk.W+tk.E)

button6 = tk.Button(buttonframe, text="6",font=('Arial',18))
button6.grid(row=1,column=2,sticky=tk.W+tk.E)

button7 = tk.Button(buttonframe, text="1",font=('Arial',18))
button7.grid(row=2,column=0,sticky=tk.W+tk.E)

button8 = tk.Button(buttonframe, text="2",font=('Arial',18))
button8.grid(row=2,column=1,sticky=tk.W+tk.E)

button9 = tk.Button(buttonframe, text="3",font=('Arial',18))
button9.grid(row=2,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

root.mainloop() # Wywołuje pętle < otwiera program >
