# conversion
print("\n binary conversion")
print(bin(5))

print("\n string conversion")
print(type(str(5)))

print("\n float conversion")
print(float(5))

print("\n ascii conversion")
print(ord("A"))

# loops
print("\n range for loop")
# print each number from 0 to 2 (3 excluded)
for i in range(0,3):  # this won't print 3
  print(i)

print("\n array for in loop")
arr = ["apple", "banana", "cherry"]
for i in arr:
  print(i)

print("\n while loop")
j = 3
while(j != 0):  # this won't print 0
  print(j)
  j = j - 1

# sorting
print("\n sort an array reverse alphabetically")
arr.sort(reverse=True)
print(arr)

print("\n sort alphabetically")
arr.sort()
print(arr)
