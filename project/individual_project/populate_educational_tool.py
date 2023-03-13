import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'individual_project.settings')

import django
django.setup()
from educational_tool.models import Category, Page, video, exercise , topic, tutorial
import inspect

def populate():
     # First, we will create lists of dictionaries containing the pages
     # # we want to add into each category.
     # # Then we will create a dictionary of dictionaries for our categories.
     # # This might seem a little bit confusing, but it allows us to iterate
     # # through each data structure, and add the data to our models.


        tutorial_pages = [
        {'id':'1','title':'Loop Tutorial',
        'problem':"""Write a program that outputs numbers one to ten using a for loop. """,
        'answer':
        """for i in range(1, 11):
                print(i)
    
    """},
        {'id':'2','title':'Comments Tutorial',
        'problem':""" write a program and include comments using a '#' sign.
          Note anything after the # sign will not be registered on the output. 
          
          Task : print('hello world') and have a comment next to it saying 'this prints hello world'
          to check your implementation look at the comments tutorial
        
        """,'answer':"""print('hello world')#this prints hello world"""},
        {'id':'3','title':'Loops 2 Tutorial',
         'problem':"""
         Write a program that uses a for loop to print all the even numbers between 1 and 20.

         Hint/help : use for loop
                use an if statement
                and a print statement to print output
         """,
         'answer':
         """for i in range(1,21):
                if i % 2 == 0:
                        print(i)
            #This program uses a for loop to iterate through the numbers 1 to 20, 
            # and then uses an if statement to check if each number is even 
            # (i.e., divisible by 2). If the number is even, it is printed to the console.
         """},
          {'id':'4','title':'Indexing Tutorial',
         'problem':"""
         Write a program that creates a list of 5 numbers and then prints the second and fourth numbers in the list.
                
         hint/ help : create a list variable
                     use list indexing 
                     remeber first element in the list
                     use print statement to output  
         """,
        'answer':
        """numList = [2, 4, 6, 8, 10]
print(numList[1], numList[3])
#This program creates a list of 5 numbers [2, 4, 6, 8, 10]
# and then uses indexing to print the second and fourth numbers in the list (which are 4 and 8, respectively).
        """},
          {'id':'5','title':'Boolean Tutorial',
         'problem':"""
        create two variables num1 and num2, let num1 = 7 and num2 = 9 
        Write a program that checks if the num1 is greater than the num2. If it is, the program should print "The first number is greater." If not, it should print "The second number is greater.
         """,'answer':
        """# This program checks if the integer value 5 is greater than the integer value 3. 
# Since 5 is greater than 3, the if statement is true and the program prints the string 
#"The first number is greater." to the console. 
# If the if statement were false, 
# the program would print the string "The second number is greater." to the console instead.

# code is below this comment
num1 = 5
num2 = 3
if num1 > num2:
        print("The first number is greater.")
else:
        print("The second number is greater.")
         """},
          {'id':'6','title':' Casting Tutorial',
         'problem':"""
         Write a program that takes the string "10" and casts it to an integer, adds 5 to it, and then prints out the result.""",
        'answer':"""numString = "10"
numInt = int(numString)
numPlusFive = numInt + 5
print(numPlusFive)
         """},
          {'id':'7','title':'Variables & DataTypes Tutorial',
         'problem':"""
         Write a program that assigns your name and age to variables, and then prints out a message that says "Hello [name], you are [age] years old.
         """,
        'answer':"""name = "John"
age = 17
print("Hello " + name + ", you are " + str(age) + " years old.")
         """},
          {'id':'8','title':'Lists',
         'problem':"""Write a program to create a list of your favorite fruits and print each fruit on a new line.""",
        'answer':"""favorite_fruits = ["apple", "banana", "mango", "strawberry"]
for fruit in favorite_fruits:
        print(fruit)
         """},
          {'id':'9','title':'Variables Tutorial',
         'problem':""" Task: Write a program to assign a value of 10 to a variable named "number" and print the value of the variable.""",
'answer':"""number = 10
print(number)

         """},
          {'id':'10','title':'If/Else & functions Tutorial ',
         'problem':"""
         Write a program to define a function that takes a number as an argument and prints "even" if the number is even, and "odd" if the number is odd. Code:
         """,
        'answer':"""def even_odd(num):
        if num % 2 == 0:
                print("even")
        else:
                print("odd")

# Example usage:
even_odd(7)  # Output: odd
even_odd(10)  # Output: even
         
         """},
         ]

        topic_pages = [
        {'id':'1','title': ' Loops',
        'content':"""Imagine you have a big box of crayons with 100 different colors, and you want to count how many colors there are. You could start at the first crayon and count  \"1 \", and then move on to the second crayon and count  \"2 \", and so on until you \'ve counted all 100 crayons. This would take a lot of time and effort! 
        Instead, you could use a loop, which is like a special kind of counting machine. You tell the computer to start at the first crayon and count up to 100, and then it does all the counting for you automatically. In the same way, when we \'re writing computer programs, we might have to do something over and over again, like adding up a bunch of numbers or checking a bunch of items in a list.

        Instead of doing the same thing manually each time, we can use loops to make the computer do it for us automatically. Loops help us save time, reduce errors, and make our programs more efficient 
        
        In programming, a loop is a way to repeat a set of instructions multiple times. There are two main types of loops in Python: for loops and while loops.
        
        A "for loop" and a "while loop" are both ways to make the computer do something over and over again, but they work in slightly different ways.

        A "for loop" is like a countdown. Imagine you're counting down from 10 to 1. You start at 10, count down to 9, then 8, then 7, and so on, until you get to 1. In a for loop, we usually know how many times we want to do something, and we count down until we're done.

        A "while loop" is more like a game of tag. Imagine you're playing tag with your friends, and you keep running until someone tags you. You don't know how long you'll be running for, but you keep going until someone tags you. In a while loop, we keep doing something until a certain condition is met.

        So, the main difference is that a "for loop" is used when we know how many times we want to do something, and a "while loop" is used when we don't know how many times we want to do something, but we have a condition that needs to be met before we stop.
        """},
        {'id':'2','title':'Lists ',
        'content':"""
        1. Lists:

                A list is an ordered collection of values. The values that make up a list are called its elements, or its items. We will use the term element or item to mean the same thing. Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can be of any type. Lists and strings — and other collections that maintain the order of their items — are called sequences.
        
        1.1. List values
                There are several ways to create a new list; the simplest is to enclose the elements in square brackets ([ and ]):

                e.g 

                >>> list1 = [10,20,30,40]
                >>> mylist2 = ["spam","bungee","swallow"]
                The first example is a list of four integers. The second is a list of three strings. The elements of a list don’t have to be the same type. The following list contains a string, a float, an integer, and (amazingly) another list:

                     >>> zs = ["hello", 2.0, 5, [10, 20]]
                
                A list within another list is said to be nested.

                Finally, a list with no elements is called an empty list, and is denoted [].
                we can assign list values to variables or pass lists as parameters to functions:

        1.2 Accessing element:
        The syntax for accessing the elements of a list is the same as the syntax for accessing the characters of a string — the index operator: [] (not to be confused with an empty list). The expression inside the brackets specifies the index. Remember that the indices start at 0:

        for example i have a list called 'numbers' which stores 2 numbers => numbers = [17,20]

        numbers[0] would access the first element of the list i.e 17 

        print(numbers[0]) would output 17.


        Any expression evaluating to an integer can be used as an index:
        
        >>> numbers[9-9] evaluates to 17 

        1.3 List transversal 

        List traversal means moving through all the elements in a list and doing something with each one, like reading, modifying, or deleting them.

        >>> horsemen = ["war", "famine", "pestilence", "death"]
        >>> for h in horsemen:
        >>>     print(h)

        outputs: 
                war
                famine
                pestilence
                death

        11.4. List length

        The function len returns the length of a list, which is equal to the number of its elements. If you are going to use an integer index to access the list, it is a good idea to use this value as the upper bound of a loop instead of a constant. That way, if the size of the list changes, you won’t have to go through the program changing all the loops; they will work correctly for any size list:

        >>> horsemen = ["war", "famine", "pestilence", "death"]
        >>> for i in range(len(horsemen)):
        >>>     print(horsemen[i])

        11.5 List Membership

        List membership in Python means checking if a particular item exists in a list or not. It's like checking if a specific item is on your shopping list or not.

        In Python, you can use the "in" operator to check if an item is in a list. For example, if you have a list called "fruits" and you want to check if "apple" is in the list, you can use the command "if 'apple' in fruits:".

        If "apple" is in the list, the condition will be True and you can perform certain actions, such as printing a message or executing a block of code. If "apple" is not in the list, the condition will be False and the actions inside the "if" statement won't be executed.

        This is a useful operation when you want to check if a particular item exists in a list before performing certain actions on it.

        example:

        >>>  fruit_list = ['apple', 'melon']
        >>>  if fruit in fruit_list:
        >>>     print(fruits)
        >>>
        >>>ouputs:
        >>>     apple 
        >>>     melon


        11.6 List Operations 

        List Operations  - addition
        >>> list1 = [1,3]
        >>> list2 = [3,4,5]
        >>> list3 = list1 + list2 
        >>> print(list3)
        =>     outputs  [1,2,3,4,5]

        List Operations - append 
         append function adds element to the end of the list.

        >>>lista = [1,2]
        >>>list.append 
        >>> lista = [1.2.3]

         Appending to a list means adding a new item to the end of the list. Imagine you have a shopping list and you want to add a new item to it. To append the item to the list, you simply write the name of the item at the end of the list. Similarly, in Python, you can use the "append" method to add a new item to a list. For example, if you have a list called "fruits" and you want to add "banana" to it, you can use the command "fruits.append('banana')" to add it to the end of the list.


        11.7 Nested Lists

        Nested lists are lists that contain other lists as elements. They allow for organizing data in a hierarchical way, like a list of lists.  An example of a nested list could be a list of classrooms, and for each classroom, a list of students with their names. This allows for a hierarchical representation of data, making it easier to access and work with specific information.

        
        Nestsed list example:

        >>> classroom = ["classroom 1",["morgan" , "farid" , "john"],"clasroom2", ["Mike" , "Pete" , "Tim"]]

        Here the names of the students in the classroom are a nested lists (lists in a list) 


        """},
        {'id':'3','title':'Syntax',
         'content':"""Python Indentation
        Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
        
        The number of spaces is up to you as a programmer, the most common use is four (or 1 tab click), but it has to be at least one.

        You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

        """},
         {'id':'4','title':'Variables',
         'content':"""In programming, a variable is a named container that holds a value, which can be a number, a text string, or other data types. Variables are used to store information that can be manipulated or used throughout a program.

        Think of it like a labeled box that can hold different things, such as apples, oranges, or bananas. The box has a name, such as "fruit," and the contents of the box can be changed or replaced as needed.

        In programming, variables allow developers to write more efficient and flexible code. They can be used to store user input, perform calculations, and pass information between different parts of a program. By using variables, developers can avoid duplicating code and make their programs easier to maintain and modify.

        
        Creating Variables

        Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
        Example:

        >>> x = 5
        >>> y = "John"
        >>>print(x)
        >>>print(y)
        
        outputs: 
        => John 
        =>  5


        Case Sensitive - In Python, variables are case sensitive, meaning that variables with different capitalization are considered different variables. For example, "variable1" and "Variable1" are two different variables.

        Dynamically Typed -  Python variables can also change type dynamically, which means that a variable's value can be reassigned with a different type of data at any point in the program. For example, a variable can start out as a string, then later be changed to an integer.

        Type casting -   Type casting is the process of changing the data type of a variable. This can be done explicitly by using functions such as int(), str(), and float(). For example, converting a string "10" into an integer using int("10").

        Scope - In Python, variables have scope, which refers to the area of the program where the variable is defined and can be accessed. There are two types of variable scope: local and global. Local variables are defined within a function or block and can only be accessed within that function or block. Global variables, on the other hand, are defined outside of any function or block and can be accessed from anywhere in the program.

        Variables Naming Coventions - Variable naming convention is important in Python to avoid syntax errors. Variable names should start with a letter or underscore, followed by any combination of letters, numbers, and underscores. It's also important to choose descriptive and meaningful variable names.

        Examples:

        Case sensitive: variable1 and Variable1 are different variables.
        Type casting: int("10") converts the string "10" to an integer.
        Scope: a local variable defined within a function can only be accessed within that function. A global variable defined outside of any function can be accessed from anywhere in the program.
        Naming convention: variable names should start with a letter or underscore and use descriptive names, like "num_of_students".

         """},
          {'id':'5','title':'Data Types',
         'content': """
         Data types are a fundamental concept in programming, as they allow computers to understand and manipulate different kinds of information. In essence, a data type is a classification of data that determines the operations that can be performed on it and the way it is stored in memory.

        In Python, there are several built-in data types that programmers can use, including integers, floating-point numbers, strings, and booleans. Integers are whole numbers that can be positive, negative, or zero. Floating-point numbers, on the other hand, are numbers with decimal points. Strings are sequences of characters, such as words or phrases, that are enclosed in quotation marks. Finally, booleans are logical values that can be either true or false.

        Each data type has its own set of operations that can be performed on it. For example, integers and floating-point numbers can be added, subtracted, multiplied, and divided, while strings can be concatenated (i.e., combined) and split into substrings. Booleans can be used in logical operations, such as "and", "or", and "not", to determine the truth value of an expression.

        In addition to the built-in data types, Python also allows programmers to create their own custom data types using classes. A class is a blueprint for creating objects that have certain attributes and methods. For example, a programmer could create a custom data type called "Person" that has attributes such as name, age, and gender, as well as methods for interacting with other objects, such as "say_hello" or "introduce".

        Overall, data types are a crucial part of programming because they allow computers to understand and manipulate different types of information. By learning about the different data types available in Python, and how to use them effectively, high school students can gain a deeper understanding of how programming works and how to solve problems using code.



         
         """},
         {'id':'6','title':'Type Casting',
         'content': """Python Type Casting
         
        Specify a Variable Type
        There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
        Casting in python is therefore done using constructor functions:

        int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
        float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
        str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

        Type casting is the process of converting a value from one data type to another. This is a useful tool in Python programming because it allows you to manipulate data in different ways depending on the context in which it is being used. Here are some examples of type casting for each data type in Python:

        Integer: You can convert a float to an integer using the int() function. For example, int(3.14) would return 3.
        Float: You can convert an integer to a float using the float() function. For example, float(3) would return 3.0.
        String: You can convert an integer or float to a string using the str() function. For example, str(3) would return "3".
        Boolean: You can convert a string to a boolean using the bool() function. For example, bool("True") would return True.
        It's important to note that type casting can sometimes lead to unexpected results or errors if not used correctly. As such, it's important to understand the data types you're working with and the implications of type casting in your code

         """},
         {'id':'7','title':'Comments',
         'content': """ 
        1.1. Comments

        As programs get bigger and more complicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why.

        For this reason, it is a good idea to add notes to your programs to explain in natural language what the program is doing.

        A comment in a computer program is text that is intended only for the human reader — it is completely ignored by the interpreter.

        In Python, the # token starts a comment. The rest of the line is ignored. Here is a new version of Hello, World!.
         
        Example:

        Example of comments will be given in the comments tutorial.
         """}, 
         {'id':'8','title':'Numbers',
         'content': """
         Python Numbers
                There are three numeric types in Python:

                int
                float
                complex

        Int
        Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

        Float
        Float, or "floating point number" is a number, positive or negative, containing one or more decimals.


        Complex
        Complex numbers are written with a "j" as the imaginary part:

        To verify the type of any object in Python, use the type() function:

         example 
        >>> x = 1    # int
        >>> y = 2.8  # float
        >>> z = 1j   # complex


         
         """},
         {'id':'9','title':'Strings',
         'content': """
         
         Strings 

         Strings are sequences of characters in programming, such as letters, numbers, and symbols. They are widely used in programming to represent text-based data, such as names, addresses, and messages. Learning how to work with strings is an essential skill for programmers.

         To use strings in programming, you need to know how to create them, manipulate them, and access their contents. You can create strings using single quotes (' ') or double quotes (" "). To manipulate strings, you can use a variety of functions, such as concatenation, slicing, and formatting. Concatenation involves joining two or more strings together using the + operator. Slicing involves selecting a portion of a string using its indices, which represent its position in the string. Formatting involves inserting values into a string using placeholders, such as { }.

         You can access individual characters in a string using indexing, which starts at 0. For example, the first character in a string is at index 0, the second character is at index 1, and so on. You can also use negative indexing to access characters from the end of a string. For example, the last character in a string is at index -1, the second last character is at index -2, and so on.

        methods:


        upper() method

        upper is a method that can be invoked on any string object to create a new string, in which all the characters are in uppercase. (The original string ((string called mystring in this case)) remains unchanged.)
        
        
        There are also methods such as lower, capitalize, and swapcase that do other interesting stuff.
        >>> mystring = "Hello, World!"
        >>> mystring2 = mystring.upper()
        >>> print(mystring2)


        other methods:

        >>> mystring2.lower() 
        >>> mystring2.capitalize()
        >>> mystring2.swapcase()


        examples:

        Sure, here are some examples of working with strings in Python:

        Creating Strings
        - using single quotes
        str1 = 'Hello, World!'

        - using double quotes
        str2 = "This is a string."

         - using triple quotes for multi-line strings
        str3 = \"\"\"This is a multi-line
        string that spans
        multiple lines.\"\"\"

        Concatenation
        str4 = "Hello" + " " + "World!" # Output: "Hello World!"

        Slicing
        str5 = "Hello, World!"
        print(str5[0]) # Output: "H"
        print(str5[7:]) # Output: "World!"
        print(str5[:5]) # Output: "Hello"

        Formatting
        name = "Alice"
        age = 25
        greeting = "My name is {} and I'm {} years old.".format(name, age)
        print(greeting) # Output: "My name is Alice and I'm 25 years old."

        Accessing Individual Characters
        str6 = "Hello"
        print(str6[0]) # Output: "H"
        print(str6[-1]) # Output: "o"



        Now try the exercise on strings on the excercise dropdown list.

         """},
         {'id':'10','title':'Booleans',
         'content': """
         Boolean Values and Boolean Expressions

        There are only two boolean values. They are True and False. Capitalization is important, since true and false are not boolean values in python (remember Python is case sensitive).

        creating boolean varables:

        >>> x = True
        >>> Y = False 
        
        Boolean values are not strings!
        It is extremely important to realize that True and False are not strings. They are not surrounded by quotes. They are the only two values in the data type bool. Take a close look at the types shown below.

        >>> print(True) # outputs True
        >>> print(type(True)) # outputs <class 'bool'>
        >>> print(type(False)) # outputs <class 'bool'>

        >>> print(type(True)) #outputs <class 'bool'>
        >>> print(type("True")) #outputs <class 'str'>

        A boolean expression is an expression that evaluates to a boolean value. The equality operator, ==, compares two values and produces a boolean value related to whether the two values are equal to one another.
        In the first statement below, the two operands are equal, so the expression evaluates to True. In the second statement, 5 is not equal to 6, so we get False.
        
        >>> print(5 == 5) # outputs True
        >>> print(5 == 6) # outputs False 


        more examples:
        >>> x != y               # x is not equal to y
        >>> x > y                # x is greater than y
        >>> x < y                # x is less than y
        >>> x >= y               # x is greater than or equal to y
        >>> x <= y               # x is less than or equal to y


        Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (=) instead of a double equal sign (==). Remember that = is an assignment operator and == is a comparison operator. Also, there is no such thing as =< or =>.

         
         """},
         {'id':'11','title':'Operators',
         'content': """

        Python Operators

        Operators are used to perform operations on variables and values.

        In the example below, we use the + operator to add together two values:

        >>> print(10 + 5)

        Python divides the operators in the following groups:

        - Arithmetic operators
        - Assignment operators
        - Comparison operators
        - Logical operators
        - Identity operators
        - Membership operators
        - Bitwise operators

        for more about operators in python visit the webpage https://www.w3schools.com/python/python_operators.asp

         """},
         {'id':'12','title':'Dictionaries',
         'content': """

         A dictionary is a data structure in programming that stores key-value pairs. Think of a dictionary as a real-life book that has words and their definitions. In programming, a dictionary allows you to access a value using its corresponding key. For example, if you have a dictionary of student names and their grades, you can use a student's name as the key to get their grade.

        To use a dictionary in programming, you first need to create it. In Python, you can create a dictionary using curly braces { } or the dict() function. Here's an example:

        student_grades = {"Alice": 90, "Bob": 85, "Charlie": 95}

        In this example, the keys are the student names, and the values are their grades. You can access a value in the dictionary by using its corresponding key, like this:

        alice_grade = student_grades["Alice"]

        This will assign the value 90 to the variable alice_grade.

        You can also add or update key-value pairs in a dictionary using square brackets []. Here's an example:

        student_grades["David"] = 80  # add a new key-value pair
        student_grades["Alice"] = 95  # update an existing key-value pair

        To loop through a dictionary, you can use a for loop. Here's an example:

        for student, grade in student_grades.items():
        print(student, grade)This will print each student's name and grade.

        In summary, a dictionary is a useful data structure in programming that allows you to store and retrieve key-value pairs. You can create a dictionary using curly braces {} or the dict() function, access values using their keys, add or update key-value pairs, and loop through a dictionary using a for loop.


         """},
         {'id':'13','title':'If/Else',
         'content': """

         Python If ... Else

         In programming with Python, if/else statements are used to make decisions based on certain conditions. These conditions can be anything from user inputs to the state of the program itself. If/else statements allow the program to choose between different paths of execution based on these conditions.

        The basic structure of an if/else statement in Python is as follows:

        if condition:
        #       code to execute if condition is true
        else:
        #       code to execute if condition is false

        The condition is what determines which path the program will take. If the condition is true, the code inside the indented block following if will be executed. If the condition is false, the code inside the indented block following else will be executed instead.

        For example, let's say we want to write a Python program that takes a number as input and prints whether that number is even or odd. We can use an if/else statement to make this decision:

        num = 6

        if num % 2 == 0:
        print("The number is even.")
        else:
        print("The number is odd.")
        

        In this case, the condition num % 2 == 0 checks whether num is evenly divisible by 2. If it is, the program will print "The number is even." If it's not, the program will print "The number is odd."

        If/else statements are an essential part of programming and are used in almost every program. Understanding how to use them will allow you to write more complex programs that can make decisions based on input and program state.


        for more examples and excercises refer to tutorials and excercises on if/else statements.
         """},
         {'id':'14','title':'Functions',
         'content': """

         In programming, functions are used to encapsulate a set of instructions that perform a specific task. Functions allow you to reuse code and make your program more modular, which can make it easier to write, read, and maintain.

        A function in programming typically has a name, inputs, and outputs. The inputs are passed to the function as arguments, and the function performs some operations on those inputs before returning an output.

        The basic structure of a function in Python is as follows:


        >>> def function_name(argument1, argument2, ...):
        >>>     # code to perform task
        >>>     return output
        
        To use a function, you call it by its name and pass in the required arguments:
        example:

        >>> result = function_name(arg1, arg2, ...)

         For example, let's say we want to write a Python function that takes two numbers as input and returns their sum:

        >>> def add_numbers(num1, num2):
        >>>     sum = num1 + num2
                return sum

         
        We can call this function like this:
        >>> result = add_numbers(3, 4)
        >>> print(result) # output: 7

        In this case, the function add_numbers takes two numbers as input and returns their sum as output.

        Functions can be very useful in programming because they allow you to break down complex problems into smaller, more manageable pieces. By writing functions that perform specific tasks, you can write more organized and readable code that is easier to test and debug.
         
         """},
         {'id':'15','title':'Arrays',
         'content': """

         Python Arrays
         Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

         Arrays 
         Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

        creating an array 

        cars = ["Ford", "Volvo", "BMW"]

        What is an Array?
        An array is a special variable, which can hold more than one value at a time.

        If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

        car1 = "Ford"
        car2 = "Volvo"
        car3 = "BMW"

        However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

        The solution is an array!

        An array can hold many values under a single name, and you can access the values by referring to an index number.

        Access the Elements of an Array
        You refer to an array element by referring to the index number.

        get the value of the first array item:

        >>> x = cars[0]

        To get second value of the array  x = cars[1]

        The Length of an Array - Use the len() method to return the length of an array (the number of elements in an array). Return the number of elements in the cars array:

        >>> x = len(cars)


        Looping Array Elements:
        You can use the for in loop to loop through all the elements of an array.

        EXAMPLE:
        
        >>> for x in cars:
        >>> print(x)

        Adding Array Elements:
        You can use the append() method to add an element to an array.
        Add one more element to the cars array:
        cars.append("Honda")

        Removing Array Elements:
        You can use the pop() method to remove an element from the array.


        Note: The list's remove() method only removes the first occurrence of the specified value.

        example >>> cars.remove("Volvo")



        Excercises: visit the excercises dropdown list and click on arrays for an excercise on this content.
      
         """},
         {'id':'16','title':'Scope',
         'content': """
         Scope 

        In programming, scope refers to the accessibility of variables, functions, and objects in a program. Every variable or function in a program has a scope, which determines where in the code that variable or function can be accessed.

        A variable is only available from inside the region it is created. This is called scope.

        There are two types of scope: global scope and local scope. Global scope refers to variables or functions that can be accessed from anywhere in the program, while local scope refers to variables or functions that can only be accessed within a certain block of code.

        When a variable or function is defined within a block of code, it is said to have local scope. This means that it can only be accessed within that block of code, and any attempts to access it outside of that block will result in an error.

        On the other hand, when a variable or function is defined outside of any block of code, it is said to have global scope. This means that it can be accessed from anywhere in the program, including within other blocks of code.

        Understanding scope is important for writing efficient and bug-free code. By keeping variables and functions within their appropriate scopes, you can prevent unintended side effects and make your code easier to read and maintain.

        In summary, scope is a crucial concept in programming that refers to the accessibility of variables and functions in a program. It can be either local or global, and understanding how to use it correctly can help you write better code.


        Try excercises of involving scope by visiting the scope exercises in the exercises dropdown list.

         """}
         ]







        video_pages = [
        {'id':'1','title': 'Intro to why you should code',
        'url':'Dv7gLpW91DM'},
        {'id':'2','title':'What is python ',
        'url':'Y8Tko2YC5hA'},
        {'id':'3','title':'Syntax',
         'url':'AGnECmJFA9U'},
         {'id':'4','title':'Loops',
         'url':'wxds6MAtUQ0'},
         {'id':'5','title':'Variables',
         'url':'cQT33yu9pY8'},
         {'id':'6','title':'lists',
         'url':'ohCDWZgNIU0'},
         {'id':'7','title':'Numbers and strings',
         'url':'yuxD8OlI7Rc'},
         {'id':'8','title':'Type Casting',
         'url':'Qtq83lAoogM'},
         {'id':'10','title':'Data Types',
         'url':'afJ2CuFbHKo'},
         {'id':'11','title':'Python cheat sheet',
         'url':'A2NnIWCYnMQ'},
         {'id':'12','title':'',
         'url':'0NO3MJkxm2g'},
       ]
        #  {'id':'4','title':'Comments',
        #  'url':''},
        #  {'id':'5','title':'Variables',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'6','title':'Data Types',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'7','title':'Numbers',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'8','title':'Type Casting',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'9','title':'Strings',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'10','title':'Booleans',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Operators',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Lists',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Tuples',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Sets',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Dictionaries',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'If/ Else',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'While Loops',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'For Loops',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Functions',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Arrays',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Scope',
        #  'url':'0NO3MJkxm2g'}

        excercise_pages = [{'id':'3','title':'comments',
         'problem':""" write a program and include comments using a '#' sign.
          Note anything after the # sign will not be registered on the output. 
          
          Task : print('hello world') and have a comment next to it saying 'this prints hello world'
          to check your implementation look at the comments tutorial
            """},
            {'id':'4','title': 'Firstname & lastname',
        'problem': """You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
            Hello firstname lastname! You just delved into python.

            Function Description:

            Complete the print_full_name function in the editor below.

            print_full_name has the following parameters:

            string first: the first name
            string last: the last name
            Prints

            string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
            Input Format

            The first line contains the first name, and the second line contains the last name.

            Constraints: 

            The length of the first and last names are each ≤ Sample Input 0

            Ross
            Taylor
            Sample Output 0

            Hello Ross Taylor! You just delved into python.
            Explanation 0

            The input read by the program is stored as a string data type. A string is a collection of characters."""},
        {'id':'1','title':'loops',
         'problem':'Write a program that outputs numbers one to ten using a for loop. '} ,
          {'id':'6','title':'Loops 2',
         'problem':"""
         Write a program that uses a for loop to print all the even numbers between 1 and 20.

         Hint/help : use for loop
                use an if statement
                and a print statement to print output
         """} ,
          {'id':'7','title':'indexing',
         'problem':"""Write a program that creates a list of 5 numbers and then prints the second and fourth numbers in the list.
                
         hint/ help : create a list variable
                     use list indexing 
                     remeber first element in the list
                     use print statement to output  

                
         """} ,
          {'id':'8','title':'Boolean',
         'problem':"""
         create two variables num1 and num2, let num1 = 7 and num2 = 9 
         Write a program that checks if the num1 is greater than the num2. If it is, the program should print "The first number is greater." If not, it should print "The second number is greater.
         """} ,
          {'id':'9','title':'Casting ',
         'problem':"""Write a program that takes the string called string1, where string1 = "10", casts string1 to an integer, add 5 to it, and then prints out the result."""} ,
          {'id':'10','title':'Variables and datatypes ',
         'problem':"""Write a program that assigns your name and age to variables, and then prints out a message that says "Hello [name], you are [age] years old."""} ,
          {'id':'11','title':'Lists',
         'problem':"""Write a program to create a list of your favorite fruits and print each fruit on a new line."""} ,
          {'id':'12','title':'Variables ',
         'problem':"""Task: Write a program to assign a value of 10 to a variable named "number" and print the value of the variable."""} ,
          {'id':'13','title':'If/else and functions:',
         'problem':"""
         Write a program to define a function that takes a number as an argument and prints "even" if the number is even, and "odd" if the number is odd. Code:
         """}      
         
         ]


        python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'} ]
    
        django_pages = [
            {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'} ]

        other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'} ]

        cats = {'Python': {'pages': python_pages,'views':128,'likes':64},
        'Django': {'pages': django_pages,'views':64,'likes':32},
        'Other Frameworks': {'pages': other_pages,'views':32,'likes':16} }

        # If you want to add more categories or pages,
        # add them to the dictionaries above.




        for video_dict in video_pages:
                id = video_dict.get('id')
                title = video_dict.get('title')
                url = video_dict.get('url')
                c = add_vid(id,title,url)
        

        # The code below goes through the cats dictionary, then adds each category,
        # and then adds all the associated pages for that category.
        for cat, cat_data in cats.items():
                c = add_cat(cat,cat_data["views"],cat_data["likes"])
                for p in cat_data['pages']:
                       add_page(c, p['title'], p['url'])

    # Print out the categories we have added.
        for c in Category.objects.all():
                for p in Page.objects.filter(category=c):
                       print(f'- {c}: {p}')
        
        for ex_dict in excercise_pages:
               id = ex_dict.get('id')
               title = ex_dict.get('title')
               problem = ex_dict.get('problem')
               p = add_excercise(id,title,problem)
        
        for topic in topic_pages:
               id = topic.get('id')
               title = topic.get('title')
               content = topic.get('content')
               p = add_top(id,title,content)
        
        for tut in tutorial_pages:
               id = tut.get('id')
               title = tut.get('title')
               problem = tut.get('problem')
               answer = tut.get('answer')
               p = add_tut(id,title,problem,answer)
               


def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title)[0]
        p.url=url
        p.views=views
        p.save()
        return p

def add_vid(id,title, url):
     v = video.objects.get_or_create(id=id,title=title,url=url)[0]
     v.save()
     return v

def add_cat(name, views=0,likes=0):
        c = Category.objects.get_or_create(name=name,views =views, likes=likes)[0]
        c.save()
        return c



def add_excercise(id,title, problem):
     p = exercise.objects.get_or_create(id=id,title=title,problem=problem)[0]
     p.save()
     return p

def add_top(id,title, content):
       t  = topic.objects.get_or_create(id=id,title=title,content=content)[0]
       print(t)
       t.save()
       return t

def add_tut(id,title,problem,answer):
        tu= tutorial.objects.get_or_create(id=id, title=title, problem=problem, answer=answer)[0]
        print(tu)
        tu.save()
        return tu
       
       




# Start execution here!
if __name__ == '__main__':
    print('Starting educational_tool population script...')
    populate()



