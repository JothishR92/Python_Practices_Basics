#practice_string

def completed():
    print("#--------------------------------x--------------------------------------")
def output():
    print("#________ OUTPUT _________")
def error():
    print("#xxxxxxxxxxx ERROR xxxxxxxxxxxx")
def Note():
    print("#========== NOTE =============")


#1. PRINT STRING USING print():
"""output()
print("Hello")
print('jotheeswaran')
completed()"""
#________ OUTPUT _________
#Hello
#jotheeswaran
#--------------------------------x--------------------------------------

#2. PRINT MULTILINE STRING USING print() and WITH VARIABLE DECLARATION:
"""output()
a="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua."
print(a)
completed()
Note()
"""
#========== NOTE =============
"""NOTE: single line only we can print in double quotes(") and single quotes(') but we cannot print multi line
if we need to multiline print use triple quotes(\""")
"""
#________ OUTPUT _________
# SINGLE LINE:
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididuntut labore et dolore magna aliqua.
#--------------------------------x--------------------------------------

#2.1- PRINT MULTILINE :
#output()
#a="""NOTE: single line only we can print in double quotes(")
#and single quotes(') but we cannot print multi line
#if we need to multiline print use triple quotes(\""").
#"""
#print(a)
#completed()
#________ OUTPUT _________
#"""NOTE: single line only we can print in double quotes(")
#and single quotes(') but we cannot print multi line
#if we need to multiline print use triple quotes(\""")
#"""
#--------------------------------x-----------------------------------

#3. CONVERT LIST TO STRING:

"""output()
a=['s', 't', 'r', 'i', 'n', 'g']
str1=""
for i in a:
    str1+=i
print(str1)
completed()"""
#________ OUTPUT _________
#string
#--------------------------------x--------------------------------------

#4. REPLACE THE STRING VALUE:

"""output()
c=""
s ="strong"
# need to replace 'o' to 'i'
b=list(s)
b[3]='i'
for str1 in b:
    c+=str1
print(c)
completed()"""

#________ OUTPUT _________
#string
#--------------------------------x--------------------------------------

#5. REPLACE THE PARTICULAR WORD IN STRING
"""output()
str1=""
s = "Replace the particular word in string"
a=s.split(' ')
a[1]= 'the value'
out = ' '.join(str(i) for i in a)
print(out)
completed()"""

#________ OUTPUT _________
#Replace the value particular word in string
#--------------------------------x--------------------------------------

#6. PRACTICE INTERVIEW QUESTION

###########

#7. VERIFY STRING EXIST OR NOT:
"""output()
s = "orange"
print("orange" in "This is orange juice" )
completed()"""
#________ OUTPUT _________
#True
#--------------------------------x--------------------------------------

# TESTING
"""strings="The lyrics is not that poor!"
s1=strings.find("not")
s2=strings.find("poor")
print(s1)
print(s2)"""

# EXAMPLE-1 CODE TEST ONLINE
"""def not_poor(str1,re_string):
    find_str = str1.find(re_string)
    last_str = len(str1)
    if find_str >= 0:
        str1 = str1.replace(str1[find_str:(last_str-1)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is poor but not that much of poor!',"poor"))
print(not_poor('The lyrics is poor!',"poor"))"""

# UNDERSTANDING BASED THIS EXAMPLE-1
"""FIND THE STRING INDEX NUMBER AND SLICING THE STRING AND REPLACE STRING USE replace()"""
# CODE
"""def not_poor(str1):
    #snot = str1.find('not') ==>14
    #spoor = str1.find('poor') ==>23
    if 23 > 14 and 14 > 0 and 23 > 0:
        str1 = str1.replace(str1[14:(23 + 4)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))"""

#8. PRACTICE STRING INTERVIEW QUESTION:

# LEARNING-1  CHECKING STRING VALUE IS POLYNDROME OR NOT
"""output()
str1="MADAM"
l=len(str1)
s=""
for i in range(l-1,-1,-1): # Reverse the value using range function
    s+=str1[i]
if s == str1:
    print("It is polyndrome")
else:
    print("It is symmetric")
completed()"""
#________ OUTPUT _________
#It is polyndrome
#--------------------------------x--------------------------------------

# LEARNING-2 CHECKING NUMBER IS POLYNDROME OR NOT
"""LOGIC :
        r=n%10
        sum=(sum*10)+r
        n=n/10
"""
"""output()
num = 151
temp= num
sum=0
while (num>0):
    r=num%10
    sum=(sum*10)+r
    num=num//10
if temp == sum:
    print("Polyndrome number")
else:
    print("not polyndrome")
completed()"""
#________ OUTPUT _________
#Polyndrome number
#--------------------------------x--------------------------------------

