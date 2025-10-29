#given value is palindrom r not 
# def is_palindr(value):
#    value=str(value)
#    return value == value[::-1]
#test_value=input('enter a value to check:')
#if is_palindr(test_value):
#    print(f"'{test_value}' is a palindr!")
#else:
#    print(f"'{test_value}'is not a palindr.")    


#collection r individual datatype
#def is_collection(value):
#    return isinstance(value,(list,tuple,set,dict))
#test_value=[1,2,3]
#if is_collection(test_value):
#    print(f"the value {test_value} is a collection datatype.")
#else:
#    print(f"the value {test_value} is an individual datatype.")    


#I/P Hi good morning O/P {'Hi':2,'good':4,'morning':7}
#def word_length_mapping(sentence):
#    words = sentence.split()
#    return {word: len(word) for word in words}
#sentence = input("Enter a sentence: ")
#result = word_length_mapping(sentence)
#print(result)

#OR

#input='hi good morning'
#ip=input.split()
#out={}
#for i in ip:    
#    out[i]=len(i)
#print(out)    


#Word only have a even characters
#def filter_even_length_words(sentence):
#    words = sentence.split() 
#    return [word for word in words if len(word) % 2 == 0]
#sentence = input("Enter a sentence: ")
#result = filter_even_length_words(sentence)
#print("Words with even number of characters:", result)

#OR

#ip='hi good morning'
#x=ip.split()
#d={}
#for i in x:
#    if len(i)%2==0:
#        d[i]=len(i)
#print(d)        


# l1=[10,20,30,'manu']
# l2=[]
# for i in l1:
#     if type(i) in(int,float,bool,complex):
#        l2.append(i)
# print(l2)       

