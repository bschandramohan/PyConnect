# PyConnect
Learn Python 

# Cheat Sheet for Kotlin programmers to get started with python
* No curly braces. Use Tabs for not only indentation but also denoting "blocks"
* no var, val for variable definitions
* def function_name(): instead of fun functionName() {}
* Note division is always float even for integer numbers (use // for integer results)
* type(obj) to get the type 
* Methods like float(), str() for conversion
* fstring - f"Value of reminder={reminder}"
* if: elif: else: syntax instead of if, else if, else
  * no support for when (or java - switch)
* or, and, not (literal strings for joining comparisons instead of || && ! respectively)
* negative index ; for e.g. [-1] for accessing list's last element
* function arguments using names=
* dictionary {} - hashmap ; for-in returns key
* docstring - function """documentation""" first line
* local scope is for functions - not if, for, while etc
* global variable using "global"
* list comprehensions 
    * squares = [i*i for i in range(10)]
    * evens = [i for i in range(100) if not i % 2]
* *args in function to denote variable-length arguments and **kwargs to get variable length pairs of key,values
* try: except: else: syntax instead of try catch finally
* class attributes and object attributes are different and can be added dynamically
* private members with __ prefix, protected with _
* inheritance with class sub_class(base_class)
* Flask is de-facto standard for beginner web apps (Django is popular for commercial grade applications) 
  - comparable to Spring boot web-mvc framework for quick starts? 

# Tips
* Thonny / PythonTutor.com <- Visual stack/debugging if you don't want heavy tools like pycharm
* pycharm tip:  Option + Shift key - click and drag down to do column wise add for all rows
* pycharm tip: Cmd+F12 to view list of all methods

# Useful links
* Ascii Art: https://ascii.co.uk/art
* Logo generator: https://patorjk.com/software/taag/#p=display&f=Big%20Money-se&t=Amazing%20%20Python%0A
    -  also check font : Graffiti
* Trivia Database API: https://opentdb.com/api_config.php
