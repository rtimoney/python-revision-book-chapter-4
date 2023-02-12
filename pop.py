# changing lists

basket = ['Apple' , 'Bun' , 'Cola']
crate = ['Egg' , 'Fig' , 'Grape']

print('Basket List :', basket)
print('Basket Elements :', len(basket))

basket.append('Raisins')
print('Appended :', basket)
print('Last Item Removed :' , basket.pop())
print('Basket List :', basket)

basket.extend(crate)
print('Extended :', basket)
del basket[1]
print('Item Removed :', basket)
# delete a slice of elements from index 1 up to but not including 3
del basket[1:3]
print('Slice Removed :', basket)

nums = [35 , 10 , 23 , 1, 7 , 4 , 2 ]

# sort a list of numbers in ascending order
print('Unsorted Numbers :' , nums)
nums.sort()
print('Sorted Numbers :' , nums)

crate = ['Zebra' , 'Kayak' , 'Ant' , 'Piano', 'X-ray']

basket.extend(crate)

print('Unsorted Basket :', basket)
# sort a list of strings in alphabetical order
basket.sort()
print('Sorted Basket :', basket)



 
