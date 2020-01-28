class RubricGenerator():
    def __init__(self, filename, all_files):
        self.file_string = "#" + filename + " rubric\n"
        self.filename = filename
        self.all_files = all_files
        self.two_spaces = "  "
        self.set_commands()
        self.input()
        self.code()
        self.output()

    def input(self):
        self.file_string += "input:\n"
        self.file_string += "  #todo:// every enter in this is an enter in the code\n"
        self.file_string += "  None\n" #temp
        self.file_string += "\n"

    def code(self):
        self.file_string += "code:\n"
        for key in self.commands.keys():
            if(key in self.all_files.get_assignment_as_string(self.filename).strip()):
                self.file_string += "  " + self.commands[key] + "\n"
        self.file_string += "\n"

    def output(self):
        self.file_string += "output:\n"
        if(self.all_files.get_assignment_output_as_string(self.filename).strip() != ""):
            self.file_string += self.two_spaces + self.all_files.get_assignment_output_as_string(self.filename).replace("\n", "\n  ")
        self.file_string += "\n"

    def get_rubric_string(self):
        return self.file_string

    def set_commands(self):
        self.commands = {
            "for": "loop",
            "while": "loop",
            "print(": "print",
            "={": "dictionary",
            "=[": "list",
            "=": "variable",
            "==": "comparison",
            ">": "comparison",
            "<": "comparison",
            "!": "comparison",
            "if(": "logic",
            "elif(": "logic",
            "else:": "logic",
            ".format": "format",
            "f\"": "format",
            "import": "import"
        }
