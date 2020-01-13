class RubricOutput:
    def __init__(self, commands, all_files, assignment_name, student_name):
        self.score = {}
        self.commands = commands
        self.all_files = all_files
        self.assignment_name = assignment_name
        self.student_name = student_name
        self.grade()

    def grade(self):
        for command in self.commands:
            if(command == "exact"):
                self.exact()

    def exact(self):
        self.score["all"] = self.all_files.get_assignment_output_as_string(self.assignment_name).strip().lower() == self.all_files.get_assignment_output_by_student_as_string(self.assignment_name + "-" + self.student_name).strip().lower()

    def get_score(self):
        return self.score
