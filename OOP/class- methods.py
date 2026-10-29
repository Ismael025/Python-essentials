class Student:
    school = " University Of Rwanda"
    
    def __init__ (self, name, marks) :
        self.name = name
        self.marks = marks
        
    def get_result (self):
        return self.name, self.marks
    
    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def is_pass ( marks):
        return marks >= 50

Student1 =Student("Ismael", 50)

print ("the Student info are:", Student1.get_result())
print ("from : ", Student1.get_school())
print ("Passed? :", Student1.is_pass(50))
