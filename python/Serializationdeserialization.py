# import json
# # serialization of a dictionary
# with open('person.json','w') as file:
#     person={
#         'name':'Bhavyashree',
#         'age':20,
#         'is_student':True
#     }
#     json.dump(person,file)
#     print("Data serialized and written to person.json")
# # Deserialization of a dictionary
# with open('person.json','r') as file:
#     loaded_person=json.load(file)
#     print("Data deserialization from person.json:",loaded_person,type(loaded_person))
#     print("Name:",loaded_person['name'])
#     print("Age:",loaded_person['age'])
#     print("IS Student:",loaded_person['is_student'])


# import pickle
# # serialization of a dictionary using pickle
# with open('person.pkl','wb')as file:
#     person={
#         'name': 'Manu',
#         'age':20,
#         'is_student':True
#     }
#     pickle.dump(person,file)
#     print("Data serialization and written to person.pkl")
# # deserialization of a dictionary using pickle
# with open('person.pkl','rb')as file:
#     loaded_person=pickle.load(file)
#     print("Data deserialization from person.pkl:",loaded_person,type(loaded_person))
#     print("Name:",loaded_person['name'])
#     print("Age:",loaded_person['age']) 
#     print("Is Student:",loaded_person['is_student'])   