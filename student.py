class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def __str__(self):
        return f'Name : {self.name}\n Roll_no : {self.roll_no}\n Marks : {self.marks}'
    
    def cal_avg_marks(self, marks):
        all_result = list(self.marks.values())
        return sum(all_result)/len(self.marks)
    def calculate_percentage(self):
        all_result=list(self.marks.values())
        total = sum(all_result)
        length = len(all_result)*100
        percentage = total / length *100
        return percentage
        