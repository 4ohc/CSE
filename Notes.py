# #this is working
# print ("hello world")
# print ("Welcome to class")
# # This is a comment.
# # I can use this to type in text
# # but it will never run
# """
# i wanted to type out a whole bunch
# but this is all
# text
# """
# # variables
a = 720
b = 420
# c = "the quick brown fox jumps over the lazy dog"
# print(a + b)
# print(a - 5 * b)
# print(a ** b)
# print(c)
# print(b)
# print(a * b + a - a)
# print(a / b)
# print(a ** b)
# a to the power of b
'''
the_count = [1, 2, 3, 4, 5]
shopping_list = ["noodles", "Eggrolls", "milk", "rice", "soda", "chips"]

print(shopping_list[2])

print(len(shopping_list))

# going through a list
for item in shopping_list:
    print(item)
for number in the_count:
    print(number * 9)

len(shopping_list)  # give me the length of the list
range(3)  # gives a list of the numbers 0 through 2
range(len(shopping_list))  # a list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list
    print("the item at index %d is %s" % (num, item))

# turn things into a list

str1 = "hello Class!"

listOne = list(str1)

print (listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

#add things to a list
shopping_list.append ("cereal")
shopping_list.append("Tide Pods")
print(shopping_list)
shopping_list.remove("soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)
# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

# dealing with strings
strtwo= "ThIs iS a VeRY oDd sEnTenCE"
lowercase= strtwo.lower()
print(lowercase)
'''

# Dictionaries - made up of key: Value pairs
dictionary = {'name': 'lance', 'age': 23, 'height': 5 * 12 + 7}

# Accessing dictionaries
print(dictionary ['name'])
print(dictionary['age'])
print(dictionary['height'])

large_dictionary = {
    'CA': "california",
    'FL': 'Florida',
    'OH': "Ohio",
    'AL': "Alabama"
}
print(large_dictionary['FL'])
print(large_dictionary['CA'])
print(large_dictionary['OH'])
print(large_dictionary['AL'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacramento',
        'Los Angeles'
    ],
    'FL': [
        'Tampa',
        'Orlando',
        'Miami'
    ],
    'OH': [
        "Cleavland",
        'Cincinnati'
    ],
}
print(larger_dictionary['OH'][1])

# adding to a dictionary
dictionary['weight'] = 2800000000000000000000000001

print(dictionary)

largest_dictionary = {
'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
           'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
           ]
    } ,
}
current_node = largest_dictionary['AZ']
print(current_node['POPULATION'])
print(current_node['NAME'])