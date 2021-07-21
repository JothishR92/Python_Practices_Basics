#Practice datatypes
"""Types of datatypes
    1. Numeric Type: Number --> 1.int, 2. float, 3. complex
    2. Text Type: String
    3. Sequence Type: List
    4. Sequence Type: Tuple
    5. Mapping Type: Dictionary
    6. Set Type: set, frozenset
    7. Boolean Type: bool
    8. Binary Type: bytes, bytearray, memoryview
"""
def completed():
    print("#--------------------------------x--------------------------------------")
def output():
    print("#________ OUTPUT _________")
def error():
    print("#xxxxxxxxxxx ERROR xxxxxxxxxxxx")

# Start practice from here Numeric Type: Number --> 1.int, 2. float, 3. complex
#1.addition
"""completed()
output()
print(2+5)"""
#________ OUTPUT _________
#7
#--------------------------------x--------------------------------------

#2.diclare the variable:

"""output()
a=5
b=6
c=a+b
print(c)
completed()"""
#________ OUTPUT _________
#11
#--------------------------------x--------------------------------------

#3.concatenate use string
"""output()
name="Jothish"
last_name="R"
print(name + " " +last_name)
completed()"""
#________ OUTPUT _________
#Jothish R
#--------------------------------x--------------------------------------

#3. Input get from user identify that data type str or int
"""output()
a=input("ENTER THE VALUE :")
print(type(a)) #type()-> returns type of value
completed()"""
#________ OUTPUT _________
#ENTER THE VALUE :5
#<class 'str'>
#--------------------------------x--------------------------------------

#4. Input get from user print that
"""output()
a=input("ENTER THE VALUE :")
print(a)
print(type(a))
completed()"""
#________ OUTPUT _________
#ENTER THE VALUE :5.5
#5.5
#<class 'str'>
#--------------------------------x--------------------------------------

#5.get int input from user print that
"""output()
a=int(input("ENTER THE INT VALUE :"))
print(a)
print(type(a))
completed()"""
#________ OUTPUT-1 _________
"""#ENTER THE INT VALUE :5.5
Traceback (most recent call last):
  File "/media/jothishr/PROJECTS_STUDY_PURPOSE/studied videos/python_practices/Basic_python/Basic_python_practice.py", line 63, in <module>
    a=int(input("ENTER THE INT VALUE :"))
ValueError: invalid literal for int() with base 10: '5.5'"""
#Note: we cannot get float value from user because use the function int().

#________ OUTPUT-2 _________
"""ENTER THE INT VALUE :5
5
<class 'int'>"""
#--------------------------------x--------------------------------------

#6.need get input from float value
"""output()
a=float(input("ENTER THE INT VALUE :"))
print(a)
print(type(a))
completed()"""
#________ OUTPUT-1 _________
"""ENTER THE INT VALUE :5
5.0
<class 'float'>"""

#________ OUTPUT-2 _________
"""ENTER THE INT VALUE :5.5
5.5
<class 'float'>"""
#--------------------------------x--------------------------------------

#7. practice complex value:
"""
    What is complex numbers?
       real part with imaginary part (6 + 0j) 6 -> real part 0 is a imaginary part
       
"""
"""output()
a=complex(input("ENTER THE COMPLEX VALUE :"))
print(a)
print(type(a))
completed()"""
#________ OUTPUT-1 _________
"""ENTER THE COMPLEX VALUE :6j
#6j
#<class 'complex'>"""

#________ OUTPUT-2 _________
"""#ENTER THE COMPLEX VALUE :6
#(6+0j)
#<class 'complex'>"""

#________ OUTPUT-3 _________
"""ENTER THE COMPLEX VALUE :"3j+5"
Traceback (most recent call last):
  File "/media/jothishr/PROJECTS_STUDY_PURPOSE/studied videos/python_practices/Basic_python/Basic_python_practice.py", line 116, in <module>
    a=complex(input("ENTER THE COMPLEX VALUE :"))
ValueError: complex() arg is a malformed string"""
#--------------------------------x--------------------------------------