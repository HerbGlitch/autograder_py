from autograde.pathing import Pathing

from os import listdir, system
from os.path import isfile, join

class Autograde:
    def __init__(self):
        self.pathing = Pathing()
        self.run()

    def run(self):
        solution_files = [f for f in listdir(self.pathing.solutions_path) if isfile(join(self.pathing.solutions_path, f))]
        assignment_files = [f for f in listdir(self.pathing.assignments_path) if isfile(join(self.pathing.assignments_path, f))]
        print(solution_files, assignment_files)
        for solution in solution_files:
            print(self.pathing.solutions_path + solution)
            system("cd " + self.pathing.solutions_path + "\npython " + solution + " >> temp.txt")
