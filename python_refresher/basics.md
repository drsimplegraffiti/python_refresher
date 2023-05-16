#### Fundamental data types

str
bool
float
int
list
set
dict
tuple

#### Classes -> custom class
#### Specialized Data types
#### None -> the absence of value

---

#### Integers -> whole numbers
```python
print(2+8)
print(4-9)
print(type(5))
```

#### floating point
```python
print(type(0.023)) #floats
```


#### Math function
```python
print(min(8,0)) #0
print(round(4.9)) #5
print(abs(-89))
```

#### binary
```python
print(bin(10)) #0b1010
print(int(0b1010))
```

#### Variable naming
```python
Dont create variables with two __ called dunders
Use snake_case over camel casing
```

#### Expression vs Statement
An expression is a piece of code that produces a value
```python
iq = 89   # statement
user_age = iq/9

iq/9 is an expression
```

A statement is the entire line of code
```python
user_age = iq/9 the whole line is a statement that performs action
```

---

##### Augmented Assignment Operator
```python
some_value = 2
some_value+=4
print(some_value)
```

---

#### String
Using triple quotes for multi line strings must be a single quote
```python
some= '''
0 0
 -
 V
'''
print(some)
```

---

#### Escape Sequence
```python
weather = "it's \"kind of\" sunny"
print(weather)
```


---

##### String indexing
```python
name = "Joseph Lieya"
#          start:stop:stepover
print(name[0:7:2])
```

```python
name = '1234567'
print(name[-1])

```

---

##### String immutability
```python
name = '1234567'
name[0] = '0'
print(name) #ERROR

```


---

##### Built in functions and methods
Functions e.g `print()` | `abs()`
```python
len()
abs()

```

Method has `.` after a function

---

##### input
```python
birth = input("year of birth? ")

age = 2023 - int(birth)
print(f"year of birth is {age}")
```

---

#### Lists
```python
amazon = [
    "notebooks",
    "sunglasses",
    "robots",
    "toys"
]

# List slicing
print(amazon[0:1])
print(amazon[1::1])

# List are mutable
amazon[0]= "lappy"
print(amazon)

```

---

##### 2 Dimensional Arrays
```python
matrix = [
    [1,0,1],
    [0,1,0],
    [0,0,1]
]

print(matrix[0][2])
```


#### list methods
```python
matrix = [1,2,3,4,5,6]
matrix.append(0)
matrix.insert(3, 89)

matrix.pop()
matrix.pop(0)
matrix.remove(3)
print(matrix)
```

---

#### range
```python
li = list(range(1,20))
print(li)
```


---

####    List unpacking
```python
a,b,c, *args = [1,2,3,4,5]
print(args)
```

---

#### None -> absence of value
```python
weapon = None
weapon = "lol"
print(weapon)
```

---

#### Dictionary aka Object, hashmap, map
```python
# Dict
dictionary ={
    "a":1,
    "b":2
}

print(dictionary)
print(dictionary["a"])

```

---

##### Another way of targetting Dictionary
```python
user = {
    "a": "male",
    "b": "male",

}

print(user.get("a"))
```

If key is not present with the method above the program will not error out
```python
user = {
    "a": "male",
    "b": "male",

}

print(user.get("age")) #produces None
```

---

#### Default value with Dict
```python
user = {
    "a": "male",
    "b": "male",

}

print(user.get("age", 55))
```

---

##### Another method of producing dict
```python
user2 = dict(name="john", age=2)
print(user2)
```

##### Check for presence of characters or value
```python

user2 = dict(name="john", age=2)

print('ohn' in user2["name"])
print('ohn' in user2["name"])
print("john" in user2.values())
print("name" in user2.keys())
print( user2.items())
print(user2.update({'age':90}))
print(user2)
```

---

##### Tuples are immutable lists
```python
my_tuple= (1,2,3,4,5)
my_tuple[1] = 0 #This will error out
```


---

#### Sets
Unordered collection of unique objects
```python

my_set = {1,2,3,4,5,6,6}
my_set.add(4) # program will ignore this
my_set.add(7)
print(my_set) # doesnt return the last 6, no duplicate 
```

#### convert a list to a set
```python
my_list = [1,2,3,4,5,6,6]
print(set(my_list))
```

---

#### convert set to list
```python
my_set = {1,2,3,4,5,6,6}
print(list(my_set))
```


```python
#### Set methods
my_set = {1,2,3,4,5,6,6}
your_set= {2,3,4,5,6,7,}

print(my_set.difference(your_set))
print(my_set.discard(1))
print(my_set)
print(f"intersection is {my_set.intersection(your_set)}")
print(my_set.union(your_set))
print(my_set | your_set)
```


---

#### Conditional flow
```python
is_old = True
is_licenced = True

if is_old and is_licenced:
    print("you are eligible")
elif is_old and not is_licenced:
    print("please get a licence")
else:
    print("you are not eligible")
```

---

#### Ternary
```python
#### Ternary operator

is_friend = False
can_message= "message_allowed" if is_friend else "not allowed"

print(can_message)
```

---

##### Short circuiting
Either one of the condition must be true

```python
is_friend = True
is_user = True

if is_friend or is_user:
    print("best friends forever")
```


---

##### Strict and unstrict equal
```python
print(True is 1)
print("1" is 1)

```

---

#### For loops
```python
for item in "Zero lord":
    print(item)

for item in "Zero lord":
    for a in ['a', 'b', 'c']:
        print(item, a)
        print(item, a)
```

---

#### Iterating over dictionary
```python
user ={
    'name':"doe",
    'age':78
}

for item in user.items():
    print(item)

```

##### Unpacking dict with for loops
```python
user ={
    'name':"doe",
    'age':78
}

for item in user.items():
    key, value = item
    print(f"key is {key} and value is {value}")
```

#### Short form of unpacking
```python
user ={
    'name':"doe",
    'age':78
}

for key, value in user.items():
    print(f"key is {key} and value is {value}")
```


---


##### Range
```python
#### Range
for n in range(0, 100):
    print(n)

for _ in range(0, 100, 2):
    print("sending emails")

print(list(range(10))) 
```


---

#### enumerate
```python
#enumerate
for i, char in enumerate("hello"):
    print(i, char)
```


---

##### While loop
```python
i = 0

while i < 50:
    print(i)
    i = i + 1
else:
    print('done looping')
```


#### Looping while 
```python
i = 0

while i < len([1,2,3,4]):
    print(i)
    i+=1

i = 0
my_list = [1,2,3,4]
while i < len(my_list):
    print(my_list[i])
    i+=1
```


---

##### Docstring
```python
def greet(a):
    '''
        Info: this is a docstring
    '''
    print(a)

greet("great")
```

```python
def greet():
    '''
    Info: this is a docstring
    '''
    print("hello")

greet()

print(greet.__doc__)
```

#### *args and *kwargs

```python
def super_funct(*args):
    print(args)
    return sum(args)

print(super_funct(1,3,4,5))

def summer(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(summer(1,2,3, num1=4, num2=5))
# Rule of precedence: params, *args, default parameters, **kwargs
```


---

##### Walrus operator
```python
# instead of writing
a = "hellooooooooo"
if len(a) > 10:
    print(f"too long {len(a)} elements")

if ((n := len(a)) > 10):
    print(f"too long {n} elements walrus")
```

---

#### Global keyword
```python
x = 7

def count():
    global x
    x +=1
    return x

print(count())
```


---

#### Importing modules 
```python
import <file name>
```