# LEARNING-1 Python program to check whether the string is Symmetrical or Palindrome
"""if 7%2: # if value not 0 if condition is pass print inside if condition, if value is 0 call else block 
    print("True")
else:
    print("false")"""

#9. FIND STRING SYMMETRIC OR NOT
    # LOGIC:
        #STRING INPUT DIVIDE THE HALF USING LENTH OF STRING STORE THE VARIABLE
        #COMPARE THE FIRST HALF AND SECOND HALF IF EQUAL EACH WORD FIRST TO LAST THAT IS SYMMETRIC
"""output()
str1 = "khokho"
n=len(str1)
first_half = 0
mid=n//2
second_half=mid
flag=0
while(first_half<second_half and second_half<n):
    if (str1[first_half] == str1[second_half]):
        first_half += 1
        second_half += 1
    else:
        flag = 1
        break
if flag == 1:
    print("this is not symetric")
else:
    print("symmetric")
completed()"""
#________ OUTPUT _________
#symmetric
#--------------------------------x--------------------------------------

#10. Reverse words in a given String in Python

"""str1 = "geeks quiz practice code"
str2= ""
l1=str1.split(' ')
l2=[]
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
    str2 = ' '.join(l2)
print(str2)"""
#________ OUTPUT _________
#code practice quiz geeks
#--------------------------------x--------------------------------------

#10.1 SAME THING USED REVERSE FUNCTION
"""output()
str1 = "geeks quiz practice code"
w=str1.split(' ')
str2=' '.join(reversed(w))
print(str2)
completed()"""
#________ OUTPUT _________
#code practice quiz geeks
#--------------------------------x--------------------------------------

#11. Ways to remove 'i' character from string in Python

#11.1 WAY OF ONE CHARACTOR OR WORD
"""output()
a="string"
l=a.split('i')
o=''.join(l)
print(o)
completed()"""
#________ OUTPUT _________
#strng
#--------------------------------x--------------------------------------

#11.2 WAY OF TWO REMOVE CHARACTOR USING INDEX VALUE:

# LEARNING:
"""output()
a="string"
b=list(a) # convert the list after convert to string
c=''.join(b)
print(c)
completed()"""
#________ OUTPUT _________
#string
#--------------------------------x--------------------------------------

#12. PRACTICE STRING FUNCTIONS:

s="string."
msg="this is the best of my life and life is worst my life"
CAPS="STRINGS"
output()
#print(s.capitalize())  # Converts the first character to upper case
#________ OUTPUT _________
#String
#========== NOTE =============
"""if i give first letter # capitalize() should not works"""

#print(CAPS.casefold())
#________ OUTPUT _________
#strings

#print(s.center(8,'#')) #Returns a centered string
#________ OUTPUT _________
#######string#######
"""SYNTAX- string.center(length, character)
    GIVE LENGTH VALUE, ABOVE LENGTH OF STRING INPUT
"""

#print(msg.count('this'))  # Returns the number of times a specified value occurs in a string
# SYNTAX --> string.count(value, start, end)
#________ OUTPUT _________
#1

#print(msg.count('best',10,16))
""" 
value -	Required. A String. The string to value to search for
start -	Optional. An Integer. The position to start the search. Default is 0
end - Optional. An Integer. The position to end the search. Default is the end of the string
"""
#________ OUTPUT _________
#1

#print(s.encode()) # The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# SYNTAX --> string.encode(encoding=encoding, errors=errors)
""" encoding-> Optional. A String specifying the encoding to use. Default is UTF-8
    errors-> Optional. A String specifying the error method. Legal values are:
            'backslashreplace'	- uses a backslash instead of the character that could not be encoded
            'ignore'	- ignores the characters that cannot be encoded
            'namereplace'	- replaces the character with a text explaining the character
            'strict'	- Default, raises an error on failure
            'replace'	- replaces the character with a questionmark
            'xmlcharrefreplace'	- replaces the character with an xml character
"""
#a=s.encode()
#print(a.decode()) # Decode the binary string
"""txt = "My name is Ståle"
print(txt.encode(encoding='ascii',errors='backslashreplace'))
print(txt.encode(encoding='ascii',errors='ignore'))
print(txt.encode(encoding='ascii',errors='namereplace'))
print(txt.encode(encoding='ascii',errors='replace'))
print(txt.encode(encoding='ascii',errors='xmlcharrefreplace'))"""

#print(msg.endswith('life')) # find the string end of value using this function
#________ OUTPUT _________
#True

#print(msg.endswith('life',20,27))
#________ OUTPUT _________
#False

#print(s.expandtabs(5))  # tab space use \t The expandtabs() method sets the tab size to the specified number of whitespaces.
#________ OUTPUT _________
#s    tring.

