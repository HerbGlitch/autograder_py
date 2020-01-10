class RubricOutput:
    def __init__(self, commands, all_files, assignment_name, student_name):
        self.commands = commands
        self.grade()

    def grade(self):
        for command in self.commands:
            if(command == "exact"):
                self.exact()

    def exact(self):
        print("Here")
