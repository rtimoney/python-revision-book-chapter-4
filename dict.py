# Naming Elements

# In Python a Dictionary is a data container that can store multiple items of data as a list
# .... of Key:value pairs
# elements are referenced by their key rather than an index number
# essentially Pythons version of an associative array

info = {'name':'Bob','ref':'Python','sys':'Win'}
print('info :' , type(info))
print('Dictionary :' , info)

print('\nReference :' , info['ref'])

print('\nKeys :' , info.keys())

del info['name']
info['user'] = 'Tom'
print('\nDictionary :' , info)

print('\nIs there a name Key? :' , 'name' in info)
