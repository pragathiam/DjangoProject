#print(bool(0))

#Logical operators
#And 
#print(5 and 0)
#print(5 and 3)
#print(6+5j and 0j and {} and 6)

#Or
#print(3 or 5j or {})
#print({} or 0j)

#And,Or 
#print(0j and {} or 2j and [1,2,3])

#Relational Operator[==,!=,>,<,>=,<=]
#a=[1,2,3]
#b=(1,2,3)
#print(a==b)    o/p: False

#a=(1,2,3)
#b=(3,1,2)
#print(a==b)    o/p: False

#print([10,6,4]>[5,3,4])   o/p: True
#print([10,6,4]>[10,6,4])   o/p: False
#print(['a','b','c']>=['A','B','C'])  o/p: True
#print(10>=10)  o/p: True

#a=40
#print(id(a))  o/p:140724969023624  [not hexa decimal]

#print(hex(id(10)))

#print([10,40,50]>=[10,40,50])  o/p: True
#print([10,40,50]>=[10,40,50,60])  o/p: False

#Bitwise Operator[&(and),|(or),^(xoy),~(/n),>>(right shift),<<(left shift)]

#Control Statements
#n=int(input("ente the num:"))
#if n%2==0:
#    print("even no")
#else:
#    print("odd:")    

#To find our string is palindrome or not
#str01=input("enter the string")
#if str01==str01[0::-1]
#    print("palindrome")
#else:
#    print("not a palindrome")   


#ch=input("enter the char:")
#if ch in ['A','E','I','O','U','a','e','i','o','u']:
#    print("vowels")
#else:
#    print("consonants")     


#To find the first letter is vowel or not
#str01=input('enter the string:')
#if str01 in 'AEIOUseiou':
#    print('vowels')
#else:
#    print('consonants')    

#Weather the length is upper or lower case
#str01=input('enter the string:')
#if str01[0].isupper():
#    print('upper case')
#else:
#    print('lower case')    

#str01=input('enter the string:')
#if 'A'<=str01<='Z':
#    print('upper case')
#else:
#    print('lower case')   


#Weather the 
#str01=input('enter the string:')
#if len(str01)%2==0:
#    print('even length')
#else:
#    print('odd length')    

#elif
#n1=int(input('enter the first value:'))
#n2=int(input('enter the second value:'))
#if n1>n2:
#    print('n1 is greater')
#elif n1==n2:
#    print('both are equals')
#else:
#    print('n2 is greater')

#4 quad
#n1=int(input('enter n1:'))
#n2=int(input('enter n2:'))
#if n1>0 and n2>0:
#    print('first quad')
#elif n1<0 and n2>0:
#    print('second quad')
#elif n1<0 and n2<0:
#    print('third quad')
#else:
#    print('forth quad')    

#Nested if
#collection value string #palindrome
# input01=eval(input('enter the value:')
# if type(input01)==str:
#     if input01==input01[::-1]:
#         print('it is palindrome')
#     else:
#         print('string is not palindrome') 
# else:
#     print('it is not string')

#Check weather the upper,lower,digit or special character
# ch=eval(input('enter a value:'))
# if ch.isupper():
#     print('is upper case')
# elif ch.islower():
#     print('is lower case')
# elif ch.isdigit():
#     print('is digit')
# else:
#     print('is special character')     

#n1,n2,n3,n4 --> greatest 


#Greater number among 3
# a,b,c=10,20,30
# if a>b and a>c:
#     print('a is greater')
# elif b>a and b>c:
#     print('b is greater')
# else:
#     print('c is greater')        

# a,b,c,d=100,20,30,400
# if a>b and a>c and a>d:
#      print('a is greater')
# elif b>c and b>d:
#      print('b is greater')
# elif c>d:
#      print('c is greater')        
# else:
#      print('d is greater')

#2nd greatest number amoung 4
# a,b,c,d=10,20,30,40
# if a>b and a>c and a>d:
#     if b>c and b>d:
#      print('b is 2nd greatest')
#     elif c>d:
#        print('c is 2nd greater')
#     else:
#        print('d is 2nd greater')
# elif b>c and b>d:
#     if a>c and a>d:
#       print('a is 2nd greatest')
#     elif c>d:
#       print('c is 2nd largest')
#     else:
#       print('c is 2nd largest')
# elif c>d:
#     if a>b and a>d:
#       print('a is 2nd largest')
#     elif  b>d:
#        print('b is 2nd greater') 
# else:
#    print('d is 2nd greatest')                            

