n=int(input("Enter users count:"))
space="\n"*2*n
print(space)
person_list=[]

for item in range(n):
    person_dict=dict()
    name=input("Enter user.name:")
    age=int(input("Enter user.age:"))
    person_dict["name"]=name
    person_dict["age"]=age
    person_list.append(person_dict)
print(person_list)
search=input("Enter name to search:")
for i in person_list:
    if i['name']==search:
        print(i["age"])
        break
    else:
        print("There is no user with given name!")
        break