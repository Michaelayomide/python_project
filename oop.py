# class Function():
#     def display1a(self) :
#         print("hello world")

#     def display1b(self):
#         print("hello cosmos")
    

# # obj1=Function()
# # obj1.display()


# class Function2(Function):
#     def display2a(self):
#         print("hello earth")

#     def display2b(self):
#         print("hello universe")



# 
# class Function3(Function2):
#     pass

# obj3=Function3()
# # obj3.
# from math import *

# class Function():
#      def allmity_formular(self):
#       a=int(input("what is a"))
#       b=int(input("what is b"))
#       c=int(input("what is c"))
#       x1=(-b+sqrt((b**2) - 4*a*c))/2*a
#       x2=(-b-sqrt((b**2) - 4*a*c))/2*a
#       print(f"""the two values of x are
#       x1={x1}
#       x2={x2}""")

# first_student=Function()
# first_student.allmity_formular()     

# class Function2(Function):
#      def cosin_rule(self):
#         a=int(input("length of a"))
#         b=int(input("length of b"))
#         c=int(input("length of c"))
#         d=int(input("enter cos"))
#         x2=c+sqrt((a**2+b**2)-2*b*cos(d))        
#         print(f"""
#               the values of x is
#                 x2={x2}
#               """)
# first_student2=Function2()
# first_student2.cosin_rule()             

# class Function3(Function2):
#     pass

# first_student3=Function3()
# first_student3.cosin_rule

#password=["Car4566","cars","car45"]



#


class Student:

    def __init__(self, name, age):   #attributes
        self.name=name
        self.age=age

    def display1(self):    #methods
        print(f'the name of the student is{self.name}, he is {self.age} years old')

#std1=Student("eto david", 13)
# std1.display1()


class Student2(Student):
    def __init__(self, height, department, name, age):
        self.height= height
        self.department=department

        Student.__init__(self,name, age)

    def display2(self):
        print(f"my name {self.name} and he is{self.age},{self.height},{self.department}")

# std2=Student2("eto", 14.5, "electrical", 14)
# std2.display2()



class Student3(Student2):
    
   def __init__(self, height, department, name, age, gender):
        self.gender=gender

        Student2.__init__(self,height,department,name,age)



   def display3(self):
        print(f"name is {self.name} age is {self.age} height{self.height} department{self.department}")  
    

obj3=Student3("eto",13.5,"art" ,14.1, 'male')
obj3.display3()
    

# class Function():
#     def display1a(self) :
#         print("hello world")

#     def display1b(self):
#         print("hello cosmos")
    

# # obj1=Function()
# # obj1.display()


# class Function2(Function):
#     def display2a(self):
#         print("hello earth")

#     def display2b(self):
#         print("hello universe")





# obj1= Function2()
# obj1.d