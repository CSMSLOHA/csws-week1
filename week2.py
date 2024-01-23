numbers = ["one","two","three","four"]
#prnt the whole list
print(numbers)

#computing the length
print(len(numbers))

#print the first element of a list 
print(numbers[0])

#print in uppercase
print(numbers[0].upper())

#access the last element
print(numbers[-1])

#modifying asn element 
numbers[0]= "zero"
print(numbers)

#adding an element at the end
numbers.append("ten")
print(numbers)

#inserting an element 
numbers.insert(2,"ten")
print(numbers)

#deleting an element
del numbers[1]
print(numbers)

#removing an element by name 
numbers.remove("ten")
print(numbers)

#reusing deleted item
x=numbers.pop(2)
print(numbers)