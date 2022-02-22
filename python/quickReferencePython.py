print("\n\n   CONVERSIONS AND TYPES")
print("\n binary conversion")
print(bin(5))

print("\n string conversion")
print(str(5))

print("\n float conversion")
print(float(5))

print("\n ascii conversion")
print(ord("A"))

print("\n get a type")
print(type("7"))

print("\n\n   LOOPS")
print("\n range for loop")
# print each number from 0 to 2 (3 excluded)
for i in range(0,3):  # this won't print 3
  print(i)

print("\n use indexes of a list")
pokemon = ["pikachu", "mew", "poliwhirl"]
for i in range(len(pokemon)):
  print(i)

print("\n iterate over list items")
arr = ["apple", "banana", "cherry"]
for i in arr:
  print(i)

print("\n get both index and item during iteration")
for index, item in enumerate(arr):
  print(index, item)

print("\n iterate over key value pairs in a dictionary")
dict_example = {"a": 1, "b": True, 300: [1,2,"zoo"]}
for key, value in dict_example.items():
  print(key, value)

print("\n while loop")
j = 3
while(j != 0):  # this won't print 0
  print(j)
  j = j - 1

print("\n\n   SORTING")
print("\n sort a list reverse alphabetically")
arr.sort(reverse=True)
print(arr)

print("\n sort alphabetically")
arr.sort()
print(arr)

print("\n\n   INPUT AND STRING INSERTION")
print("\n getting input and string insertion")
name = input("What is your name? ")
print(f"Your name is: {name}")

print("\n\n   STRING MANIPULATION")
word = "eXaMpLe"
sentence = "as far as the eye can see."
print(f"\nword: {word}")
print(f"sentence: {sentence}")
print(f"\nword.upper() does all uppercase: {word.upper()}")
print(f"\nword.lower() does all lower: {word.lower()}")
print(f"\nsentence.capitalize() capitalizes the first word of a sentence: {sentence.capitalize()}")
print(f"\nyou can chain together like word.lower().capitalize() and get\
 (the next layers over the previous): {word.lower().capitalize()}")
print(f"\nsentence.count('substring') let's you see how many times the substring (case sensitive)\
  appears in the string like sentence.count('as'): {sentence.count('as')}")
print(f"len(sentence) gives you the number of characters in a string: {len(sentence)}")

print("\n\n   LIST MANIPULATION")
list_1 = ["apple", "banana", "cherry"]
print(f"\nHere is the list we are using for the example: {list_1}")
print(f"\nlen(list_1) gives you the number of items: {len(list_1)}")
list_1.append('dragon fruit')
print(f"\nlist_1.append('dragon fruit') adds something to the end of the list: {list_1}")
list_1.extend(['elderberry', 'fig'])
print(f"\nlist_1.extend(['elderberry', 'fig']) will take all of the elements from the parentheses and append them: {list_1}")
list_1.pop()
print(f"\nlist_1.pop() removes AND returns the last item in a list: {list_1}")
list_1.pop(2)
print(f"\nlist_1.pop(2) you can also use an index in pop to remove AND return a specific element: {list_1}")
del list_1[1]
print(f"\ndel list_1[index] let's you delete a list item by its index, del list_1[1]: {list_1}")

print("\n\n   SLICES")
print("\ncan be used on strings, lists, and tuples")
print("list[start:stop_exclusive:step] each value is optional")
print("list[2:] means start at element 2 and stop at the end")
print("list[::-1] will go backwards one element at a time")

print("\n\n   LIST COPYING AND REFERENCES")
print(f"\nlists are mutable, meaning they can be changed. list_2 = list_1 makes a reference to list_1,\
 meaning changing list_1 will change list_2,\
 to instead copy a list, you would need to do list_3 = list_1[:]")
list_2 = list_1
list_3 = list_1[:]
list_1.pop()
print(list_2) # we will see that elderberry is missing in list_2 because it referenced list_1
print(list_3) # we will see elderberry is NOT missing in list_3 because we copied list_1

print("\n\n   TUPLES")
print("\n tuples are just like lists, but are immutable (no changing elements, pop, or append),\
 you just use () instead of []")
tuple_1 = (1,2,3)

print("\n\n   SETS")
print("A set is an unordered list")
print("Extremely fast, can be manipulated in constant time O(1), so the val in set is much faster than\
 val in list, which is linear O(n)")
x = set()
x = {1,200,32}
x2 = {200, 58}
print(200 in x)
print(x.union(x2)) # has all values of the two sets, so full venn diagram
print(x.difference(x2)) # has only the unique values in each set, so venn diagram with middle removed
print(x.intersection(x2)) # has only the shared values in each set, so only middle of venn diagram

print("\n\n   DICTIONARIES")
print("Collection of key, value pairs. Very similar to a hash table or a map")
print("Values can be all sorts of data types, lists, dictionaries, tuples, sets")
print("Can assume constant time for add, delete, and read, although there could be hash collisions")
dict_1 = {"key": 1}
dict_1["key2"] = "whatever" # this adds a new key value pair to the dictionary
dict_1[2] = True # notice a key can be an int
dict_1["list1"] = list_1
dict_1["dict2"] = {"ex1": "hi", "ex2": 3}
dict_1["set1"] = x
print(dict_1)
print("key" in dict_1) # let's you check if a key is in the dictionary
print(list(dict_1.values())) # gets all values in the dictionary and puts it in a list
print(list(dict_1.keys())) # gets all keys and puts it in a list
del dict_1["key"] # removes the key value pair at the specified key
for key, value in dict_1.items():
  print(key, value)

print("\n\n   TRY/EXCEPT/FINALLY")
try:
  x = 7/0
except Exception as e:
  print(e)
finally:
  print("finally happens no matter what")

print("\n\n   MAP")
print("\n maps will execute a function on all elements of a list")
print("\nyou can replace the lambda part with a call to a function instead")
prices = [5.0, 21.99, 17.5]
increase_10_percent = map(lambda element: element * 1.1, prices)
# increase_10_percent = map(function_name, prices) # function call example
print(list(increase_10_percent)) # map() returns a map object, so let's convert it to a list

print("\n\n   FILTER")
print("\n filter will iterate through a list and will include it in the result if it meets the condition")
print("\nlike with map, you can replace the lambda part with a call to a function instead")
prices = [5.0, 21.99, 17.5]
over_15_dollars = filter(lambda element: element > 15, prices)
# over_15_dollars = filter(function_name, prices) # function call example
print(list(over_15_dollars)) # map() returns a map object, so let's convert it to a list
