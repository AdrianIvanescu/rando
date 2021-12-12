import os

class OpenFile:
    def __init__(self,file_name):
        self.file_name = file_name
    
    def readFile(self):
        try:
            rel_path = "input"
            file_text = open(
                f"{os.path.join(os.path.dirname(__file__), rel_path)}/{self.file_name}",
                "r",
                )
        except Exception as e:
            print(f"{self.file_name} does not exist!")

    def closeFile(self,file_text):
        # closing the connection
        file_text.close() 

        