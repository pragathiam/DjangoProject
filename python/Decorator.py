# def decor1(func):
#     def inner1():
#         print('inner1')
#         return inner1
# def decor2(func):                        o/p:inner2
#     def inner2():
#         print('inner2') 
#     return inner2
# @decor2
# @decor1
# def disp():
#     print('display func')
# disp()           


# def decor1(func):
#     def inner1():
#         print('decor1 func...')
#         func()
#     return inner1
# def decor2(func):                            o/p:decor2 func
#     def inner2():                                decor1 func
#         print('decor2 func...')                  original func...!
#         func()
#     return inner2
# @decor2
# @decor1
# def disp():
#     print('original func..!')
# disp()                                

                                           

