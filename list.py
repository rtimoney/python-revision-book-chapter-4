# writing lists 
# Python does not have arrays like in other languages but it does have 'lists' which work in much the same way 

# in Python we cannot declare a variable without initializing with a value

#multiple variables can be declared with common values
a = b = c = 10

#multible variables can be initialized with different values in a single statement using comma separators
d , e , f = 1 , 2 , 3

# creating a list
# we can reference an element within the list using its index
# as with other languages indexes begin at 0 so intex 1 references the second entry

listnums = [0,1,2,3,4,5]
# listnums[0] is 0
# listnums[1] is 1 etc

listcolours = ['green','blue','red','yellow','orange','purple']
# listcolours[0] is green
# listcolours[1] is blue
# listcolours[2] is red
# listcolours[3] is yellow
# listcolours[4] is orange
# listcolours[5] is purple

# demonstration

quarter = ['January','February','March']

print('First Month :', quarter[0])
print('Second Month :', quarter[1])
print('Third Month :', quarter[2])

coords = [[1,2,3],[4,5,6]]

print('\nTop Left 0,0 :', coords[0][0])
print('\nBottom Right 1,2 :', coords[1][2])
print('\nSecond Month First Letter :', quarter[1][0])

# string indices can also be given as negative numbers starting with -1 as the last character, -2 as the second last etc
print('\nSecond Month Last Letter :', quarter[1][-1])

