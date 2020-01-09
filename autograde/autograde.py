from .file_manipulation import RunFiles

class Autograde:
    def __init__(self):
        self.all_files = RunFiles()
        self.run()

    def run(self):
        print("done")
