#PYTHON DATA TYPES
##data types in  python are - string ,integers,float,boolean,tuple,list,dict,none,set
#to know the type of the datatype use the type() 
# in python everything is an object to know the methods that the object responds to use dir()

#STRING
"""
written in either single or double quotes
"dave" or 'dave'

you can also create a string using the built in string constructor function str("this is a string")

for string interpolation use the f-string like so (f"{variable_name}")
dog-name="miles"
print(f"I love you {dog-name}")

strings have different methods like .upper() ,.lower(), .capitalize()
to know the methods that the string responds to use dir(string)
"""
dog_name="miles"
print(f"I love you {dog_name}")

price_1=2;
price_2=3.5;

print(f"Price_1 is {price_1:.2f}") #2.00
print(f"Price_2 is {price_2:.2f}") #3.50

greeting="hello"
name="dave"
print(greeting.upper())
print(greeting.lower())
print(greeting +" "+ name)
print(greeting*3)
print(type(name))
print(dir(name))

##NUMBER -float and integer
"""
Integers are whole numbers like 7
Float are numbers like 9.45

you can convert some other data types into int or float using int() and float() constructor functions

"""
link_1=1
link_2=3.0
link_3="2"
print(float(link_1))
print(float(link_3))
print(int(link_2))
print(int(link_3))


#LIST [1,2,3,4,5]
"""
data separated by comma in brackets is a list [1,2,3,4]
you can create a list with the list syntax list() this creates an empty list []

to access a value in the list you shold know its index ,indices start from 0
list_1=["A","B","C","d"]
list_1[1] ...B

to get the length of the list use len()

to sort numbers in the list use sorted()

.pop() removes the specified index
.remove removes the specified item and if there are multiple items it removes the first occurence of the item

"""
list_1=["A","B","C","d","A"]
list_2=[1,2,3]
fruits=["banana","mango","orange","banana"]
print(list_1[1]) ##acccessing a value in the list
print(len(list_1)) ##getting the length of the list
print(sorted([24,0.24,-1,9])) #sorts the numbers in the list from the smallest to the largest
print(list_2.pop()) #removes the last item when it has no value specified and it returns the item that has been removed
fruits.remove("banana") #removes the first banana it encounters
print(fruits)


##TUPLES (1,2,3)
"""
tuples are created with opening and closing parenthesis in place of square brackets
    created with the tupple() syntax constructor
    tupple([1,2,3]) ...(1,2,3)

tupples are immutable once a tupple is created it cannot be changed
    Python functions that work on lists to create new data will still work on tuples, but tuples do not contain methods like .pop() and .insert() that would change their contents.
the most common application of tupples is data being retrieved from the database.since you want to protect the data and keep a fresh record of the data

"""
items=(1,2,3,4,5,6)
print(type(items))

##SETS AND DICTS
#Sets
"""
a set is unindexed ,unordered and unchangable
    
"""