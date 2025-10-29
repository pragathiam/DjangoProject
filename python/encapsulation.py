# class Employee:
#     def __init__(self,eid,name,sal,job):
#         self.__eid=eid
#         self.__ename=name
#         self.__sal=sal
#         self.__job=job
#     def get_eid(self):
#         return self.__eid
#     def set_eid(self,eid):
#         self.__eid=eid
#     def get_ename(self):
#         return self.__ename
#     def set_ename(self,name):
#         self.__ename=name
#     def get_sal(self):
#         return self.__sal
#     def set_sal(self,sal):
#         self.__sal=sal
#     def get_job(self):
#         return self.__job
#     def set_job(self,job):
#         self.__job=job
# e=Employee(101,'manu',10000,'clerk')
# print('eid:',e.get_eid()) 
# print('ename:',e.get_ename()) 
# print('sal:',e.get_sal()) 
# print('job:',e.get_job())
# e.set_sal(3000000)
# e.set_job('manager')
# print('eid:',e.get_eid())                

# class Student:
#     def __init__(self,sid,name,branch):
#         self.__sid=sid
#         self.__name=name
#         self.__branch=branch
#     def get_sid(self):
#         return self.__sid
#     def set_sid(self,sid):
#         self.__sid=sid
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name=name
#     def get_branch(self):
#         return self.__branch
#     def set_branch(self,branch):
#         self.__branch=branch  
# s=Student(101,'manu','ise')
# print('sid:',s.get_sid())  
# print('name:',s.get_name()) 
# print('branch:',s.get_branch()) 
# s.set_branch('cse')
# print('branch:',s.get_branch())        


# class Employee:
#     def __init__(self,id,name,sal):
#         self.__id=id
#         self.__name=name
#         self.__sal=sal
#     @property
#     def id(self):
#         return self.__id
#     @id.setter
#     def id(self,id):
#         self.__id=id
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
#     @property
#     def sal(self):
#         return self.__sal
#     @sal.setter
#     def sal(self,sal):
#         self.__sal=sal
    
# e=Employee(101,'josh',80000)
# print(e.id)

# from abc import abstractmethod, ABC
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#     def m3(self):
#         print('m3 method....')
# class Demo1(Test):
#     def m2(self):
#         print('m2 method...')
# class Demo2(Demo1):
#     def m1(self):
#         print('m1 method...')  
# d2=Demo2()
# d2.m1()                     