class User():
    def __init__(self,user_name,user_age):
        self.name = user_name
        self.age = user_age

    def show(self):
        print(self.name)
        print(self.age)

class Student(User):
    def __init__(self,name,age,course):
        User.__init__(self,user_name = name,user_age = age)
        self.course = course
    def display(self):
        self.show()
        print(self.course) 

stud_obj = Student("sam",21,"python") 
stud_obj.display()          
