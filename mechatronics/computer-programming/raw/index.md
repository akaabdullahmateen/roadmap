## Notes

- print() built-in function
  - print function will advance to the next line by default
  - sep and end parameters of print()
- python is case sensitive
- whitespace is mostly irrelevant except for indentation
- "5+5" is a string, while 5+5 is a mathematical expression
- repeated strings using string * 10 method
- concatenation using + and , inside print()
- operator , automatically inserts a space between its operands
- escape sequences, table of escape sequences
- data types, strings + numbers
- variables, assignment operator =
    - variable types are inferred
    - lhs = variable name, constants are not allowed
    - rhs = expressions or literals
- rules for naming variables or identifiers:
    - digits are not allowed as first characters, only a-z, A-Z, and underscore _
    - rest of the characters can be a-z, A-Z, underscore, and 0-9
    - names are case sensitive
  - use descriptive names for variables
- reserved words known as keywords that can not be used as names for variables
- list of keywords can be shown in program using:
    ```py
    import keyword
    keyword.kwlist()
    ```
- variables can be reassigned to new values
- list of mathematical operators
  - addition +
  - subtraction -
  - multiplication *
  - division /
  - modulus %
  - exponent **
  - floor division //
- augmented assignment: x+=5 instead of x = x + 5
- input from user with input() function
- eval() function to taking numeric input
- precedence of mathematical operators
  - parenthesis () (highest)
  - exponent **
  - division /, floor division //, modulus %
  - multiplication *
  - addition +, subtraction - (lowest)
