import tkinter as tk
from tkinter import messagebox
import requests
import re

class MathExpressionGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Math Expression Generator")
        self.answer=""
        self.num_cnt_label = tk.Label(self.root, text="Number of random numbers:")
        self.num_cnt_entry = tk.Entry(self.root,textvariable=tk.StringVar(value='4'))
        self.level_label = tk.Label(self.root, text="Difficulty level (1 or 2):")
        self.level_entry = tk.Entry(self.root,textvariable=tk.StringVar(value='1'))
        self.generate_button = tk.Button(self.root, text="Generate Expressions", command=self.generate_expressions)
        self.result_text = tk.Text(self.root)
        self.show_button = tk.Button(self.root, text="Show answer", command=self.show_answer)
        self.answer_text=tk.Text(self.root)
        
    def show_answer(self):
        self.answer_text.insert(tk.END,f"{self.answer}\n")
        
    def generate_expressions(self):
        num_cnt = int(self.num_cnt_entry.get())
        level = int(self.level_entry.get())
        response = requests.get(f"http://localhost:5000/expressions?num_cnt={num_cnt}&level={level}")
        if response.status_code == 200:
            self.answer = response.json()["expression"]
            nums = re.findall(r'\d+', self.answer.split('=')[0])
            test=f",\t".join(nums)        
            self.result_text.insert(tk.END, f"{test}\n")
        else:
            messagebox.showerror("Error", "Failed to generate expressions")

    def run(self):
        self.num_cnt_label.grid(row=0, column=0)
        self.num_cnt_entry.grid(row=1, column=0)
        self.level_label.grid(row=2, column=0)
        self.level_entry.grid(row=3, column=0)
        self.generate_button.grid(row=4, column=0)
        self.show_button.grid(row=5,column=0)
        self.result_text.grid(row=6, column=0,columnspan=2)
        self.answer_text.grid(row=6, column=2)
        
        self.root.mainloop()

if __name__ == "__main__":
    generator = MathExpressionGenerator()
    generator.run()