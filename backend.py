import random
import json
from timer import CountdownTimer
import time


class Backend:
    def __init__(self):
        self.List_habit_names = []
        self.type_of_habits = []
        self.amount_of_habits = []
    def add_habit(self, habit_name, habit_type,habit_amount):
        self.List_habit_names.append(habit_name)
        self.type_of_habits.append(habit_type)
        self.amount_of_habits.append(habit_amount)
    def load_habits(self):
        try:
            with open('habits.json', 'r') as file:
                
                habits = json.load(file)
                self.List_habit_names = habits['habit_names']
                self.type_of_habits = habits['habit_types']
                self.amount_of_habits = habits['habit_amounts']
        except FileNotFoundError:
            print("No habits file found. Starting with an empty list.")
            self.List_habit_names = []
            self.type_of_habits = []
            self.amount_of_habits = []
    def save_habits(self):        
        with open('habits.json', 'w') as file:
            habits = {
                'habit_names': self.List_habit_names,
                'habit_types': self.type_of_habits,
                'habit_amounts': self.amount_of_habits
            }
            json.dump(habits, file, indent=4)
    def timer(self, hours):
        timer = CountdownTimer(hours)
        timer.start()

        return timer
    def get_random_habit(self):
        rando_habit = random.randint(0,2)
        return rando_habit
    def get_habbits(self):
        return self.List_habit_names ,self.type_of_habits ,self.amount_of_habits