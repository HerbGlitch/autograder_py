from .rubric.rubric_grader import RubricGrader

class Autograde:
    def __init__(self, all_files):
        self.all_files = all_files
        self.run()

    def run(self):
        graded_by_rubric = []
        for assignment in self.all_files.get_assignments():
            graded_by_rubric.append(RubricGrader(self.all_files.rubric_input_path, self.all_files, assignment))
