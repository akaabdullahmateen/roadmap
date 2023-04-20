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

## Confusions

- For taking a numeral from a user why is `eval()` used, when we can equivalently use `int()` or `float()` to convert input string to a number as needed.
- Which method is preferred to create empty lists. `a = []` or `a = list()` and why.
- What is list comprehension?
- Why does the lab manuals and Python's own documentation use single quotes as delimiters for string such as `'Hello'` rather than double quotes?
- What does `zip()` function do?
- Where is lab manual 21 and lab manual 22 duplicates? Is it a mistake?
- Why is there not a lab manual 26?