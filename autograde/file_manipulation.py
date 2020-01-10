from os import listdir, system
from os.path import isfile, join

class RunFiles:
    def __init__(self):
        self.rubric_input_path = "input/rubric/"
        self.solutions_input_path = "input/solutions/"
        self.assignments_input_path = "input/assignments/"
        self.solutions_output_path = "output/solutions/"
        self.assignments_output_path = "output/assignments/"
        self.check_path()
        self.clear_out_folders()
        self.run_files()

    def check_path(self):
        print("check path")

    def clear_out_folders(self):
        system("del /q " + self.assignments_output_path.replace('/','\\')[0:] + "*")
        system("del /q " + self.solutions_output_path.replace('/', '\\')[0:] + "*")

    def run_files(self):
        self.solution_files = [f for f in listdir(self.solutions_input_path) if isfile(join(self.solutions_input_path, f))]
        self.assignment_files = [f for f in listdir(self.assignments_input_path) if isfile(join(self.assignments_input_path, f))]
        for solution in self.solution_files:
            system("python " +  self.solutions_input_path + solution + " >> " + self.solutions_output_path +  solution.split(".")[0] + ".out")
        for assignment in self.assignment_files:
            system("python " +  self.assignments_input_path + assignment + " >> " + self.assignments_output_path + assignment.split(".")[0] + ".out")

    def get_assignments(self):
        assignments = []
        for assignment in self.get_solution_files():
            if(assignment.split(".")[0] not in assignments):
                assignments.append(assignment.split(".")[0])
        return assignments

    def get_students_from_assignment(self, assignment_name):
        students = []
        for assignment in self.get_assignment_files():
            if(assignment.split("-")[0] in assignment_name):
                students.append(assignment.split("-")[1].split(".")[0])
        return students

    def get_solution_files(self):
        return self.solution_files

    def get_assignment_files(self):
        return self.assignment_files



# from Tkinter import Tk
# from tkinter.filedialog import askopenfilename
#
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)
