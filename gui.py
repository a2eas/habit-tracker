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
        self.load_prev_habits()

        
    def on_selection(self,event):
        self.habit_type = self.habit_type_choice.get()
        self.habit_input_name = ttk.Entry(self.habit_window)
        self.habit_input_name.insert(0, "Enter habit name")
        if self.habit_input_name.get() == "Enter habit name":
            self.habit_input_name.bind("<FocusIn>", lambda e: self.habit_input_name.delete(0, "end"))
        self.habit_input_name.pack(padx=10, pady=10)
        self.habits_input_amount = ttk.Entry(self.habit_window)
        self.habits_input_amount.insert(0, "Enter habit amount")
        if self.habits_input_amount.get() == "Enter habit amount":
            self.habits_input_amount.bind("<FocusIn>", lambda e: self.habits_input_amount.delete(0, "end"))
        self.habits_input_amount.pack(padx=10, pady=10)
        self.add_button = ttk.Button(self.habit_window,text='Add',command=self.habit_update)

        self.add_button.pack(padx=10, pady=10)
    def load_prev_habits(self):
        try:
            self.habits_name,self.habit_type,self.habits_amount = self.back.load_habits()
        except Exception as e:
            print(f"Error loading habits: {e}")
            self.habits_name = []
            self.habit_type = []
            self.habits_amount = [] 
        for habit in self.habits_name:
            self.entry_frame1 = ttk.Frame(self.root)
            self.entry_frame1.pack(padx=10, pady=10)

            # Add label inside the frame
            self.label = ttk.Label(self.entry_frame1, text=habit, font=25)
            self.label.pack(side="left", padx=(0, 10))

            # Add checkbox inside the frame next to the label
            self.checkbox = ttk.Checkbutton(self.entry_frame1)
            self.checkbox.pack(side="left")
    def habits_remove_button(self,frame,habit_name=None):
        self.remove_button = ttk.Button(frame,text='--', command=lambda: self.entry_frame.destroy())
        self.remove_button.pack(side="left", padx=(0, 10))
        self.habits_name.remove(habit_name) if habit_name else None
        self
    def habit_update(self):
        self.name = self.habit_input_name.get()
        self.habits_name.append(self.name)
        
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(padx=10, pady=10)

        # Add label inside the frame
        self.label = ttk.Label(self.entry_frame, text=self.habits_name[-1], font=25)
        self.label.pack(side="left", padx=(0, 10))

        # Add checkbox inside the frame next to the label
        self.checkbox = ttk.Checkbutton(self.entry_frame)
        self.checkbox.pack(side="left")
        self.back.add_habit(self.name, self.habit_type, 0)
        self.back.save_habits()
        self.habits_remove_button(self.entry_frame,self.name)
    def on_button_click(self):
        self.habit_window = Toplevel(self.root)
        self.habit_window.title("Add Habit")
        self.habit_window.geometry("300x200")
        self.habit_window.configure(background="gray")
        self.habit_type_choice = ttk.Combobox(self.habit_window,values= ['checkbox','time'],state='readonly')
        self.habit_type_choice.pack(padx=10, pady=10)
        self.habit_type_choice.set("Select Habit Type")
        self.habit_type_choice.bind("<<ComboboxSelected>>", self.on_selection)
        self.habit_type.append(self.habit_type_choice.get())

if __name__ == "__main__":
    guy = GUI(tkinter.Tk())
    guy.root.mainloop()