- data type casting
- comments in python
  - comments are ignored by the interpreter
  - single line comments start with #
  - multiline comments are enclosed in triple quotes """
- number type in python
  - int - integers both positive and negative
  - float - floating-point real values both positive and negative
  - complex - complex numbers such as 2 + 3i
  - python does not need explicit type specifier, it infers type based on value for the variable
- data type casting/conversion: float() and int()
- multiple assignment of a variable
  - a = b = c = 5
  - x, y = 100, 200
  - x, y, z = 100, 200, "Alphabet"
- swapping values of two variables
  - a, b = b, a
  - x,y,z = z,x,y
- multiple inputs from user
  - x,y = eval(input("Enter two numbers separated by commas: "))
- f-strings for formatted strings, where expressions are embedded in curly braces {}
- TypeError that occurs when operands are not of correct type
- Type casting from string to integer, float
- Type casting from integer, float to string
- Useful functions in math module
- constants in math module (pi, tau, e, inf, nan)
- multiline statement with backslash \
- number formatting in f-strings: Format Specification Mini-Language
- round(x,p) rounds the floating point number x to precision p
- complex numbers, j is used as the imaginary unit
  - y = 3+4j
  - y = complex(3,4)
  - y = complex("3+4j")
  - y = complex(input("Enter a complex number: "))
- mathematical functions are valid for complex numbers as well
  - complex1 * complex2
  - abs(complex1)
- methods from complex class
  - real_part = complex_number.real
  - imag_part = complex_number.imag
  - conjugate_part = complex_number.conjugate()
- relational operators: >, <, >=, <=, ==, !=
- The if conditional statement
  - the statements inside the if block must be indented
- The if else statement
- logical operators: and, or, not
- elif statement for else if blocks
- user defined functions:
  - def func_name():
  - function name can be any name following the variable naming rules
  - function is called by func_name()
  - add comment at the first line of function to write description of what the program does
  - after functions, before the program start, at global indent, write a comment that program starts here
- flow of execution of programs which have functions
  - execution flow jumps to function when the function is called
  - and returns to the calling position after the function returns
- functions can have parameters in parenthesis
  - def func_name(arg_name)
  - this parameter becomes locally available inside the function so it can be used like any other variable
- functions can return values
  - def sum(a, b): return a + b
- variables created inside functions are local variables and are only visible inside the function
  - variables declared elsewhere with the same names as the function's local variables are totally different objects
- python has two types of loops: for and while
- just like if-else and function blocks, for loop body needs to be indented as well
- the range function is commonly used to iterate over a sequence of numbers
- range(start, stop, step)
  - start is the inclusive start number
  - stop is the exclusive stop number. the exact number stop is not included in the sequence
  - step is the difference between two consecutive numbers
  - for positive steps: range[i] = start + step * i, i >= 0, with constraint range[i] < stop
  - for negative steps: range[i] = start + step * i, i >= 0, with constraint range[i] > stop
- boolean type: True or False, True == 1, False == 0
  - False is null objects, and zero etc
  - True is anything other than zero and null objects, so True == 5 etc
- when functions return nothing, we can check for None
  - y = func_name(something)
  - if y == None: # means that the function did not return anything
  - None means that the variable is defined but contains nothing
- nested loops, where a for loop is nested inside an outer for loop
- while loop is another form of loop that iterates as long as the condition is true
- any logic written in for loop can be written using while loop and vice versa
  - however, in practice the use cases are slightly different
  - for loop is used when we need a fixed number of iterations
  - while loop is used when we need an arbitrary number of iterations constrained by some condition
- break statement terminates loop execution and transfers the execution to the statement immediately outside the loop block
- the break statement breaks the execution of its parent loop only, so it terminates the inner loop but the outer loop keeps on iterating
- break statements are often used with infinite loops such as while true
- continue statement makes the execution skip the remaining part of the loop for that iteration and skip to the next iteration
- the pass statement is a null operation; nothing happens when it executes
  - the pass statement is useful in places where the execution will eventually go, but code has not been written yet. for example:
  - if x < 100: do something;;;; else: pass
- the builtin function exit() ends the whole program. this can be used in an if-else block, user-defined functions, etc.
- else statement can be used with for and while loops
  - the else block is executed when the loop does not encounter any break statement
  - the else block is not executed when the loop encounters any break statement
  - this allows to write logic compactly which would otherwise require a flag to handle
  - such as:
  ```py
  flag = False
  for i in range(2, n):
    if n % i == 0:
      flag = True
      break
  if flag == True:
    print("Not prime")
  else:
    print("Prime")
  ```
  ```py
  for i in range(2,n):
    if n % i == 0:
      print("Not prime")
      break
  else:
    print("Prime)
  ```
- to clear screen, we use either os.system("cls") if on windows , or os.system("clear") if on linux or mac.
  ```py
  import os
  if os.name() == "nt":
    os.system("cls")
  else:
    os.system("clear")
  ```
- to introduce some time delay. we use the sleep(n) function from the time module in python, where n is the number of seconds to sleep for. for example: time.sleep(5) pauses the execution for 5 seconds.
- the builtin input() function waits for the user to enter something, however, sometimes we do not want to wait. bcz we need to keep running the program and do not want to halt it, such as in games. in a game loop we want to detect if a user entered some key and update game logic accordingly, but we do not want to pause the game loop while the user enters something or not, the game screen will be frozen until the user enters something. in this type of scenario, we use kbhit() function from msvcrt module. kbhit() detects if the user hit any keyboard key, while the program is running. it does not wait for user to hit any key. if the user did hit some key, it returns True, if the user did not enter any key, it returns False. the program keeps running smoothly, and does not halt while the user is hitting keys or not. when kbhit() returns True, we want to detect what the entered key was. so we use the getch() or getwch() methods from msvcrt module. this function reads the key that was pressed by the user, bcz of which kbhit() returned True. i.e., it reads the character already present on the stdin. the user does not need to press enter for the key to be detected.
  ```py
  import msvcrt
  while True:
    # some program logic
    if msvcrt.kbhit():
      char = msvcrt.getch() # or char = msvcrt.getwch()
      # use char value to do whatever u like, like exit loop, update variables etc
  ```
- however, msvcrt.kbhit() and msvcrt.getch() are available for windows only. only posix (linux and mac), we need to use different logic to get the same result. for kbhit(), the equivalent is the following code:
  ```py
  def posix_kbhit():
    import select
    import sys
    dr,dw,de = select.select([sys.stdin],[],[],0)
    if dr != []:
      return True # some key was hit
    else:
      return False # no key was hit
  ```
- for getch(), the equivalent is the following code:
  ```py
  def posix_getch():
    import sys
    char = sys.stdin.read(1)
    return char
  ```
- now on posix (linux and mac), we can do the following:
  ```py
  while True:
    # some program logic
    if posix_kbhit():
      char = posix_getch()
      # do something with char
  ```
- to import a specific function or object from a module, instead of importing the whole module, we can do this: `from module import object`, such as `from math import sqrt`
- we can import the entity with a custom name using the `as` keyword. this is helpful when the imported entity has a long name by default. such as `from math import sqrt as sq`, now we can use `sq(34)` to get the squareroot.
- to generate random number, we use the python `random` module, the random module provides three functions to generate random numbers:
  - `random()` which generates a random floating point number from `0.0` (inclusive) to `1.0` (not inclusive).
  - `randint(a,b)` which generates a random integer from `a` (inclusive) to `b` (inclusive)
  - `randrange(a,b)` which generates a random integer from `a` (inclusive) to `b` (not inclusive)
- lists are array-like objects in python to store a lot of anonymous values. the entries of lists are generally known as elements or items
- a list is defined by specifying its element inside square braces: `a = [4,5,2,-1]`
- lists can contain elements of different types: `a = [0.1, "Something", 5, True]`
- lists can be printed simply by: `print(list_name)`
- lists are zero indexed. so individual elements are accessed like: `a[0]`, `a[1]`, ... , `a[len(a) - 1]`
- lists are mutable, so elements can be modified.
  ```py
  a = [1,2,5,-4]
  a[2] = 0.1
  # a = [1,2,0.1,4]
  ```
- to access the elements in reverse direction, i.e., from the other end, we use negative indexes. where last element of the list has index `-1`, second last has index `-2`, etc, till the first element with index `-(len(a))`
- apart from accessing single elements from a list, multiple elements can be selected from a list using list slicing
- list slicing is similar to `range()`, where we provide start, stop, and step values
- negative indexes can be used as well in list slicing
  ```py
  a=[  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
  # [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9]  Positive Indices
  # [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]  Negative Indices
  print(a[0:4]) # Will print [1, 2, 3, 4]
  print(a[2:4]) # Will print [3, 4]
  print(a[0:9:2]) # Will print [1, 3, 5, 7, 9]
  # We can also specify the last index as -1
  # So that we do not need to know total number of List elements.
  print(a[0:-1:2]) # Will print [1, 3, 5, 7, 9]
  print(a[2:-2]) # Will print [3, 4, 5, 6, 7, 8]
  ```
- we can use the builtin `len()` function to get the length or size of a list
- we can use the `in` operator to test membership of an element in a list:
  ```py
  a = [7,6,4,-2,-4,0,2]
  if 6 in a:
    print("6 is in the list A")
  else:
    print("6 is not in the list A")
  if 2 not in a:
    print("2 is not in the list A")
  else:
    print("2 is in the list A")
  ```
- we can also iterate over an entire list using the `for ele in list` syntax
  ```py
  some_list = [2,5,56,251]
  for list_item in some_list:
    # do something
  ```
- the `list_item` will contain the items from the list, rather than index. so in the first iteration, `list_item == 2`, in the second, `list_item = 5`, and so on.
- list operations:
  - list concatenation: `list_a + list_b` evaluates to a new list that has the elements of list_a followed by the elements of list_b. so if `list_a = [1,2,3]` and `list_b = ["a","b","c"]`, `list_a + list_b = [1,2,3,"a","b","c"]`
  - list repetition: `list_a * n` evaluates to a new list that has the elements of list_a repeatedly concatenated `n` times, in order. so if `list_a = [1,2,3]`, then `list_a * 3 = [1,2,3,1,2,3,1,2,3]`.
  - list equality. two lists are equal if and only if they have the same length and there corresponding elements are equal. so `[1,2,3] == [1,2]` evaluates to False, whereas, `[1,2,3] == [1,2,3]` evaluates to True.
  - list comparison. two lists are compared like this: the first elements (at index 0) are compared. if the first element in list_a is greater than the first element in list_b, list_a is greater than list_b. if the first_elements are equal, the second element is compared in a similar manner. if all the elements in the shorter list are equal to the corresponding elements in the longer list, the list that is longer, is considered greater.
    ```py
    [1,2,3] > [1,1] # True because second element is greater
    [1,2,3] > [1,2] # True because the first list is longer even though corresponding elements are same
    ```
- empty lists can be defined in two ways. `my_list = []` and `my_list = list()`.
- lists have builtin methods: for the examples, we assume `my_list = [1,2,3]` initially.

| Method | Description | Example | Output |
| - | - | - | - |
| `append(x)` | Appends `x` at the end of the list | `my_list.append(6)` | `[1,2,3,6]` |
| `insert(i,x)` | Inserts `x` at the index `i` | `my_list.insert(1,6)` | `[1,6,2,3]` |
| `pop(i)` | Removes the element at index `i` | `my_list.pop(1)` | `[1,3]` |
| `remove(x)` | Removes the first occurrence element `x` from the list | `my_list.remove(2)` | `[1,3]` |
| `count(x)` | Gives the number of times `x` is present in the list | `my_list.count(2)` | `1` |
| `index(x)` | Returns the index of the first occurrence of `x` in the list | `my_list.index(2)` | `1` |
| `clear()` | Removes all entries from the list | `my.list.clear()` | `[]` |
| `sort(reverse=False)` | Sorts the elements in the list in ascending order, if `reverse=False` (default), and in descending order if `reverse=True` | `my_list.sort(reverse=True)` | `[3,2,1]` |
| `reverse()` | Reverses the list | `my_list.reverse()` | `[3,2,1]` |
| `extend(list_a)` | Concatenates the `list_a` at the end of the calling list | `my_list.extend([5,4,3])` | `[1,2,3,5,4,3]` |

- Python has builtin methods that can be used on lists:

| Method | Description | Example | Output |
| - | - | - | - |
| `len(a)` | Returns the length of the list `a` | `len(my_list)` | `3` |
| `max(a)` | Returns the maximum value inside list `a` | `max(my_list)` | `3` |
| `min(a)` | Returns the minimum value inside list `b` | `min(my_list)` | `1` |
| `sorted(a, reverse=False)` | Returns the list `a` sorted in ascending order if `reverse=False` (default), or in descending order if `reverse=True` | `sorted(my_list,reverse=True)` | `[3,2,1]` |
| `sum(a)` | Returns the sum of all the elements inside the list `a` | `sum(my_list)` | `6` |
| `all(a)` | Returns `True` if all values inside the list `a` are truish (only `0` and `False` are falsey, all other values are truish) | `all(my_list)` | `True` |
| `any(a)` | Returns `True` if there is at least one value inside the list `a` that is truish. Returns `False` when all the values inside the list are falsey | `any(a)` | `True` |

- Aside from these list methods and builtin methods, there is a keyword `del` in python, that is used to delete any variable, and likewise can be applied on lists.

```py
a = [1,2,3,4,5]
del a[2]
print(a) # [1,2,4,5]
del a
print(a) # NameError: name 'a' is not defined
```

- `list()` can be used to convert a lot of objects to lists.
  - `list(range(start,stop,step))` will convert the values given by `range()` to a list in order
  - `list("somestring")` will create a list: `["s","o","m","e",...]`
  - `list(my_tuple)` will convert the tuple to a list
  - `list(my_set)` will convert the set to a list
- apart from accessing a single element from a list through indexing, we can also access multiple elements through list slicing
  - list slicing follow a syntax similar to the `range()` function: `a[start:stop:step]`.
  - if `step` is not given, the default `step=1` is used
  - if `start` is not provided, the default `start=0` is used (i.e., the first index)
  - if `stop` is not provided, the default `stop=len(a)` is used i.e, the one past the last index.
  - when both `start` and `stop` are omitted, they become the ends of the list `0` and `len(a)`. whether `start` becomes `0` or `stop` becomes `0` depends on the sign on `step`. so `a[::1]` means, `start=0`, `stop=len(a)`, whereas, `a[::-1]` means, `start=-1` and `stop=-len(a)-1`
- the random module has some functions that can be used with lists. we assume `a=[3,6,10,6]`

| Function | Description | Example | Output |
| - | - | - | - |
| `choice(a)` | Picks a random item from list `a` | `random.choice(a)` | `10` |
| `sample(a,n)` | Picks a group of `n` random items from list `a` | `random.sample(a,2)` |`[6,6]` |
| `shuffle(a)` | Shuffles the items in list `a` | `random.shuffle(a)` | `[6,6,3,10]` |

- Lists can be passed as input parameters to functions. Likewise, list can be used as return values of a function.
- A variable declared inside a function is called a local variable
- A variable declared at global indentation is called a global variable.
- Local variables are only accessible inside the function they are declared
- Global variables are accessibly available.
- If a function declares a variable with the same name as a global variable, the local variable will take preference.
- A function can not both use a global variable and a local variable with the same names. Look at the function below:

```py
def func():
  y = x        # Intention: assign y with the value of the global variable x
  x = 10       # Intention: assign the local variable x with the value 10
  return y

x = 50
print(func())
```

- This function wants to use both a global variable and a local variable with the same names. This will raise an error: "UnboundLocalError: local variable 'x' referenced before assignment.
- This is necessary to ensure that there is no ambiguity between a global and local variable.
- However, to explicitly use the global variable WHEN there is an assignment to the same name inside the function, we need to use the `global` keyword. The `global` keyword tells the interpreter that we intend to use the global variable x, and any assignments to x does not mean that we are creating a new local variable x, but rather, we are assigning to the global variable x.
- The `global` keyword states that the identifier is to be interpreted as a global variable. And that any consequent use of it (including assignments) refers to that global variable, and not a local variable.
- Therefore, to correct the function written in the previous example, and do exactly what the intention is, we need to modify it as such:

```py
def func():
  global x     # x is to be interpreted as a global variable throughout the function block
  y = x        # assign y with the value of the global variable x
  x = 10       # assign the global variable x with the value 10
  return y

x = 50
print(func())
print(x)       # x = 10 since changes to the global variable in the function
               # are reflected throughout the program
```

- Generally, global variables are discouraged. However, there are certain situations where global variables must be used. The possible cases where we need to use global variables is the possibility to update variable in multiple functions e.g. score of a player in some game. There can be multiple functions in a game that can change or reset the score so in such case we should declare score variable as a global variable.
- Modifying global names is generally considered bad programming practice because it can lead to code that is:
  - Difficult to debug: Almost any statement in the program can change the value of a global name.
  - Hard to understand: You need to be aware of all the statements that access and modify global names.
  - Impossible to reuse: The code is dependent on global names that are specific to a concrete program.
- When a function is declared inside another function it is called a nested function or enclosed function, and the outer function is called the enclosing function. For example, in the code sample below, `outer_func()` is the enclosing function of the nested function called `inner_func()`.

```py
def outer_func():
  print("Enclosing function")
  def inner_func():
    print("Nested function")
    return
  return
```

- Just like functions can access names from the global scope, inner functions can access names from the enclosing scope. Enclosing scope is the scope of the enclosing function.
- However, just like there can be ambiguity between global and local variables, there can be ambiguity between nested function's local variables, and enclosing scope's variables.
- As a result, just like we can use `global` keyword to unambiguously declare that the name belongs to the global scope, we can use `nonlocal` keyword to unambiguously declare that the name belongs to the enclosing scope.
- The `nonlocal` keyword specifies that the name does not belong to the local scope, and it is sharing the scope of the outer (enclosing) function.

```py
def outer_func():
  x = 5
  print(f"Outer function: {x}")           # x = 5
  def inner_func():
    nonlocal x
    x = 10
    print(f"Inner function: {x}")         # x = 10
  inner_func()
  print(f"Back to outer function: {x}")   # x = 10
```

- Python resolves names using the LEGB rule, where it first searches for the variable inside the local scope, then in the enclosing scope, then the next enclosing scope, and so on, until the global scope, then it searches in the global scope, and finally in the builtin scope.
  - L: Local
  - E: Enclosing
  - G: Global
  - B: Builtin
- This means that the variable will be first searched for in the function's own local scope. If found it will be used, otherwise, it will looked for in the function's enclosing scope, which is the scope of the function enclosing it (i.e, its outer function). If found, then that variable will be used, otherwise, the search will be moved to the function's outer function's enclosing scope, and so on. If the variable is not found, it will be searched for in the global scope, if found then that will be used, otherwise, it will be searched for in the builtin scope.
- The builtin scope includes the builtin functions, variables, methods, classes etc. These are error names like: `ArithmeticError`, keywords like `False`, special names like `__name__`, builtin functions like `abs()`, etc.

```py
import builtins
print(dir(builtins))
```

- For longer programs, the Python script can be broken down into multiple files called modules. This makes the maintenance easier and also allows to define a function once for use in multiple programs without copying its definition into each separate program.
- Either the whole module can be imported (`import module_name`) or individual definitions inside that module can be imported (`from module_name import definition_name`).
- A module is a Python file containing definitions and statements. The file name is the module name with the `.py` extension. So a module named `math` will have a file name `math.py`. Within the module, the module's name is available as the value of the global variable `__name__` as a string.
- To create a Python package (a package is a collection of multiple modules), we can create a directory with the name `package_name`, and add module files into it `module1.py`, `module2.py` etc. But we also need to add one additional file called `__init__.py`. This `__init__.py` file is often empty, but can contain anything like normal Python scripts. Therefore, the package directory will look like this:

```plain
/package_name
  /__init__.py
  /module1.py
  /module2.py
```

- When you import a module into a python script, the module file is searched for in the same directory as the file importing the module. Then it searches for in specific locations. To see these locations, run the following code:

```py
import sys
print(sys.path)
```

- If you want to add the module into some other directory (which is not the directory where the module will be imported, or one of the paths specified by `sys.path`), you can edit the shell variable `PYTHONPATH`. On Windows, this can be done by opening: Edit Environment Variables, and creating a new variable called PYTHONPATH, and setting its value with the path that you want.
- An interesting thing about modules is that, inside the module file, the value of the global variable `__name__ ` is the module name. However, when the module file is run with something like `python module_name.py`, the value of the global variable `__name__` is set to `"__main__"`.
- This feature allows you to use command line arguments when the module is run directly with `python module_name.py`, while at the same time, allowing it to behave properly when imported as a module.

```py
if __name__ == "__main__":
  import sys
  sys.argv[1] # do something with these command line arguments
```

- For example, if the module contains the above code, the `if` statement will not be executed when the module is imported since `__name__` would be the module name and NOT `__main__`, and therefore, the program will not crash as `sys.argv[]` is not available, However, when the same module is run from the command line with `python module_name.py`, the `if` statement will be executed, since `__name__` will be set to `__main__`, and therefore, the command line arguments would be available.
- A Python list can contain elements of different data types. So, `my_list = [1, "Hello", False]` is a valid list. Likewise, it can contain another list as an element as well. So `my_list = [1, "Hello", False, [1,2,3,4,5]]` is also a valid list. This list contains four elements, the last element is itself a list, and its elements can be accessed by `l[3][0]`, `l[3][1]`, and so on. Basically, the expression `l[3]` evaluates to the sublist `[1,2,3,4,5]` and so the expression `l[3][0]` is reduced to `sublist[0]`.
- The fact that lists can contain sublists, allows use to create two dimensional lists, i.e., lists whose elements are lists. for example: `A = [[1,2,3],[2,3,4],[3,4,5]]`.
- Just like lists, tuples are ordered sequences of objects. And just like lists, tuples can contain elements of different data types.
- Tuples are initialized with parenthesis instead of square brackets:

```py
my_tuple = (1,"Hello",False)
```

- The builtin `sorted()` function when applied on lists, returns the sorted list. However when we apply `sorted()` on a tuple, it returns a list.
- So the question is why do we need tuples when we have lists?
  - To answer this, we need two key indicators of performance: memory consumption and time for execution.
  - Memory consumption can be tested with the `getsizeof()` method available in the `sys` module. So to check the size of a list and a tuple we can compare `sys.getsizeof(my_list)` and `sys.getsizeof(my_tuple)`. It can be shown that tuples take much less memory than lists.
  - Execution time can be tested with `timeit()` method from the `timeit` module. In this function, we need to specify the statement whose execution time we want to measure, and the number of times, we want to execute that statement. So to measure the execution time of an operation on list, and similarly for a tuple, we can use `timeit.timeit(stmt="a=[1,2,3,4,5],number=100_000_000)` and `timeit.timeit(stmt="a=(1,2,3,4,5),number=100_000_000)` respectively. here we are measuring the execution time for initializing a list 100 million times, and similarly for a tuple. We need to run this 100 million times, because a single initialize statement very very little time. It can be shown that tuples are much faster than lists.
- Now, the question is, if tuples are both faster and take less memory than lists, why do we need lists?
  - First because, the list class supports much more methods than what the tuple class provides. This can be tested with `dir(list)` and `dir(tuple)`. Other than the magic methods (starting and ending with double underscores), there are only 2 methods in the tuple class, whereas list class has 11. The 2 methods of the tuple class are `count()` and `index()` which works exactly the same as those for lists,i.e., return the number of elements with the specific value (provided as argument) in that tuple, and the index of the first occurence of the element with the specific value (provided as argument) in that tuple.
  - Tuples are immutable whereas lists are mutable. Elements inside the tuple can not be reassigned in any form or way. Thus a tuple can not be modified once it is created. Whereas, elements in a list can be freely modified in many ways.
- Packing: We can create a tuple like this: `a = (1,2,3,4)`. This will create a tuple `a` with the said values. However, we can remove the parenthesis, and still get a tuple: `a = 1,2,3,4`. This will also create a tuple. This is not as **packing** the objects into a tuple.
- Unpacking: We can also retrieve all elements of the tuple as: `a,b,c = t`, provided `t = (1,2,3)`. This will assign the elements of the tuple to the respective variables `a`, `b`, and `c`, in order. This is called **unpacking** a tuple.
- Unpacking like this does not work when the number of variables on the left side are not equal to the number of elements inside the tuple. If the number of variables are greater, we will get the error: bot enough values to unpack. Whereas, if the number of variables are lesser, we will get the error: too many values to unpack.
- However, we can do this:

```py
t = (1,2,3,4,5,6,7,8) # a tuple
a, b, *c = t
print(a) # a = 1
print(b) # b = 2
print(c) # c = [3,4,5,6,7,8]
```

- This will unpack the first element to `a`, the second element to `b`, and unpack the rest of the elements to `c` as a list. Therefore, `c` will be a list with values of third, fourth, so on, elements.
- We can place the operator `*` to any one of the variables on the left side. So `*a,b,c = t` will unpack all the elements in order to `a` as a list, except the last two elements, which will be assigned to `b` and `c` respectively. However, we can only use `*` operator on any one of the variable, and not more than that.
- Consequences of packing and unpacking:

```py
# 1) Multiple assignments
t,u,v = 3,4,5

# This is possible because the right side values are packed to a tuple
# And the left side is unpacking those values in order to the variables

# This is equivalent to the following two statements:

temp_tuple = 3,4,5 # Packing
t,u,v = temp_tuple # Unpacking

# 2) Swapping values
m,n = n,m

# Again, this works because the RHS is being packed to a tuple
# while the left side is unpacking those values
# in order to the variables m and n respectively

# This is equivalent to:
temp_tuple = n,m # Packing
m,n = temp_tuple # Unpacking

# 3) Returning multiple objects
def some_func():
  x = 4
  y = 5
  return x,y

# This works because, the function is packing the two objects x and y
# as a tuple and returning A SINGLE TUPLE
# This apparently allows us to return multiple values
# When it is basically just returing a single object, which is a tuple
# whose values are created by packing the multiple objects in the return statement

# This is equivalent to;
def some_func():
  x = 4
  y = 5
  temp_tuple = x,y # Packing
  return temp_tuple

# So when we assign to multiple variables from the return of such a function
# like this:
m,n = some_func()
# We are basically unpacking that temporary tuple and assigning to m and n
```

- Singleton tuple: An interesting fact about defining tuple is that the common sense to initialize a tuple with onle one value does not work. That is, `a = (1)`. This will create an integer rather than a tuple, because the parenthesis are being considered as the mathematical operator rather than the delimiters for a tuple. To avoid this ambiguity, python allows adding a comma after the last element in the sequence. Thus, we can add a comma after the last element, to make `a` a tuple. Therefore, the intended effect will be from a statement like this: `a = (1,)`.

```py
a = ()
type(a) # tuple

a = (1) # <- a singleton tuple
type(a) # integer

# to make this a tuple:
a = (1,)
type(a) # tuple

a = (1,2)
type(a) # tuple

a = (1,2,3)
type(a) # tuple
```

- use cases for tuples: when we want to store a sequence that we know is constant and will not change, such as information about elements in a periodic table, month and days, zodiac signs and their corresponding dates, etc.
- however, if we have a nested sequence, such as this one: `[["A",1],["B",2],["C",3]]`, where the inner sequence has constant data that we know wont change, we should make the inner sequence a tuple, for faster and efficient operations. whereas, we should make the outer sequence a list, to be able to use the various list class methods. so something like this: `[("A",1),("B",2),("C",3)]`

- iterating over lists of tuples:

```py
t = [["A",1],["B",2],["C",3]]

for element in t:
  letter,code = element # unpacking
  # do something

# or equivalently
for letter,code in t: # directly unpack elements of t
  # do something
```

- Strings are contiguous set of characters enclosed within quotation marks. We have already seen string concatenation: `"Hello" + " " + "World"` and string repetition: `"A" * 8`.
- Similar to lists and tuples, strings can be indexed. Both forward and reverse indexing is possible. For example to access the character element at 4th index, `my_str[4]`. Also, just like lists, not only can we access individual elements, but we can also use slicing, so `my_str[1:10:2]` will select all elements at odd indexes till (but not including) index 10, and from (including) index 1.
- Some useful builtin methods support strings:

| Method | Description |
| - | - |
| `len(a)` | Returns the length of the string |
| `max(a)` | Returns the maximum character in the string. (maximum is determined based on the ASCII codes) |
| `min(a)` | Returns the minimum character in the string. (minimum is determined based on the ASCII codes) |
| `sorted(a)` | returns a new string that is the sorted version of a (sorting is done based on the ASCII code). if `reverse=False` is given as argument, then the sorting will be in descending order. |

- String class itself has a lot of builtin methods: (47 non-special methods), can be checked with `dir(str)` method. These are the most commonly used ones:

| Method | Description |
| - | - |
| `lower()` | Returns a copy of the string converted to all lowercase. |
| `upper()` | Returns a copy of the string converted to all uppercase. |
| `count(sub,start,end)` | Returns the number of non-overlapping occurences of substring `sub` in the string. The optional arguments `start` and `end` are interpreted as in slice notation.
| `replace(old,new,count)` | Returns a copy of string with all occurences of the substring `old` replaced with `new`. The optional argument `count` is the maximum number of occurences to replace. The default is `-1` which means to replace all occurences. If `count` is given, for example, `count=2`, only the first two matched occurences will be replaced. |
| `index(sub,start,end)` | Returns the index of the first occurence of the substring `sub` in the string. The optional arguments `start` and `end` are interpreted as in slice notation. |
| `capitalize()` | Returns the capitalized version of the string, where the first character is made uppercase, and the rest of the characters lowercase |
| `isalpha()` | Returns `True` if all the characters in the string are alphabetic, and there is atleast one character; otherwise it returns `False`. |

These are all other methods:

| Method | Description |
| - | - |
| `casefold()` | Returns the casefolded version of the string. Casefolded strings and lowercase strings are usually similar, but for certain Unicode codepoints, the conversions are different. Casefolded strings should be used for caseless comparisons. |
| `center(width,fillchar)` | Returns a centered string of length `width`, padded with the fill character, default is space. |
| `expandtabs()` | Replaces Tab character With Spaces |
| `encode()` | Returns encoded string of given string |
| `find()` | Returns the index of first occurrence of substring |
| `format()` | Formats string into nicer output |
| `isalnum()` | Checks Alphanumeric Character |
| `isdecimal()` | Checks Decimal Characters |
| `isdigit()` | Checks Digit Characters |
| `isidentifier()` | Checks for Valid Python Identifier |
| `islower()` | Checks if all Alphabets in a String are Lowercase |
| `isnumeric()` | Checks Numeric Characters |
| `isprintable()` | Checks Printable Character |
| `isspace()` | Checks Whitespace Characters |
| `istitle()` | Checks for Title cased String |
| `isupper()` | Returns if all characters are uppercase characters |
| `join()` | Returns a Concatenated String |
| `ljust()` | Returns left-justified string of given width |
| `rjust()` | Returns right-justified string of given width |
| `startswith()` | Returns True if the string starts with the specified value |
| `endswith()` | Returns True if the string ends with the specified value |
| `swapcase()` | Swap uppercase characters to lowercase; vice versa |
| `lstrip()` | Removes Leading/Leftmost Characters |
| `rstrip()` | Removes Trailing/Rightmost Characters |
| `strip()` | Removes Both Leading and Trailing Characters |
| `partition()` | Will return the partition of the string into three parts based on the separator provided as input. Returns a Tuple with three values; the string part before separator, the separator and the string part after separator. | |
| `rpartition()` | Similar to partition() but will search for the separator from right side. |
| `maketrans()` | Returns a translation table |
| `translate()` | Returns mapped charactered string |
| `rfind()` | Returns the Highest Index of Substring |
| `rindex()` | Returns Highest Index of Substring |
| `split()` | Splits String from Left |
| `rsplit()` | Splits String From Right |
| `splitlines()` | Splits String at Line Boundaries |
| `title()` | Returns a Title Cased String |
| `zfill()` | Returns a Copy of The String Padded With Zeros |
| `format_map()` | Formats the String Using Dictionary |

- We can loop over individual characters of a string using the `in` keyword:

```py
for character in my_string:
  pass

# Equivalent to:
for index in range(len(my_string)):
  character = my_string[index]
  pass
```

- We can also use the `in` keyword to test if a character is in the string:

```py
test_char = "a"
my_string = "alphabets"
if test_char in my_string:
  print("The word \"alphabets\" contains the letter \"a\"")
else:
  print("The word \"alphabets\" does not contain the letter \"a\"")
```

- This allows us to check if a character is a vowel:
```py
test_char = "a"
vowels = "aeiou"
if test_char in vowels:
  print("The letter \"a\" is indeed a vowel")
else:
  print("The letter \"a\" is not a vowel")
```

- We can convert a string to a list, such that each character in the string becomes an element of the list. We can do this by:

```py
my_string = "Hello, World!"
my_string_as_list = list(my_string)
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
```

- If we want to get a list of all words inside the string, we can use the `split()` method, where we specify a delimiter character. To split the string into words, we specify space as the delimiter character.

```py
my_string = "Hello, World!"
words_in_my_string = my_string.split(" ")
# ["Hello,", "World!"]
```

- The opposite is also possible, where we convert a list to a string. If we have a list containing string elements, we can merge them using the `join()` method. The `join()` method is applied on a string, which is inserted between the other strings provided as a list in argument.

```py
a = "&".join(["abc","def","ghi","jkl"])
# "abc&def&ghi&jkl"
```

- We can use the `" ".join()` method as a reverse for the `split(" ")` method.

```py
my_string = "Hello, World!"
words_in_my_string = my_string.split(" ")
# ["Hello,", "World!"]
restored_string = " ".join(words_in_my_string)
# "Hello, World!
```

- However, we can not use `join()` method on an argument list, if that list contains numeric values as well. For that, we need to convert each element to a string before processing using string comprehension.

```py
words_list = ["The",7,"is","called","seven"]
joined_string = " ".join([str(element) for element in words_list])
# The 7 is called seven
```

- Sets: Besides, lists and tuples, python also have sets, which are just like the sets in mathematics. A set is an unordered collection of elements. However, the elements of a set must be unique, so no duplicates are allowed. Moreover, individual elements of a set are immutable. But the set itself is mutable. This means that we can not change the value of an element once it is assigned, but we can add or remove elements from a set.
- Sets have builtin methods that perform the mathematical operations in set theory: such as union of two sets, intersections, checking if two sets are disjoint, etc.
- A set is defined with curly braces. If duplicate elemets are entered in the initialization, the duplicates are simply ignored, since sets only contain unique elements.

```py
my_set = {1,2,3,4,5}     # {1,2,3,4,5}
my_set = {3,5,4,5,3,1,2} # {1,2,3,4,5}
```

- Sets are implemented using hash tables to store the elements. Therefore, the order in which the elements are stored depends on the hash function used. (Remember, sets are unordered collection of unique elements). Also, sets can not be indexed. So `s[0]` will raise an error, instead of retrieving the value at index 0.
- Although sets are not indexable (indexing does not work because sets are implemented as hash tables, where elements can not be found at fixed distances). Nevertheless, sets are iterable, so we can use `for` loop to iterate over each element of a set. Also, we can use the `in` keyword to test membership on a set.

```py
my_set = {1,2,3,4,5}
my_set[0] # Error! Set object is not subscriptable

# we can iterate over all elements of a set
for element in my_set:
    pass
  
if 2 in my_set: # True
  pass

if 44 in my_set: # False
  pass
```

- A set without any element is called an empty set. However, we can not define an empty set by just adding an empty pair of curly braces, since curly braces are also used as delimiters for dictionaries. And because, dictionaries are much more commonly used than sets, the syntax `{}` creates an empty dictionary rather a set, to facilitate easy creation of dictionaries.
- Therefore, to create an empty set, we have to use the set class constructor.

```py
x = {}
type(x) # <class 'dict'>

x = set()
type(x) # <class 'set'>
```

- Remember that elements in set are immutable, but set itself is mutable. Also, we can not use indexing to access elements. So how do we modify the set? We use the class methods available for set.

| Method | Description |
| - | - |
| `add()` | Adds the given element `x` to the set |
| `clear()` | Removes all elements from the set |
| `copy()` | Returns a copy of the set (This is needed because, assigning a set to another set, creates a shallow copy pointing to the same underlying set. So `a = b`, points to the same underlying set. So changes in `b` will be reflected in `a`) |
| `difference()` | Returns the difference between two or more sets as a new set |
| `difference_update()` | Removes all elements of another set from this set |
| `discard()` | Removes an element from the set if it is a member, otherwise (if the given element is not a member of the set), it does nothing |
| `intersection()` | Returns the intersection of two sets as a new set |
| `intersection_update()` | Updates the set with the intersection of itself and another set, basically, replaces the set with its intersection with another given set |
| `isdisjoint()` | Returns True if the two sets have null intersection |
| `issubset()` | Returns True if another set contains this set |
| `issuperset()` | Returns True if this set contains another set |
| `pop()` | Removes and returns an arbitrary element. Raises KeyError if the set is empty |
| `remove()` | Removes an element from the set if the element is a member, otherwise if the element is not a member, raises KeyError |
| `symmetric_difference()` | Returns the symmetric difference between two sets as a new set |
| `symmetric_difference_update()` | Updates the set with the symmetric difference of itself and another set |
| `union()` | Returns the union of sets in a new set |
| `update()` | Updates the set with the union of itself and another set |

Besides the class methods, there can be different operators that can be used on python sets. However, note that these operators are only applied on two sets. The class methods listed above will take any iterable as an argument, convert them to a set, and then perform the operations.

| Operator | Description |
| - | - |
| `|` | Union (creates a new set) |
| `&` | Intersection (creates a new set) |
| `-` | Difference (creates a new set) |
| `^` | Symmetric difference (creates a new set containing elements from both sets except common elements) |
| `==` | Equality test |
| `<` | Subset test |
| `>` | Superset test |

- Note: Mathematically, symmetric difference is the disjunct union of the two sets. Whereas, difference is simply the elements not in other set. So symmetric difference is the union of `A - B` and `B - A`.
- Just like list comprehension, we have set comprehension. The only difference is the delimiting brackets that you use, curly braces instead of the square brackets.

```py
l = [i * i for i in range(20)] # List comprehension
s = {i * i for i in range(20)} # Set comprehension
```

- Dictionaries: Besides, lists, tuples, sets, python also have dictionaries.

| Lists | Tuples | Sets | Dictionaries |
| - | - | - | - |
| Elements are accessed by indexing | Elements are accessed by indexing | Elements can not be accessed | Elements are accessed through keys |
| Mutable | Immutable | Element immutable, itself mutable | Mutable |
| Ordered sequence | Ordered sequence | Unordered sequence | Unordered sequence |
| Duplicates allowed | Duplicates allowed | Duplicates not allowed | Duplicate keys not allowed |

- Dictionaries have elements that are key-value pairs. The values can be any data type, but the keys must be of an immutable data type, such as strings, numbers, or tuples; but generally, the keys are strings. You can mix different types of keys in a dictionary, and different types of values, too.

```py
my_dict_1 = {} # Empty dictionary
my_dict_2 = {"a":0,"b",1} # "a" is a key with value 0, and "b" is a key with value 1
my_dict_3 = {0:False, "true":True} # Notice how keys are of different types
my_dict_4 = {2:"two","a":4,(4,5,6):False} # Notice how keys and values are of different types
```

- Individual elements are accessed through their keys. If you write `my_dict[my_key]` and `my_key` is defined in the dictionary, you will get the value of that key, and you can modify or change the value as well. But if `my_key` is not defined in the dictionary, you will get the KeyError. But errors are problematic, so it is always better to use the `get()` method of the dictionary class. If the key is not defined, `get()` will simply return `None`, instead of raising an error. This allows to freely access values for an arbitrary key, without worrying about errors. We can also return some custom message instead of `None` by passing that message as the second argument to the `get()` method.

```py
# The numbers in the brackets [] are not indexes, rather they are keys
my_dict_1[0] # Error: KeyError
my_dict_1.get(0) # None
my_dict_1.get(0, "Key not found :/") # Key not found :/
my_dict_2["a"] # 0
my_dict_2.get("a") # 0
my_dict_3["true"] # True
my_dict_3.get("true") # True
my_dict_4[(4,5,6)] # False
my_dict_4.get((4,5,6)) # False
```

- This allows us to store related pairs of data. So, if we want to store the data about each student within a class, we can create a dictionary with keys that are rollnos of students, and the values of these keys are lists or tuples of different characteristics of students, like their name, gender, age, height, scores, grade, etc.

```py
students_record = {
  "2019-MC-01": ["Ali Irfan", "Male", 21, "A+"],
  "2019-MC-02": ["Hamza Khan", "Male", 19, "C-"],
  "2019-MC-03": ["Fawad Aslam", "Male", 20, "F"],
  "2019-MC-04": ["Maryam Nawaz", "Femal", 24, "D"],
}
```

- Now, we can very easily access the record of a student just by knowing their roll nos. If we had instead created a list of lists, the access would have been very unintuitive.
- Once a dictionary is defined, we can add more key-value pairs (dictionaries are mutable).

```py
student1={'fName':'Ahmad','lName':'Hassan','courses':['CP','ED','EM']}
student1['email']='ahmad.hassan@gmail.com'
print(student1.get('email','Key not found')) # ahmad.hassan@gmail.com
```

- The above method can also be used to modify the value of a particular key.

```py
student1={'fName':'Ahmad','lName':'Hassan','courses':['CP','ED','EM']}
student1['courses']=['ED','EM']
print(student1.get('courses','Key not found')) # ['ED','EM']
```

- To add or modify one or more key value pairs in a dictionary, we can use the `update()` method, instead of writing separate lines of code for each key value pair. If an existing key is passed to the `update()` function, its value will be updates, otherwise if the key is not defined, it will be added.

```py
student1={'fName':'Ahmad','lName':'Hassan','courses':['CP','ED','EM']}
student1.update({
  'courses':['ED','EM'],             # Updating an existing key-value pair
  'fName':'Muhammad Ahmad',          # Updating an existing key-value pair
  'email':'ahmad.hassan@gmail.com'}) # Adding a new key-value pair
print(student1)
# {
# 'fName': 'Muhammad Ahmad',
# 'lName': 'Hassan',
# 'courses': ['ED', 'EM'],
# 'email': 'ahmad.hassan@gmail.com'
# }
```

- Dictionary class methods:

| Method | Description |
| - | - |
| `copy()` | Returns a copy of the dictionary. (This is necessary, because assignment only creates shallow copies pointing to the same dictionary object underneath) |
| `clear()` | Removes all key-value pairs from the dictionary (makes the dictionary empty) |
| `pop(k)` | Removes the key-value pair with the key `k`, and returns the value from the dictionary |
| `popitem()` | Removes an arbitrary key-value pair from the dictionary, and returns it as tuple. Before Python 3.7, arbitrary meant a random pair, but after Python 3.7, it means the last pair |
| `get(k,msg)` | Returns the value for the key `k`, if `k` is defined, otherwise returns `None` (if `msg` is not provided), or the custom message (if `msg` is provided) |
| `values()` | Returns a list of all the values in the dictionary |
| `setdefault(k,v)` | Returns the value of the key `k` (if `key` is defined). If not, it defines the key `k` with the value `v` to the dictionary |
| `keys()` | Returns a list of all the keys in the dictionary |
| `items()` | Returns a list of dictionary (key-value) pairs as tuples. So basically, it returns a list of tuples, where each tuple is a key-value pair |

- Iterating over a dictionary: The convenient `for-in` loop works for dictionaries too, but it iterates over the keys of the dictionary only. If we want to iterate over the values of the dictionary, we need to use the `values()` method. If we want to access the key-value pairs, we need to use the `items()` method.

```py
my_dict = ["a":1,"b":2,"c":3,"d":4]

for x in my_dict:
  pass # x will be the keys: "a","b","c","d"

for value in my_dict.values():
  pass # value will be the values: 1,2,3,4

for x in my_dict.items():
  pass # x will be the tuples: ("a":1),("b":2),("c":3),("d":4)

for key,value in my_dict.items():
  pass # key,value will be the unpacked tuple variables: "a":1,"b":2,"c":3,"d":4
```

- Just like empty lists,tuples, and sets, we can define empty dictionaries:

```py
empty_list = []
empty_tuple = ()
empty_set = set()
empty_dict = {}
```

- We can convert a dictionary to a list using the `list()` method on the `items()` method of the dictionary, which will create a list of tuples, since `items()` returns key-value pairs as tuples. This is useful when we want to sort a dictionary based on its keys. Dictionaries themselves can not be easily sorted, but lists can be.

```py
my_dict = {'a': 1,'s': 3,'i': 1,'m': 1,'p': 1,'l': 1,'e': 7,'n': 2,'t': 5}
my_list = list(my_dict.items())
my_list.sort()
```

- If we want to sort the dictionary based on the `value` rather than the `key`, we can reverse the positions of keys and values. The following example, sorts the dictionary, such that the pairs with the highest value appear first.

```py
my_list = list(my_dict.items())
reversed_pairs = [(y,x) for (x,y) in my_list]
# If you want lists of lists rather lists of tuples
# reversed_pairs = [[y,x] for (x,y) in my_list] 
items.sort(reverse=True)
```

- To create a 2D dictionary, a dictionary which contains dictionaries: we can create a dictionary with some keys, and the values are themselves dictionaries. In such a 2D dictionary, we can access the individual record like: `allStudents["2018-MC-01"]`, and to access a sub-record of a record in the dictionary: `allStudents["2018-MC-01"]["Name"]`.

```py
allStudents={
 '2018-MC-01': {'Name':'Muhammad Usman','Sec':'A','Courses':['CP','ED','EM']},
 '2018-MC-02': {'Name':'Tahir Mehmood','Sec':'A','Courses':['CP','DLD','EM']},
 '2018-MC-03': {'Name':'Muhammad Bilal','Sec':'A','Courses':['VCA','ED','EM']}
}
```

- Like list comprehensions, and set comprehensions, we have dictionary comprehensions:

```py
my_list = [i for i in range(15)]     # elements are 0:14
my_set = {i for i in range(15)}      # elements are 0:14
my_dict = {i:i*i for i in range(15)} # keys are 0:14 and values are key's square
```

- Often we need to create a dictionary from two iterables: one iterable will be the keys for the dict, and the other iterable will contain the corresponding values. To do that, we can use the `zip()` function and then we can use dictionary comprehension on that. An even simpler solution is to use the `dict()` constructor on the zip object.

```py
# Keys
gLetters=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
# Values
gPoints=[4,4,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0.0]

# Using the dict() constructor on the zip object
gDict = dict(zip(gLetters,gPoints))

# Alternatively, using dictionary comprehension on the zip object
gDict = {k:v for k,v in zip(gLetters,gPoints)}
```

- There are three types of errors in a program:
  - Syntax error: This type of error occurs because of wrong syntax. Syntax error are the easiest to detect and fix, since the interpreter would not even run the program unless the syntax errors are fixed. The interpreter will execute the Traceback function and will also indicate the error name with the line number where the error occured, with a little description.
  - Logical error: This type of error is the hardest to detect. Since it is not an actual error, rather an error in the program logic.
  - Run-time error: This type of error occurs when the program executes a syntactically correct piece of code, but there is some error in it. Such as dividing by zero; this is syntactically correct, logically correct, but will produce an error in runtime.
- Syntax errors are called Errors, whereas, logical/runtime errors are called exceptions. However, both the terms are often used interchangably. Exceptions must be handled carefully.

```py
# This will generate a runtime error when b = 0
a,b = eval(input("Enter two numbers: "))
print(f"Ratio of the two numbers: {a/b}")

# Here we handle the exception when b = 0
a,b = eval(input("Enter two numbers: "))
if(b != 0):
    print(f"Ratio of the two numbers: {a/b}")
else:
    print("Divisor can not be zero")
```

- The above approach to handling exception is called Look Before You Leap (LBYL). We are applying the checks before executing a statement that might raise an exception.
- Second approach to handling exception is called its Easy to Ask Forgiveness than Permission (EAFTP). In this approach, we try to execute one statement, and if it executes successfully, we are good to go, but if there is any exception then instead of generating that exception, we catch that. This is done with `try except` block. In `try` block we write the statements (usually just one or two that we think might raise an exception), and then there is an `except` block. If the statements in the `try` block do not raise an exception, the interpreter skips past the `except` block, but if there is an exception when executing the `try` block, instead of raising an exception, the interpreter will leave the try clause and enter into the `except` clause. We call this catching an exception. The error inside the try clause can be any type of error.

```py
try:
    a,b = eval(input("Enter two numbers: "))
    print(f"Ratio of the two numbers: {a/b}")
except:
    print("Enter only numbers and the second number must be non-zero)
```

- We can also target different errors by their error names. Every error has its associated exception name. For example, if we try to divide by zero, the exception name is `ZeroDivisionError`. If some non-numeric number is entered into `eval()`, the error name is `NameError`.

```py
try:
    a,b = eval(input("Enter two numbers: "))
    print(f"Ratio of the two numbers: {a/b}")
except ZeroDivisonError:
    print("Second number can not be zero")
except NameError:
    print("Enter numeric values only")
except:
    print("Something bad happened -_-!")
```

- If there is some error other than the two specific ones, the last anonymous except clause targets it. Note that the order of the exception clauses is important; the first block that can catch the exception will be executed, and others will be skipped. So if the anonymous block is the first block, it will be executed every time there is any error, and the specific named blocks would be skipped over.
- We can also access the default exception message (the one that is displayed by the Traceback function) by using the `as` keyword.

```py
a,b = 5,0
try:
    c = a / b
except ZeroDivisionError as e:
    print("Second number can not be zero")
    print(e)
```

- Out of the two approaches, if else (LBYK) and try except (EAFP), it can be seen that EAFP is not a replacement for an if else block. Only when an if statement is used to handle an error, then we can have a try except block to catch the error.
- However, to catch an error, the EAFP block is better, since it is succint. If we were to write all the checks in the if else for a possible exception condition, that would be too long. But if we just write the error name in a try except block, the whole check is just one line. Moreover, even if the values are such that the exception would not be raised, the checks in the if else block will still be executed. Whereas, in the try except block, only when the values are troublesome that the error handling block will be executed. Also, the if else conditions are much less intuitive as to why they exist, and what they do, whereas, the error name in the try except shows very clearly what is being handled.

```py
# The chechs are long
# The code does not look Pythonic
# The checks are executed every time, wasting precious time
# It is hard to understand what the checks are trying to catch
if (b != 0 and c != 0 and d != 0):
    exp = a / b + b / c + c / d
else:
    print("Division by zero is not allowed")

# There is not check, only an error name
# The code looks more Pythonic
# There are no checks, the except block is executed only when there is an error
# It is very easy to see what error is being handled
try:
    exp = a / b + b / c + c / d
except ZeroDivisionError as e:
    print(e)
```

- Although in many cases, we only use the `try` and `except` blocks, but there can be `else` and `finally` blocks as well. The `else` block is executed when the exception is not raised. And the `finally` block is executed regardless of whether an exception was raised or not.
- So, if the statements inside the `try` block raise an exception, the `except` block will be executed, and if they do not raise an exception, the `else` block will be executed. And in both cases, the `finally` block will be executed afterwards.
- This helps in intuitivity. Only the statements that might raise an error are included in the `try` block, whereas, the rest of the code once those risky statements are successfully run, is included in the `else` block. So we can clearly see what statements are being handled for exceptions.

```py
# Here we do not know which of the three statements are being tested for exceptions
try:
    f = open("test.txt")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("No such file exists")

# Here we can clearly see which statement is considered risky 
# and being tested for exceptions
# We can also clearly see what and how the exception is being handled
try:
    f = open("test.txt")
except FileNotFoundError:
    print("No such file exists")
else:
    print(f.read())
    f.close()

# Improved version of the try-except-else statements
# We added an anonymou catch for exceptions other than FileNotFoundError
try:
    f = open("test.txt")
except FileNotFoundError:
    print("No such file exists")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
```

- The `finally` block is executed regardless of whether the exception occured or not. This block should contain code that needs to be executed regardless of the error status.
- It might seem unknown as to why `finally` block exists, when we can just write the statements after the whole try-except-else block. Those statements will also be executed in either case.
- But, there is one problem: If there is an exception in the `else` block, what will happen? In our above code, for example, lets say that the `f.read()` was unsuccessful because the file contains unrecognized line endings. What will happen? The program will raise an exception and halt the program right after executing the `f.read()` statement. The statement that closes the file `f.close()` will NOT be executed. So the computer resources are not freed before the program crashed, and those will remain unclaimed until the system is rebooted. Clearly not an optimal scenario.
- However, if we have the `finally` block, THE STATEMENTS INSIDE OF IT WILL BE EXECUTED BEFORE THE EXCEPTION IS RAISED IN THE `else` block. So the file will be closed first, before the program crashes and raises an exception.
- So we include in the `finally` block those statements that need to be executed in the worst case scenario, where there is an error inside the `else` block. So we put, things like closing files and databases in the `finally` block to make sure that they still are closed even in the worst case scenarios. The finally block guarantees that they will be executed before the program crashes.
- Another important use of the `finally` block is inside the user-defined functions.

```py
def my_func():
    try:
        # some risky statements
    except:
        return None
    else:
        # do something
        # return something
    finally:
        # do some clean up
```

- Here, if the statemetns inside the `try` block raise an exception, the function will return None. We know that when the return statemetn is excuted, the program will return to the calling point. But, what if we wanted to do some cleaning up before the return. Lucky for you, the finally block can help. The statements inside the finally block will be executed BEFORE THE FUNCTION RETURNS FROM THE except block.
- So this is what the structure of EAFP method of exception handling looks like:

```py
try:
    # Statement(s) that might raise an exception
except ErrorName1 as e:
    # Handle the error: ErrorName1
except ErrorName2 as e:
    # Handle the error: ErrorName2
except Exception as e:
    # Handle errors that are not handled by the previous specific except clauses
else:
    # Statements that need to be executed
    # only if the try clause statments did not raise any exception
finally:
    # Clean up code, such as closing files, freeing resources
    # that must be executed in the worst-case scenario
    # where the program crashes due to an exception in the else block
    # Remember: the finally block is executed BEFORE
    # the exception is raised from the else block statements
    # and BEFORE the program crashes
    # so we are guaranteed that these statements WILL be executed
```

- We can also raise our own exceptions. This is very useful when writing classes.

```py
# Without custom message
if x == fatal_condition:
    raise Exception

# With custom message
if x == fatal_condition:
    raise Exception(f"The value {x} is not allowed")
```

- If the condition is met, the exception will be raised, and the program will terminate.
- We can also raise some specific exceptions:

```py
# Raising a KeyError without a custom message
if x == fatal_condition:
    raise KeyError

# Raising a TypeError without a custom message
if x == fatal_condition:
    raise TypeError

# Raising a TypeError with a custom message
if x == fatal_condition:
    raise TypeError(f"The value {x} is not allowed")
```

- Lets consider the following user-defined function:

```py
def my_func(x,y):
    return x*y
```

- Here, we take two arguments, `x` and `y`. We usually call this function with only the values for these arguments, such as `my_func(1,2)` means `x` will be `1` and `y` will be `2`.
- But we can also specify the arguments through their names, such as `my_func(x=1,y=2)` means `x` will be `1` and `y` will be `2`.
- The advantage of specifying the arguments through their names is that the order of the parameters do not matter. So `my_func(y=2,x=1)` and `my_func(x=1,y=2)` both mean the same thing. Also we can be sure, that if a new function parameter is inserted between the existing paramters in the function prototype, the arguments will still be correctly initialized, since we are not depending on their position, rather their names.
- When we specify the arguments through their name, they are called Keyword Arguments, whereas, when we specify arguments without the names, then they are passed based on their position, and are hence called Positional Arguments.
- Remeber that we can use keyword and positional arguments at the same time, so `my_func(1,y=2)` means that `x=1` and `y=2`. Just remember that even when keyword arguments are used, the positional arguments MUST BE IN THEIR CORRECT POSITION, although the keyword arguments can be in any position. So `my_func(1,x=2)` will raise an error, since the positional argument `1` already provided the value for `x`, and `x=2` provides another value, while there is no value for the `y` parameter. Also remember that all positional arguments must come before the keyword arguments. So `my_func(x=2,1)` is invalid.
- A function can also have optional parameters. These are parameters with a default value. So if a value for them is specified, then that is value is used. Otheriwse, if no value is provided for them, then the default value is simply used.

```py
def my_func(required_paramter,optional_parameter=10):
    return required_parameter * optional_parameter

my_func(8)   # return 8 * 10
my_func(8,9) # return 8 * 9
```

- We can also make the certain input arguments to be positional arguments only, and certain input arguments to be keyword arguments only. The general rule to remember is that, THE POSITIONAL ARGUMENTS MUST COME BEFORE THE KEYWORD arguments.
- If we put a `/` slash as an argument, all arguments to the left of it are positional arguments only. If we put a `*` asterisk as an argument, all arguments to the right of it are keyword arguments only.

```py
# All arguments can be provided as either positional or keyword arguments
# The only requirement is that the positional arguments must come before the keyword argument
def my_func(height,width,ratio,volume,area,perimeter)

# The arguments to the left of the slash are positional-only arguments.
# this means that we must provide positional arguments for height and width
def my_func(height,width,/,ratio,volume,area,perimeter)

# The arguments to the right of asterisk must be keyword-only arguments
# this means that we must provide keyword arguments for ratio,volume,area, and perimiter
def my_func(height,width,*,ratio,volume,area,perimeter)

# height and width must be positional-only arguments
# ratio and volume can be either positional or keyword arguments
# as long as the positional first requirement is fulfilled
# area and perimter must be keyword-only arguments
def my_func(height,width,/,ratio,volume,*,area,perimeter)
```

- We can unpack a list and pass it as arguments to a function using the starred notation.

```py
# A function that takes three arguments
def my_func(arg1,arg2,arg3):
    return

# Lets say that this list contains the arguments in order
args = [1,2,3]

# We can pass these arguments as
my_func(args[1],args[2],args[3])

# But a better way is to use the starred notation
my_func(*args)
```

- But the unpacking produces only as many arguments as there are elements in the list, common sense, right. So, if the list had only two arguments, we would get a TypeError.
- In such a case, where the list does not contain all the arguments, we can pass the other arguments as normal.

```py
def my_func(arg1,arg2,arg3):
    return

args = [1,2]

# Notice how we can pass the third argument as normal
my_func(*args,3) # arg1 = 1, arg2 = 2, arg3 = 3

# We can also use the unpacking in any other position of consecutive arguments
my_func(3,*args) # arg1 = 3, arg2 = 1, arg3 = 2 
```

- We can also use the starred notation in the function prototype.

```py
def my_func(*args):
    for arg in args:
        print(arg)
    return

my_func(1)
my_func(1,2)
my_func(1,2,3)
my_func(1,2,3,4)
```

- The `*args` will pack the passed arguments into a tuple, and inside the function, the `args` variable is a tuple, and it can be used like one.
- Remember, that in the function prototype, the starred notation PACKS the arguments into a tuple, and in the function call, the starred notation UNPACKS the list into individual arguments. So, we can use the starred notation inside the function call to pass a list.

```py
def my_func(*args):
    return

l = [1,2,3,4]

# This does not do what is intended
# The list l is treated as a single element
# So inside the function, args will be ([1,2,3,4])
# instead of (1,2,3,4)
my_func(l)

# l will be unpacked into individual elements
# which will then be packed into a tuple in the function
# This does exactly what is intended
# args will be (1,2,3,4)
my_func(*l) # Success
```

- We can have single valued functions alongside one variable-length argument. But we can have only one variable-length argument. We can not have more than one variable length arguments as the interpreter can not decide how many elements should be assigned to each variable-length argument.

```py
def my_func(a,b,*x):
    ans = 0
    for i in x:
        ans += x * x
    ans = ans / a + b
    return ans

my_func(10,2,1,2,3,4) # a = 10, b = 2, x = (1,2,3,4)
```

- Similar to this, we can also have variable length keyword arguments.

```py
def my_func(**kwarg):
    for k,v in kwarg.items():
        print(f"{k} : {v}")
    return

my_func(A=1,B=2,C=3)
```

- We can observe that the keyword arguments (kwargs) are passed as a dictionary, with the keywords appearing as keys.
- So `def my_func(*args)` packs positional arguments into a tuple, whereas, `def my_func(**kwargs)` packs the keyword arguments into a dictionary. Also, similar to unpacking the list into individual positional arguments in function calls with the single starred notation, we can unpack a dictionary into keyword argumetns in functioon calls with the double starred notation. See the example code below:

```py
def my_func1(*args):
    return

def my_func2(**kwargs):
    return

my_list = [1,2,3,4]
my_dict = {"A":1,"B":2,"C":3,"D":4}

my_func1(1,2,3,4)
my_func1(*my_list)

my_func2(A=1,B=2,C=3,D=4)
my_func2(**my_dict)
```

- A function can have single valued, arbitrary length positional, and arbitrary length keyword arguments. But remember that the positioinal arguments must come before the keyword arguments. Also remember, that there can be only one arbitrary length positional argument, and only one arbitrary length keyword argument. So the general form is:

```py
# arg1,arg2,...,argn are single valued arguments
# args is a tuple which packs arbitrary number of positional arguments
# kwargs is a dictionary which packs arbitrary number of keyword arguments
def my_func(arg1,arg2,argn,*args,**kwargs)

my_func("Hello",4.5342,False,    # arg1,arg2,argn
        "A",1,False,2.4,         # args
        A=1.7,B="HELLO",C=False) # kwargs
```

- Arguments can be passed by value or passed by reference. Passing by value means that only their value is passed and not the variable itself. This means that the value is used to create a new variable for the function, and the function uses that variable, and not the original variable. so changes to this variable in the function are not reflected to the original variable. Whereas, passing by reference means that the variable itself is passed. This is done by passing a reference which points to the same underlying object. So the original variable and this passed reference, both point to the same underlying obejct. Therefore, changes to the variable in the function are reflected in the original variable.
- Immutable data types like int, float, string, boolean etc, are always passed by value. Whereas, the mutable data types like list, tuples, dictionaries, etc are passed by reference by default.
- Passing mutable data types by reference allows them to be modified by a user-defined function. So for eaxmple, functions like `removeLastEntry()` can work as intended, without copying the whole data container multiple times.
- This passing by reference and passing by value can be verified by using the `id()` function. The `id(x)` function gives the memory address of the object `x`. So, if a variable is passed by value, the `id()` function will return different memory addresses for the original variable and variable inside the fnction. Whereas, if the variable is passed by reference, the originakl variable and the argument variable will have the same memory address.
- However, there is one thing to note. If we use assignment on a passed variable (which is passed by reference), a new variable copy will be created with A DIFFERENT MEMORY ADDRESS. So a totally new variable will be created (just like when passing by value). However, this new variable is not created initially, but only after the assignment takes place. This is clear in the example below:

```py
def my_func1(arg):
    print(id(arg))

# x is a list which is a mutable data type
# so x is passed by reference by default
# so id(x) and id(arg) will both give the same memory address
# since they both point to the same underlying object
# only with different reference names (identifiers)
x = [1,2,3]
print(id(x))
my_func1(x)

# Lets look at this function
def my_func2(arg):
    # so far, the arg is not assigned, and because x was passed by reference
    # id(arg) is the same as id(x)
    print(id(arg))
    # now, we used assignment on a passed variable
    # this created a new object with the same name as arg
    arg = [4,5,6]
    # now id(arg) will be different than id(x)
    print(id(arg))

x = [1,2,3]
print(id(x))
my_func2(x)
```

- Calling the function itself from within the function is called recursion, and the function that calls itself is known as a recursive function.

```py
def recursive_function(x):
  print(x)
  recursive_function(x + 1)

recursive_function(1)
```

- You can see that the recursive function will call itself for some time, before the program terminates due to the recursive depth limit. This is because, the above function does not a stopping condition for the recursion, and so the recursion is infinite. Such an infinite recursion will very quickly exhaust the computer memory, due to the function calls taking a lot of space in the stack. To prevent this, python implements a limit on how many times a single self-recursion can happen. This limit can be checked like this:

```py
import sys
# Using this function from sys, you can view the maximum recursion depth
print(sys.getrecursionlimit())

# Using this function from sys, you can change the maximum recursion depth
sys.setrecursionlimit(1500)
```

- To make recursion useful, we need to add a base case, a condition that will end the recursion after certain amount of self-calling the function.

```py
# This function will recurse 100 times if x = 0 initially
# If f is called with arguments other than x=0,
# the function will recurse until x is 99
# so f(5) will recurse 94 times
# f(99) will recurse 1 times
# f(100) will resurse 0 times
def f(x):
  print(x)
  if x < 100:
    f(x + 1)

f(0)
```

- Memorization is an optimization technique where the results of function calls are stored. This allows to use the cached result instead of wasting time calling the function again, if the same input occurs again.

```py
def fibo_recursive(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  if(n > 1):
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
```

- In the above function, you will notice that the function takes exponentially more time to compute larger values of n. This is because the function has an time complexity O(n^2).
- This can be improved by noticing that once a value is found, it does not need to be calculated again. So we can just store the previously calculated results, and use these results to calculate the next value. We only calculate by recursively calling for a single depth, when a new value is required.

```py
fibo_dict = {} # key = n, value = F(n)
def fibo_cache(n):
  if n in fibo_dict:
    return fibo_dict[n]
  else:
    if n == 0:
      ans = 1
    if n == 1:
      ans = 1
    if(n > 1):
      ans = fibo_cache(n - 1) + fibo_cache(n - 2)
    fibo_dict[n] = ans
    return ans
```

- Instead of creating a dictionary and storing the function calls manually, the `lru_cache()` function decorator can be used. LRU means Least Recently Used. This is available in `functools` module. Decorators are used to add extra features to any function. The `lru_cache()` function decorator does the job of memorization all by itself. It stores the function calls result, and uses it when the same call is made. It takes some argumetns, such as `maxsize=128` which sets the size of memorization container. It also has `typed=False`, which treats different types separately. If `typed=True`, `f(3)` and `f(3.0)` are considered as separate calls, and so the results would be recalculted.

```py
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
```

- Without memorization, the recursive fibonacci function has time compelxity O(2^n) which is very very bad. But with memorization, the time complexity becomes just O(n), which is really really good.
- You can accurately measure the improvement in time by using the `timeit()` function from the `timeit` module. But you need to add `globals=globals()` because the `timeit()` executes code in its namespace and not the global namespace, so it does not know about the function `fibonacci()`. Therefore, we need to pass the argument `globals=globals()` to tell it to use the `globals()` namespace.

```py
import timeit

timeit.timeit(fibonacci(10),globals=globals(),number=10)
```

- One thing to note is taht the memorization function decorator `lru_cache()` or any other memorization technique is not just limited to recursive functions. If a non-recursive function is called repeatedly with the same values, it can also be improved by adding memorization.
- Anonymous functions or lamdba expressions are functions with no names. They are used to implement very simple, usually single expression functions, which are not meant to be used often.

```py
# Named function
def unitDigit(x):
  return x % 10

# Lambda expression
lambda x:x % 10
```

- The `lambda` is a keyword, not the function's name.
- To call the lambda function, we enclose the lambda expression in parenthesis, and add the argument in another pair of parenthesis right next to it.

```py
# Calling a lambda expression
(lambda x:x % 10)(19)

# Lets see what happens when we do not add the parethesis around lambda
lambda x:x % 10(19)
# This makes the argument value 19 become a part of the expression
# The above is equivalent to:
lambda x:x % 10 *19

# So we need to add the a pair of parenthesis around the lambda expression as well
(lambda x:x % 10)(19)

# To store the return value in some variable
a = (lambda x:x % 10)(19) # a = 9
```

- One thing to note is taht we can assign the lambda expression to a variable

```py
# a variable assigned a lambda expression
my_lambda = lambda x:x % 10

# the variable is of type function since lambda expression is a function
print(type(my_lambda)) # <class 'function'>

# we can use this variable name like any other function name
my_lambda(19) # evaluates to 9
```

- In the above example, it function looks like as if it is no more anonymous, since we now have a name for it `my_lambda`. No. The lambda expression is still anonymous, but it is assigned to an identifier `my_lambda`. And we are using this identifier as a vehicle to access the underlying lambda expression.

```py
my_lambda = lambda x:x % 10

# This expression:
my_lambda(19)
# Simplifies to this:
(lambda x:x % 10)(19)
```

- Lambda expressions can also take no argument or more than one input argument:

```py
# Lambda expression with no input argument
x = lambda : print("Hello")
x() # Hello

# Lambda expression with two input arguments
x = lambda a,b: (a + b) / 2
x(10,15) # 12.5
```

- Use cases for lambda expressions:
  - When a function is very simple. It contains only a single expression. Such a function can be converted to a lambda expression to save lines of code.
  - When we need to pass a function as input argument of another function.
  - The best use for lambda expressions is using it with some other built-in function like `map`, `sort`, `reduce`, `filter` etc.

```py
# This function returns a lambda, not a value
# but to use that lambda
# we need to pass the argument base to the function first
def pow(base):
  return lambda n: base ** n

twoPow = pow(2) # lamdbda n:2 ** n
threePow = pow(3) # lambda n:3 ** n

# Now we can use the twoPow() lambda function
twoPow(3) # 8

# This whole sequence can be summarized as:
pow(2)(3)
# This evaluates to:
# (lambda x:2**x)(3)
```

- However, the most common use of lambda functions is with the builtin functions `map`, `sort`, etc.
- We can sort a list through either the list class `sort()` method or the builtin `sorted()` method.

```py
# The original list will be modified
l = [6,4,7,2,4,1,2]
l.sort()

# The original list will not be modified
# instead, the sorted list is returned and can be assigned to another variable
l = [6,4,7,2,4,1,2]
l = sorted(l)
```

- The tuples and sets can be sorted using the `sorted()` builtin method. They do not have class methods to sort, so we have to use the `sorted()` builtin mehtod. The thing to note is that the sorted() method will return a list for both of these cases, instead of tuple or set respecitvely. So if we are interested in getting a tuple or set, we need to cast them.

```py
t = (6,4,7,2,4,1,2)
t = tuple(sorted(t))

s = {6,4,7,2,4,1,2}
s = set(sorted(s))
```

- Dictionaries can also be sorted using the `sorted()` builtin method. They also do not have a class method for sorting. There sorting can be done in a variety of ways:

```py
products={'walnuts':1500,'cashew':1800,'almond':2000,'pine nuts':8000}

# Both of these will sort the keys
# Only the keys will be sorted, and a list will be returned
# No values are present
s = sorted(products)
s = sorted(products.keys())
# ['almond', 'cashew', 'pine nuts', 'walnuts']

# This will sort the values and values only
# There will be no keys in the sorted list
s = sorted(products.values())
# [1500, 1800, 2000, 8000]

# This will sort both the keys and values
# But the sorting will be based on the keys
s = sorted(products.items())
```

- To sort a list of lists, or a list of tuples, or a list of sets, we can also use the sorted method.

```py
l = [[10,4,3],[2,4,1,8],[3,2,1]]

# Both of these will sort the nested list l
# but depending on the first elements only
# So the sorting is done based on l[0][0], l[1][0], l[2][0] etc
l.sort()
l = sorted(l)
```

- However, if we use the `sorted()` or `list.sort()` method on a list of dicitonaries, we will get an error, saying that the relational operator is not supported between dictionaries. This is because Python does not know how to compare the two dictionaries.
- To sort a list of dictionaries, we have to use the optional keyword argument `key` in the `sorted()` method. The `key` argument takes a function. It then uses that function on each element, and the return value is used to compare, and hence sort.

```py
# In the following example, we are using the len() method as key argument
# The len function is applied on each string element
# The resulint number is compared
# And the list is sorted based on those numbers representing lengths

# This will sort the list "a" based on the lengths of the element strings
a = ['Computer','Programming','Python','Pakistan','UET','Mechatronics']
a = sorted(a,key=len)
# This will also sort the list "a" based on the lengths of the element strings
# But in reverse order, i.e., lengthier strings first.
a = sorted(a,key=len,reverse=True)

# Here the nums list is sorted based on their absolute magnitude
nums = [5,-3,8,-2,0,7]
nums = sorted(nums,key=abs)
# The list class method sort() also has an optional keyword argument key
nums.sort(key=abs)

# Lets define a custom function to get the unit digit
def uDigit(x):
  return x % 10

a = [2314,432,675,9983]

# Both of these do the same thing
a = sorted(a,key=uDigit)
a.sort(key=uDigit)

# However, we should note that a lambda expression will be more appropriate here
a = sorted(a,key=lambda x:x%10)
a.sort(key=lambda x:x%10)
```

- Now that we know how the `key` argument works, we can sort a list of dictionaries.

```py
student1 = {
  'Reg':'2018-MC-01',
  'Name':'Muhammad Usman',
  'Sec':'A',
  'Courses':['CP','ED','EM']
}
student2 = {
  'Reg':'2018-MC-02',
  'Name':'Tahir Mehmood',
  'Sec':'A',
  'Courses':['CP','DLD','EM']
}
student3 = {
  'Reg':'2018-MC-03',
  'Name':'Muhammad Bilal',
  'Sec':'A',
  'Courses':['VCA','ED','EM']
}

# A list of dictionaries
allStudents = [student1,student2,student3]

# This will sort based on the values of the Name key-value pairs in the students
s = sorted(allStudents,key=lambda x:x["Name"])
```

- We can also do multilevel sorting using `key`. The idea is to sort based on the first criteria, if the first criteria is equal, sort based on the second criteria, and so on. This is possible, because the `key` argument function can return a sequence of values. If the first value in this sequence is same, the sorting is done based on the second value, and so on.

```py
a = [[1,2,3],[5,2,8,7],[1,3,1,7],[5,3,2],[8,2,1,5,1],[5,2,1]]

# Sort based on first element of each sublist
a = sorted(a,key=lambda x:x[0])

# If the first element in equal
# Sort based on second element of each sublist
a = sorted(a,key=lambda x:(x[0],x[1]))

# if both the first and second element are equal
# sort based on the lenght of the sublist
a = sorted(a,key=lambda x:(x[0],x[1],len(x)))

# The negative sign will make the longer list sorted earlier
a = sorted(a,key=lambda x:(x[0],x[1],-len(x)))
```

- The `zip()` function zips together two or more iterables, so that they can be iterated together in a single loop. It takes at least one iterable, but we can provide as many iterables as required. It returns a zip object.

```py
zip(*iterables,strict=False)
```

- The `help(zip)` says: The zip object yields n-length tuples, where `n` is the number of iterables passed as positional arguments to zip(). The i-th element in every tuple comes from the i-th iterable argument to zip(). The continues until the shortest argument is exhausted. If `strict=True`, and one of the arguments is exhausted before the others, raises a `ValueError`.
- One thing to remember is that the zip object is an iterator, not an iterable. So the zip object can be used only once. Once used, the zip object will become empty, i.e., it is exhausted. We will see the difference between iterator and iterable later on.

```py
subjects = ["FOTS","CP","LA"]
credit_hours = [3,2,4]
z = zip(subjects,credits_hours)
print(z) # <zip object at 0x7f0fc4c486c0>

# We can convert the zip object to other data types, for example a list
l = list(z)
print(l) # [("FOTS",3),("CP",2),("LA",4)]

# We can iterate over a zip object once before exhausting it
# This loop will print the tuples of each subject-credit hours pairs
for i in z:
  print(i) # ("Subject",credit_hour)
```

- The `zip()` function is used when we want to process multiple iterables together. Without `zip()` we would have to process these iterables in a complex loop through a common index. The zip function makes this easy since it picks the corresponding elements from each iterable and creates a tuple of those elements, and then we can iterate over these tuples.
- As said in the help message, if iterables are of unequal length, the zip function processes till the shortest iterable is exhausted, at which point, it either simply finsihes, or raises a ValueError, depedning on whether `strict=False` or `strict=True`.
- However, it is possible to continue till the largest iterable is exhausted. This is possible because we can supply a fill value to be used for the missing elements when the shorter iterables are exhausted. To do this, we can use the `zip_longest()` function from the `itertools` module. The fill value is passed through the `fillvalue` argument. If we do not supply the `fillvalue` argument, `None` is used by default.

```py
from itertools import zip_longest

subj = ['Mech','CP2','ES','MoM']
ch   = (3,2,4)
prof = ['Dr. Ali','Ahsan Naeem','Ahsan Masud','Dr. Baneen']

z = zip_longest(subj,ch,prof,fillvalue='x')

for s,c,p in z:
  print(f"{s} has {c} Credit Hours and will be taught by {p}")

# Mech has 3 Credit Hours and will be taught by Dr. Ali
# CP2 has 2 Credit Hours and will be taught by Ahsan Naeem
# ES has 4 Credit Hours and will be taught by Ahsan Masud
# MoM has x Credit Hours and will be taught by Dr. Banee
```

- If we have multiple separate collections (or sequences) and we want to sort them based on one of them, we can zip them together using the `zip()` function, convert them into a list, and then, use the `sorted()` function or something else.

```py
subj = ['Mech','CP2','ES','MoM']
ch   = (3,2,4)
prof = ['Dr. Ali','Ahsan Naeem','Ahsan Masud','Dr. Baneen']

l = list(zip(subj,ch,prof))

# Sort based on the second element of each tuple, i.e, credit hours
l.sort(key=lambda x:x[1])

# Unpack each tuple from the list and iterate over them
for s,c,p in z:
  print(f"{s} has {c} Credit Hours and will be taught by {p}")
```

- The `zip()` function can be used to construct a dictionary from two iterables, considering that the first iterable contains the keys, and teh second iterable contains teh values.

```py
subj = ["LA","VCA","FOTS"]
ch   = [3,4,2]
my_dict = dict(zip(subj,ch))
```

- We can also zip two dictionaries together, in which, the corresponding key-value pairs are zipped together. This means that if the resulting tuples will be like this:
  - ((key1_from_dict1,value1_from_dict1),(key1_from_dict2,value1_from_dict2))
  - ((key2_from_dict1,value2_from_dict1),(key2_from_dict2,value2_from_dict2))
  - ((key3_from_dict1,value3_from_dict1),(key3_from_dict2,value3_from_dict2))
  - and so on
  - basically a tuple of two tuples, where these subtuples are the corresponding key-value pairs from each dictionary

```py
student1 = {
  'Reg':'2018-MC-01',
  'Name':'Muhammad Usman',
  'Sec':'A',
  'Courses':['CP2','ES']}
student2 = {
  'Reg':'2018-MC-02',
  'Name':'Tahir Mehmood',
  'Sec':'A',
  'Courses':['ES','LA']}

# We have to use items() to get the key,value pair
# if we just zip(student1,student2)
# the resulint zipped object will only contain keys and no values 
z = zip(student1.items(),student2.items())
for (k1,v1),(k2,v2) in z:
  print(f"{k1} of first student is {v1}")
  print(f"{k2} of second student is {v2}")
```

- We also have a builtin `map()` method. Its signature is given below:

```py
map(func,*iterables)
```

- The `map()` method takes an arbitrary number of iterables and computes the given function using the corresponding elements from the iterables, and returns a map object. The map object is an iterator just like zip object, so it can also only be used once before being exhausted.
- The number of iterables that should be provided to the `map()` method depends on the number of arguments of the given function. If this mapping function takes one argument, only one iterable should be provied, if that mapping function takes two argumetn, only two iterables should be provided. If that mapping function takes three arguments, three iterables should be provieded.
- Lets consider this expression: `map(my_func,list1,list2)` and lets assume `my_func` is defined as a function `lambda x,y: x + y`. Now `map()` goes over each pair of corresponding values from the `list1` and `list2`, applies the `my_func(x,y)` on these values (`x = list1[i]` and `y = list2[i]`), and then the produced value is added to the map object. Lets see some examples:

```py
import math
nums = [1,4,9,16,25]

m = map(math.sqrt,nums)
print(list(m)) # [1,2,3,4,5]

list1 = [1,2,3,4,5]
list2 = [-1,2,-3,4,-5]

m = map(lambda x,y:x+y,list1,list2)
print(list(m)) # [0,4,0,8,0]
```

- And similar to zip(), the map() also continues until one of the iterables is exhausted. This means that when the shortest iterable is exhausted, the map() terminates. So the resulting map object only has a length equal to the lenght of shortest iterable provided.
- Besides, zip() and map(), there is another very useful builtin method called `filter()`. Data sets often need to be filtered based on some criteria. The filter() prototype looks like this:

```py
filter(func or None,iterable)
```

- The filter() returns an iterator yielding those items in the iterable for which `func(item)` is `True`. If the function is `None`, return those items that are `True`.
- The filter() returns a filter object, which is an iterator just like map object and zip object.
- For example, if the argument function is `lambda x: True if x%2 == 0 else False`, then only the even numbers in the iterable will be yielded to the filter object. And all odd numbers will be rejected.
- One thing to remember here is that, Python treats all values other falsey values to be truish, so we do not necessarily have to return a boolean value, but is a good practice to do so. These are the falsey values:
  - Sequences: empty lists `[]`, tuples `()`, sets `set()`, dictionaries `{}`, strings `""`, ranges `range(0)`.
  - Numbers: zero integer `0`, zero float `0.0`, zero complex `0j`
  - Constans: `False` and `None`

```py
nums = [1,2,3,4,5]

# filter out odd numbers and yield only even numbers
even_nums = filter(lambda x: x % 2 == 0, nums)
list(f) # [2,4]

# filter out even numbers, and yield only odd numbers
odd_nums = filter(lambda x: x % 2 == 1, nums)
list(f) # [1,3,5]
```

- Often we need to remove missing values from a dataset. To do that, we can simply use `filter(None,iterable)`. This works because missing values like empty sets, empty lists, 0 numbers, `None` etc are treated as False, and hence removed when `None` is passed as the function argument to the filter() method.
- However, sometimes, `0` is considered a valuable information and not a missing value. To let the filter method allow `0` in the output filter object, we can explicitly tell it to consider `0` as `True`.

```py
filter(lambda x: True if x == 0 else x,iterable)
```

- However, this approach will also allow `False` value in the iterable, since `False == 0`. But we do not want it. So what do we do? Remember that the equality operator `==` checks for equivalence of values, and since `False` is converted to `0` when converted from boolean to a number. But the `is` operator checks for the object representation in memory. So `False is not 0`.

```py
filter(lambda x: True if x is 0 else x,iterable)
```

- There is one more very useful function that operates on iterables called `reduce()` available in `functools` modeule. The `reduce()` method has the following prototype:

```py
reduce(func,iterable[,initial])
```

- The reduce() method takes an iterable and reduces it to a single value, by applying the argument function cummutatively on two items from the iterable. For example, `reduce(lambda x, y: x+y, [1,2,3,4,5])` calculates the sum of the given list as `((((1+2)+3)+4)+5)`. If the optional `initial` argument is given, it is placed before the items of the iterable in the calculation, and serves as the default value when the iterable is empty.
- The calculation is done as follows:
  - Initially, the function `func(x,y)` is applied on the first two items of the iterable.
  - The function is then called again with the result obtained in the previous step as the first argument, and the next value from the iterable as the second argument.
  - This process keeps repeating until the last item in the iterable is processed.

```py
from functools import reduce

nums = [1,2,3,4,5]

# The following three examples can be achieved by builtin methods:
# 1. sum(nums)
# 2. min(nums)
# 3. max(nums)

# Calculates the sum of every element in the sequence
reduce(lambda x,y: x + y, nums) # 15
# ((((1+2)+3)+4)+5) = 15
# 1+2+3+4+5

# Calculates the minimum value in the sequence
reduce(lambda x,y: x if x < y else y, nums) # 1
# ((1 if 1 < 2 else 2) if (1 if 1 < 2 else 2) < 3 else 3) if ((1 if 1 < 2 else 2) if (1 if 1 < 2 else 2) < 3 else 3) < 4 else 5

# Calculates the maximum value in the sequence
reduce(lambda x,y: x if x > y else y, nums) # 5
# ((1 if 1 > 2 else 2) if (1 if 1 > 2 else 2) > 3 else 3) if ((1 if 1 > 2 else 2) if (1 if 1 > 2 else 2) > 3 else 3) > 4 else 5

# These examples can be elegantly achieved by reduce()
# Doing them otherwise is complex

# Calculates the product of every element in the sequence
reduce(lambda x,y: x * y, nums) # 120
# ((((1*2)*3)*4)*5) = 120
# 1*2*3*4*5

reduce(lambda x,y: x + math.factorial(y), nums, 0) # 153
# (((((0+1!)+2!)+3!)+4!)+5!)
# 1!+2!+3!+4!+5!
```

- There is no tuple comprehension, and if we try to code what seems to be a tuple comprehension, we instead get a generator object.

```py
nums = (5,4,1,2,3)
x = (i * i for i in nums)
type(x) # <generator object <genexpr> at 0x0000ffffff7f>
```

- Generator objects are also an iterator, just like zip, map, and filter.
- Generator objects unlike list comprehensions, are much more memory efficient. This is because unlike lists, they do not store their contents in memory and do not calculate each element at definition. Instead they only yield each element successively. As we iterate over a generator object, the next element is calculated on the fly, and yielded. When the complete collection is exhausted, the generator object is left empty with nothing stored.

```py
nums = (5,3,4,6,8)

# List comprehension
sqNums1 = [i * i for i in nums]

# Generator expression
sqNums2 = (i * i for i in nums)
```

- The generator object `sqNums2` only holds the rule (squaring the numbers and a reference to the `nums` tuple). They do not calculate or store any squared number.
- When we iterate over the generator object, an element is picked from the `nums` tuple, and the rule is applied to yield an element, that we can access. The generated element is used and discarded. In next iteration, the same procedure occurs and so on, till the last element is processed, at which point, the generator object is exhausted, with no value stored. So generator objects are one time usable. Therefore, generators are known as lazy single-use iterable.

```py
from sys import getsizeof

sqNumbers = [n * n for n in range(10_000_000)]
print(f"Size of list: {getsizeof(sqNumbers)} bytes")
# Size of list: 89,095,160 bytes

sqNumbers = (n * n for n in range(10_000_000))
print(f"Size of generator: {getsizeof(sqNumbers)} bytes")
# Size of generator: 104 bytes
```

- Some things to note are that:
  - Generators are iterators (iterators are also iterables)
  - Generators do not know how many elements are inside, so we can not use the `len()` function on them.
  - Generators are single use iterators. Once used, we can not get the elements again. Once the generator is completely used, it is called as being exhausted.
  - Because generators are single use, they are generally used immediately after creating them.
- Generators are used when we need to process a sequence without needing access to individual elements arbitrarily, and we do not need those elements afterwards. Such a use is very common. For example, we might be interested in calculting the sum of all fibonacci numbers till 1000. We are only interested in their sum. And we do not want to use these fibonacci numbers after calculating their sum. So creating a list of these fib numbers and calculating their sum is a waste of memory. So we should use a generator expression.
- There are two ways to create a generator: generator expressions and generator functions.
- Iterable vs iterator: An iterable is a data type that can be directly iterated over, using a `for` loop for eaxmple. Iterators can also be iterated over directly, but only once. Once the iterator has produced all its elements, it will be exhausted and become empty.
- Iterable is an object that has an `__iter__` method which returns an iterator, or which has an `__getitem__` method that can take take sequential indexes from zero (and raises an `IndexError` when the indices are no longer valid). So an iterable is an object that you can get an iterator from.
- An iterator is an object with a `__next__` (Python 3) or `next` (Python 2) method. Whenever an iterator is iterated over, using a `for` loop for example. the `__next__` method is called autiomatically.
- generator object, zip object, map object, filter object are all iterators. Whereas, list, tuples, sets, and dictionaries are iterables.
- An iterator has a state that remembers where it is during iteration. During each iteration, it updates the state to point at the next value. When the iteration is done, it signals when it is done by raising `StopIteration`. An iterator also has `__iter__` method that returns itself. So an iterator is self-iterable. Whereas, an iterable returns an iterator that is a separate object.
- Because an iterator depends on the `__next__` method to iterate, it can not be indexed arbitrarily. It can only be accessed sequentially. Whereas, an iterable uses the `__getitem__` method which can access an arbitrary element through an index value.
- So an iterator uses `__next__` method for sequential access. Whereas an iterable uses the `__getitem__` method for arbitrary access. The `__next__` method raises the `StopIteration` exception to signal the end of an iteration. Whereas, the `__getitem__` method raises the `IndexError` exception to signal the end of an iteration, that the larger indexes are not valid.
- However, an iterable can produce an iterator as well, thorugh the `__iter__` method. Which returns an iterator. This iterator is then used for a sequential iteration, and behaves the same way as any other iterator. An iterator also has an `__iter__` method, but `__iter__` returns itself. So an iterator is referred to as a self-iterable.
- Any object of a class that follows the iterator protocol is an iterator. The iterator protocol requires the class to has two methods: `__iter__` and `__next__`.
- Iterators are designed to be one time usable only. That is to say that they can not be reset. Once they raise the `StopIteration` exception, they will continue to do so.
- Iterables on the other hand are not themselves iterators, rather they create a new iterator each time we use them. So alhough the iterator produced from an iterable by using the `__iter__` method is one time usable only. The iterable itself is not, as the next time we use the iterable, it simply generates a new iterator, which can be used to iterate over again. So iterables can be used as many times as required.
- The following syntax is an example of a generator expression. It looks very similar to list comprehension, and it is designed to look like a list comprehension. Generator expressions werre introduced to be an alternative for list comphrehensions. A memory-efficient and time-efificnet alternative. They do not precalculate and store their elements from the rule specified for them. Rather they just store the rule. Whereas, the list comphrehension calculates each element and store them in memory, on definition. Thus, generator expressioons are used when we just want to iterate over a list for some reason, without the need for arbitrary access of the elements themselves after that particular use is over.

```py
# Generator expression
g = (i for i in range(10))

from sys import getsizeof
getsizeof(g) # 104 bytes

# Generator objects are iterators, so they have follow the iterator protocol
g.__iter__() == g # True

g.__next__() # 0
g.__next__() # 1
# ... so on
g.__next__() # 9
g.__next__() # StopIteration

l = [i for i in range(10)]
getsizeof(l) # 184 bytes
# this looks small, but we have seen the value for range(10_000_000))

# List objects are iterables, so they can generate an iterator
# and have the __getitem__(idx) method
itr = l.__iter__()

itr.__next__() # 0
itr.__next__() # 1
# ... so on
itr.__next__() # 9
itr.__next__() # StopIteration

# Arbitrary access is possible on iterables because they have __getitem__(idx) method
l.__getitem__(5) # 5
```

- Generator expressions can be used directly as an input to a function that requires an iteratable input. Remember that iterators are also iterables.

```py
# Generator objects can be assigned to an identifier
# and that identifier can be used as an argument to sum(iterable)
g = (i for i in range(10))
sum(g)

# Generator object can be directly used as an argument to sum(iterable)
sum((i for i in range(10)))

# And we can even eliminate the parenthesis around the generator object
sum(i for i in range(10))

# Similarly, lists created from list comprehension can be assigned to an identifier
# and these list identifiers can be used as argument to sum(iterable)
l = [i for i in range(10)]
sum(l)

# List comprehension objects can be directly used as an argument to sum(iterable)
# But we can not eliminate the square brackets around the list comprehension
# as that would lead to ambiguity
sum([i for i in range(10)])
```

- Generator objects are most commonly used in two ways:
  - they are iterated over in a loop, for example the `for` loop
  - they are used as an argument to a function that requires an iterable argument
- If we partly use a generator object, the next time we access it, we only access from that point onwards. It is as if, the used elements were never there.

```py
g = (i for i in range(10))

# Lets use the first 3 elements inside the generator object
g.__next__() # 0
g.__next__() # 1
g.__next__() # 2

# Now when we use them, we can only access the rest of the elements
# 0,1,2 are not accessible anymore
# the generator object can only iterate from 3 to 9
sum(g) # 42
# Notice that the sum is 42 (= 3+4+5+6+7+8+9)
# instead of 45 (= 0+1+2+3+4+5+6+7+8+9)
```

- We can also cast a generator object to other iterables like a list, tuple, or set. But note that doing so would violate the very purpose they were designed for. We create generator objects as a memory-efficient, time-efficient single-use alternative to lists, tuples, etc. But if we cast them to a list, or tuple etc, datatype, although we can, it violates that very principle.

```py
g = (i for i in range(10))
# Casting to list
g_obj_casted_to_list = list(g)

g = (i for i in range(10))
# Casting to tuple
g_obj_casted_to_tuple = tuple(g)
```

- Besides generator expressions, generator objects can be created using generator functions. Generator functions use a special keyword `yield`, and they behave differently than normal functions.

```py
def count(n):
  while True:
    yield n
    n += 1

# Main program
a = count(0) # <generator object count at 0x7fd7e0c135a0>

a.__next__() # 0
a.__next__() # 1
a.__next__() # 2
# ... so on
```

- This function `count(n)` returns a generator object. The statement `a = count(0)` created the generator object. Now, we can use it as any other generator object.
- The generator function contains the `yield` keyword. The `yield` keyword is like a `return` statement, but behaves slightly different.
- The generator function is called by using the `__next__()` or `next` methods. When the generator function reaches the `yield` keyword, the interpreter returns back to the calling site with the value that is yielded (just like a `return n` statement). But when the `next()` is executed again, the interpreted continues from the next line of the `yield` statement rather than restarting from the function entry. In our example, since we were in a `while` loop, the interpreter jumps to the next line of the yield statement, which incremented `n` and goes on to the next iteration of the while loop, yields the new value of `n`. And returns to the calling site again. The `next` method will keep going until the loop inside the function is valid. If we were instead to have a `for` loop with a fixed number of iterations. Imagine the `for` loop has 5 iterations. On the 5th iteration we would continue from the next line of yield statement, just like all previous iterations, nothing fancy so far. But when we execute the `next()`, the 6th time (remember tha the `for` loop only allowed 5 iterations), the interpreter would jump to the next line of the yield statement, execute those lines until the end of the function. And when the function ends, instead of returning, it would raise the `StopIteration` exception. And when we execute `next()` once more, we would still get only the `StopIteration` exception.

```py
def func():
  print("Function entry")
  for i in range(5):
    yield i
    print("Next line of yield statement")
  print("Function end")

g = func()

print(g.__next__())
# Function entry
# 0

print(g.__next__())
# Next line of yield statement
# 1

print(g.__next__())
# Next line of yield statement
# 2

print(g.__next__())
# Next line of yield statement
# 3

print(g.__next__())
# Next line of yield statement
# 4

print(g.__next__())
# Next line of yield statement
# Function end
# StopIteration

print(g.__next__())
# StopIteration
```

- Because of the behavior of the `yield` statement, the generator functions need a loop to be useful. Although, of very little use, we can write a generator function without any loop.

```py
def func():
  print("Function entry")
  yield
  print("Function end")

g = func()

g.__next__()
# Function entry

g.__next__()
# Function end
# StopIteration

g.__next__()
# StopIteration
```

- Because of the behavior of the yield statement, generator functions are also sometimes called pause-able functions. Since they can be paused and resumed.
- Although normal functions can be considered `NoneType` if they do not contain any exectuable code, however, functions with `yield` statement are always considered as generator functions, and produce a generator object, even if they do not have any executable code.

```py
# Regular function # 1
def func():
  return

a = func()
print(a) # None
type(a) # <class 'NoneType'>

# Regular function # 2

def func():
  if 1 == 2:
    return 1

a = func()
print(a) # None
type(a) # <class 'NoneType'>

# Generator function # 1
def func():
  yield

a = func()
print(a) # <generator object func at 0x7fd7e0c135a0>
type(a) # <class 'generator'>

# Generator function # 2
def func():
  if 1 == 2:
    yield 1

a = func()
print(a) # <generator object func at 0x7fd7e0b1c4a0>
type(a) # <class 'generator'>
```

- The generator function can have the `return` keyword. But they behave differently compared to non-genreator functions. When the `return` is encountered, the generator function terminates and raises the `StopIteration` exception. Which means, that the generator object is exhausted. So to "return" a value from a genrator function, always ue the `yield` statement. Since using a `return` statement would instead terminate the function and raise the `StopIteration` exception, wihtout actually returning anyhting.

```py
# This function shows why you should not use the return
# and yield statements together in a generator function
def func():
  return 1
  yield 1

a = func()

next(a)
# StopIteration: 1

# This happens because the return 1 statement is interpreted as:
# raise StopIteration: 1

next(a)
# StopIteration

# This happens because just like any iterator,
# once a StopIteration is raised, it will continue to raise it
# but this time (and from now on) without the message
# that we gave with the return value statement
```

- Also the `return value` will not return the value, instead the `value` is used as the message for the `StopIteration` exception.

```py
# The following function
def gen_func():
  yield 1
  return value

# is equivalent to this function
def gen_func():
  yield 1
  raise StopIteration(value)
```

- An important thing to note that the generator functions create a generator object. And these genrator objects behave like any other generator object.

```py
def func(n):
  for i in range(10):
    yield n
    n += 1

g = func(0)
next(g) # 0
next(g) # 1
list(g) # [2,3,4,5,6,7,8,9]
next(g) # StopIteration
```

- A regular (non-generator) function can return a generator expression. That means, that when the function is called, it returns a generator object, just like a genrator function returns a genrator object. But that does not make it a generator fucntion. A function is not called a generator function just because it returns a generator object. Rather if it contains a `yield` statement.

```py
# Non-generator function that does not return generator object
def sqNums1(aList):
  return [i * i for i in aList]

# A generator function that returns a generator object
def sqNums2(aList):
  for i in aList:
    yield i * i

# A non-generator function that returns a generator object
def sqNums3(aList):
  return (i * i for i in aList)
```

- Also a generator function can contain more than one `yield` statements. The first `yield` statement will make the execution jump back to the calling site. When the `next()` is exewucted, the execution continues from the next line of the previous `yield` statement. And if it encounters another `yield` statement, it again returns to the calling site. Now if the `next()` is executed again, the execution continues from the next line of this `yield` statement, and so on.

```py
def func():
  for i in range(5):
    yield i
    yield i * 2

g = func()

next(g) # 0 (i)
next(g) # 0 (i * 2)
next(g) # 1 (i)
next(g) # 2 (i * 2)
next(g) # 3 (i)
next(g) # 6 (i * 2)
next(g) # 4 (i)
next(g) # 8 (i * 2)
next(g) # StopIteration
```

- Object oriented programming is a programming paradigm where we create objects. Objects are created from abstract data types called classes that encapsulate data and functions together.
- There are primarily two methods of programming today: procedural and object-oriented. Procedural programming is focused on creating procedures or functions, whereas, object-oriented programming is focused on creating objects. The programming we did so far was procedural, since we were mainly focused on writing standalone functions to do everything.
- Object is a software entity that contains both data and procedures. The data contained in an object is called the object's data attributes. Whereas, the procedures contained in an object are called methods. The data attributes are simply variables that reference data, and the methods are functions that perform operations on these data attributes. The object is conceptually a self-contained unit that consists of data attributes and methods that operate on these data attributes.
- To define an object, we must first define a class of which type the object shall be.

```py
class Student:
  pass

student1 = Student() # <__main__.Student object at 0x7f1d65440dc0>
type(student1) # <class '__main__.Student'>
isinstance(student1,Student) # True
```

- The definition of an object (sometimes called an instance of the class) is more properly called **intantiation**.
- The assigning of the data attributes to the object is called **initialization**.
- The reason you see `__main__` before the class names in the above output, is because Python creates a module named as `__module__` in which the class is defined. However, you do not need to worry about it, as it is created and managed automatically behind the scenes.
- Once an object is created, we can add different attributes to it as shown here:

```py
# class definition
class Student:
  pass

student1 = Student() # object instantiation

# We can add data attributes after instantiation using dot notation
student1.reg = "2018-MC-01"
student1.name = "Mr. Shawn Johnson"
student1.sec = "B"

# Now we can access these attributes using the dot notation
student1.reg # "2018-MC-01"
student1.name # "Mr. Shawn Johson"
student1.sec # "B"
```

- However, adding all these attributes for every object we create of our class is very time consuming. A better approach would be to create a class method that does this automatically for us.

```py
# class definition
class Student:
  def initialize(obj,n,r,s):
    obj.name = n
    obj.reg = r
    obj.sec = s

student1 = Student() # instantiation

# we can call the class method to set the data attributes automatically
Student.initialize(student1,"Mr. Shawn Johnson","2018-MC-71","B")
# note that the method initialize() is called on the Student class
```

- Methods defined in a class have bindings (they are bound or connected to something). Based on the type of binding, methods are of three types:
  - Instance methods: A method bound with the instance (object) of a class. By default a method defined in a class is an instance method
  - Class method: A method bound with the class. We will see these later.
  - Static method: A method defined in a class, but is bound to neither the class nor any instance of it, is called a static method. We will see these later as well.
- So, a method defined in a class, is by default, an instance method. When we call an instance method on an instance, the instance is passed as the first argument automatically. So we can simplify our example code as:

```py
# notice that although the method initialize() takes 4 arguments
# we provided only 3
# the first argument is automatically provided as the instance itself
# which in this case is student1
student1.initialize("Mr. Shawn Johnson","2018-MC-71","B")
```

- However, there are a few naming conventions that we need to follow:
  - The first argument of an instance method is named `self`.
  - The rest of the arguments should have the same name as the data attributes they are used to assign with.
- With these two naming conventions applied, our above code looks like this:

```py
class Student:
  def initialize(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec

student1 = Student()
student1.initialize("Mr. Shawn Johnson","2018-MC-71","B")
```

- Python has a special method or a magic method called `__init__()`, known as a constructor in other programming languages. Lets replace the name of our `initialize()` method with this magic function name.

```py
class Student:
  def __init__(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec

student1 = Student()
student1.initialize("Mr. Shawn Johnson","2018-MC-71","B")
```

- With the magic method `__init__()` we can instantiate and initialize our object at the same time. We can pass in the initializing arguments at the time of instantiation. And the magic method gets called automatically.

```py
class Student:
  def __init__(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec

student1 = Student("Mr. Shawn Johnson","2018-MC-71","B")
```

- Even with the `__init__()` class constructor, we can still add more data attributes, and modify existing data attributes later using the dot notation.

```py
class Student:
  def __init__(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec

student1 = Student("Mr. Shawn Johnson","2018-MC-71","B")

# modifying an existing data attribute
student1.sec = "A"
# adding a new data attribute
student1.email = "example@example.com"
```

- We can use the data attributes inside class methods.

```py
class Student:
  def __init__(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec
    self.email = reg + "@student.uet.edu.pk"

# we do not need to pass the email argument
# as that will be created automatically from the reg argumetn
student1 = Student("Mr. Shawn Johnson","2018-MC-71","B")
```

- Besides instance attributes, we can define class attributes as well. These class attributes will be assigned to all instances of the class without manually doing it. We can however modify its value later (after instantiation) to suit our needs, wihtout affecting other instances of that class.

```py
class Student:
  department = "Mechatronics"
  
  def __init__(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec
    self.email = "".join(reg.split("-")).lower() + "@student.uet.edu.pk"

student1 = Student("Yahya Mateen","2019-R-2018-MC-71","B")
student2 = Student("Dr. Ali Raza","2010-MC-01","B")

student1.department # "Mechatronics"
student2.department # "Mechatronics"

student1.department = "Computer Science"

student1.department # "Computer Science"
student2.department # "Mechatronics"
```

- We can define more instance methods in a similar way as we define regular functions. With one important change. We must pass `self` as the first argument of the method. This `self` argument will be initialized with the reference of the instance itself. So we can apply changes to the object (instance) through this parameter.

```py
def Student:
  department = "Mechatronics"
  offered_subjects = ["LA","ES","CP","PD","VCA"]
  
  def __init__(self,name,reg,sec):
    self.name = name
    self.reg = reg
    self.sec = sec
    self.email = "".join(reg.split("-")).lower() + "@student.uet.edu.pk"
    self.subjects = []

  def register_subject(self,*subjects):
    for subject in subjects:
      if subject in Student.offered_subjects:
        self.subjects.append(subject)
      else:
        raise ValueError("subjects should be from the offered subjects list")

student1 = Student("Yahya Mateen","2019-R-2018-MC-71","B")
student1.register_subject("LA","ISL","CP","PD")
student1.subjects # ["LA","CP","PD"]
```

- The class attributes are accessible through either the class or the instance.

```py
def MyClass:
  myattribute = 5

  def __init__(self):
    pass

  def myfunc(self):
    MyClass.myattribute # 5
    self.myattribute # 5
```

- Initially on instantiation, the `self.myattribute` and `MyClass.myattribute` both will have the same value. But if we change the value of `self.myattribute` for an object, the `MyClass.myattribute` will still remain the same.
- Every class and instance of it has a magic attribute called `__dict__` that contains all the class/instance attributes and methods as a dictionary.

```py
class Student:
  department = "Mechatronics"

  def __init__(self,name):
    self.name = name
  
  def change_name(self,new_name):
    self.name = new_name

student1 = Student("Mr. Earl")

Student.__dict__()
# {
#   '__module__': '__main__',
#   'department': 'Mechatronics',
#   '__init__': <function Student.__init__ at 0x7f1a5cbb7ac0>,
#   'change_name': <function Student.change_name at 0x7f1a5cbb7b50>,
#   '__dict__': <attribute '__dict__' of 'Student' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Student' objects>,
#   '__doc__': None
# }
student1.__dict__()
# {
#   'name': 'Mr. Earl'
# }
```

- Some things to note is that, the instance of a class does not contain the class methods. Also, the `department` attribute is missing from the instance `student1`. How? If you type `student1.department`, it correctly returns the value `"Mechatronics"`. So what is happening here? Actually, the `department` attribute is a class attribute, and not the instance attribute. When we try to access the department attribute, the interpreter searches for this attribute in the instance namespace. If it does not find it, it searches for it in its parent class namespace, and from there, it gets the value `"Mechatronics"`. So no, `department` is not an instance attribute. Atleast not now. If we however, change the department attribute for the instance, it becomes an instance attribute and starts to show up in the instance `__dict__` as well.

```py
class Student:  
  department = "Mechatronics"

  def __init__(self,name):
    self.name = name
  
  def change_name(self,new_name):
    self.name = new_name

student1 = Student("Mr. Earl")
student1.department = "Computer Science"

Student.__dict__()
# {
#   '__module__': '__main__',
#   'department': 'Mechatronics',
#   '__init__': <function Student.__init__ at 0x7f1a5cbb7ac0>,
#   'change_name': <function Student.change_name at 0x7f1a5cbb7b50>,
#   '__dict__': <attribute '__dict__' of 'Student' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Student' objects>,
#   '__doc__': None
# }
student1.__dict__()
# {
#   'name': 'Mr. Earl'
#   'department': 'Computer Science'
# }
```

- In our student class we created an instance attribute `email` which we initialized with a value created from `reg` and appending the domain name next to it. However, if we change the `reg` value, the `email` attribute is not automatiocally updated. So what do we do?

```py
# Approach 0: do nothing
class Student:
  def __init__(self,reg):
    self.reg = reg
    self.email = "".joing(self.reg.split("-")).lower() + "@student.uet.edu.pk"

# Approach 1: create an setEmail function
# that updates the email to reflect changes in the reg attribute
# however, we need to call this function manually
# to update the email everytime reg changes
class Student:
  def __init__(self,reg):
    self.reg = reg
    self.email = "".joing(self.reg.split("-")).lower() + "@student.uet.edu.pk"

  def setEmail(self):
    self.email = "".joing(self.reg.split("-")).lower() + "@student.uet.edu.pk"

# Approach 2: make email a method rather than an attribute
# whenever we need the email, we call this method to get the latest value
# however, technically, the email is no longer an attribute, rather a method
class Student:
  def __init__(self,reg):
    self.reg = reg

  def email(self):
    return ("".joing(self.reg.split("-")).lower() + "@student.uet.edu.pk")

# Approach 3: make email a method and add the @property function decorator
# this makes the email method behave like an attribute
# so we can simply call Student.email instead of Student.email()
class Student:
  def __init__(self,reg):
    self.reg = reg

  @property
  def email(self):
    return ("".joing(self.reg.split("-")).lower() + "@student.uet.edu.pk")
```

- When we try to print an object or use an object as a string, the default conversion is not very useful. It just tells the class name with its memory address.
- To change that we can define two special methods `__str__()` and `__repr__()`. Both of these need to return a string. These strings will then be used where a string representation is needed for example in a `print()` statement.
- The difference between these two is that the `__str__()` is intended for user readability, whereas `__repr__()` is intended for uniqueness and completeness in debugging purposes for developers.
- Conventionally, the string from `__str__()` should describe the user-friendly information about the object. It can be anything that you deem appropriate.
- Conventionally, the string from `__repr__()` should be such that `eval(repr(c)) == c` is True. Thus, the `__repr__()` needs to return the instantiating constructor of the object, such that if we copy paste this string, it should be evaluated to produce the an exact copy of the object.
- By default, any function that expects a string argument, will choose the `__str__()` return value, but if there is not `__str__()` method, it will go for the `__repr__()` method. If even that is not defined, it will use the default `__str__()`, which just returns the class name and memory location. The default `__str__()` and `__repr__()` both return the same string. It has a class name and memory location.
- To use the `__repr__()` string representation instead of the `__str__()`, we need to explicitly call `__repr__()`, or use a expressions that explicitly uses `__repr__()` such as `repr()` or `%r` format etc.
- However, there is an interesting situation where the `__repr__()` is used by default instead of `__str__()`, and that is a container. The `__str__()` of a container is the `__repr__()` of its objects.
- So if we have a list of objects. The list will contain the `__repr__()` of its children objects.
- This is because, the `__str__()` representation of the objects will cause a lot of trouble, as the strings could contain characters that would interfere with the delimiters of the container itself. So `__repr__()` is used as a safe alternative.

```py
class Student:
  pass

std1 = Student()

# If we do not define our own __str__() and __repr__() methods
# the defaults are used
# the default __str__() and __repr__() both return the same string
print(std1)            # <__main__.X object at 0x7f52592e4dc0>
print(std1.__str__())  # <__main__.X object at 0x7f52592e4dc0>
print(std1.__repr__()) # <__main__.X object at 0x7f52592e4dc0>

class Student:
  def __str__(self):
    return "__str__()"

  def __repr__(self):
    return "__repr__()"

std1 = Student()

# Any function that expects a string argument
# will prefer __str__() over __repr__()
# however, if it does not find a __str__() definition
# it will use the __repr__()
print(std1)            # __str__()
print(std1.__str__())  # __str__()
print(std1.__repr__()) # __repr__()

# but there are some functions and expressions
# that explicitly need the __repr__()
# if __repr__() is not defined
# instead of trying __str__()
# they will rather chose the default __repr__() method
# this means that if the __repr__() was not defined in our class
# instead of "__str__()", we would get "<__main__.Student object at 0x7f5259215ff0>"
repr(std1)             # __repr__()
"%r" % std1            # __repr__()

l = [Student(),Student()]

# The __str__() of a container consists of __repr__() of its objects
# this is because if python instead used __str__() of the container's objects
# the __str__() of the container could be a total mess
# for example, imagine if the __str__() used the quotation marks in its return value
# the same rule applies here as repr() and %r
# if __repr__() is not available, it will choose the default __repr__()
# instead of going for the __str__(), even if it is defined
print(l) # [__repr__(), __repr__()]

# Conventionally, the __str__() should return a user readable string
# even if it is ambiguous, as it is solely used for readability
# not for debugging
# however, the __repr__() should return a string such that
# eval(repr(c)) == c
def Student:
  def __init__(self,name,reg):
    self.name = name
    self.reg = reg

  def __str__(self):
    return f"{name} - {reg}"

  def __repr__(self):
    return f"Student({self.name},{self.reg})"
```

- Encapsulation in object-oriented programming is a mechanism of restricting direct access to some componenets of an object, so users can not access state of the object and alter that.
- In class programming, there are three types of attributes:
  - public: class attributes that are accessible everywhere (outside and inside the class). The way we have used the attributes so far, are all public attributes.
  - private: class attribute that are accesssible only within the class and not outisde the class.
  - protected. class attributes that are accessible within the class and other classes that inherit from that class, but not outisde the class.
- Unlike many other programming languages, all attributes in python are actually public. Encapsulation in python is used as a convention rather than enforcement. This is because python is built on trust, and allows outside users to access apparently private attributes.
- Private names help to prevent access from outside code. For eaxmple, consider the following code used to decide a lottery winner.

```py
import random

class Lottery:
  def __init__(self):
    self.participants = []
    self.winner = None

  def add_participant(self,p):
    self.participant.append(p)
  
  def select_winner(self):
    self.winner = random.choice(self.participant)
  
  def get_winner(self):
    return self.winner

my_lottery = Lottery()
# We assume the numbers 1,2,...,100 are ID numbers of participants
my_lottery.add_participant(1)
my_lottery.add_participant(2)
# ... so on
my_lottery.add_participant(100)

# Intended usage
my_lottery.select_winner()
winner = my_lottery.get_winner()

# Exploitation
my_lottery.winner = 5 # Lets assume 5 is the ID number of the hacker himself
winner = my_lottery.get_winner()
```

- So we need a way to prevent sensitive attributes from being modified by code outside the class. Python does not have a true private concept. Instead, it uses naming conventions to indicate privateness.
- Single leading underscore `_x` indicate that a name is meant to be private. This is merely a hint that the name is intended to be used internally only, and does not modify the program behavior in any way.

```py
import random

class Lottery:
  def __init__(self):
    self.participants = []
    self._winner = None

  def add_participant(self,p):
    self.participant.append(p)
  
  def select_winner(self):
    self._winner = random.choice(self.participant)
  
  def get_winner(self):
    return self._winner

my_lottery = Lottery()
# We assume the numbers 1,2,...,100 are ID numbers of participants
my_lottery.add_participant(1)
my_lottery.add_participant(2)
# ... so on
my_lottery.add_participant(100)

# Intended usage
my_lottery.select_winner()
winner = my_lottery.get_winner()

# Note: Exploitation is possible,
# but a single leading underscore indicates that this is not intended to be modified
# so although exploitation is possible, accidents would not happen 
# Exploitation
my_lottery._winner = 5 # Lets assume 5 is the ID number of the hacker himself
winner = my_lottery.get_winner()
```

- Double leading underscore `__x` does not only indicates the name is private, but it also mangles its name, so outside access is difficult. IT STILL DOES NOT MAKE IT PRIVATE, IT JUST MAKES IT HARDER TO ACCESS THE NAME FROM OUTSIDE THE CLASS. It does so by name mangling. So `__x` is transformed to `_ClassName__x`. This has one other benefit. It prevents name clashes between derived classes and parent classes having the same attributes. This is possible because in the mangled name the `_ClassName__` prefix would be differnt. From outside the class, `my_object.__x` would not work and raise an `AttributeError`, but `_ClassName__x` would work.
- However, there is one thing that we need to remeber here. you can add more attributes to the object. So the access `my_lottery.__winner = 5` is not changing the `__winner` that we have defined as a private name inside the class. Because that private name (the one we are concerned with) is mangled to `_Lottery__winner`. So `my_lottery.__winner = 5` will add a new attribute with name `__winner` to the `my_lottery` instance, rather than raising an error. So if we attempt to view the `my_lottery.__dict__`, we will see two so called winners: `_Lottery__winner` and `__winner`. The class code that uses `self.__winner` is also changed to reference the mangled name instead of `__winner`. So adding a new attribute woudl not have any effect.

```py
import random

class Lottery:
  def __init__(self):
    self.participants = []
    self.__winner = None

  def add_participant(self,p):
    self.participant.append(p)
  
  def select_winner(self):
    self.__winner = random.choice(self.participant)
  
  def get_winner(self):
    return self.__winner

my_lottery = Lottery()
# We assume the numbers 1,2,...,100 are ID numbers of participants
my_lottery.add_participant(1)
my_lottery.add_participant(2)
# ... so on
my_lottery.add_participant(100)

# Intended usage
my_lottery.select_winner()
winner = my_lottery.get_winner()

# Exploitation attempt
my_lottery.__winner
# AttributeError: 'Lottery' object has no attribute '__winner'
my_lottery.__winner = 5
winner = my_lottery.get_winner() # None since we didnot call select_winner() yet

my_lottery._Lottery__winner = 5 # This would work however, but please don't
```

- Getter and setter methods:
- python provides builtin methods called `getattr(instance_name,attribute_name)` and `setattr(instance_name,attribute_name,attribute_value)`, to get and set attributes respectively. Although these two methods are not used often, they are useful when the attribute we have to access, is in the form of a variable as a string.

```py
my_attr = input("Enter the attribute you want to access: ")
my_object.my_attr # AttributeError: 'Lottery' object has no attribute 'my_attr'
my_object.my_attr = 4 # AttributeError: 'Lottery' object has no attribute 'my_attr'
```

- However, `getattr` and `setattr` will work in this scenario.

```py
my_attr = input("Enter the attribute you want to access: ")
getattr(my_object,my_attr) # Works correctly as expected
setattr(my_object,my_attr,4) # Works correctly as expected
```

- Another advantage is that, in case the attribute does not exist, the dot notation would produce an attribute error, but `getattr` allows us to pass a default value as the third argument. This will be returned to the user, BUT WILL NOT CHANGE THE ATTRIBUTE VALUE.

```py
my_attr = "some_attr" # Lets assume my_object does not have this attribute
my_object.my_attr # AttributeError

getattr(my_object,my_attr) # AttributeError
getattr(my_object,my_attr,5) # 5
# This 5 is just returned as a default value
# and the my_attr is neither created nor modified
```

- There is also a buultin function `hasattr(instance_name,attribute_name)` that checks if the object has the given attribute. If it does, it returns `True`, otherwise `False`.

```py
if hasattr(my_object,my_attr):
  print(my_object.my_attr) # We can access it without worrying
else:
  print("Oops! The attribute does not exist") # We can handle it properly
```

- However, mostly we define our own getters and setters methods. The getters are also called accessors and setters are also called mutators. There are three common ways to do it. The best appraoch is given at last, and not so good approach is given first.

```py
class MyClass:
  # Notice that the __x is defined as a "private" name
  def __init__(self,x):
    self.__x = x
  
  def get_x(self):
    return self.__x
  
  def set_x(self,new_x):
    self.__x = x

my_object = MyClass(5) # initial value 5
my_object.get_x() # 5
my_object.set_x(7) # Will set __x to 7
```

- The advatange of using getter instaed of dot notation is that, is that it provides a formal channel to access a private attribute. And it can modify that private value if required as appropriate.
- The advantage of using setter instead of dot notation is that, we can add validation rules beforing blindly modifying a private name. We can check for things like, correct data type, acceptable length, pattern etc.

```py
class MyClass:
  def __init__(self,x):
    self.__x = x

# If there was some error in initializing __x
# and so __x is None
# we can return 0 intead of None as a default value
# so the client-side code does not crash with an unexpected value of None
  def get_x(self):
    if self.__x == None:
      return 0
    else:
      return self.__x
  
# Notice how we can validate the new_x before blindly assigning it to __x
  def set_x(self,new_x):
    if isinstance(new_x,int) and x > 0 and x < 1000:
      self.__x = new_x
    else:
      raise ValueError("x should be an integer between 0 and 1000")
```

- Lets add one more private attribute:

```py
class MyClass:
  def __init__(self,x,y):
    self.__x = x
    self.__y = y

  def get_x(self):
    if self.__x == None:
      ret_x = 0
    else:
      ret_x = self.__x
    
  def get_y(self):
    if self.__y == None:
      ret_y = 0
    else:
      ret_y = self.__y
  
  def set_x(self,new_x):
    if isinstance(new_x,int) and x > 0 and x < 1000:
      self.__x = new_x
    else:
      raise ValueError("value should be an integer between 0 and 1000")

  def set_y(self,new_y):
    if isinstance(new_y,int) and y > 0 and y < 1000:
      self.__y = new_y
    else:
      raise ValueError("value should be an integer between 0 and 1000")
```

- The code has become lengthly and unmanageable. We are reusing the same validation rules. So its a good idea to create separate validation methods.

```py
class MyClass:
  def __init__(self,x,y):
    self.__x = x
    self.__y = y

  def safe_get(self,z):
    if z == None:
      return 0
    else:
      return z

  def isvalid(self,z):
    if isinstace(z,int) and z > 0 and z < 1000:
      return True
    else:
      raise ValueError("value should be an integer between 0 and 1000")

  def get_x(self):
    return self.safe_get(self.__x)
  
  def get_y(self):
    return self.safe_get(self.__y)

  def set_x(self,new_x):
    if self.isvalid(new_x):
      self.__x = new_x

  def set_y(self,new_y):
    if self.isvalid(new_y):
      self.__y = new_y
```

- We can add these safety validation rules to our constructor as well, by reusing the setters.

```py
class MyClass:
  def __init__(self,x,y):
    self.set_x(x)
    self.set_y(y)

# full code not shown
```

- One last improvement here, before we move to the second approach. Notice that the `isvalid` method does not need the instance or the class. It might as well be a standalone function outside the class. Therefore, we should declare it as a static method. To do that, we add the `@staticmethod` function decorator. Static methods are used with reference to their class. So `ClassName.static_method()`. Also, because it is now a static method, we can not pass the first argument as `self`, as we would not be calling it on the instance. The final code is this:

```py
class MyClass:
  def __init__(self,x,y):
    self.set_x(x)
    self.set_y(y)

  def safe_get(self,z):
    if z == None:
      return 0
    else:
      return z

  @staticmethod
  def isvalid(z):
    if isinstace(z,int) and z > 0 and z < 1000:
      return True
    else:
      raise ValueError("value should be an integer between 0 and 1000")

  def get_x(self):
    return self.safe_get(self.__x)
  
  def get_y(self):
    return self.safe_get(self.__y)

  def set_x(self,new_x):
    if MyClass.isvalid(new_x):
      self.__x = new_x

  def set_y(self,new_y):
    if MyClass.isvalid(new_y):
      self.__y = new_y

my_object = MyClass(4,5)
my_object.get_x()
my_object.set_x(9)
```

- Approach 2: We can use the `property(fget,fset,fdel,doc)` method. It will set the `fget` as the getter, `fset` as the setter, `fdel` as the deleter, and the `doc` as the docstring for the attribute.
- We use it as: `attribute_name = property(fget,fset,fdel,doc)`. This will allows the attribute name to be used with the dot notation. This maintains compatibility with old code that might be using dot notation instead of formal getter, setter, deleters.
- In this appraoch, we make two attributes with the same name. One private to be used internally `__x`, and the other `x` to be used externally with the dot notation. Also, we make the getter and setter themselves private if we need to, by using the leading double underscores.
- if we dont define the getter, `fget` will be set to `None`, similarly, if we do not define setter, `fset` will be set to `None`, and similarly if we dont define deleter, `fdel` will be set to `None`. So, we can define arbitrarily any of these three, and can use what we have defined, without the necessity to define all three.

```py
class MyClass:
  def __init__(self,x):
    self.x = x
  
  def __get_x(self):
    return self.__x

  def __set_x(self,new_x):
    if (MyClass.isvalid(new_x)):
      self.__x = new_x
  
  def __del_x(self):
    del x

  x = property(__get_x,__set_x,__del_x)

  @staticmethod
  def isvalid(z):
    if isinstance(z,int) and z > 0 and z < 1000:
      return True
    else:
      raise ValueError("value must be an integer between 0 and 1000")

my_object = MyClass(4)
my_object.x # 4, calls __get_x()
my_object.x = 5 # sets __x to 5, calls __set_x()
# remember, that x is an artificial construct, the concerned name is __x
del my_object.x # deletes __x, calls __del_x()
```

- Third approach uses the `@property` function decorator. For getter, we simply use the `@property` function decorator, for setter, we use `@attribute_name.setter`, for deleter, we ue `@attribute_name.deleter`.
- The important thing to note is that all three methods, getter, setter, and deleter must have the same names, which is the name that we will use to access the attribute from outside using dot notation.
- Also, as with the `property()` method, we need to keep an internal private name, and the same name but without leading double underscores for external use. The internal private name is what we will process. The external name is what will be used to call the getter, setter, and deleter as appropriate.
- Also since, the setter and deleter function decorators depend on the name of the getter, we must define getter method to be able to define setter and deleter. getter however can be defined alone, without a setter or deleter, as it doesnot depend on them anyway.

```py
class MyClass:
  def __init__(self,x):
    self.x = x
  
  @property
  def x(self):
    return self.__x
  
  @x.setter
  def x(self,new_x):
    if (MyClass.isvalid(new_x)):
      self.__x = new_x
  
  @x.deleter
  def x(self):
    del x

  @staticmethod
  def isvalid(z):
    if isinstance(z,int) and z > 0 and z < 1000:
      return True
    else:
      raise ValueError("value must be an integer between 0 and 1000")

my_object = MyClass(4)
my_object.x # 4, calls @property x
my_object.x = 5 # sets __x to 4, calls @x.setter x
del my_object.x # deletes __x, calls @x.deleter x
```

- Lastly, we need to rediscuss, that we had different types of methods, that decides how they are called:
  - instance method: a method defined without any function decorator inside a class is an isntance method. Instance methods takes the first argument as `self`, which is the instance or object on which that method is called. If we call an isntance method through the class name such as `MyClass.func()`, we need to explicitly give the object reference as an argument. So `MyClass.func(my_object)`. If we however call an instance method on an object, the first argument of `self` is automatically passed, so we only need to write: `my_object.func()`. instance methods process attributes of the instance, so we usually almost always calls them on instances and not trhough the class name.
  - class methods: a method that is called through the class rather than an instance. since these methods are bound to the class rather than the instance, i,.e, they process class attributes (not instance attributes), they also take a first argument conventionaly called `cls`. If we call a class method through the class, we automatically pass the class as the first argument, much like, `self` is passed as the first argument automatically when called on the instance. To define a class method, we need to use the `@classmethod` function decorator.
  - static methods. a method that is not bound to either an instance or the class. it can be used freely. such a method might as well be not defined in the class at all, and rather be an external function. but because there functionality is closely tied to the class or instance of that class, they are defined in the class. unlike instance methods which takes the first argument of `self` (which is an isntance reference), and class methods which takes the first argument `cls` (whiuch is the class reference), static methods takes neither of such arguments. They only take regular arguments like regular functions. To defined a static method, we need to use the `@staticmethod` function decorator. static methods can be called through either the instance or the class. but it is common to call them through the class, as it clearly indicates that there is no bound between the instance and the method.

```py
class MyClass:
  def instance_func(self):
    return
  
  @classmethod
  def class_func(cls):
    return
  
  @staticmethod
  def static_func():
    return
```

- To sum up:

```py
class MyClass:
  # class attributes
  __c = "value"

  # constructor
  def __init__(self,x):
    self.x = x

  # getter,setter,deleter
  @property
  def x(self):
    return self.__x

  @x.setter
  def x(self,new_x):
    if MyClass.isvalid(new_x):
      self.__x = new_x

  @x.deleter
  def x(self):
    del self.__x

  # static methods
  @staticmethod
  def isvalid(z):
    if isinstance(z,int):
      return True
    else:
      raise ValueError("value must be an integer")

  # instance methods
  def hello(self):
    print("Hello, World!")
    return

  # class methods
  @classmethod
  def get_c(cls):
    return cls.__c

  # magic methods
  def __str__(self):
    return f"[x: {self.x}]"

  def __repr__(self):
    return f"MyClass({self.x})"
```

- Instance methods can also take other objects are arguments. This is really useful for operator overloading.

```py
class MyClass:
  _s = []
  def __init__(self,v):
    self.v = v
  
  @property
  def v(self):
    return self.__v

  @v.setter
  def v(self,val):
    if type(self).isvalid(val):
      self.__v = val

  @v.deleter
  def v(self):
    del self.__v

  @staticmethod
  def isvalid(val):
    if isinstance(val,int):
      return True
    else:
      raise ValueError("value must be an integer")

  @classmethod
  def isempty(cls):
    return len(cls._s) == 0

  def __str__(self):
    return f"(v: {self.v})"

  def __repr__(self):
    return f"({type(self)}({self.v}))"

  def __add__(self,other):
    if self.v is not None and other.v is not None:
      return self.v + other.v
    else:
      raise ValueError(f"can not add {type(self.v)} and {type(other.v)}")
```

- Polymorphism: (*Poly* means *many* and *morph* means *shape*), so polymorphism means that multiple methods (or operators) have the same name but different definitions, and so behave differently depending on some factors. There are three types of polymorphism:
  - Method overloading, operator overloading, and method overriding
- Method overloading is when different functions have the same name but different input arguments (possibly different number of input arguments, or different types of input argumnets). Other languages like C/C++ and Java have method overloading, but Python does not support method overloading.
- Operator overloading is when an operator such as `+`, or `*` is overloaded to behave differently for operands of different data types. This is possible because `x.__operator__(y)` is called. So we can add a custom dunder method in our class.
- Method overriding. subclasses of a class can have methods of the same name as their parent class, and can override them with different behavior.

- Magic methods:
  - String reprsentation
    - `__str__(self) -> str` : neat pretty readble string representation of object
    - `__repr__(self) -> str` : string such that `eval(repr(c)) == c`.
  - Comparison:
    - `__lt__(self,other) -> bool` : less than
    - `__gt__(self,other) -> bool` : greater than
    - `__le__(self,other) -> bool` : less than or equal to
    - `__ge__(self,other) -> bool` : greater than or equal to
    - `__eq__(self,other) -> bool` : equal to
    - `__ne__(self,other) -> bool` : not equal to
    - Note: these are a lot of operators to define, with repeated logic. If we have one ordering comparison such as `<` and a equal-to test `==`, we should be able to derive all others.
    - To do that, we can use the `total_ordering` class decorator from `functools` module. It requires that the class define one of `__lt__()`, `__le__()`, `__gt__()`, or `__ge__()`, in addition to the `__eq__()` method.

```py
from functools import total_ordering

@total_ordering
class MyClass:
  def __lt__(self,other):
    return self.x < other.y

  def __eq__(self,other):
    return self.x == other.x

# Possible implementation:

# def __gt__(self,other):
#   return not self.__lt__(self,other) and not self.__eq__(self,other)

# def __le__(self,other):
#   return self.__lt__(self,other) or self.__eq__(self,other)

# def __ge__(self,other):
#   return self.__gt__(self,other) or self.__eq__(self,other)
```

- Magic methods (continued):
  - Comparison: however, careful that the previous code would now behave unexpectedly where it uses the `==` operator, such as `self.groupmember == None`. Here, it would call `self.__eq__(self,None)`. And try to do nasty stuff on `other=None`, which will raise an exception. To be safe from these side effects of operator overloading, use the `is` oeprator instead of `==`.
  - Length of object:
    - `__len__(self) -> int` : the length of the object. This will allow to use the builtin wrapper function `len(x)` which interanlly calls `x.__len__()`
  - Absolute value:
    - `__abs__(self) -> any` : the absolute value of the object. allows to use the builtin `abs(x)` on any object `x`.
  - Iterable:
    - The `__iter__(self) -> iterator` : is a method that can be defined to return an iterator which can be used to iterate over the object. There are multiple ways to define this:
      - If there is an iterable inside the object that we would want to iterate over any way, just return its iterator
      - If there is a custom sequence in which we want to iterate, we can define a generator function with `yield`.
      - Or, we can return a generator expression, that will be used for iteration.

```py
class MyClass:
  def __init__(self):
    self.mylist = [1,2,3,4,5]

  # Return a generator expression
  def __iter__(self):
    return (x for x in self.mylist)

  # Return an iterator for an iterable attribute
  def __iter__(self):
    return iter(self.mylist)

  # Create a generator function yielding custom values
  def __iter__(self):
    yield mylist[0]
    yield mylist[1]
    yield mylist[2]
    yield mylist[3]
    yield mylist[4]

# We can now iterate over an object of this class
myobject = MyClass

for i in myobject:
  print(i) # 1\n2\n3\n4\n5\n
```

- Magic methods (continued):
  - Mathematical and logical operators:
    - Likewise, we have so many of mathematical operators `__add__(self,other)`, and logical opertaors `__and__(self,other)`, and in-placed opertors `__iadd__(self,other)` (+=), unary operators `__pos__(self)` (+x), etc.

- If the magic methods for mathematical and logical operators etc do not support certain operands, they should return `NotImplemented`. For example, if we create a class for a point object, and we define the `__mul__(self,other)` function. And if we call it as `p1 * "Hello"` where `p1` is a valid point object, it should return `NotImplemented`. This should happen because the said expression invokes `type(p1).__mul__(p1,"Hello")`. But `__mul__(self,other)` can not handle `other` as a string object. So the `NotImplemented` singleton signals python to ask someone else for help. Which in this case, would be to look for the said operation in the class of `"Hello"` or `str`, instead of our own class. Maybe the `str` class defines the multiplication operation between strings and our class.
- So it might happen that the right operand class implements a method that can handle the the type of the two different operands. To facilitate this, the reflection methods are called with reflected (swapped operands).

```py
class MyClass:
  def __init__(self,v):
    self.v = v

  def __mul__(self,other):
    if type(other) != type(self):
      return NotImplemented
    return self.v * other.v

  def __rmul__(self,other):
    return self.v * n

my_object = MyClass(5)
n = 6

my_object * n
# TypeError: unsupported operand type(s) for *: 'MyClass' and 'int'

# Sequence of operations:
# ----------------------
# my_object * n
# type(my_object).__mul__(my_object,n)
# if type(other) != type(self): return NotImplemented
# NotImplemented
# <runtime reflects the operands and looks for __rmul__(self,other)>
# type(n).__rmul__(n,my_object)
# <int raise TypeError because it can not handle my_object>
# TypeError: unsupported operand type(s) for *: 'MyClass' and 'int'

n * my_object
# 30

# Sequence of operations:
# ----------------------
# n * my_object
# type(n).__mul__(n,my_object)
# <int returns NotImplemented>
# <runtime reflects the operands and looks for __rmul__(self,other)>
# type(my_object).__rmul__(my_object,n)
# return self.v * n
# return 5 * 6
# 30
```

- Lets create an `Author` class.

```py
class Author:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.books = []

  def __str__(self):
    return f"{self.name} - {self.age}"
```

- The `books` property is empty at initialization. This property will be a list of books, so lets create a `Book`.

```py
class Book:
  def __init__(self,title,year,author=None):
    self.title = title
    self.year = year
    if authors == None:
      self.authors = []
    else:
      self.authors = authors
  
  def __str__(self):
    return f"{self.title} - {self.year}"
```

- If we now add the authors to the book, like this:

```py
author1 = Author("JK Rowling", 56)
author2 = Author("Allama Iqbal", 48)
book1 = Book("Harry Porter",2002,[author1])
book2 = Book("Shikwa",1920,[author2])

print(book1.authors)
# Prints the authors list with the correct author in it
print(author1.books)
# Prints an empty list
```

- As you can see, there is no cyclic link between the author and the book. If a book gets an author, the author should also get that book.
- We can solve this by creating getters and setters for the `Book` class that will handle the cyclic linking.

```py
class Book:
  def __init__(self,title,year,author=None):
    self.title = title
    self.year = year
    if authors == None:
      self.authors = []
    else:
      self.authors = authors
  
  def __str__(self):
    return f"{self.title} - {self.year}"

  @property
  def authors(self):
    return self.__authors
  
  @authors.setter
  def authors(self,new_authors):
    for a in new_authors:
      if isinstance(a,Author):
        a.books.append(self)
        self.__authors = new_authors
      else:
        raise TypeError
```

- Now when we set an author for a book, that author will automatically have its books property updated as well.

- `Enum` is a class for enumeration available from `enum` module. It allows to enumerate constants with a name.

```py
from enum import Enum

class Colors(Enum):
  RED = 1
  BLUE = 2
  GREEN = 3

# call notation
Colors.RED # <Colors.RED: 1>
# index notation
Colors["RED"] # <Colors.RED: 1>

# access through value
Colors(1) # <Colors.RED: 1>

my_red = Colors.RED
my_red.name  # "RED"
my_red.value # 1

# __members__ allows to access all members
Colors.__members__
# mappingproxy({
#  'RED': <Colors.RED: 1>,
#  'BLUE': <Colors.BLUE: 2>,
#  'GREEN': <Colors.GREEN: 3>})
```

- Each object of an enumeration class is called its member. Each member has two properties `name` and `value`. The `name` is a string that denotes the name for that constant e.g. `RED`. And the `value` is the value for that name, e.g., `1`.
- The members of an Enumeration class can be accessed through either call notation or the index notation.
- Lets create an `Instructor` class to see an example use case:

```py
class Instructor:
  roles = [
    "Professor",
    "Associate Professor",
    "Assistant Professor",
    "Lecturer",
    "Teaching Fellow"]
  
  def __init__(self,name,role):
    self.name = name
    self.role = role

  @property
  def role(self):
    return self.__role

  @role.setter
  def role(self,new_role):
    if new_role in type(self).roles:
      self.__role = new_role
    else:
      raise ValueError("Invalid role selected")

instructor = Instructor("Dr. Ali Raza", "Professor")
instructor.role # Professor
```

- We can clearly see that the role names can become frustrating, as we need to remember them all, and type them correctly, and because they are long names, it takes a lot of typing.
- An easy solution would be create an enumeration class, that assigns short names to these long values.

```py
from enum import Enum

class Role(Enum):
  PROF   = "Professor"
  ASSOC  = "Associate Professor"
  ASSIST = "Assistant Professor"
  LECT   = "Lecturer"
  TF     = "Teaching Fellow"
```

- Now, we can easily initialize instructor objects.

```py
class Instructor:
  def __init__(self,name,role):
    self.name = name
    self.role = role

  @property
  def role(self):
    return self.__role.value

  @role.setter
  def role(self,new_role):
    self.__role = new_role

instructor = Instructor("Dr. Ali Raza", Role.PROF)
instructor.role.value # Professor
```

- Classes can inherit from other classes. The derived class is called the child class, whereas the base class is called the parent class.

```py
def ParentClass:
  pass

def ChildClass(ParentClass):
  pass
```

- The child class inherits all of the properties and methods of the parent class, and can define its own properties and methods.
- If we define methods or properties in the child class with the same name as that in the parent class, they will override. This is a form of polymorphism, known as method overriding.
- Basically, Python uses the Method Resolution Order to find a method. Which is the order in which different classes are searched for the said method.

```py
ChildClass.__mro__
# (
# <class '__main__.ChildClass'>,
# <class '__main__.ParentClass'>,
# <class 'object'>
# )
```

- It can be seen that the name is first searched for in the child class, then its immediate parent, and then its parent (if any), and so on, until it reaches the `builtins.object`
- The child classes reuses many of the properties of the parent class. So to repeat the same code in the `__init__` and its getters and setters is a tiring process, so we can simply use the parents `__init__`.

```py
class Parent:
  def __init__(self,name):
    self.name = name

class Child(Parent):
  def __init__(self,name,age):
    Parent.__init__(self,name)
    self.age = age
```

- However, we can use the `super()` method.

```py
class Parent:
  def __init__(self,name):
    self.name = name

class Child(Parent):
  def __init__(self,name,age):
    super().__init__(name)
    self.age = age
```

- The `super()` method returns a proxy object that represents the immediate parents class. With this syntax, we do not pass `self`, as that is automatically done, just like anyother instance methods in python. This is because we are not longer using the Class method syntax.
- However, sometimes we have a long chain of inheritance and the MRO is not doing what is intended. See the following code.

```py
class GrandParent:
  def get_pronouns(self):
    return "He/Him"

class Parent:
  def get_pronouns(self):
    return "They/Them"

class Child:
  pass
```

- Here we do not want our woke parent's pronouns, instead we want the regular he/him pronouns from the grandparent. But if we use `Child.get_pronouns()` the MRO will get us the `Parent` class `get_pronouns` method. So we need to explicitly mention the class from which we need to refer:

```py
class GrandParent:
  def get_pronouns(self):
    return "He/Him"

class Parent:
  def get_pronouns(self):
    return "They/Them"

class Child:
  def get_pronouns(self):
    GrandParent.get_pronouns(self)
```

- Remember that, since this is a class method syntax, we need to pass the `self` ourselves.

- list comprehension:
- List comprehension (and similarly, set comprehension and dictionary comprehension - there is no tuple comprehension however) allows to create a list from another list using a succint syntax.

```py
nums = [14,67,18,42,51,69]
l = []
for i in nums:
  l.append(i * i)
```

- This can be written elegantly and pythonic as:

```py
nums = [14,67,18,42,51,69]
l = [i * i for i in nums]
```

- The syntax is:

```py
list = [expression for element in iterable]
```

- We can also add conditionals:

```py
l = [i * i for i in nums if i % 2 == 0]
```

- The conditional syntax now becomes:

```py
list = [expression for element in iterable if condition]
```

- The `if-else` conditional is placed before the `for` expression, unlike the only `if` conditional which is placed after the `for` expression.

```py
list = [expression if condition else expression for element in iterable]
```

- We can also add nested for loops. The sequence is: outer for loop followed by inner for loop and so on.

```py
list = [expression for subcontainer in iterable for element in subcontainer]
```

- The simplest use case is to flatten out a nested list:

```py
nested_list = [[3,4,1],[1,5,7,2,3],[2,8]]
flattened_list = [i for sublist in nested_list for i in sublist]
```

- JSON (JavaScript Object Notation)
- JSON is a very common file format, that is used to exchange data as name-value pairs. similar to python dictionaries.
- Python supports JSON using the `json` module.
- See the following example JSON file:

```json
{
 "name": "Ahmed",
 "age": 30,
 "city": "Lahore"
}
```

- For contrast, the following is an equivalent python dictionaries:

```py
{
 "name": "Ahmed",
 "age": 30,
 "city": "Lahore"
}
```

- As you can see, the syntax is very similar. However, there are a few differences:
  - In JSON, `false` is used instead of `False` (as in Python), and similary `true` instead of `True`.
  - In JSON, `null` is used to represent `None` (as in Python).
- However, the `json` module handles these automatically, and we do not need to do anything manually.

- JSON can be parsed from a string or a file.

```py
import json
my_json = '{"name": "Ahmed", "age": 30, "city": "Lahore"}'

# Parsing JSON string into a dictionary
my_dict = json.loads(my_json)

# Generating JSON string from a dictionary
my_json = json.dumps(my_dict)

# Parsing JSON file into a dictionary
with open("in.json","r") as f:
  my_dict = json.load(f)

# Generating JSON file from a dictionary
with open("out.json","w") as f:
  json.dumps(my_dict,f)
  # We can provide an optional indent argument to indent the output json
  json.dumps(my_dict,f,indent=4)
```

- To import JSON file from a website, we can use the `get(url)` method from the `requests` module (not available by default, we have to install it using pip).

```py
import requests

url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2018/worldcup.standings.json"

r = requests.get(url) # this returns a requests object containing HTTP response
my_dict = r.json() # this returns a dictionary NOT a json string
```

## Confusions

- For taking a numeral from a user why is `eval()` used, when we can equivalently use `int()` or `float()` to convert input string to a number as needed.
- Which method is preferred to create empty lists. `a = []` or `a = list()`.
- Why does the lab manuals and Python's own documentation use single quotes as delimiters for string such as `'Hello'` rather than double quotes?
- Function decorators???
- What keyboard shortcut do you use to comment out selected lines of code?
- What extensions to install to use Python on VS Code + any other settings?
- What does the `|` mean when used with dictionaries. For example, what is this piece of code doing?

```py
data = {
"Lahore": ["Badshahi Mosque", "Lahore Fort", "Shalimar Gardens"],
"Karachi": ["Mazar-e-Quaid", "Clifton Beach", "Frere Hall"],
"Islamabad": ["Faisal Mosque", "Margalla Hills", "Rawal Lake"]
}
new_data = {"Peshawar": ["Peshawar Museum", "Bala Hisar Fort", "Qissa Khwani Bazaar"]}
data = data | new_data
```

## Styling

Google Python Style Guide has the following naming conventions:

module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name

The PEP has the following naming conventions:

Function names should be lowercase, with words separated by underscores as necessary to improve readability. Variable names follow the same convention as function names.

mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.