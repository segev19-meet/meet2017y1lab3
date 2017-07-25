Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "dont"+"forget"+"to"+"conserve"+"water"
'dontforgettoconservewater'
>>> 'dont'+'forget'+'to'+'conserve'+'water'
'dontforgettoconservewater'
>>> "the"*3
'thethethe'
>>> 'the'+3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'the'+3
TypeError: Can't convert 'int' object to str implicitly
>>> "the"*3+"beautiful"+"earth"
'thethethebeautifulearth'
>>> 2*"true"
'truetrue'
>>> 'the'+3
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    'the'+3
TypeError: Can't convert 'int' object to str implicitly
>>> a='save'
>>> b='the'
>>> c='planet'
>>> 'save the plnet'
'save the plnet'
>>> '4 ''panda ''bears '
'4 panda bears '
>>> dog="love to eat"
>>> len(1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
>>> len(dog)
11
>>> 11
11
>>> 
>>> 
>>> upper()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    upper()
NameError: name 'upper' is not defined
>>> dog="love to eat"
>>> dog.upper()
'LOVE TO EAT'
>>> god="love to eat"
>>> dog.lower()
'love to eat'
>>> dog="love to eat"
>>> dog.capitalize()
'Love to eat'
>>> dog="love to eat"."food"
SyntaxError: invalid syntax
>>> dog="love tp eat.food"
>>> dog.capitalize
<built-in method capitalize of str object at 0x7fbaf58c2978>
>>> dog="love to eat"
>>> dog.swapcase()
'LOVE TO EAT'
>>> dog=love to eat
SyntaxError: invalid syntax
>>> dog="love to eat"
>>> dog="loveto eat.food"
>>> dog.capitalize()
'Loveto eat.food'
>>> dog="love to eat"
>>> dig.replace()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dig.replace()
NameError: name 'dig' is not defined
>>> dog="love to eat"
>>> dog.rep
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dog.rep
AttributeError: 'str' object has no attribute 'rep'
>>> dog="love to eat"
>>> dog.replace("o","i")
'live ti eat'
>>> 
>>> 
>>> a="meet"
>>> b="meet"
>>> c="Meat""meet"
>>> a="MEET"
>>> b="meet"
>>> c=Meat"
SyntaxError: EOL while scanning string literal
>>> a="MEET"
>>> b="meet"
>>> c=Meat"
SyntaxError: EOL while scanning string literal
>>> a="MEET"
>>> b="meet"
>>> c="Meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a!b
SyntaxError: invalid syntax
>>> a!=b
True
>>> a!=c
True
>>> b!=
SyntaxError: invalid syntax
>>> b!=c
True
>>> a="MEET"
>>> B="MEET"
>>> "MEET".lower()
'meet'
>>> a=b
>>> a="meet
SyntaxError: EOL while scanning string literal
>>> a="meet"
>>> b="meet"
>>> a==b
True
>>> b='MEET'
>>> A
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> B.lower()
'meet'
>>> a==b
False
>>> b
'MEET'
>>> b="MEET"
>>> "MEET".lower()
'meet'
>>> b
'MEET'
>>> b=b.lower()
>>> a==b
True
>>> 
>>> my_string="bananayellowthinkhatgreyBIGcalifornia314"
>>> meet_value="THINK BIG"
>>> MY_STRING[12:17]
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    MY_STRING[12:17]
NameError: name 'MY_STRING' is not defined
>>> my_string[12:17]
'think'
>>> my_string[25:28]
'IGc'
>>> my_string[24:27]
'BIG'
>>> meet_value=my_string[12:17]+my_string[24:27]
>>> meet_value
'thinkBIG'
>>> meet_value=my_string[12:17] +" "
=
>>>  meet_value=my_string[12:17] +" "+meet_string[24:27]
 
SyntaxError: unexpected indent
>>> meet_value=my_string[12:17] +" "+meet_string[24:27]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    meet_value=my_string[12:17] +" "+meet_string[24:27]
NameError: name 'meet_string' is not defined
>>> meet_value=my_string[12:17] +" "+my_string[24:27]
>>> meet_value
'think BIG'
>>> meet_value.upper()
'THINK BIG'
>>> 
