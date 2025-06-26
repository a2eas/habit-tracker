from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.ttk as ttk
from backend import Backend


class GUI:
    def __init__(self, root):
        self.back = Backend()
        self.root = root
        self.root.title("habit tracker")
        self.root.geometry("900x400")
        self.root.configure(background= "gray")
        self.button = ttk.Button(self.root, text="+", command=self.on_button_click)
        self.button.configure(width=10, padding=10)
        self.button.place(x=800,y=10)
        self.habits_name,self.type,self_amount = self.back.get_habbits()
        
        self.root.resizable(False, False)
        
    def on_selection(self,event):
        self.habit_type = self.habit_type_choice.get()
        self.habit_input = ttk.Entry(self.habit_window)
        self.habit_input.pack(padx=10, pady=10)
        self.add_button = ttk.Button(self.habit_window,text='Add',command=self.habit_update)

        self.add_button.pack(padx=10, pady=10)
    def habit_update(self):
        self.name = self.habit_input.get()
        self.habits_name.append(self.name)
        
        self.lable = ttk.Label(self.root,text=self.habits_name[-1],font=25)
        self.lable.pack()
        self.checkbox = ttk.Checkbutton(self.root)
        self.checkbox.pack()
    def on_button_click(self):
        self.habit_window = Toplevel(self.root)
        self.habit_window.title("Add Habit")
        self.habit_window.geometry("300x200")
        self.habit_window.configure(background="gray")
        self.habit_type_choice = ttk.Combobox(self.habit_window,values= ['hours','time'],state='readonly')
        self.habit_type_choice.pack(padx=10, pady=10)
        self.habit_type_choice.set("Select Habit Type")
        self.habit_type_choice.bind("<<ComboboxSelected>>", self.on_selection)
print('helpwao')
print('help')
guy = GUI(tkinter.Tk())
guy.root.mainloop()
