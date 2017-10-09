#Nested Structures from Minh weeekend lecture
# students = [ #array/list
#     {'first_name': 'Michael', 'last_name':'Jordan'}, #object/dictionary
#     {'first_name': 'John', 'last_name':'Rosales'},
#     {'first_name': 'Mark', 'last_name':'Cuban'},
#     {'first_name': 'Eron', 'last_name':'Musk'}
# ]

# for i in range(0, len(students)): #for(var i=0, i < students.length; i++)
    # print i
    # print students[i]
    # print students[i]["first_name"]
    # print students[i]["last_name"]

    # print students[i]["first_name"] + " " + students[i]["last_name"]
    #you can format by doing the following
    #print "{} {}".format(students[i]["first_name"],students[i]["last_name"])
users = {
    'Students': [
        {'first_name': 'Michael', 'last_name':'Jordan'}, #object/dictionary
        {'first_name': 'John', 'last_name':'Rosales'},
        {'first_name': 'Mark', 'last_name':'Cuban'},
        {'first_name': 'Eron', 'last_name':'Musk'}
    ],
    'Instructors': [
         {'first_name': 'Michael', 'last_name':'Choi'},
        {'first_name': 'Martin', 'last_name':'Puryear'}
    ]
}
for group in users:
    # print group
    # print users[group]
    group_of_users = users[group]
    for i in range(0, len(group_of_users)):
        # print i
        full_name = group_of_users[i]["first_name"] + group_of_users[i]["last_name"]
        print "{} - {} {} - {}".format(i+1, group_of_users[i]["first_name"], group_of_users[i]["last_name"], len(full_name))

