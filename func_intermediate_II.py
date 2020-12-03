# A -- Update Values in Dictionaries and Lists
    # 1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    # 2) Change the last_name of the first student from 'Jordan' to 'Bryant'
    # 3) In the sports_directory, change 'Messi' to 'Andres'
    # 4) Change the value 20 in z to 30

# 1) 
x = [ [5,2,3], [10,8,9], [5,5,5]] # change 10 to 15 using a function/for loop  -- I added a third list to x to see if my targeting worked, and it did!
x[1][0] = 15 # target
x[2][2] = 15
print(x)

# 2)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'  # target the first index (first_name: Michael, 'last_name' : Jordan -- this whole thing is index [0]) and change it to Bryant.

print(students) 


# 3)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres' # target the list sports_directory, and the index [0] of that list, and change it to Andres.  I could have also just not typed [0], and entered all three names but that would be more lines to add.
print(sports_directory)


# 4) Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30 # target the first index value of z, which is [0], then target whatever you wanna change, in this case 'y'.
print(z)



# B -- Iterate through List of Dictionaries
    # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}  # so this is the list of dictionaries and associated key-value pairs we are given
    ]

def keyvaluepair(list):  # So i created a function that will be passed an array, aka list.
    for i in list:  # here's where I wanna iterate through the entire list, in this case 'students'
        print(i)  # just print it! It should pop up exactly in the same format as above.

keyvaluepair(students)  # call the function.


# C -- Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}  # so this is the list of dictionaries we are given
    ]


def keyvaluepair2(key, list):  # so once again, creating a function that we will pass parameters of the key name, in the parent list (because if you list the parent list first, you'll get an error message saying you can't pass strings as indices).
    for i in key: #iterate through the list of keys
        print(i[list]) # print all those values in whatever list we're iterating through
keyvaluepair2(students, 'first_name') # when I call the function, I have to pass it the arguments i want to print, which is basically saying "Hey computer, print me the first names of all the students in this list"
keyvaluepair2(students, 'last_name') # similarly, if i wanted to print the last names, do the same thing.

# --------------------------

# keyvaluepair2(students, 'first_name', 'last_name')  # this should print out the first and last names next to each other

# it did not! 

# --------------------------


# D -- Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'] #here is the dictionary that contains values that are all lists (2 lists, technically -- pay attention to the brackets)
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon