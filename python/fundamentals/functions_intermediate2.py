
# x = [ [5,2,3], [10,8,9] ]
# x[1] = [15,8,9]
# print(x[1])


# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0] = {'first_name':  'Michael', 'last_name' : 'Bryant'} 
# print(students)

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'] = ['Andres', 'Ronaldo', 'Rooney']
# print(sports_directory)

# z =  {'x': 10, 'y': 20}
# z['y'] = 30
# print(z)

# def iterateDictionary(dict):
#     for i in range(len(dict)):
#         for key, val in dict[i].items():
#             print(key, "-", val)


# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# z = iterateDictionary(students)

# print(z)


# def iterateDictionary2(key_name, some_list):


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# # for i in range(len(students)):
# #     for val in students[i].values():
# #         print(val)

# def iterateDictionary2(value, dict):
#     for i in range(len(dict)):
#         for val in dict[i].values():
#             print(val)

# w = iterateDictionary2('first_name', students)
# print(w)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# for key, val in dojo.items():
#     print(key, "-", val)

def printInfo(dict):
    for key, val in dict.items():
        print(key, " ", val)
        print(len(val))


y = printInfo(dojo)
print(y)