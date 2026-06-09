# iter() function: A built-in Python function that returns an iterator object from an iterable (like list, tuple, string, etc.). It converts any iterable into an iterator that can be traversed one element at a time.
# Iterator: An object that implements the iterator protocol, which consists of __iter__() and __next__() methods. It represents a stream of data and returns one element at a time when next() is called on it.
# next() function: A built-in Python function that retrieves the next item from an iterator. It calls the __next__() method of the iterator object. When there are no more items, it raises a StopIteration exception.

#ex= 
fruits = ["apple", "banana", "mango", "kiwi"]

var = iter(fruits)
print(next(var))  
print(next(var)) # aise karte karte i got my all list items

# Create a tuple of subject names and access each element using iterator
s = ("Math", "Science", "English", "History")
iter1 = iter(s)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(iter1) # it give the address



# there is string python, convert the string into itrator and print each charactor
text = "python"
iter2 = iter(text)
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))


#create a dict of student detsiles as name, roll no, age, =and iter each element and each itration line by line values got print like 1st name print then roll no etc...

student = {"name:": "John", "roll_no:": 101, "age:": 20}
iter3 = iter(student.items())
for k, v in iter3:
    print(k, v) 