#Looping stmts: While Loop
# i=0
# while i<5:
#     print('Hello india')
#     i+=1

#even numbers b/w 1 to 20
# i=10
# while i<=20:
#     if i%2==0:
#      print(i)
#     i+=1

#10,3j,40,5j,60
# a=[10,3j,40,5j,60]
# i=0
# while i<len(a):
#     if type(a[i])==complex:
#         print(a[i])
#     i+=1

# i=1
# while i<=5:
#     if i==2:
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=5:
#     if i==2:
#         i+=1
#         continue
#     print('i')
#     i+=1

# i=1
# while i<=5:
#      if i==2:
#          i+=1
#          break
#      print('i')
#      i+=1

# for loop
# s={1,2,3,5}
# for i in s:
#     print(i)

# l=[10,20,30,60]
# for i in l:
#     print(i)

#vowels
# st = 'dinesh'
# out=[]
# for i in st:
#     if i in 'AEIOUaeiou':
#         #print(i)
#         #out.append(i)
#         out+=[i]
# print(out)

#or 

# st = 'dinesh'
# for i in st:
#     if i in 'AEIOUaeiou':
#         print(i)

# st=(1,3.5,'hii',6j,'Travel')
# out={}
# for i in st:
#     if type(i)==str:
#         out[i]=len(i)
# print(out)               o/p: {'hii':3,'travel':6}


# st="Hello we are ready for trek"
# a=""
# for i in st:
#     if i==" ":
#         a+="_"
#     else:
#         a+=i
# print(a)             o/p: "Hello_we_are_ready_for_trek"       

#OR

#st.replace(old,new) it is inbuild fuction we can use this for projects.

#check weather it is palindrome r not without using slicing 
# Question (st='Diving')
# st=input('enter the string:')
# st2=''
# for i in st:
#     st2=i=st2
# if st==st2:
#     print('palindrome')
# else:
#     print('not a palindrome')    

#Functions
#Check weather the number is odd r even
# def even(a):
#     if a % 2 == 0:
#         print("Even")   or  return "even"
#     else:
#         print("odd")    or  return "odd"
# even(10)        

#Find the length without using length function(in function)
#n=153

#Leap Year
# n=int(input('enter the year:'))
# if(n%4==0 and n%100!=0) or n%400==0:
#    print('hurry it is a leap year')
# else:
#     print('not a leap year')

#Fibonacci series
# def fibonacci(n):
#     n1=0
#     n2=1
#     print(n1)
#     print(n2)
#     for i in range(n-2):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#     print(n3)
# fibonacci(6)    

#Prime Number
# n=12
# for i in range(2,n):
#     if n%i==0:
#         print('not a prime number')
#     else:
#         print('prime number')  


# def primeno(n):
#     for i in range(2,n):
#         if n%2==0:
#             return False
#     return True    
# print(primeno(7))

#Decimal to binary
# a=int(input('enter'))
# binary=''
# while a>0:
#     binary=str(a%2)+binary
#     a//=2
# print(binary)    

# or 

# n=8
# v=str()
# while n>0:
#     i=n%2
#     n=n//2
#     v=str(i)+v
# print(v)   

#Pattern Matching
# n=5
# for i in range(1,n+1):
#     for j in range(n*2-1):
#         if n==i+j or j-i==n-2 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print() 

# OR 

# n=int(input('enter the number'))

# for i in range(1,n+1):
#     for j in range(1,2*n):
#         if i==n or j-i==n-1 or i+j==n-1:
#             print('*',end='')
#         else:
#             print(' ',end=' ')
#     print()            

#First n(10) even  number
# n=10
# i=0
# count=0
# while count<n:
#     if i%2==0:
#         print(i)
#         count+=1
#     i+=1    

#OR 
# n=10
# i=0
# count=0
# while True:
#     if i%2==0:
#         print(i)
#         count+=1
#     i+=1
#     if count==10:
#         break    

#First n prime number 
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
   