#print(msg.find('life')) # Searches the string return the position of index value
#________ OUTPUT _________
# Index value 'life'--> 23

#print("this is {} life".format("worst"))
#________ OUTPUT _________
#this is worst life

#print("this is {x} life".format(x="worst"))
#________ OUTPUT _________
#this is worst life

#a="""NOTE: single line only we can print in {x} quotes(")
#and {y} quotes(') but we cannot print multi line
#if we need to {a} print use {z} quotes(\""").
#"""
#print(a.format(a='multiline',y='single',x='double',z='trible'))  # why using key using this type pairing only
#________ OUTPUT _________
#NOTE: single line only we can print in double quotes(")
#and single quotes(') but we cannot print multi line
#if we need to multiline print use trible quotes(""").

#p={'x':4,'y':3}
#print("{x} to {y} welcome of you".format(**p))
#print("{x} {y}".format_map(p)) # only use dict value used in format map function
#Formats specified values in a string
""" l=['4','3','2','1']
print("{l[0]} {l[1]} {l[2]}".format_map(l)) # we cannot use list value in format_map function
 Note error: Traceback (most recent call last):
  File "/media/jothishr/PROJECTS_STUDY_PURPOSE/studied videos/python_practices/Basic_python/String_practices.py", line 334, in <module>
    print("{l[0]} {l[1]} {l[2]}".format_map(l))
TypeError: list indices must be integers or slices, not str
"""

"""print(s.index('i'))
#________ OUTPUT _________
3 -->index value of string
print(msg.index('l',20,27)) # search index value to particular range
#________ OUTPUT _________
23 -->-->index value of string
 SYNTAX : string.index(value, start, end) 

value - Required. The value to search for
start - Optional. Where to start the search. Default is 0
end - Optional. Where to end the search. Default is to the end of the string
"""
a="str12"
b="welcome"
txt="\u0033"
#print(a)
# its return boolean value only
#print(a.isalnum()) # Returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

#print(b.isalpha()) # Returns True if all the characters are alphabet letters (a-z).

#print(txt.isdecimal()) #  returns True if all the characters are decimals (0-9).This method is used on unicode objects.

#val='58000'
#print(val.isdigit()) # Returns to true or false if value is digit
#print(val.isnumeric()) # Returns to true or false if value is digit
#________ OUTPUT _________
#True

#ident="Str" # contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces
#print(ident.isidentifier())# returns True if the string is a valid identifier, otherwise False.
#________ OUTPUT _________
#True

#g= "Its works with enable"
#print(g.islower()) # Returns True if all characters in the string are lower case
#________ OUTPUT _________
#False

#a="$" #its return true or false if be printable value
#print(a.isprintable())
#________ OUTPUT _________
#True

#b="This value is find space is there or not"
#c=" "
#print(b.isspace())
#________ OUTPUT _________
#False
#print(c.isspace())
#________ OUTPUT _________
#True

#print(CAPS.isupper()) # returns True if all the characters are in upper case
#print(s.isupper())
#________ OUTPUT _________
#True
#False
#l=['s','t','r','i','n','g']
#print("".join(l)) # Joins the elements of an iterable(list,tuple) and (dict,set) to the end of the string
#________ OUTPUT _________
#string
#d={'set':'dict','list':'tuple'} # if we have dict means only join key only
#print(" ".join(d))
#s={'a','b','c','d'}
#print("".join(s))

#print(s.ljust(10,'1')) #The ljust() method will left align the string, using a specified character (space is default) as the fill character.
""" SYNTAX: string.ljust(length, character)
    length --> Required. The length of the returned string
    character --> Optional. A character to fill the missing space (to the right of the string). Default is " " (space).
"""
#________ OUTPUT _________
#string.111

"""content= "Length of the RETURNED STRING VALUE TrUe"
#print(content.lower())
#________ OUTPUT _________
#length of the returned string
splt=content.split(" ")
for i in splt:
    if i.isupper():
        print(i," yes i'm caps letter word")
    else:
        continue"""

#print(msg)
#a=msg.partition('the best') # Returns a tuple where the string is parted into three parts
#print(a)
#________ OUTPUT _________
#this is the best of my life
#('this is ', 'the best', ' of my life')

#print(msg)
#a=msg.replace('life','friend',2) # This function replace the values
#print(a)
""" 
oldvalue - Required. The string to search for
newvalue - Required. The string to replace the old value with
count - Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
"""
#b=msg.replace('worst','good')
#print(b)
#________ OUTPUT _________
#this is the best of my life and life is good my life

#print(msg.rfind('life'))
"""
finds the last occurrence of the specified value
returns -1 if the value is not found.
almost the same as the rindex() method. See example below.
"""
#print(msg.rindex('life'))
#________ OUTPUT _________
#49
#49


