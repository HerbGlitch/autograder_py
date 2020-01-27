from os import listdir, system
from os.path import isfile, join

class RunFiles:
    def __init__(self, solutions_input_path, assignments_input_path):
        self.solutions_input_path = str(solutions_input_path)
        self.assignments_input_path = str(assignments_input_path)
        self.rubric_input_path = "input/rubric/"
        self.solutions_output_path = "output/solutions/"
        self.assignments_output_path = "output/assignments/"
        self.clear_out_folders()
        self.run_files()

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

    def get_assignment_as_string(self, assignment_name):
        if(assignment_name + ".py" in self.solution_files):
            assignment_string = ""
            assignment_file = open(self.solutions_input_path + assignment_name + ".py", 'r')
            for line in assignment_file:
                assignment_string += line
            assignment_file.close()
            return assignment_string
        return ""

    def get_assignment_by_student_as_string(self, assignment_student_name):
        if(assignment_student_name + ".py" in self.assignment_files):
            assignment_string = ""
            assignment_file = open(self.assignments_input_path + assignment_student_name + ".py", 'r')
            for line in assignment_file:
                assignment_string += line
            assignment_file.close()
            return assignment_string
        return ""

    def get_assignment_output_as_string(self, assignment_name):
        if(assignment_name + ".py" in self.solution_files):
            assignment_string = ""
            assignment_file = open(self.solutions_output_path + assignment_name + ".out", 'r')
            for line in assignment_file:
                assignment_string += line
            assignment_file.close()
            return assignment_string
        return ""

    def get_assignment_output_by_student_as_string(self, assignment_student_name):
        if(assignment_student_name + ".py" in self.assignment_files):
            assignment_string = ""
            assignment_file = open(self.assignments_output_path + assignment_student_name + ".out", 'r')
            for line in assignment_file:
                assignment_string += line
            assignment_file.close()
            return assignment_string
        return ""

    def get_solution_files(self):
        return self.solution_files

    def get_assignment_files(self):
        return self.assignment_files
