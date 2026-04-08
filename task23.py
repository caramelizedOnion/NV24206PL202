class Student:
    def __init__(self, nvno, name, class_name):
        self.nvno = nvno
        self.name = name
        self.class_name = class_name

    def learning(self):
        print("I belong to the class", self.class_name, "learning Programming Language")


# Example usage
Raghu = Student(1, "Ali", "AI")
Raghu.learning()