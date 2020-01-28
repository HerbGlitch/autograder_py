from .rubric_code import RubricCode
from .rubric_output import RubricOutput

class RubricGrader:
    def __init__(self, rubric_path, all_files, assignment_name):
        self.rubric_path = rubric_path + assignment_name + ".hrb"
        self.students = {}
        self.rubric = {}
        self.all_files = all_files
        self.assignment_name = assignment_name;
        self.strip_rubric_parts()
        self.grade()

    def grade(self):
        for student in self.all_files.get_students_from_assignment(self.assignment_name):
            rubric_code = RubricCode(self.get_rubric_by_topic("code"), self.all_files, self.assignment_name, student)
            rubric_output = RubricOutput(self.get_rubric_by_topic("output"), self.all_files, self.assignment_name, student)
            self.students[student] = {
                "code": rubric_code.get_score(),
                "output": rubric_output.get_score(),
            }
        print(self.students)

    def set_rubric_path(self, rubric_path):
        self.rubric_path = rubric_path

    def strip_rubric_parts(self):
        rubric_string = self.get_rubric_string()
        rubric_array = rubric_string.split("\n")
        topic = ""
        for line in rubric_array:
            if(":" in line):
                topic = line.strip(":")
                self.rubric[topic] = []
                continue
            if(topic == ""):
                continue
            if(len(line) > 2 and line.lstrip()[0] == '/' and line.lstrip()[1] == '/'):
                continue
            if("//" in line):
                line = line.split("//")[0]
            if(len(line.lstrip()) < 1):
                continue
            self.rubric[topic].append(line.lstrip().rstrip())

    def get_rubric_string(self):
        rubric_string = ""
        rubric_file = open(self.rubric_path, 'r')
        for line in rubric_file:
            rubric_string += line
        rubric_file.close()
        return rubric_string

    def get_rubric(self):
        return self.rubric

    def get_rubric_by_topic(self, topic):
        return self.rubric[topic]

    def add_student(self, student):
        self.students[student] = []
