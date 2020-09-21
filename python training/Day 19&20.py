Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pow(2,3)
8
>>> x=(23,214,12)
>>> pow(x[0],2)
529
>>> sumUp(x)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sumUp(x)
NameError: name 'sumUp' is not defined
>>> def sumup(f):
	j=0
	for k in f:
		j+=k
		return j
sumUp(x)
SyntaxError: invalid syntax
>>> sumup(x)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sumup(x)
NameError: name 'sumup' is not defined
>>> def sumup(f):
	j=0
	for k in f:
		j+=k
	return j

>>> sumup(x)
249
>>> print(sum((2, 3))))
SyntaxError: unmatched ')'
>>> 'My name's Dude'

SyntaxError: invalid syntax
>>> 'My name's Dude"

SyntaxError: invalid syntax
>>> "My name is Dude'

SyntaxError: EOL while scanning string literal
>>> 'My name's Dude"

SyntaxError: invalid syntax
>>> x = (2,)

>>> x = (2)

>>> x = 2,

>>> {2: "two"}
{2: 'two'}
>>> def foo(a, b):
        return a+b

        x = foo(2, 4)
print(x)
SyntaxError: invalid syntax
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 16.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 16.py", line 5, in <module>
    print(x)
NameError: name 'x' is not defined
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 16.py
>>> 
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 16.py
9
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 17.py
Hello
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 17.py
Holla
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 17.py
[2]
[2, 3]
>>> x = '6' + 6
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x = '6' + 6
TypeError: can only concatenate str (not "int") to str
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 17.py
19 and [(5,), [8]]
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 17.py
18
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 17.py
18
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 11, in <module>
    foo = Dude(3,4)
TypeError: Dude() takes no arguments
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 12, in <module>
    foo = Dude(3,4)
TypeError: Dude() takes no arguments
>>> foo.show() prints
SyntaxError: invalid syntax
>>> foo.show()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    foo.show()
NameError: name 'foo' is not defined
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 12, in <module>
    foo = Dude(3,4)
TypeError: Dude() takes no arguments
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 1, in <module>
    class Dude:
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 11, in Dude
    foo=Dude(3,4)
NameError: name 'Dude' is not defined
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 11, in <module>
    foo = Dude(3,4)
TypeError: Dude() takes no arguments
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 11, in <module>
    foo = Dude('3,4')
TypeError: Dude() takes no arguments
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 18.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 18.py", line 11, in <module>
    foo = Dude('3','4')
TypeError: Dude() takes no arguments
>>> import math
>>> import math as ma
>>> ma.ceil(23.7)
24
>>> ma.ceil(23.3)
24
>>> round(23.3)
23
>>> ma.floor(24.5)
24
>>> ma.floor(34)
34
>>> mma.flor(24.9)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    mma.flor(24.9)
NameError: name 'mma' is not defined
>>> ma.flor(24.9)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    ma.flor(24.9)
AttributeError: module 'math' has no attribute 'flor'
>>> mma.floor(24.9)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    mma.floor(24.9)
NameError: name 'mma' is not defined
>>> ma.floor(24.9)
24
>>> ma.factorial(4)
24
>>> ma.sqrt(49)
7.0
>>> ma.sin(90)
0.8939966636005579
>>> ma.sin(60)
-0.3048106211022167
>>> ma.sin(ma.radians(60))
0.8660254037844386
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 20.py
Traceback (most recent call last):
  File "C:/Users/Michał/Desktop/Sun/python training/Day 20.py", line 2, in <module>
    x=ab.sqrt(45)
NameError: name 'ab' is not defined
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 20.py
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 20.py
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 20.py
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 20.py
>>> 
= RESTART: C:/Users/Michał/Desktop/Sun/python training/Day 20.py
6.708203932499369
>>> abs(-34)
34
>>> all(34)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    all(34)
TypeError: 'int' object is not iterable
>>> all(23, '12', '67')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    all(23, '12', '67')
TypeError: all() takes exactly one argument (3 given)
>>> all([23,'34','45'])
True
>>> any([23,'34','45', 'name'])
True
>>> bin(10)
'0b1010'
>>> 