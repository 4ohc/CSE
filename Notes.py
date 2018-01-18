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
print(listOne.join(" "))