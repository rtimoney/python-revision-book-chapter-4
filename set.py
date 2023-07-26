# Setting Lists 

#Python sets are restrictive lists of unique values surrounded by braces {curly brackets}  


# initializing a set for demonstration purposes
party_goers = {'Andrew', 'Barbara' , 'Carole' , 'David'}
print('party_goers :' , type(party_goers))

print('Did David go to the party?' , 'David' in party_goers)
print('Did Kelly go to the party?' , 'Kelly' in party_goers)

students = {'Andrew' , 'Kelly' , 'Lynn' , 'David'}

commons = party_goers.intersection(students)

# list function may not place element values in the same order as they appear in the set
party_students = list(commons)

print('Students at the party : ' , party_students)
print('First student at the party : ' , party_students[0])



