# from random import*
# alp='abcdefghijklmnopqrstuvwxyz'
# job=['clerk','analyst','salesman','manager']
# loc=['chennai','bangalore','pune','hyderabad']
# digit='0987654321'

# def get_eid():
#     eid=choice(alp)+'-'+str(randint(1000,9999))
#     return eid
# def get_ename():
#     ename=choice(alp).upper()
#     for i in range(randint(4,10)):
#         ename+=choice(alp)
#         return ename
# def get_sal():
#     return uniform(1000,999999)
# def get_job():
#     return choice(job)
# def get_loc():
#     return choice(loc)
# def get_phno():
#     phno='6789'
#     no=choice(phno)
#     for i in range(9):
#         no+=choice(digit)
#     return no
# def get_emp():
#     print('eid:',get_eid())
#     print('enmae:',get_ename())
#     print('salary{:.2f}'.format(get_sal()))
#     print('job:',get_job())
#     print('loc:',get_loc())
#     print('phno:',get_phno())
#     print('--------------')

# for i in range(10):
#     get_emp()
