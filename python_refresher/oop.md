Everything in python is an object
Object has methods that we can access with the .

```python
class BigObject:
    pass

print(type(BigObject)) #<class 'type'>


```

```python
class BigObject: # Created a class here
    pass

obj1 = BigObject() # we instantiated a class using () to create a new object
print(type(obj1)) #<class '__main__.BigObject'>


```


---

##### Creating objects
```python
class PlayerCharacter:
    def __init__(self, name): #dunder method / a constructor method
        self.name = name # self refers to PlayerCharacter, name here is an attribute 

    def run(self):
        print('run')


player1 = PlayerCharacter("joe")
player2 = PlayerCharacter("mimi")


print(player1) #<__main__.PlayerCharacter object at 0x000001E64F36B910>
print(player1.name) #joe
print(player2.name) #mimi

    
```

```python
class PlayerCharacter:
    def __init__(self, name, age): #dunder method / a constructor method
        self.name = name # self refers to PlayerCharacter
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter("joe", 67)

print(player1) #<__main__.PlayerCharacter object at 0x000001E64F36B910>
print(player1.age) #joe
```

```python
class PlayerCharacter:
    def __init__(self, name, age): #dunder method / a constructor method
        self.name = name # self refers to PlayerCharacter
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("joe", 67)

print(player1.age) #joe
print(player1.run())
```


```python
class PlayerCharacter:
    def __init__(self, name, age): #dunder method / a constructor method
        self.name = name # self refers to PlayerCharacter
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("joe", 67)

help(player1.age)

```


---

##### Class class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        self.name = name # self refers to PlayerCharacter
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("joe", 67)

print(player1.membership)
object attribute
```python
class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        if(self.membership):
            self.name = name # self refers to PlayerCharacter
            self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("joe", 67)

print(player1.membership)
print(player1.name)

```

```python
class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        if(PlayerCharacter.membership):
            self.name = name # self refers to PlayerCharacter
            self.age = age

    def run(self):
        print(f'running to {self.name}')
        return 'done'


player1 = PlayerCharacter("joe", 67)

print(player1.membership)
print(player1.name)

```

```python
class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        if(PlayerCharacter.membership):
            self.name = name # self refers to PlayerCharacter
            self.age = age

    def run(self):
        print(f'running to {self.name}')
        return 'done'


player1 = PlayerCharacter("joe", 67)

print(player1.membership)
print(player1.name)
print(player1.run())

```


---

#### Class method
```python
class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        if(PlayerCharacter.membership):
            self.name = name # self refers to PlayerCharacter
            self.age = age

    def run(self):
        print(f'running to {self.name}')
        return 'done'
    @classmethod
    def adding_things(cls, num1, num2): #cls is like the self
        return num1 + num2

player1 = PlayerCharacter("joe", 67)

print(player1.membership)
print(player1.name)
print(player1.run())
print(player1.adding_things(2,3))
```

```python
class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        if(PlayerCharacter.membership):
            self.name = name # self refers to PlayerCharacter
            self.age = age

    def run(self):
        print(f'running to {self.name}')
        return 'done'
    @classmethod
    def adding_things(cls, num1, num2): #cls is like the self
        return num1 + num2

player1 = PlayerCharacter("joe", 67)

print(player1.adding_things(2,3))
# we can call the PlayerCharacter.adding_things directly
print(PlayerCharacter.adding_things(3,4))
```

```python
class PlayerCharacter:
    membership = True
    def __init__(self, name, age): #dunder method / a constructor method
        if(PlayerCharacter.membership):
            self.name = name # self refers to PlayerCharacter
            self.age = age

    def run(self):
        print(f'running to {self.name}')
        return 'done'
    @classmethod
    def adding_things(cls, num1, num2): #cls is like the self
        return num1 + num2

    @staticmethod
    def adding_things( num1, num2):  # cls is like the self
        return num1 + num2

player1 = PlayerCharacter("joe", 67)

print(player1.adding_things(2,3))
# we can call the PlayerCharacter.adding_things directly
print(PlayerCharacter.adding_things(3,4))
```


---

#### 4 pillars of OOP
ENCAPSULATION
packaging data and functions into attributes and methods
```python
class PlayerCharacter:
    def __init__(self, name,age):
        self.name - name
        self.age = age
    def run(self):
        print("run")
    def speak(self):
        print(f"my name is {self.name} and i am {self.age} years old")
    
```

Abstraction
Hiding of information and getting access to whats necessary
```python
class PlayerCharacter:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def run(self):
        print("run")
    def speak(self):
        print(f"my name is {self.name} and i am {self.age} years old")
    
player1 = PlayerCharacter("joe", 34)
print(player1.speak())
```

---

##### Setting private attribute in python class
```python
class PlayerCharacter:
    def __init__(self, name,age):
        self._name = name # _ denotes private 
        self._age = age
    def run(self):
        print("run")
    def speak(self):
        print(f"my name is {self._name} and i am {self._age} years old")
    
player1 = PlayerCharacter("joe", 34)
print(player1.speak())
```

---


#### Inheritance
```python
class User:
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, number_arrows):
        self.name = name
        self.number_arrows = number_arrows

    def attack(self):
        print(f"arrows left {self.number_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Jmes", 100)
# print(wizard1.sign_in())
print(wizard1.attack())
print(archer1.attack())
```


---

##### Error hadnling
```python
try:
    age = int(input("Enter your age? "))
    print(age)
except:
    print("please enter a number")
```

```python
while True:
    try:
        age = int(input("Enter your age? "))
        10/0
        print(age)
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("please enter a number")
    else:
        print("thanks")
        break
```

```python
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as error:
        print(f"please enter a number {error}")
        return "error"


print(sum(1,"90"))
```

---

##### Grouping Errors
```python
def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as error:
        print(f"please enter a number {error}")
        return "error"


print(sum(1,"90"))
```