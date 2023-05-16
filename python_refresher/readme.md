#### Read files
use the `open` command

```python
f = open("file path", "method")
f = open("index.txt", "r")

f = open("index.txt", "r")
print(f.read())

```

#### specify file path
```python
f = open("hidden/use.txt", "r")
print(f.read())
```

#### It is a good practice to always close the file when you are done with it.
```python
f = open("index.txt", "r")
print(f.read())
f.close()
```

---

#### Write to files
```python
f = open("index.txt", "a")
f.write("hello world")
f.close()
```

#### combine read and write
```python
f = open("index.txt", "a")
f.write("hello world")
f.close()

g = open("index.txt", "r")
print(g.read())
```

---

#### Create a file
> f = open("app.txt", "x")

---

#### Delete files
```python
import os as operate

operate.remove("app.txt")
```

#### use conditionals
```python
import os as sys

if sys.path.exists("index.txt"):
    sys.remove("index.txt")
    print("removed success")
else:
    print("path does not exist")
```

---

#### Delete folder
```python
import os as sys

sys.rmdir("my_folder")
```

---

#### String format
```python
name = "doe"
age = 8

result = f"my name is {name} and i am {age} years old"
print(result)
```

```python
name = input("what is your name? ")
print(f"your name is {name}")
```


---

#### Try exception
```python
num1 = 7
num2 = 9
try:
    if( num2 > num1 ):
        print("booyah")
    else:
        print('nil')
except:
    raise Exception("something bad happened")
```

#### Raising an Exception
```python
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 
```

```python
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed") 
```

```python
num1 = '9'

if not type(num1) is int:
    raise Exception("something bad happened")


```

```python
num1 = '9'

if type(num1) is not int:
    raise Exception("something bad happened")



```

---

#### Working with json
```python
import json as js
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

result = js.loads(x)
print(result['name'])
```

---

#### importing modules
in app.py
```python
def greeting(fname):
    print(f"hello {fname}")
```

in test.py

```python

from python_refresher import app

app.greeting("james")
```

---

#### importing just a function from several functions

in app.py
```python
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

in test.py

```python
from python_refresher.app import person1

print(person1)
```


---

#### Rules of having package
you have to have the __init__.py in the package or directory

#### Install Jupiter notebook with anaconda
Make sure you don't add to path in order not to conflict with the previous python version you have


---

#### Import using the from keyword
```python
from util import divide, sum
import shop.cart
from python_refresher.shop.more.donk import order

print(sum(3, 4))
print(divide(8, 9))
print(shop.cart.buy(90))
print(order("lol"))
```

---

#### imbuilt package
```python
import random
print(random.random())
print(random.randint(1,7))
print(random.choices([1,2,3,4,5]))
# print(random.shuffle([12,13,14]))
```

```python
from random import choices
print(choices([1,2,3,4,5]))
# print(random.shuffle([12,13,14]))
```

---

#### __name__

the __name__ refers to the actual file/module you are in
```python
if __name__ == "__main__":
    print("We are in the root file")
```


---

#### System modules
```python
import sys
print(sys.path)
print(sys.argv)
# print(sys.copyright)
```

---

##### Python packages 
> pypi.org


---


##### Install packages using pycharm
go to file -> settings -> python interpreter -> search for package and click save

```python
import pyjokes

print(pyjokes.get_jokes('en', 'neutral'))
```

---

#### Using pip
Get pip version
> pip -V 

#### Install using pip
> pip install pyjokes


---

#### Install Pip env for virtual environment for each project
In pycharm the virtualenv is built in


#### usefl built in packages example
```python
from collections import  Counter, defaultdict, OrderedDict

li = [1,2,3,4,1,2,3,1]
sentence = 'black black ship'
print(Counter(li))
print(Counter(sentence))
```

```python
import datetime
import time
from array import array

print(datetime.time(5,45,2))
print(datetime.date.today())
print(time.time())

arr = array('i', [1,2,3,4,5])
print(arr[0])

```

---

##### Reading and writing files
```python
my_file = open('file.txt')
print(my_file.read())
```

```python
my_file = open('file.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())
```

```python
my_file = open('file.txt')
print(my_file.readline())
print(my_file.readline())
```

---

##### Working with files the proper way
```python
with open('file.txt') as my_file:
    print(my_file.read())
```

```python
with open('file.txt', mode='r') as my_file: #default is read only
    print(my_file.read())
```

```python
with open('file.txt', mode='r+') as my_file: #read and write
    print(my_file.read())
```

##### Write into a file
```python
with open('file.txt', mode='r+') as my_file: #read and write
    text = my_file.write("hey it's me shegz")
    print(text)
```

---

##### Append mode
```python
with open('file.txt', mode='a') as my_file: #read and write
    text = my_file.write("hey it's me shegz")
    print(text)
```

---

##### Using paths
```python
with open('./file.txt', mode='a') as my_file: #read and write
    text = my_file.write("hey it's me shegz")
    print(text)
```

##### Handling file errors
```python
try:
    with open('./file.txt', mode='a') as my_file: #read and write
    text = my_file.write("hey it's me shegz")
    print(text)
except FileNotFoundError as error:
    print("file not found")
    raise error
except IOError as error:
    print("IO error")
    raise error
```


---

#### Regular exception
```python
import re

string ="hello there my name is abayomi"

print(re.search("abayomi",string ))
```


---

#### Testing
Unit test
```python
# app.py

def do_stuff(num):
    return num + 5


```

Then in test.py
```python
import unittest
import app 

```