# def first_prime(a):
#     count=0
#     i=2
#     while True:
#         if prime(i):
#             print(i)
#             count+=1
#         i+=1
#         if count==a:
#             break
# first_prime(20)       

#Happy Number
# def happy_number(n):
#     sum1=n
#     temp=n
#     while sum1>9:
#         sum1=0
#         while temp>0:
#             rem=temp%10
#             sum1=rem*rem
#             temp//=10
#         temp=sum1
#     if sum1==1 or sum1==7:
#         return True
#     return False
# print(happy_number(19))               o/p:True


#Pattern Matching
# i=1
# n=9
# st=1
# sp=n//2
# while i<n+1:
#     for j in range(sp):
#         print(' ',end=' ')
#     for j in range(st):
#         print('*',end=' ')
#     if i<n//2+1:
#        st=st+2
#        sp=sp-1
#     else:
#         st=st-2
#         sp=sp+1 
#     print()
#     i=i+1          

#Half Butterfly
# n=5
# st=1
# sp=2*n-2 # 7
# i=1
# while i<=n:
#     for j in range(st):
#         print('*',end=' ')
#     for j in range(sp):    # or for j in range(sp+1): 
#         print(' ',end=' ') 
#     for j in range(st):
#         print('*',end=' ')
#     st=st+1
#     sp=sp-2
#     i=i+1
#     print()


# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# out={4,5} using while loop

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# list_s1=list(s1)
# i=0
# out=set()
# while i<len(list_s1):     #//5 times
#     if list_s1[i] in s2:
#         out.add(list_s1[i])
#     i+=1
# print(out)    

# OR

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# out=set()
# i=0 
# while s2:
#     a=s2.pop()
#     if a in s1:
#         out.add(a)
# print(out)        

#Pattern Matching
# n = 5
# st = n*2-1
# sp = 0
# i = 1
# while i < n+1:
#     for j in range(sp):
#         print(' ',end=' ')
#     for j in range(st):
#         print('*',end=' ') 
#     print()
#     sp += 1
#     st -= 2
#     i += 1

#l=[[1,2,3],
#  [8,9,4],
#  [6,7,5]]

# l=[[1,2,3],
#   [8,9,4],
#   [6,7,5]]
# output=[]
# output+=l[0]
# output.append(l[1][2])
# output.append(l[2][2])
# output+=l[2][1::-1]
# output.append(l[1][0])
# output.append(l[1][1])
# print(output)   

#OR

# l1=[[1,2,3],
#   [8,9,4],
#   [6,7,5]]
# out=[]
# for i in range(len(l1)):
#     if i%2==0:
#         for j in range(len(l1[i])):
#          out.append(l1[i][j])
#     else:
#         for j in range(len(l1[i])):
#            b=l1[i][::-1]
#            out.append(b[j])  
#     out.extend(l1[i])
#     out.extend(l1[i][::-1])
#     print(out)  


# l1=[1,2,1000,1050,4,3]
# out=4

# l1=[1,2,1000,1050,4,3]
# out=[]
# out.append(l1[4])
# print(out)

#ugly number only divided by 2,3,5
# n=6
# if n<=0:
#     print('not a ugly number')
# else:
#  while n%2==0:
#     n//=2
#  while n%3==0:
#     n//=3
#  while n%5==0:
#     n//=5
#  if n==1:
#     print('ugly number')
#  else:
#     print('not  a ugly number')    

# str01='433'
# out=433
# str02='--100'
# output=-100
# str03='1345+ab4'
# output=13457
#str04='-15'
# ouut=-15
# str05='[][]54'
# out=54
# str06='4479acb'
# out=4479

str01='433'
str02='--100'
str03='1345+ab4'
str04='-15'
str05='[][]54'
str06='4479acb'
n=0
while  i<len(str01) and str[i]==' ':
    i+=1
sign=1
if i<n and (str[i]=='-' or str[i]=='+'):
    if str[i]=='-':
        sign=-1
    elif str[i]=='+':
        sign=1
    i+=1
res=0
while i<n and str[i].isdigit():
    res=res*10+i*(str[i])   
    i+=1
return sign*res         



# n=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(n%2,end=' ')
#             n+=1
#         else:
#             print(' ',end=' ')   




     















