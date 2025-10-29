#import re
#exp=re.finditer('aa','abcaaabcdaa')
#for i in exp:
#    print(i.start(),'____',i.end()-1,'___',i.group())

#import re
#snt=input('enter sentence:')
#exp=re.finditer('[0-9]{10}',snt)
#for i in exp:
#   print(i.start(),'____',i.end()-1,'___',i.group())

#match(pat,targetedstr)------>it will return output object not matching not return any object
#import re
#m=re.match('ma','manu') #in the oplace of ma if we give ga the output will be the (no match)
#if m is not None:
#    print('pattern matched')
#    print(m.group())
#else:
#    print('no match...!')

#import re
#m=re.match('manu','manu') 
#if m is not None:
#    print('pattern matched')
#    print(m.group())
#else:
#    print('no match...!')

#Search
# import re
#m=re.match('manu','python is easy manu') 
#if m is not None:
#    print('pattern matched')
#    print(m.group())
#else:
#    print('no match...!')

#findall
#import re
#m=re.findall('[7-9]','jio7hotstar9u432')
#print(m)

#Substitute
#import re
#m=re.sub('a','#','nayana')
#print(m)

#import re
#m=re.subn('a','$','nayanaa')
#print(m)

#Split
#import re
#m=re.split('-','josh-manu-jio-indu-bindu')
#print(m)

#phone number starts with 6,7,8,9
#import re
#txt=input('enter sent:')
#exp=re.search('[6-9][0-9]{9}',txt)
#if exp:
#    print('match no found....!')
#    print(exp.group())
#else:
#    print('match no found')

#import re
#txt='manoj 8765432109 and 9087654321 and 8765432121'
#exp=re.findall('[6-9][0-9]{9}',txt)
#print(exp)

#import re
#txt='manoj 8765432109 and 9087654321 and 8765432121'
#exp=re.finditer('[6-9][0-9]{9}',txt)
#for i in exp:
#    print(i.group(),'--',i.start(),'----',i.end()-1)

#Applying Boundry
#phone number starts with 6,7,8,9
#import re
#txt=input('enter sent:')
#exp=re.search(r'\b[6-9][0-9]{9}\b',txt)
#if exp:
#    print('match found....!')
#    print(exp.group())
#else:
#    print('match no found')

#import re
#txt='manoj 8765432109 and 9087654321 and 8765432121'
#exp=re.findall(r'\b[6-9][0-9]{9}\b',txt)
#print(exp)

#import re
#txt='manoj 8765432109 and 9087654321 and 8765432121'
#exp=re.finditer(r'\b[6-9][0-9]{9}\b',txt)
#for i in exp:
#    print(i.group(),'--',i.start(),'----',i.end()-1)

#\d
#import re
#txt=input('enter sent:')
#exp=re.search(r'\b[6-9]\d[0-9]{9}\b',txt)
#if exp:
#    print('match no found....!')
#    print(exp.group())
#else:
#    print('match no found')

#import re
#txt='manoj 8765432109 and 9087654321 and 8765432121'
#exp=re.findall(r'\b[6-9]\d[0-9]{9}\b',txt)
#print(exp)

#import re
#txt='manoj 8765432109 and 9087654321 and 8765432121'
#exp=re.finditer(r'\b[6-9]\d[0-9]{9}\b',txt)
#for i in exp:
#    print(i.group(),'--',i.start(),'----',i.end()-1)

#Find words in 5 sentence 
#import re
#txt=input('enter a sent:')
#exp=re.search(r'\b[a-zA][5]\b',txt)
#if exp:
#    print('match found....!')
#    print(exp.group())
#else:
#    print('match no found')

#import re
#txt='indu bindu manoj aishu usha'
#exp=re.findall(r'\b[a-zA]{5}\b',txt)
#print(exp)

#import re
#txt='indu bindu manoj aishu usha'
#exp=re.finditer(r'\b[a-zA]{5}\b',txt)
#for i in exp:
#    print(i.group(),'--',i.start(),'----',i.end()-1)

#Pattern for gmail
#import re
#txt='indu@gmail.com bindu.j@gmail.com ab@gmail.com'
#pattern = r'\b[a-zA-Z0-9.%_]+@gmail\.com\b'
#matches = re.findall(pattern, txt)
#print(matches) 




