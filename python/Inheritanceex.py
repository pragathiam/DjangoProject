#'''employee is a person'''
# class Person:
#      def __init__(self,name,dob,phno,mail):
#          self.name=name
#          self.dob=dob
#          self.phno=phno
#          self.mail=mail
#      def disp_person(self):
#          print('person details:')
#          print(f'name:{self.name}dob:{self.dob}phno:{self.phno}mail:{self.mail}')
# class Employee(Person):
#      def __init__(self,eid,name,dob,phno,mail):
#          super().__init__(name,dob,phno,mail)
#          self.eid=eid
#      def emp_details(self):
#          print('employee details:')
#          print(f'eid:{self.eid}')
#          super().disp_person()
# e=Employee(101,'alexander','04-july-1934',9876543210,'alex@gmail.com')
# e.emp_details()            

# class GrandFather:
#     def __init__(self):
#         print('grand father constructor')
# class parents(GrandFather):
#     def __init__(self):
#         print('parent constructor')
# class Child(parents):
#     pass
# c=Child()                

# class GrandFather:
#     def m1(self):
#         print('m1 method of gf')
# class Parents(GrandFather):
#     pass
# class Child(Parents):
#     pass
# c=Child()
# c.m1()        

# class Employee:
#      def __init__(self,name,dob,phno,mail):
#          self.name=name
#          self.dob=dob
#          self.phno=phno
#          self.mail=mail
#      def disp_employee(self):
#          print('Employee details:')
#          print(f'name:{self.name}dob:{self.dob}phno:{self.phno}mail:{self.mail}')
# class Manager(Employee):
#      def __init__(self,eid,name,dob,phno,mail):
#          super().__init__(name,dob,phno,mail)
#          self.eid=eid
#      def manager_details(self):
#          print('manager details:')
#          print(f'eid:{self.eid}')
#          super().disp_employee()
# e=Manager(101,'alexander','04-july-1934',9876543210,'alex@gmail.com')
# e.manager_details()     

# class Car:
#      def __init__(self,brand,color):
#           self.brand=brand
#           self.color=color
#      def disp_car(self):
#           print('car details:')
#           print(f'brand:{self.brand} color:{self.color}')
# class Manager(Car):
#       def __init__(self,eid,name,dob,phno,mail):
#           super().__init__('jeep','black')
#           self.eid=eid
#       def manager_details(self):
#           print('manager details:')
#           print(f'eid:{self.eid}')
#           super().disp_car()
# m=Manager(101,'manu','01-02-1993',9876543210,'manu@gmail.com')
# m.manager_details()     

# class Student:
#       def __init__(self,name,dob,phno,mail):
#           self.name=name
#           self.dob=dob
#           self.phno=phno
#           self.mail=mail
#       def disp_student(self):
#           print('student details:')
#           print(f'name:{self.name} dob:{self.dob} phno:{self.phno} mail:{self.mail}')
# class Teacher(Student):
#       def __init__(self,eid,name,phno,mail):
#           super().__init__('name','dob','phno','mail')
#           self.eid=eid
#       def teacher_details(self):
#           print('teacher details:')
#           print(f'eid:{self.eid}')
#           super().disp_student()
# t=Teacher(101,'alexander',9876543210,'alex@gmail.com')
# t.teacher_details()     

# class Brain:
#       def __init__(self,Function):
#           self.function=function
#       def disp_brain(self):
#           print('brain details:')
#           print(f'function:{self.function}')
# class Human(Brain):
#       def __init__(self,eid,name,phno):
#           super().__init__('thinking')
#           self.eid=eid
#       def human_details(self):
#           print('human details:')
#           print(f'eid:{self.eid}')
#           super().disp_brain()
# h=Human(101,'indu',9876543210)
# h.human_details()   


# class Charger:
#       def __init__(self,cable):
#           self.cable=cable
#       def disp_charger(self):
#           print('Charger details:')
#           print(f'cable:{self.cable}')
# class Mobile(Charger):
#       def __init__(self,eid,brand,model):
#           super().__init__('cable')
#           self.eid=eid
#       def mobile_details(self):
#           print('mobile details:')
#           print(f'eid:{self.eid}')
#           super().disp_charger()
# c=Charger(101,'samsung','a15')
# c.charger_details()     

# class Demo1:
#     def m1(self):
#         print('demo1 m1 method')
# class Demo2:
#     def m1(self):
#         print('demo2 m1 method')
# class Demo3:
#     def m1(self):
#         print('demo3 m1 method')
# class Demo4:
#     def m1(self):
#         print('demo4  m1 method')
# class Demo5:
#     def m1(self):
#         #super().m1()
#         Demo3.m1(self)
#         # Demo3.super().m1()
#         print('demo5 m1 method')
# d=Demo5()
# d.m1()                                        
