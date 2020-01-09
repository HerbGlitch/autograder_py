class RubricGrader:
    def __init__(self, rubric_path):
        self.rubric_path = rubric_path
        self.students = {}
        self.strip_rubric_parts()

    def set_rubric_path(self, rubric_path):
        self.rubric_path = rubric_path

    def strip_rubric_parts(self):
        rubric_string = get_rubric_string()


    def get_rubric_string(self):
        rubric_string = ""
        rubric_file = open(self.rubric_path, 'r')
        for line in rubric_file:
            rubric_string += line
        rubric_file.close()
        return rubric_string

    def add_student(self, student):
        self.students[student] = []

class RubricCode:
    def __init__(self):
        print("code section")

class RubricOutput:
    def __init__(self):
        print("output section")


# [
# code:
#
#
#
#
#
# output:
# ]
