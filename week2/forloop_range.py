# Range
for i in range(0, 5, 1):
	print(i)

my_range = range(8)
for h in my_range:
	print(h)

# Iterable: String
for x in "The fox":  # "The quick brown fox jumps over the lazy dog"
	print(x)

# Iterable: List
myList = ["apple", "banana", "cherry"]
print(myList)

for i in myList:
	print(i)

# Iterable: Tuple
myTuple = ("car", "plane", "boat")
print(myTuple)

for i in myTuple:
	print(i)

# Iterable: Dictionary
myDict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

for x in myDict:
	print(x, ":", myDict[x])

# Iterable: Set
mySet = {"dog", "cat", "fish"}

for x in mySet:
	print(x) 
