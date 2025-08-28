from student import *
class Model:
    def __init__(self):
        self.students=[]
    
    def add_student(self, student):
        self.students.append(student)
    
    def show_student_details(self, name):
       # return self.name
       for student in self.students:
           if student.name == name:
               return student
    #
        
if __name__ == '__main__':
    m1=Model()
    s1 = Student("Shristi", 20, {"Maths":57, "Microprocessor": 55, "DSA":52  })
    s2 = Student("Kritishma", 8, {"Maths":59, "Microprocessor": 60, "DSA":52  })
    s3 = Student("Arina", 1, {"Maths":58, "Microprocessor": 42, "DSA":51 })
    
    m1.add_student(s1)
    m1.add_student(s2)
    m1.add_student(s3)
    print('The details of the student \n',m1.show_student_details('Shristi'))
    #s1.calculate_avg_marks()
    
    m1.add_student(s1.name)
    m1.add_student(s2.name)
    m1.add_student(s3.name)
    print(m1.students)
    
    s1.calculate_percentage()
    
    