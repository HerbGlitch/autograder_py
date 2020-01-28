class RubricCode:
    def __init__(self, commands, all_files, assignment_name, student_name):
        self.score = {}
        self.commands = commands
        self.all_files = all_files
        self.assignment_name = assignment_name
        self.student_name = student_name
        self.set_commands()
        self.grade()

    def grade(self):
        for command in self.commands:
            for command_item in self.commands_check[command]:
                if(command_item in self.all_files.get_assignment_by_student_as_string(self.assignment_name + "-" + self.student_name).strip(" ").lower()):
                    self.score[command] = True
                    break
                else:
                    self.score[command] = False

    def set_commands(self):
        self.commands_check = {
            "loop": ["for","while"],
            "print": ["print("],
            "dictionary": ["={"],
            "list": ["=["],
            "variable": ["="],
            "comparison": ["==", ">", "<", "!"],
            "logic": ["if(", "elif(", "else:"],
            "format": [".format", "f\""],
            "import": ["import"]
        }

    def get_score(self):
        return self.score
