import tkinter as tk
from .autograde import Autograde
from .file_manipulation import RunFiles
from .rubric.rubric_generator import RubricGenerator
from tkinter import *
from tkinter.filedialog import askdirectory

class Window(Frame):
    def __init__(self):
        self.master = Tk()
        self.solutions_path = "input/solutions/"
        self.solution_path_var = StringVar()
        self.solution_path_var.set("input/solutions/")
        self.assignments_path = "input/assignments/"
        self.assignment_path_var = StringVar()
        self.assignment_path_var.set("input/assignments/")
        Frame.__init__(self, self.master)

    def main_screen(self):
        self.screen_width = 695
        self.screen_height = 600
        self.master.geometry(str(self.screen_width) + "x" + str(self.screen_height))
        self.master.title("Auto Grader v.0.1")
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_columnconfigure(0, weight=0)
        self.main_screen_title = Label(self.master, text="Auto Grader", font=("arial",16,"bold")).grid()
        self.assignment = Button(self.master, text="assignment path", command=self.set_assignment_path, width=20).grid(column=0, row=1, padx=10, pady=5, sticky=tk.W + tk.S)
        self.assignment_path = Label(self.master, textvariable=self.assignment_path_var, anchor='w', width=50).grid(column=1, row=1, padx=5, ipady=5, sticky=tk.W + tk.S)
        self.solution = Button(self.master, text="solutions path", command=self.set_solution_path, width=20).grid(column=0, row=3, padx=10, pady=5, sticky=tk.W + tk.S)
        self.solution_path = Label(self.master, textvariable=self.solution_path_var, anchor='w', width=50).grid(column=1, row=3, ipadx=5, pady=5, sticky=tk.W + tk.S)
        self.main_button = Button(self.master, text="run files", command=self.run_files, width=20).grid(column=5, row=3, pady=5, padx=5, sticky=tk.E + tk.S)

    def run_files(self):
        self.all_files = RunFiles(self.solutions_path, self.assignments_path)
        run = Button(self.master, text="run", command=self.run, width=20).grid(column=5, row=4, pady=5, padx=5, sticky=tk.W + tk.S)
        self.rb_text = tk.Text(self.master, height=20, width=60)
        r_g = RubricGenerator("test", self.all_files) #generate rubric
        self.rb_text.insert(INSERT, r_g.get_rubric_string())
        self.rb_text.grid(column=0, columnspan=3, row=4, pady=5, padx=5, sticky=tk.W + tk.E)

    def run(self):
        self.all_files.write_to_rubric("test", self.rb_text.get("1.0",'end-1c')) #write to rubric file
        autograde = Autograde(self.all_files)

    def set_assignment_path(self):
        temp = askdirectory()
        if(temp != ""):
            self.assignments_path = temp
            self.assignment_path_var.set(temp)

    def set_solution_path(self):
        temp = askdirectory()
        if(temp != ""):
            self.solutions_path = temp
            self.solution_path_var.set(temp)
