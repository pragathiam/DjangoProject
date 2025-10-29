#WAPP to find square of a given integer number using lambda
# square=lambda a:a*a
# print(square(2))

#WAPP to check weather the 1st value is greater than the 2nd value if 1st value is greater than the 2nd value print that number is greater else 2nd number is grater
# a=int(input('enter first value:'))
# b=int(input('enter second value:'))
# greater=lambda a,b: 'if the first value {a} is greater.' if a>b else 'if the second value {b} is greater.'
# print(greater(a,b))

#WAPP to print square of a integer number if the given value is even else print the cube of a given number
# a=int(input('enter number:'))
# square=lambda a:a*a if a%2==0 else a*a*a
# print(square(a))

#WAPP to print a value in reverse only if a given value is collection else print the value as it is
# val=lambda a:a[::-1] if type(a) in (list,tuple,str) else a
# print(val())

#WAPP to check weather the given char is present inside the given str or not if char is present then print it's initial index else print char as it is 
# str1=lambda a,b:b[0] if a in b else b
# print(str1())

#WAPP to find sum of min 3 numbers and max 5 numbers 
# sum=lambda a,b,c,d=0,e=0: a+b+c+d+e
# print(sum())

#WAPP to return true if both the input strs are exactly equal
# are_equal=lambda s1,s2:s1==s2
# print(are_equal('a','a'))
# print(are_equal('a','b'))