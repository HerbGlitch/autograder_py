class RubricCode:
    def __init__(self, commands, all_files, assignment_name, student_name):
        self.commands = commands
        self.grade()

    def grade(self):
        for commmand in self.commands:
            print(command)
