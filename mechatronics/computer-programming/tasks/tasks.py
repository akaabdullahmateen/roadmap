#############################################
# Author:       Yahya Mateen                #
# Reg. ID:      2019-R/2018-MC-71           #
# Course:       Computer Programming-II     #
# Teacher:      Mr. Ahsan Naeem             #
#############################################

# -------------------------------------------
#               Lab 1 - Task 1
# -------------------------------------------

def lab1_task1():
    task_header(1,1)
    print("*" * 20)
    print("*" * 20)
    print("*" * 20)
    print("*" * 20)
    return

# -------------------------------------------
#               Lab 1 - Task 2
# -------------------------------------------

def lab1_task2():
    task_header(1,2)
    print("*")
    print("*" * 2)
    print("*" * 3)
    print("*" * 4)
    return

# -------------------------------------------
#               Lab 1 - Task 3
# -------------------------------------------

def lab1_task3():
    task_header(1,3)
    print("*" * 20)
    print("*" + " " * 18 + "*")
    print("*" + " " * 18 + "*")
    print("*" * 20)
    return
# -------------------------------------------
#               Lab 2 - Task 1
# -------------------------------------------

def lab2_task1():
    task_header(2,1)
    print("Yahya Mateen\n2019-R/2018-MC-71")
    return

# -------------------------------------------
#               Lab 2 - Task 2
# -------------------------------------------

def lab2_task2():
    task_header(2,2)
    print("*" * 20 + "\n" + "*" * 20 + "\n" + "*" * 20 + "\n" + "*" * 20 + "\n")
    return

# -------------------------------------------
#               Lab 2 - Task 3
# -------------------------------------------

def lab2_task3():
    task_header(2,3)
    print("*" + "\n" + "*" * 2 + "\n" + "*" * 3 + "\n" + "*" * 4)
    return

# -------------------------------------------
#               Lab 2 - Task 4
# -------------------------------------------

def lab2_task4():
    task_header(2,4)
    print("*" * 20 + "\n" + "*" + " " * 18 + "*" + "\n" + "*" + " " * 18 + "*" + "\n" + "*" * 20)
    return

# -------------------------------------------
#               Lab 2 - Task 5
# -------------------------------------------

def lab2_task5():
    task_header(2,5)
    number = eval(input("Enter any value you want: "))
    print(f"You entered: {number}, double of which is: {number * 2}")
    return

# -------------------------------------------
#               Lab 2 - Task 6
# -------------------------------------------

def lab2_task6():
    task_header(2,6)
    first_number = eval(input("Enter first number: "))
    second_number = eval(input("Enter second number: "))
    print(f"The product of the two numbers is: {first_number * second_number: .2f}")
    return

# -------------------------------------------
#               Lab 2 - Task 7
# -------------------------------------------

def lab2_task7():
    task_header(2,7)
    import math
    print("This program calculates the area and volume of a sphere.")
    radius = eval(input("Enter the radius: "))
    print(f"Area of the sphere is A: {4 * math.pi * radius ** 2}")
    print(f"Volume of the sphere is V: {(4 / 3) * math.pi * radius ** 3}")
    del math
    return

# -------------------------------------------
#               Lab 3 - Task 1
# -------------------------------------------

def lab3_task1():
    task_header(3,1)
    first_number = eval(input("Enter first number: "))
    second_number = eval(input("Enter second number: "))
    print(f"{first_number} is {first_number / second_number * 100}% of {second_number}")
    return

# -------------------------------------------
#               Lab 3 - Task 2
# -------------------------------------------

def lab3_task2():
    task_header(3,2)
    number = eval(input("Enter a floating point number: "))
    print(f"Integer part: {int(number)}")
    print(f"Fractional part: {number - int(number)}")
    return

# -------------------------------------------
#               Lab 3 - Task 3
# -------------------------------------------

def lab3_task3():
    task_header(3,3)
    number = eval(input("Enter a 3-digit number: "))
    unit_digit = number % 10
    number //= 10
    tenth_digit = number % 10
    number //= 10
    hundredth_digit = number % 10
    print(f"{hundredth_digit}\n{tenth_digit}\n{unit_digit}\n{hundredth_digit} + {tenth_digit} + {unit_digit} = {hundredth_digit + tenth_digit + unit_digit}")
    return

# -------------------------------------------
#               Lab 4 - Task 1
# -------------------------------------------

def lab4_task1():
    task_header(4,1)
    time = eval(input("Enter seconds: "))
    minutes = time // 60
    seconds = time - minutes * 60
    print(f"{minutes} : {seconds}")
    return

# -------------------------------------------
#               Lab 4 - Task 2
# -------------------------------------------

def lab4_task2():
    task_header(4,2)
    time = eval(input("Enter seconds: "))
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60
    print(f"{hours} : {minutes} : {seconds}")
    return

# -------------------------------------------
#               Lab 4 - Task 3
# -------------------------------------------

def lab4_task3():
    task_header(4,3)
    time = eval(input("Enter seconds: "))
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60
    print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
    return

# -------------------------------------------
#               Lab 4 - Task 4
# -------------------------------------------

def lab4_task4():
    task_header(4,4)
    import math
    complex_number = complex(input("Enter a complex number: "))
    magnitude = math.sqrt(complex_number.real ** 2 + complex_number.imag ** 2)
    print(f"The magnitude of the complex number is: {magnitude:.2f}")
    del math
    return

# -------------------------------------------
#               Lab 4 - Task 5
# -------------------------------------------

def lab4_task5():
    task_header(4,5)
    import math
    complex_number = complex(input("Enter a complex number: "))
    magnitude_squared = complex_number * complex_number.conjugate()
    magnitude = math.sqrt(magnitude_squared.real)
    print(f"The magnitude of the complex number is: {magnitude:.2f}")
    del math
    return

# -------------------------------------------
#               Lab 4 - Task 6
# -------------------------------------------

def lab4_task6():
    task_header(4,6)
    import math
    vector = complex(input("Enter a vector (as a complex number): "))
    magnitude_squared = vector * vector.conjugate()
    magnitude = math.sqrt(magnitude_squared.real)
    unit_real = vector.real / magnitude
    unit_imag = vector.imag / magnitude
    print(f"The unit vector is: ({unit_real:.2f}{unit_imag:+.2f}j)")
    del math
    return

# -------------------------------------------
#               Lab 5 - Task 1
# -------------------------------------------

def lab5_task1():
    task_header(5,1)
    number = eval(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")
    return

# -------------------------------------------
#               Lab 5 - Task 2
# -------------------------------------------

def lab5_task2():
    task_header(5,2)
    centimeters = eval(input("Enter a length in centimeters: "))
    if centimeters < 0:
        print("Error: Negative lengths are invalid")
    else:
        print(f"The length is equivalent to {centimeters / 2.54:.2f} inches")
    return

# -------------------------------------------
#               Lab 5 - Task 3
# -------------------------------------------

def lab5_task3():
    task_header(5,3)
    first_number = eval(input("Enter first number: "))
    second_number = eval(input("Enter second number: "))
    if abs(first_number - second_number) <= 10:
        print("The two numbers are close")
    else:
        print("The two numbers are not close")
    return

# -------------------------------------------
#               Lab 5 - Task 4
# -------------------------------------------

def lab5_task4():
    task_header(5,4)
    hour_12h = eval(input("Enter an hour in 12h format: "))
    if hour_12h > 12 or hour_12h < 0:
        print("Error: Hour must in range 0 through 12")
        return
    am_or_pm = input("Enter \"am\" or \"pm\": ")
    if am_or_pm == "am":
        hour_24h = hour_12h
    else:
        hour_24h = hour_12h + 12
    print(f"{hour_12h:0>2}:00 {am_or_pm} in 24h format is: {hour_24h:0>2}:00")    
    return

# -------------------------------------------
#               Lab 5 - Task 5
# -------------------------------------------

def lab5_task5():
    task_header(5,5)
    import math
    number = eval(input("Enter a number: "))
    if number < 0:
        square_root = complex(0,round(math.sqrt(abs(number)),2))
    else:
        square_root = round(math.sqrt(number),2)
    print(f"The square root of {number} is {square_root}")
    del math
    return

# -------------------------------------------
#               Lab 5 - Task 6
# -------------------------------------------

def lab5_task6():
    task_header(5,6)
    first_number = eval(input("Enter the first number: "))
    second_number = eval(input("Enter the second number: "))
    if second_number == 0:
        print("Error: Division by zero is not possible")
    else:
        print(f"Ratio of the two numbers is: {first_number / second_number}")
    return

# -------------------------------------------
#               Lab 5 - Task 7
# -------------------------------------------

def lab5_task7():
    task_header(5,7)
    import math
    number = eval(input("Enter a number: "))
    square_root = math.sqrt(number)
    squared_square_root = square_root * square_root
    if number == squared_square_root:
        print(f"The number {number} is a perfect square")
    else:
        print(f"The number {number} is not a perfect square")
    del math
    return

# -------------------------------------------
#               Lab 5 - Task 8
# -------------------------------------------

def lab5_task8():
    task_header(5,8)
    marks = eval(input("Enter five subject marks: "))
    total_marks = 0
    for every_mark in marks:
        total_marks += every_mark
    average_marks = total_marks / len(marks)
    print(f"Average of five subject marks is: {average_marks:.2f}")
    if average_marks >= 80:
        print("You are an outstanding student")
    elif average_marks >= 70 and average_marks < 80:
        print("You are a good student")
    elif average_marks >= 60 and average_marks < 70:
        print("You are an average student")
    elif average_marks >= 50 and average_marks < 60:
        print("You are a below average student")
    elif average_marks >= 40 and average_marks < 50:
        print("You are a poor student")
    else:
        print("You need extraordinary efforts")
    return

# -------------------------------------------
#               Lab 5 - Task 9
# -------------------------------------------

def lab5_task9():
    task_header(5,9)
    import math
    sides = eval(input("Enter sides of a triangle: "))
    if len(sides) != 3:
        print("The triangle is invalid")
        return
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print("The triangle is invalid")
        return
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Area of the triangle is: {area:.2f}")
    del math
    return

# -------------------------------------------
#               Lab 5 - Task 10
# -------------------------------------------

def lab5_task10():
    task_header(5,10)
    first_number = eval(input("Enter first number: "))
    second_number = eval(input("Enter second number: "))
    third_number = eval(input("Enter third number: "))
    if first_number >= second_number and first_number >= third_number:
        maximum = first_number
    if second_number >= first_number and second_number >= third_number:
        maximum = second_number
    if third_number >= first_number and third_number >= second_number:
        maximum = third_number
    print(f"{maximum} is the largest number")
    return

# -------------------------------------------
#               Lab 5 - Task 11
# -------------------------------------------

def lab5_task11():
    task_header(5,11)
    martial_status = input("Enter martial status (M/U): ")
    gender = input("Enter your gender (M/F): ")
    age = eval(input("Enter your age: "))
    if (martial_status == "M") or \
        (martial_status == "U" and gender == "M" and age > 30) or \
        (martial_status == "U" and gender == "F" and age > 25):
        print("Congratulations! You are eligible for the insurance")
    else:
        print("Sorry! You are not eligible for the insurance")
    return

# -------------------------------------------
#               Lab 6 - Task 1
# -------------------------------------------

def lab6_task1():
    task_header(6,1)
    a, b, c = eval(input("Enter three numbers: "))
    if a >= c:
        if a >= b:
            maximum = a
        else:
            maximum = b
    else:
        if c >= b:
            maximum = c
        else:
            maximum = b
    print(f"{maximum} is the largest number")
    return

# -------------------------------------------
#               Lab 6 - Task 2
# -------------------------------------------

def lab6_task2():
    task_header(6,2)
    martial_status = input("Enter martial status (M/U): ")
    gender = input("Enter your gender (M/F): ")
    age = eval(input("Enter your age: "))
    if (martial_status == "M" or martial_status == "m"):
        eligible = True
    else:
        if (gender == "M" or gender == "m"):
            if age > 30:
                eligible = True
            else:
                eligible = False
        else:
            if age > 25:
                eligible = True
            else:
                eligible = False
    if eligible:
        print("Congratulations! You are eligible for the insurance")
    else:
        print("Sorry! You are not eligible for the insurance")
    return

# -------------------------------------------
#               Lab 6 - Task 3
# -------------------------------------------

def lab6_task3():
    task_header(6,3)
    martial_status = input("Enter martial status (M/U): ")
    if (martial_status == "M" or martial_status == "m"):
        eligible = True
    else:
        gender = input("Enter your gender (M/F): ")
        age = eval(input("Enter your age: "))
        if (gender == "M" or gender == "m"):
            if age > 30:
                eligible = True
            else:
                eligible = False
        else:
            if age > 25:
                eligible = True
            else:
                eligible = False
    if eligible:
        print("Congratulations! You are eligible for the insurance")
    else:
        print("Sorry! You are not eligible for the insurance")
    return

# -------------------------------------------
#               Lab 6 - Task 4
# -------------------------------------------

def lab6_task4():
    task_header(6,4)
    day = eval(input("Enter day: "))
    month = eval(input("Enter month: "))
    if (day <= 27 or day == 29):
        next_day = day + 1
    else:
        if (day == 28 and month == 2):
            next_day = 1
        if (day == 28 and month != 2):
            next_day = 29
        if (day == 31):
            next_day = 1
        if day == 30:
            if month in [1,3,5,7,8,10,12]:
                next_day = 31
            else:
                next_day = 1
    print(f"The next day is: {next_day}")
    return

# -------------------------------------------
#               Lab 6 - Task 5
# -------------------------------------------

def lab6_task5():
    task_header(6,5)
    day = eval(input("Enter day: "))
    month = eval(input("Enter month: "))
    if month == 2:
        if day == 28:
            next_day = 1
        else:
            next_day = day + 1
    if month in [4,6,9,11]:
        if day == 30:
            next_day = 1
        else:
            next_day = day + 1
    if month in [1,3,5,7,8,10,12]:
        if day == 31:
            next_day = 1
        else:
            next_day = day + 1
    print(f"The next day is: {next_day}")
    return

# -------------------------------------------
#               Lab 6 - Task 6
# -------------------------------------------

def lab6_task6():
    task_header(6,6)
    units = eval(input("Enter electricity units consumed: "))
    if units <= 100:
        ec_cost = 13.85 * units
    elif units <= 200:
        ec_cost = 13.85 * 100 + \
                  15.86 * (units - 100)
    elif units <= 300:
        ec_cost = 13.85 * 100 + \
                  15.86 * 100 + \
                  16.83 * (units - 200)
    elif units <= 700:
        ec_cost = 13.85 * 100 + \
                  15.86 * 100 + \
                  16.83 * 100 + \
                  18.54 * (units - 300)
    else:
        ec_cost = 13.85 * 100 + \
                  15.86 * 100 + \
                  16.83 * 100 + \
                  18.54 * 400 + \
                  20.94 * (units - 700)
    nj_sur = 0.1 * units
    fc_sur = 0.43 * units
    tv_charge = 35
    before_tax = ec_cost + nj_sur + fc_sur + tv_charge
    after_tax = before_tax * 1.12
    after_due_date = after_tax * 1.0834
    print(f"Amount payable within due date: {after_tax:.2f}")
    print(f"Amount payable after due date: {after_due_date:.2f}")
    return

# -------------------------------------------
#               Lab 7 - Task 1
# -------------------------------------------

def lab7_task1_printTwice(msg):
    print(f"{msg} {msg}")

def lab7_task1():
    task_header(7,1)
    lab7_task1_printTwice(input("Enter any message: "))
    return

# -------------------------------------------
#               Lab 7 - Task 2
# -------------------------------------------

def lab7_task2_printTimes(s:str,n:int):
    for i in range(n):
        print(s, end=" ")
    print("\b")

def lab7_task2():
    task_header(7,2)
    msg = input("Enter any message: ")
    count = eval(input("Times to repeat: "))
    lab7_task2_printTimes(msg,count)
    return

# -------------------------------------------
#               Lab 7 - Task 3
# -------------------------------------------

def lab7_task3_dist(x1,y1,x2,y2):
    import math
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    del math
    return distance

def lab7_task3():
    task_header(7,3)
    x1,y1 = eval(input("Enter first point (format: x1,y1): "))
    x2,y2 = eval(input("Enter second point (format: x2,y2): "))
    result = lab7_task3_dist(x1,y1,x2,y2)
    print(f"Distance between the two points is: {result:.2f}")
    return

# -------------------------------------------
#               Lab 7 - Task 4
# -------------------------------------------

def lab7_task4_triAreaSides(a,b,c):
    import math
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    del math
    return area

def lab7_task4():
    task_header(7,4)
    sideA,sideB,sideC = eval(input("Enter sides of a triangle: "))
    print(f"The area of the triangle is: {lab7_task4_triAreaSides(sideA,sideB,sideC):.2f}")
    return

# -------------------------------------------
#               Lab 7 - Task 5
# -------------------------------------------

def lab7_task5_billElect(units):
    if units <= 100:
        ec_cost = 13.85 * units
    elif units <= 200:
        ec_cost = 13.85 * 100 + \
                  15.86 * (units - 100)
    elif units <= 300:
        ec_cost = 13.85 * 100 + \
                  15.86 * 100 + \
                  16.83 * (units - 200)
    elif units <= 700:
        ec_cost = 13.85 * 100 + \
                  15.86 * 100 + \
                  16.83 * 100 + \
                  18.54 * (units - 300)
    else:
        ec_cost = 13.85 * 100 + \
                  15.86 * 100 + \
                  16.83 * 100 + \
                  18.54 * 400 + \
                  20.94 * (units - 700)
    nj_sur = 0.1 * units
    fc_sur = 0.43 * units
    tv_charge = 35
    before_tax = ec_cost + nj_sur + fc_sur + tv_charge
    after_tax = before_tax * 1.12
    after_due_date = after_tax * 1.0834
    return after_tax,after_due_date

def lab7_task5():
    task_header(7,5)
    units = eval(input("Enter electricity units consumed: "))
    due_amount,late_amount = lab7_task5_billElect(units) 
    print(f"Amount payable within due date: {due_amount:.2f}")
    print(f"Amount payable after due date: {late_amount:.2f}")
    return

# -------------------------------------------
#               Lab 8 - Task 1
# -------------------------------------------

def lab8_task1_dist(x1,y1,x2,y2):
    import math
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    del math
    return distance

def lab8_task1_triAreaSides(a,b,c):
    import math
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    del math
    return area

def lab8_task1_triAreaPoints(x1,y1,x2,y2,x3,y3):
    sideA = lab8_task1_dist(x1,y1,x2,y2)
    sideB = lab8_task1_dist(x2,y2,x3,y3)
    sideC = lab8_task1_dist(x3,y3,x1,y1)
    return lab8_task1_triAreaSides(sideA,sideB,sideC)

def lab8_task1():
    task_header(8,1)
    x1,y1 = eval(input("Enter first point: "))
    x2,y2 = eval(input("Enter second point: "))
    x3,y3 = eval(input("Enter third point: "))
    area = lab8_task1_triAreaPoints(x1,y1,x2,y2,x3,y3)
    print(f"The area of the triangle is {area:.2f}")
    return

# -------------------------------------------
#               Lab 8 - Task 2
# -------------------------------------------

def lab8_task2_dist(x1,y1,x2,y2):
    import math
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    del math
    return distance

def lab8_task2_triAreaSides(a,b,c):
    import math
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    del math
    return area

def lab8_task2_triAreaPoints(x1,y1,x2,y2,x3,y3):
    sideA = lab8_task2_dist(x1,y1,x2,y2)
    sideB = lab8_task2_dist(x2,y2,x3,y3)
    sideC = lab8_task2_dist(x3,y3,x1,y1)
    return lab8_task2_triAreaSides(sideA,sideB,sideC)

def lab8_task2_pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    partialA = lab8_task2_triAreaPoints(x1,y1,x2,y2,x3,y3)
    partialB = lab8_task1_triAreaPoints(x1,y1,x3,y3,x5,y5)
    partialC = lab8_task1_triAreaPoints(x3,y3,x4,y4,x5,y5)
    return partialA + partialB + partialC

def lab8_task2():
    task_header(8,2)
    x1,y1 = eval(input("Enter first point: "))
    x2,y2 = eval(input("Enter second point: "))
    x3,y3 = eval(input("Enter third point: "))
    x4,y4 = eval(input("Enter fourth point: "))
    x5,y5 = eval(input("Enter fifth point: "))
    area = lab8_task2_pentaArea(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
    print(f"The area of the pentagon is {area:.2f}")
    return

# -------------------------------------------
#               Lab 8 - Task 3
# -------------------------------------------

def lab8_task3_dist(x1,y1,x2,y2):
    import math
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    del math
    return distance

def lab8_task3_triAreaSides(a,b,c):
    import math
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    del math
    return area

def lab8_task3_triAreaPoints(x1,y1,x2,y2,x3,y3):
    sideA = lab8_task3_dist(x1,y1,x2,y2)
    sideB = lab8_task3_dist(x2,y2,x3,y3)
    sideC = lab8_task3_dist(x3,y3,x1,y1)
    return round(lab8_task3_triAreaSides(sideA,sideB,sideC),2)


def lab8_task3():
    task_header(8,3)
    x1,y1 = eval(input("Enter first point: "))
    x2,y2 = eval(input("Enter second point: "))
    x3,y3 = eval(input("Enter third point: "))
    px,py = eval(input("Enter point to check: "))
    area = lab8_task3_triAreaPoints(x1,y1,x2,y2,x3,y3)
    partialA = lab8_task3_triAreaPoints(px,py,x1,y1,x2,y2)
    partialB = lab8_task3_triAreaPoints(px,py,x1,y1,x3,y3)
    partialC = lab8_task3_triAreaPoints(px,py,x2,y2,x3,y3)
    if (area == partialA + partialB + partialC):
        print(f"The point ({px}, {py}) is inside the triangle")
    else:
        print(f"The point ({px}, {py}) is outside the triangle")
    return

# -------------------------------------------
#               Lab 9 - Task 1
# -------------------------------------------

def lab9_task1():
    task_header(9,1)
    rows = eval(input("Enter the number of rows: "))
    columns = 10
    for _ in range(rows):
        print("*" * columns)
    return

# -------------------------------------------
#               Lab 9 - Task 2
# -------------------------------------------

def lab9_task2():
    task_header(9,2)
    n = eval(input("Enter a number: "))
    for i in range(1, n + 1):
        print(f"{i}\t{i * i * i}")
    return

# -------------------------------------------
#               Lab 9 - Task 3
# -------------------------------------------

def lab9_task3():
    task_header(9,3)
    print()
    for i in range(1, 11):
        print(f"12 \xd7 {i}\t= {12 * i}")
    return

# -------------------------------------------
#               Lab 9 - Task 4
# -------------------------------------------

def lab9_task4():
    task_header(9,4)
    multiplicand = eval(input("Enter the multiplicand: "))
    max_multiplier = eval(input("Enter the maximum multiplier: "))
    print()
    for multiplier in range(1, max_multiplier + 1):
        print(f"{multiplicand} \xd7 {multiplier}\t= {multiplicand * multiplier}")
    return

# -------------------------------------------
#               Lab 9 - Task 5
# -------------------------------------------

def lab9_task5():
    task_header(9,5)
    height = eval(input("Enter the height: "))
    print()
    for width in range(1, height + 1):
        print("*" * width)
    return

# -------------------------------------------
#               Lab 9 - Task 6
# -------------------------------------------

def lab9_task6():
    task_header(9,6)
    height = eval(input("Enter the height: "))
    print()
    for width in range(height, 0, -1):
        print("*" * width)
    return

# -------------------------------------------
#               Lab 9 - Task 7
# -------------------------------------------

def lab9_task7():
    task_header(9,7)
    height = eval(input("Enter the height: "))
    print()
    for width in range(1, height + 1):
        print((" " * (height - width)) + ("*" * width))
    return

# -------------------------------------------
#               Lab 9 - Task 8
# -------------------------------------------

def lab9_task8_DistTable(m, n):
    print()
    for multiplier in range(1, n + 1):
        print(f"{m} \xd7 {multiplier}\t= {m * multiplier}")
    return

def lab9_task8():
    task_header(9,8)
    multiplicand = eval(input("Enter the multiplicand: "))
    max_multiplier = eval(input("Enter the maximum multiplier: "))
    lab9_task8_DistTable(multiplicand,max_multiplier)
    return

# -------------------------------------------
#               Lab 9 - Task 9
# -------------------------------------------

def lab9_task9():
    task_header(9,9)
    for i in range(1,101):
        square = i * i
        unit_digit = square % 10
        tenth_digit = (square // 10) % 10
        if (unit_digit == tenth_digit and unit_digit != 0):
            print(f"Number: {i}\t Square: {square}")
    return

# -------------------------------------------
#               Lab 9 - Task 10
# -------------------------------------------

def lab9_task10():
    task_header(9,10)
    countEven = countOdd = 0
    for _ in range(10):
        number = eval(input("Enter number: "))
        if (number % 2 == 0):
            countEven += 1
        else:
            countOdd += 1
    print(f"You entered {countEven} even and {countOdd} odd numbers")
    return

# -------------------------------------------
#               Lab 10 - Task 1
# -------------------------------------------

def lab10_task1():
    task_header(10,1)
    sumEven = sumOdd = 0
    for _ in range(10):
        number = eval(input("Enter number: "))
        if (number % 2 == 0):
            sumEven += number
        else:
            sumOdd += number
    print()
    print(f"Sum of even numbers: {sumEven}")
    print(f"Sum of odd numbers: {sumOdd}")
    return

# -------------------------------------------
#               Lab 10 - Task 2
# -------------------------------------------

def lab10_task2():
    task_header(10,2)
    total_marks = 0
    n = 5
    for _ in range(n):
        marks = eval(input("Enter subject marks: "))
        total_marks += marks
    average_marks = total_marks / n
    print()
    print(f"Mean of the five subject marks: {average_marks:.2f}")
    return

# -------------------------------------------
#               Lab 10 - Task 3
# -------------------------------------------

def lab10_task3():
    task_header(10,3)
    number = eval(input("Enter a number: "))
    if number < 0:
        print("Error: Negative numbers are not allowed")
    else:
        if (number % 2 == 0):
            start = 0
        else:
            start = 1
        total = 0
        for i in range(start,number + 1,2):
            total += i
            if i == number:
                print(f"{i}",end="")
            else:
                print(f"{i}",end="+")
        print(f" = {total}")
    return

# -------------------------------------------
#               Lab 10 - Task 4
# -------------------------------------------

def lab10_task4_fact(n):
    factorial = 1
    for i in range(2,n + 1):
        factorial *= i
    return factorial

def lab10_task4():
    task_header(10,4)
    number = eval(input("Enter a number: "))
    print(f"{number}! = {lab10_task4_fact(number)}")
    return

# -------------------------------------------
#               Lab 10 - Task 5
# -------------------------------------------

def lab10_task5_isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def lab10_task5():
    task_header(10,5)
    number = eval(input("Enter a number: "))
    if lab10_task5_isprime(number):
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")
    return

# -------------------------------------------
#               Lab 10 - Task 6
# -------------------------------------------

def lab10_task6_isprime(n):
    import math
    sqrt_n = math.ceil(math.sqrt(n))
    del math
    for i in range(2,sqrt_n + 1):
        if n % i == 0:
            return False
    return True

def lab10_task6():
    task_header(10,6)
    number = eval(input("Enter a number: "))
    if lab10_task6_isprime(number):
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")
    return

# -------------------------------------------
#               Lab 11 - Task 1
# -------------------------------------------

def lab11_task1():
    task_header(11,1)
    matrix_sum = 0
    matrix_product = 1
    print(f"Enter the elements of a 3 by 3 matrix", end="\n\n")
    for row in range(3):
        for column in range(3):
            element = eval(input(f"a{row + 1}{column + 1} = "))
            matrix_sum += element
            matrix_product *= element
    print(f"\nSum of all elements: {matrix_sum}")
    print(f"Product of all elements: {matrix_product}")
    return

# -------------------------------------------
#               Lab 11 - Task 2
# -------------------------------------------

def lab11_task2():
    task_header(11,2)
    n = eval(input("Enter the value of \"n\": "))
    summation = 0
    for k in range(1,n + 1):
        k_factorial = 1
        for i in range(2,k + 1):
            k_factorial *= i
        summation += (1 / k_factorial)
    print(f"Sum of series: {summation}")
    return

# -------------------------------------------
#               Lab 11 - Task 3
# -------------------------------------------

def lab11_task3_fact(k):
    if k < 0:
        return 0
    if k == 0:
        return 1
    factorial = 1
    for i in range(2,k + 1):
        factorial *= i
    return factorial

def lab11_task3_mySeries(n):
    summation = 0
    for k in range(1,n + 1):
        k_factorial = lab11_task3_fact(k)
        summation += (1 / k_factorial)
    return summation

def lab11_task3():
    task_header(11,3)
    n = eval(input("Enter the value of \"n\": "))
    print(f"Sum of series: {lab11_task3_mySeries(n)}")
    return

# -------------------------------------------
#               Lab 11 - Task 4
# -------------------------------------------

def lab11_task4():
    task_header(11,4)
    import math
    n = eval(input("Enter a number: "))
    for i in range(2,n + 1):
        is_prime = True
        for j in range(2,math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{i}",end=" ")
    print()
    del math
    return

# -------------------------------------------
#               Lab 11 - Task 5
# -------------------------------------------

def lab11_task5_isprime(n):
    import math
    limit = math.ceil(math.sqrt(n)) + 1
    del math
    for i in range(2,limit):
        if n % i == 0:
            return False
    return True

def lab11_task5():
    task_header(11,5)
    maximum = eval(input("Enter a number: "))
    for n in range(2,maximum + 1):
        if lab11_task5_isprime(n):
            print(f"{n}",end=" ")
    print()
    return

# -------------------------------------------
#               Lab 12 - Task 1
# -------------------------------------------

def lab12_task1():
    task_header(12,1)
    n = eval(input("Enter a number: "))
    print()
    i = 1
    while i <= n:
        cube = i * i * i
        print(f"{i}\t{cube}")
        i += 1
    return

# -------------------------------------------
#               Lab 12 - Task 2
# -------------------------------------------

def lab12_task2_fact(n):
    factorial = 1
    i = 2
    while i <= n:
        factorial *= i
        i += 1
    return factorial

def lab12_task2():
    task_header(12,2)
    n = eval(input("Enter a number: "))
    factorial = lab12_task2_fact(n)
    if factorial == None:
        print("ERROR: Factorial is not defined for negative numbers")
    else:
        print(f"{n}! = {factorial}")
    return

# -------------------------------------------
#               Lab 12 - Task 3
# -------------------------------------------

def lab12_task3():
    task_header(12,3)
    n = 1
    total_count = 0
    total_sum = 0
    while n != 0:
        n = eval(input("Enter a number: "))
        if n != 0:
            total_count += 1
            total_sum += n
    average = total_sum / total_count
    print()
    print(f"Count: {total_count}")
    print(f"Average: {average:.2f}")
    return

# -------------------------------------------
#               Lab 12 - Task 4
# -------------------------------------------

def lab12_task4():
    task_header(12,4)
    n = eval(input("Enter initial value: "))
    steps = 0
    while n != 1:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        steps += 1
        n = int(n)
        print(f"Next value: {n}")
    print()
    print(f"Steps: {steps}")
    return

# -------------------------------------------
#               Lab 12 - Task 5
# -------------------------------------------

def lab12_task5():
    task_header(12,5)
    prompt = "Enter initial value: "
    n = eval(input(prompt))
    while n < 2:
        n = eval(input(prompt))
    steps = 0
    while n != 1:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        steps += 1
        n = int(n)
        print(f"Next value: {n}")
    print()
    print(f"Steps: {steps}")
    return

# -------------------------------------------
#               Lab 12 - Task 6
# -------------------------------------------

def lab12_task6():
    task_header(12,6)
    n = eval(input("Enter a number: "))
    count = 0
    duplicate = n
    while n != 0:
        digit = n % 10
        n //= 10
        if digit == 0:
            count += 1
    print(f"Number of zeroes in {duplicate}: {count}")
    return

# -------------------------------------------
#               Lab 12 - Task 7
# -------------------------------------------

def lab12_task7_isprime(n):
    import math
    limit = math.ceil(math.sqrt(n)) + 1
    del math
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def lab12_task7():
    task_header(12,7)
    n = eval(input("Enter a number: "))
    x = n + 1
    while not lab12_task7_isprime(x):
        x += 1
    print(f"First prime encountered: {x}")
    return

# -------------------------------------------
#               Lab 12 - Task 8
# -------------------------------------------

def lab12_task8_isprime(n):
    import math
    limit = math.ceil(math.sqrt(n)) + 1
    del math
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def lab12_task8():
    task_header(12,8)
    n = eval(input("Enter a nunber: "))
    count = 0
    i = 2
    while count < n:
        if lab12_task8_isprime(i):
            print(f"{i}", end=" ")
            count += 1
        i += 1
    print()
    return

# -------------------------------------------
#               Lab 13 - Task 1
# -------------------------------------------

def lab13_task1():
    task_header(13,1)
    n = eval(input("Enter a number: "))
    isprime = True
    import math
    limit = math.ceil(math.sqrt(n)) + 1
    del math
    for i in range(2, limit):
        if n % i == 0:
            isprime = False
            break
    if isprime:
        print(f"The number {n} is prime")
    else:
        print(f"The number {n} is not prime")
    return

# -------------------------------------------
#               Lab 13 - Task 2
# -------------------------------------------

def lab13_task2():
    task_header(13,2)
    sum = 0
    count = 0
    while True:
        n = eval(input("Enter a number: "))
        if n != 0:
            sum += n
            count += 1
        else:
            break
    if count != 0:
        average = sum / count
    else:
        average = 0
    print()
    print(f"Average: {average}")
    return

# -------------------------------------------
#               Lab 13 - Task 3
# -------------------------------------------

def lab13_task3():
    task_header(13,3)
    import time
    import os
    ss = 0
    mm = 0
    while True:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(f"{mm:0>2}:{ss:0>2}")
        time.sleep(1)
        ss += 1
        if ss == 60:
            ss = 0
            mm += 1
        if mm == 60:
            mm = 0
    del time
    del os
    return

# -------------------------------------------
#               Lab 13 - Task 4
# -------------------------------------------

def lab13_task4_clear():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    del os
    return

def lab13_task4_kbhit():
    import os    
    if os.name == "nt":
        import msvcrt
        c = msvcrt.kbhit()
        del msvcrt
        return c
    else:
        import select
        import sys
        dr,dw,de = select.select([sys.stdin],[],[],0)
        del select
        del sys
        return dr != []

def lab13_task4_getch():
    import os
    if os.name == "nt":
        import msvcrt
        c = msvcrt.getch().decode("utf-8")
        del msvcrt
    else:
        import sys
        c = sys.stdin.read(1)
        del sys
    del os
    return c

def lab13_task4():
    task_header(13,4)
    import time
    ss = 0
    mm = 0
    paused = False
    while True:
        if not paused:
            lab13_task4_clear()
            print(f"{mm:0>2}:{ss:0>2}")
            time.sleep(1)
            ss += 1
            if ss == 60:
                ss = 0
                mm += 1
            if mm == 60:
                mm = 0
        if lab13_task4_kbhit():
            char = lab13_task4_getch()
            if char == "p" or char == "P":
                paused = True
            elif char == "s" or char == "S":
                paused = False
            elif char == "r" or char == "R":
                ss = 0
                mm = 0
            elif char == "q" or char == "Q":
                break
    del time
    return

# -------------------------------------------
#               Lab 14 - Task 1
# -------------------------------------------

def lab14_task1():
    task_header(14,1)
    print("*" * 70)
    print("1. Coffee\t2. Tea\t\t3. Coke\t\t4.Orange juice")
    print("*" * 70)
    print("This is a survey for the favorite beverage")
    print()
    print("Choose (1-4) from the above menu or 0 to exit the program")
    print()
    count = 0
    coffee_count = 0
    tea_count = 0
    coke_count = 0
    juice_count = 0
    while True:
        choice = eval(input(f"Please input the favorite beverage of person #{count + 1}: "))
        is_valid = False
        if choice == 0:
            break
        if choice >= 1 and choice <= 4:
            is_valid = True
        if is_valid:
            count += 1
            if choice == 1:
                coffee_count += 1
            elif choice == 2:
                tea_count += 1
            elif choice == 3:
                coke_count += 1
            else:
                juice_count += 1
        else:
            print("Error: Please enter a number in the range [1-4]")
    print()
    print("The results are as follows:")
    print(f"The total number of participants: {count}")
    print()
    print("Beverage\tNumber of votes")
    print("*" * 35)
    print(f"Coffee\t\t{coffee_count}")
    print(f"Tea\t\t{tea_count}")
    print(f"Coke\t\t{coke_count}")
    print(f"Orange juice\t{juice_count}")
    return

# -------------------------------------------
#               Lab 14 - Task 2
# -------------------------------------------

def lab14_task2_isPerfSq(x):
    import math
    squareroot = math.floor(math.sqrt(x))
    del math
    if squareroot ** 2 == x:
        return True
    else:
        return

def lab14_task2_isSqFree(x):
    for i in range(2, x + 1):
        if x % i == 0:
            if lab14_task2_isPerfSq(i):
                return False
    return True

def lab14_task2():
    task_header(14,2)
    n = eval(input("Enter a number: "))
    if lab14_task2_isSqFree(n):
        print(f"The number {n} is a square free number")
    else:
        print(f"The number {n} is not a square free number")
    return

# -------------------------------------------
#               Lab 14 - Task 3
# -------------------------------------------

def lab14_task3():
    task_header(14,3)
    n = eval(input("Enter a number: "))
    original = n
    reversed = 0
    while n != 0:
        d = n % 10
        n //= 10
        reversed = reversed * 10 + d
    if original == reversed:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
    return

# -------------------------------------------
#               Lab 14 - Task 4
# -------------------------------------------

def lab14_task4():
    task_header(14,4)
    for n in range(1,10000):
        original = n
        reversed = 0
        while n != 0:
            d = n % 10
            n //= 10
            reversed = reversed * 10 + d
        if original == reversed:
            print(f"{original}")
    return

# -------------------------------------------
#               Lab 14 - Task 5
# -------------------------------------------

def lab14_task5():
    task_header(14,5)
    while True:
        n = eval(input("Enter a number: "))
        is_valid = False
        chances = 3
        while not is_valid:
            if chances == 0:
                print("You failed 3 times")
                print("Good bye!")
                return
            s = eval(input("Enter a digit: "))
            if s >= 0 and s < 10:
                is_valid = True
            chances -= 1
        count = 0
        original = n
        while n != 0:
            d = n % 10
            n //= 10
            if d == s:
                count += 1
        print(f"Number of {s} in {original}: {count}")
        user_input = input("Repeat [y/n]: ").lower()
        if user_input == "n":
            break
        else:
            print()
    return

# -------------------------------------------
#               Lab 15 - Task 1
# -------------------------------------------

def lab15_task1():
    task_header(15,1)
    import random
    selected_number = random.randint(5,10)
    del random
    print("An integer is selected between 5 and 10 (both inclusive)")
    print()
    chances = 0
    while True:
        guessed_number = eval(input("Guess what is it: "))
        chances += 1
        if guessed_number == selected_number:
            print("Correct!")
            break
        else:
            print("Wrong!")
    print()
    print(f"You tried {chances} times to guess the number {selected_number}")
    return

# -------------------------------------------
#               Lab 15 - Task 2
# -------------------------------------------

def lab15_task2():
    task_header(15,2)
    import random
    selected_number = random.randint(0,100)
    del random
    print("An integer is selected between 0 and 100 (both inclusive)")
    print()
    chances = 0
    while True:
        guessed_number = eval(input("Guess what is it: "))
        chances += 1
        if guessed_number == selected_number:
            print("Correct!")
            break
        else:
            if guessed_number < selected_number:
                print(f"Hint: It is ABOVE {guessed_number}")
            else:
                print(f"Hint: It is BELOW {guessed_number}")
    print()
    print(f"You tried {chances} times to guess the number {selected_number}")
    return

# -------------------------------------------
#               Lab 15 - Task 3
# -------------------------------------------

def lab15_task3():
    task_header(15,3)
    trials = eval(input("Enter the number of trials: "))
    import random
    count = 0
    for trial in range(1, trials + 1):
        print()
        _ = input("[Press any key to roll dice]")
        dice_a = random.randint(1,6)
        dice_b = random.randint(1,6)
        dice_sum = dice_a + dice_b
        print(f"Trial: {trial} Dice A: {dice_a} Dice B: {dice_b} Sum: {dice_sum}")
        if dice_sum >= 7:
            count += 1
    print()
    print(f"The win condition occurred {count} times in {trials} trials")
    if count > (trials / 2):
        print("Congratulations: You won!")
    else:
        print("Sorry: You lost!")
    del random
    return

# -------------------------------------------
#               Lab 15 - Task 4
# -------------------------------------------

def lab15_task4():
    task_header(15,4)
    import random
    score = 0
    for _ in range(10):
        operand_a = random.randint(1,15)
        operand_b = random.randint(1,15)
        user_sum = eval(input(f"{operand_a} + {operand_b} = "))
        if user_sum == operand_a + operand_b:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print()
    print(f"Score: {score} out of 10")
    del random
    return

# -------------------------------------------
#               Lab 15 - Task 5
# -------------------------------------------

def lab15_task5():
    task_header(15,5)
    import random
    score = 0
    for _ in range(10):
        operand_a = random.randint(1,15)
        operand_b = random.randint(1,15)
        operation_index = random.randint(1,3)
        if operation_index == 1:
            operation_symbol = "+"
            solution = operand_a + operand_b
        elif operation_index == 2:
            operation_symbol = "-"
            solution = operand_a - operand_b
        else:
            operation_symbol = "*"
            solution = operand_a * operand_b
        user_sum = eval(input(f"{operand_a} {operation_symbol} {operand_b} = "))
        if user_sum == solution:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print()
    print(f"Score: {score} out of 10")
    del random
    return

# -------------------------------------------
#               Lab 15 - Task 6
# -------------------------------------------

def lab15_task6():
    task_header(15,6)
    import random
    for n in [10,100,1000,10000,100000]:
        count = 0
        for _ in range(n):
            dice_a = random.randint(1,6)
            dice_b = random.randint(1,6)
            if dice_a == dice_b:
                count += 1
        probability = count / n
        print(f"Iterations: {n}")
        print(f"\tProbability: {probability}")
    del random
    return

# -------------------------------------------
#               Lab 16 - Task 1
# -------------------------------------------

def lab16_task1():
    task_header(16,1)
    n = 10
    my_list = []
    import random
    for _ in range(n):
        my_list.append(random.randint(1,20))
    del random
    print(f"Generated list: {my_list}")
    element_sum = 0
    for i in range(len(my_list)):
        element_sum += my_list[i]
    average = element_sum / n
    print(f"Sum: {element_sum}\tAverage: {average:0.2f}")
    return

# -------------------------------------------
#               Lab 16 - Task 2
# -------------------------------------------

def lab16_task2():
    task_header(16,2)
    my_list = []
    n = 10
    import random
    for _ in range(n):
        my_list.append(random.randint(-20,20))
    print(f"Initial list:\t{my_list}")
    for i in range(len(my_list)):
        if my_list[i] > 10:
            my_list[i] = 10
        elif my_list[i] < 0:
            my_list[i] = 0
    print(f"Final list:\t{my_list}")
    del random
    return

# -------------------------------------------
#               Lab 16 - Task 3
# -------------------------------------------

def lab16_task3():
    task_header(16,3)
    my_list = []
    n = 10
    import random
    for _ in range(n):
        my_list.append(random.randint(2,100))
    del random
    print(f"List elements:\t\t{my_list}")
    import math
    count = 0
    prime_list = []
    for i in range(len(my_list)):
        isprime = True
        element = my_list[i]
        limit = int(math.sqrt(element)) + 1
        for j in range(2, limit):
            if element % j == 0:
                isprime = False
        if isprime:
            prime_list.append(element)
            count += 1
    print(f"Prime elements:\t\t{prime_list}")
    print(f"Number of primes:\t{count}")
    del math
    return

# -------------------------------------------
#               Lab 16 - Task 4
# -------------------------------------------

def lab16_task4_isprime(n):
    import math
    limit = int(math.sqrt(n)) + 1
    del math
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True
        
def lab16_task4():
    task_header(16,4)
    my_list = []
    n = 10
    import random
    for _ in range(n):
        my_list.append(random.randint(2,100))
    del random
    print(f"List elements:\t\t{my_list}")
    count = 0
    prime_list = []
    for i in range(len(my_list)):
        element = my_list[i]
        if lab16_task4_isprime(element):
            prime_list.append(element)
            count += 1
    print(f"Prime elements:\t\t{prime_list}")
    print(f"Number of primes:\t{count}")
    return

# -------------------------------------------
#               Lab 16 - Task 5
# -------------------------------------------

def lab16_task5():
    task_header(16,5)
    import random
    my_list = []
    n = 10
    for _ in range(n):
        my_list.append(random.randint(1,100))
    del random
    print(f"List elements: {my_list}")
    maximum = my_list[0]
    for i in range(1,len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]
    print(f"Maximum value: {maximum}")
    return

# -------------------------------------------
#               Lab 16 - Task 6
# -------------------------------------------

def lab16_task6():
    task_header(16,6)
    import random
    my_list = []
    n = 10
    for _ in range(n):
        my_list.append(random.randint(1,100))
    del random
    print(f"List elements: {my_list}")
    maximum = my_list[0]
    minimum = my_list[0]
    for i in range(1,len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]
        if my_list[i] < minimum:
            minimum = my_list[i]
    print(f"Maximum value: {maximum}")
    print(f"Minimum value: {minimum}")
    return

# -------------------------------------------
#               Lab 17 - Task 1
# -------------------------------------------

def lab17_task1_part1(l):
    max_value = max(l)
    index = l.index(max_value)
    return index

def lab17_task1_part2(l):
    sorted_list = sorted(l)
    index = sorted_list.index(7)
    return index

def lab17_task1_part3_approach1(l):
    sorted_list = sorted(l,reverse=True)
    index = sorted_list.index(7)
    return index

def lab17_task1_part3_approach2(l):
    sorted_list = sorted(l)
    index = sorted_list.index(7)
    repeated = l.count(7)
    count = len(l) - index - repeated
    return count

def lab17_task1_part4(l):
    sorted_list = sorted(l)
    number = sorted_list[-2]
    index = l.index(number)
    return index

def lab17_task1_part5(l):
    max_value = max(l)
    min_value = min(l)
    index = l.index(min_value)
    l[index] = max_value
    return l

def lab17_task1_print(l):
    print("Elements: [ ",end="")
    for i in range(len(l)):
        if i == len(l) - 1:
            separator = ""
        else:
            separator = ", "
        print(f"{l[i]:>-3}",end=separator)
    print("]")
    print("Indices:  [ ",end="")
    for i in range(len(l)):
        if i == len(l) - 1:
            separator = ""
        else:
            separator = ", "
        print(f"{i:>3}",end=separator)
    print("]")

def lab17_task1():
    task_header(17,1)
    a = [7,3,6,10,6,7,-2,7,5,-8,23,12,-22,3,6,-5,7,5,10,-20]
    lab17_task1_print(a)
    print(f"Index of  maximum number: {lab17_task1_part1(a)}")
    print(f"Count of numbers less than seven: {lab17_task1_part2(a)}")
    print(f"Count of numbers greater than seven (Approach 1): {lab17_task1_part3_approach1(a)}")
    print(f"Count of numbers greater than seven (Approach 2): {lab17_task1_part3_approach2(a)}")
    print(f"Index of second largest number: {lab17_task1_part4(a)}")
    print(f"Modified list: {lab17_task1_part5(a)}")
    return

# -------------------------------------------
#               Lab 17 - Task 2
# -------------------------------------------

def lab17_task2():
    task_header(17,2)
    l = list()
    while True:
        e = eval(input("Enter a number: "))
        if e == -1:
            break
        l.append(e)
    if len(l) == 0:
        print("Error: List is empty")
        return
    maximum = l[0]
    minimum = l[0]
    element_sum = 0
    for e in l:
        if e > maximum:
            maximum = e
        if e < minimum:
            minimum = e
        element_sum += e
    average = element_sum / len(l)
    print()
    print(f"Maximum value: {maximum}")
    print(f"Minimum value: {minimum}")
    print(f"Average value: {average:.2f}")
    return

# -------------------------------------------
#               Lab 17 - Task 3
# -------------------------------------------

def lab17_task3_isprime(n):
    import math
    limit = int(math.sqrt(n)) + 1
    del math
    for i in range(2,limit):
        if n % i == 0:
            return False
    return True

def lab17_task3():
    task_header(17,3)
    l = []
    n = 20
    import random
    for _ in range(n):
        l.append(random.randint(1,50))
    del random
    print(f"Randomly populated list: {l}")
    p = []
    for e in l:
        if lab17_task3_isprime(e):
            p.append(e)
    print(f"List of prime numbers:   {p}")
    return

# -------------------------------------------
#               Lab 17 - Task 4
# -------------------------------------------

def lab17_task4():
    task_header(17,4)
    marks = []
    print("This program displays the result of Computer Programming-I")
    n = eval(input("Enter total number of students in class: "))
    for i in range(n):
        marks.append(eval(input(f"Enter marks of roll no. {i + 1}: ")))
    average = sum(marks) / n
    failing_count = 0
    for mark in marks:
        if mark < 40:
            failing_count += 1
    highest_marks = max(marks)
    highest_roll = marks.index(highest_marks) + 1
    lowest_marks = min(marks)
    lowest_roll = marks.index(lowest_marks) + 1
    print()
    print("*************************************************")
    print("* Result of Computer Programming-I              *")
    print("*************************************************")
    print(f"* Average marks: {average:>4.2f}                           *")
    print(f"* Failing students: {failing_count}                           *")
    print(f"* Highest marks: {highest_marks} obtained by roll no. {highest_roll}       *")
    print(f"* Lowest marks: {lowest_marks} obtained by roll no. {lowest_roll}        *")
    print("*************************************************")
    return

# -------------------------------------------
#               Lab 17 - Task 5
# -------------------------------------------

def lab17_task5():
    task_header(17,5)
    List1 = []
    List2 = []
    import random
    for _ in range(20):
        List1.append(random.randint(1,10))
    del random
    for i in range(10):
        List2.append(List1.count(i + 1))
    print(f"List 1: {List1}")
    print(f"List 2: {List2}")
    return

# -------------------------------------------
#               Lab 17 - Task 6
# -------------------------------------------

def lab17_task6():
    task_header(17,6)
    n = eval(input("Enter an integer: "))
    limit = n // 2
    factors = []
    for i in range(2, limit):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    factors.insert(0,1)
    print(f"Factors: {factors}")
    return

# -------------------------------------------
#               Lab 17 - Task 7
# -------------------------------------------

def lab17_task7():
    task_header(17,7)
    my_list = []
    n = 10
    import random
    for _ in range(n):
        my_list.append(random.randint(1,50))
    del random
    print(f"Original list: {my_list}")
    last_value = my_list[-1]
    for i in range(-1, -len(my_list), -1):
        my_list[i] = my_list[i - 1]
    my_list[0] = last_value
    print(f"Rotated list:  {my_list}")
    return

# -------------------------------------------
#               Lab 17 - Task 8
# -------------------------------------------

def lab17_task8():
    task_header(17,8)
    binary_list = []
    n = 100
    import random
    for _ in range(n):
        binary_list.append(random.choice([0,1]))
    del random
    print(f"Binary list: {binary_list}")
    chain_count = 0
    maximum = 0
    for digit in binary_list:
        if digit == 0:
            chain_count += 1
        else:
            if chain_count > maximum:
                maximum = chain_count
            chain_count = 0
    print(f"Longest run of zeroes: {maximum}")
    return

# -------------------------------------------
#               Lab 17 - Task 9
# -------------------------------------------

def lab17_task9():
    task_header(17,9)
    my_list = []
    n = 20
    import random
    for _ in range(n):
        my_list.append(random.randint(1,50))
    del random
    print(f"Original list: {my_list}")
    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    print(f"Modified list: {new_list}")
    return

# -------------------------------------------
#               Lab 18 - Task 1
# -------------------------------------------

def lab18_task1_func(num_list):
    average = sum(num_list) / len(num_list)    
    lt_list = []
    eq_list = []
    gt_list = []
    for num in num_list:
        if num < average:
            lt_list.append(num)
        elif num == average:
            eq_list.append(num)
        else:
            gt_list.append(num)
    return average,lt_list,eq_list,gt_listn

def lab18_task1():
    task_header(18,1)
    num_list = []
    while True:
        user_input = input("Enter a number (enter space to quit): ")
        if user_input == " ":
            break
        num_list.append(eval(user_input))
    average, lt_list, eq_list, gt_list = lab18_task1_func(num_list)
    print()
    print(f"Average: {average}")
    print()
    print(f"Values less than average:    {lt_list}")
    print(f"Values exactly average:      {eq_list}")
    print(f"Values greater than average: {gt_list}")
    return

# -------------------------------------------
#               Lab 18 - Task 2
# -------------------------------------------

def lab18_task2_factors(n):
    factors = []
    limit = n // 2 + 1
    for i in range(2, limit):
        if n % i == 0:
            factors.append(i)
    factors.insert(0,1)
    factors.append(n)
    return factors

def lab18_task2():
    task_header(18,2)
    n = eval(input("Enter an integer: "))
    print(f"Factors: {lab18_task2_factors(n)}")
    return

# -------------------------------------------
#               Lab 18 - Task 3
# -------------------------------------------

def lab18_task3_isSorted(l):
    n = len(l)
    if n == 0:
        return True
    last = l[0]
    for i in range(1, n):
        current = l[i]
        if current < last:
            return False
        last = current
    return True

def lab18_task3():
    task_header(18,3)
    my_list = []
    while True:
        user_input = input("Enter a number (enter space to exit): ")
        if user_input == " ":
            break
        my_list.append(eval(user_input))
    print()
    print(f"List: {my_list}")
    if lab18_task3_isSorted(my_list):
        print("List is sorted")
    else:
        print("List is not sorted")
    return

# -------------------------------------------
#               Lab 18 - Task 4
# -------------------------------------------

def lab18_task4_bestOfTwo(l1,l2):
    n1 = len(l1)
    n2 = len(l2)
    if n1 > n2:
        longer_length = n1
        shorter_length = n2
        longer_list = l1
    else:
        longer_length = n2
        shorter_length = n1
        longer_list = l2
    bestOfTwo = []
    for i in range(shorter_length):
        if l1[i] > l2[i]:
            bestOfTwo.append(l1[i])
        else:
            bestOfTwo.append(l2[i])
    for i in range(shorter_length, longer_length):
        bestOfTwo.append(longer_list[i])
    return bestOfTwo

def lab18_task4():
    task_header(18,4)
    l1 = eval(input("Enter a list [x1,x2,x3,...]: "))
    l2 = eval(input("Enter a list [x1,x2,x3,...]: "))
    bestOfTwo = lab18_task4_bestOfTwo(l1,l2)
    print(f"Best of two: {bestOfTwo}")
    return

# -------------------------------------------
#               Lab 18 - Task 5
# -------------------------------------------

def lab18_task5_countRange(iterable,value,start,end):
    count = 0
    for index in range(start,end + 1):
        if iterable[index] == value:
            count += 1
    return count

def lab18_task5_randomList(size,low,high):
    randomList = []
    import random
    for _ in range(size):
        randomList.append(random.randint(low,high))
    del random
    return randomList

def lab18_task5():
    task_header(18,5)
    randomList = lab18_task5_randomList(20,1,10)
    print(f"Random list: {randomList}")
    print()
    value = eval(input("Value: "))
    start = eval(input("Start: "))
    end = eval(input("End: "))
    print()
    print(f"Count: {lab18_task5_countRange(randomList,value,start,end)}")
    return

# -------------------------------------------
#               Lab 18 - Task 6
# -------------------------------------------

def lab18_task6_dispList(container):
    size = len(container)
    if size == 0:
        text = ""
    elif size == 1:
        text = container[0]
    else:
        text = ""
        for index in range(size - 2):
            text = text + container[index] + ", "
        text = text + container[size - 2] + " and " + container[size - 1]
    return text

def lab18_task6():
    task_header(18,6)
    fruits = ["Apple","Banana","Orange","Pear","Mango"]
    print(f"List: {fruits}")
    print()
    for end in range(len(fruits) + 1):
        sublist = fruits[0:end]
        print(f"String: {lab18_task6_dispList(sublist)}")
    return

# -------------------------------------------
#               Lab 18 - Task 7
# -------------------------------------------

def lab18_task7():
    task_header(18,7)
    import random
    player1_score = 0
    player2_score = 0
    step = 0
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 > dice2:
            player1_score += (dice1 - dice2)
        elif dice2 > dice1:
            player2_score += (dice2 - dice1)
        else:
            player1_score = 0
            player2_score = 0  
        step += 1
        print()
        print(f"[{step}]\tDice A: {dice1} Dice B: {dice2}")
        print(f"[{step}]\tScore A: {player1_score} Score B: {player2_score}")
        if player1_score == 20:
            winner = "Player 1"
            break
        elif player2_score == 20:
            winner = "Player 2"
            break
    print()
    print(f"The winner is {winner}")
    del random
    return

# -------------------------------------------
#               Lab 19 - Task 1
# -------------------------------------------

def lab19_task1_maxSum(parent_list):
    highest_index = 0
    highest_sum = 0
    for element in parent_list[highest_index]:
        highest_sum += element
    for sublist_index in range(1, len(parent_list)):
        sum = 0
        sublist = parent_list[sublist_index]
        for element in sublist:
            sum += element
        if sum > highest_sum:
            highest_sum = sum
            highest_index = sublist_index
    return parent_list[highest_index]

def lab19_task1():
    task_header(19,1)
    parent_list = eval(input("Enter a list of sublists of numbers: "))
    print(lab19_task1_maxSum(parent_list))
    return

# -------------------------------------------
#               Lab 19 - Task 2
# -------------------------------------------

def lab19_task2_populate(n):
    l = []
    lowest = 0
    highest = 20
    import random
    for _ in range(n):
        l.append(random.randint(lowest,highest))
    del random
    return l

def lab19_task2():
    task_header(19,2)
    original_list = lab19_task2_populate(10)
    print(f"Original list: {original_list}")
    first_length = eval(input("Enter the length of the first part: "))
    first_part = original_list[0:first_length]
    second_part = original_list[first_length:]
    print(f"First part: {first_part}")
    print(f"Second part: {second_part}")
    return

# -------------------------------------------
#               Lab 19 - Task 3
# -------------------------------------------

def lab19_task3_splitList(a,n):
    nested_list = []
    sublist = []
    for index in range(0,len(a)):
        sublist.append(a[index])
        is_appended = False
        if (index + 1) % n == 0:
            nested_list.append(sublist)
            sublist = []
            is_appended = True
    if not is_appended:
        nested_list.append(sublist)
    return nested_list

def lab19_task3_populate(n):
    import random
    l = []
    lowest = 0
    highest = 50
    for _ in range(n):
        l.append(random.randint(lowest,highest))
    del random
    return l

def lab19_task3():
    task_header(19,3)
    a = lab19_task3_populate(20)
    n = eval(input("Enter the size of sublists: "))
    nested_list = lab19_task3_splitList(a,n)
    print(f"Nested list: {nested_list}")
    return

# -------------------------------------------
#               Lab 19 - Task 4
# -------------------------------------------

def lab19_task4_mergeSubLists(l1,l2):
    merged_list = []
    for i in range(len(l1)):
        sublist = []
        for j in l1[i]:
            sublist.append(j)
        for j in l2[i]:
            sublist.append(j)
        merged_list.append(sublist)
    return merged_list

def lab19_task4_populate(n):
    import random
    nested_list = []
    min_len = 1
    max_len = 5
    min_val = 0
    max_val = 50
    for _ in range(n):
        sublist = []
        sublist_length = random.randint(min_len,max_len)
        for _ in range(sublist_length):
            sublist.append(random.randint(min_val,max_val))
        nested_list.append(sublist)
    del random
    return nested_list

def lab19_task4():
    task_header(19,4)
    n = 5
    l1 = lab19_task4_populate(n)
    l2 = lab19_task4_populate(n)
    print(f"First list: {l1}")
    print(f"Second list: {l2}")
    merged_list = lab19_task4_mergeSubLists(l1,l2)
    print(f"Merged list: {merged_list}")
    return

# -------------------------------------------
#               Lab 19 - Task 5
# -------------------------------------------

def lab19_task5_get_subject_string(subject):
    if subject == 0:
        subject_str = "Calculus"
    elif subject == 1:
        subject_str = "Algebra"
    elif subject == 2:
        subject_str = "Programming"
    elif subject == 3:
        subject_str = "Electronics"
    elif subject == 4:
        subject_str = "Statistics"
    else:
        subject_str = "Undefined"
    return subject_str

def lab19_task5_get_subject_details(marks):
    subject_prompt = """Enter the subject for details:
    0 - Calculus
    1 - Algebra
    2 - Programming
    3 - Electronics
    4 - Statistics
>> """
    subject = eval(input(subject_prompt))
    max_marks = marks[0][subject]
    min_marks = marks[0][subject]
    marks_sum = marks[0][subject]
    max_index = 0
    min_index = 0
    n = len(marks)
    for i in range(1,n):
        subject_marks = marks[i][subject]
        marks_sum += subject_marks
        if subject_marks > max_marks:
            max_marks = subject_marks
            max_index = i
        if subject_marks < min_marks:
            min_marks = subject_marks
            min_index = i
    average = marks_sum / n
    subject_str = lab19_task5_get_subject_string(subject)
    print(f"Average marks for {subject_str}: {average:.2f}")
    print(f"Highest marks: {max_marks} obtained by roll no.: {max_index + 1}")
    print(f"Lowest marks: {min_marks} obtained by roll no.: {min_index + 1}")

def lab19_task5_get_student_details(marks):
    student = eval(input("Enter the roll number of the student: "))
    student_result = marks[student - 1]
    max_marks = student_result[0]
    min_marks = student_result[0]
    marks_sum = student_result[0]
    max_subject = 0
    min_subject = 0
    n = len(student_result)
    for i in range(1,n):
        subject_marks = student_result[i]
        marks_sum += subject_marks
        if subject_marks > max_marks:
            max_marks = subject_marks
            max_subject = i
        if subject_marks < min_marks:
            min_marks = subject_marks
            min_subject = i
    average = marks_sum / n
    max_subject_str = lab19_task5_get_subject_string(max_subject)
    min_subject_str = lab19_task5_get_subject_string(min_subject)
    print(f"Average marks for roll no. {student}: {average:.2f}")
    print(f"Highest marks: {max_marks} in subject {max_subject_str}")
    print(f"Lowest marks: {min_marks} in subject {min_subject_str}")

def lab19_task5():
    task_header(19,5)
    marks = [[89,91,68,88,93],
            [78,79,87,78,67],
            [94,83,69,79,82],
            [67,78,77,82,66],
            [88,82,87,77,69],
            [93,55,90,82,67],
            [76,69,86,75,94],
            [66,77,67,64,83],
            [82,79,83,71,68],
            [59,83,88,84,79]]
    option_prompt = """Enter the category for details:
    \"s\" or \"S\" - Subject
    \"r\" or \"R\" - Student
>> """
    while True:
        option = input(option_prompt)
        if option.lower() == "s":
            lab19_task5_get_subject_details(marks)
        elif option.lower() == "r":
            lab19_task5_get_student_details(marks)
        else:
            print("Error: Invalid option")
        print()
        option = input("Repeat for another query (y/n): ")
        if option.lower() == "n":
            break
        print()
    return

# -------------------------------------------
#               Lab 19 - Task 6
# -------------------------------------------

def lab19_task6_det2(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return det

def lab19_task6_det3(A):
    sm1 = [A[1][1],A[1][2]],[A[2][1],A[2][2]]
    sm2 = [A[1][0],A[1][2]],[A[2][0],A[2][2]]
    sm3 = [A[1][0],A[1][1]],[A[2][0],A[2][1]]
    c1 = A[0][0]
    c2 = A[0][1]
    c3 = A[0][2]
    det = c1 * lab19_task6_det2(sm1) - c2 * lab19_task6_det2(sm2) + c3 * lab19_task6_det2(sm3)
    return det

def lab19_task6_print(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:<6}",end="")
        print()
    print()
    return

def lab19_task6():
    task_header(19,6)
    import random
    matrix = []
    n = 3
    low = 1
    high = 9
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.randint(low,high))
        matrix.append(row)
    del random
    lab19_task6_print(matrix)
    print(f"Determinant: {lab19_task6_det3(matrix)}")
    return

# -------------------------------------------
#               Lab 19 - Task 7
# -------------------------------------------

def lab19_task7_det2(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return det

def lab19_task7_inv2(A):
    det = lab19_task7_det2(A)
    inv_det = 1 / det
    inverse = [inv_det * A[1][1],-inv_det * A[0][1]],[-inv_det * A[1][0],inv_det * A[0][0]]
    return inverse

def lab19_task7_dispMat(A,name):
    print(f"{name}:")
    for row in A:
        for element in row:
            print(f"{element:< 6.2f}",end=" ")
        print()
    print()
    return

def lab19_task7_populate(n):
    import random
    matrix = []
    low = 1
    high = 9
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.randint(low,high))
        matrix.append(row)
    del random
    return matrix

def lab19_task7():
    task_header(19,7)
    n = 2
    matrix = lab19_task7_populate(n)
    lab19_task7_dispMat(matrix,"Matrix")
    inverse = lab19_task7_inv2(matrix)
    lab19_task7_dispMat(inverse,"Inverse")
    return

# -------------------------------------------
#               Lab 19 - Task 8
# -------------------------------------------

def lab19_task8_displayGrid(grid):
    print("-----------------------------------")
    print("            Tic Tac Toe")
    print("-----------------------------------")
    print()
    print("Player 1 [X]           Player 2 [O]")
    print()
    print(f"           {grid[0][0]}  |  {grid[0][1]}  |  {grid[0][2]}")
    print("         -----+-----+-----")
    print(f"           {grid[1][0]}  |  {grid[1][1]}  |  {grid[1][2]}")
    print("         -----+-----+-----")
    print(f"           {grid[2][0]}  |  {grid[2][1]}  |  {grid[2][2]}")
    print()

def lab19_task8_clear():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    del os
    return

def lab19_task8_fillSlot(grid,slot,mark):
    column = (slot % 3) - 1
    row = (slot - 1) // 3
    if(grid[row][column] not in [1,2,3,4,5,6,7,8,9]):
        return False
    grid[row][column] = mark
    return True

def lab19_task8_playerTurn(grid,player):
    if player == 1:
        mark = "X"
    else:
        mark = "O"
    success = False
    while not success:
        slot = eval(input(f"[Player {player}] Enter the slot number: "))
        success = lab19_task8_fillSlot(grid,slot,mark)
        if success == False:
            print("Error: Invalid slot number - Please try again!")
    return

def lab19_task8_isWinner(grid):
    if  grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] or \
        grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] or \
        grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] or \
        grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] or \
        grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] or \
        grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] or \
        grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] or \
        grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return True
    return False

def lab19_task8_gameEnd(code):
    if code == 1:
        print("Congratulations! Player 1 won")
    elif code == 2:
        print("Congratulations! Player 2 won")
    else:
        print("Draw! No one won")

def lab19_task8():
    task_header(19,8)
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    max_turns = 9
    turn = 0
    player = 1
    while turn < max_turns:
        lab19_task8_clear()
        lab19_task8_displayGrid(grid)
        lab19_task8_playerTurn(grid,player)
        if lab19_task8_isWinner(grid):
            lab19_task8_clear()
            lab19_task8_displayGrid(grid)
            lab19_task8_gameEnd(player)
            break
        turn += 1
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        lab19_task8_clear()
        lab19_task8_displayGrid(grid)
        lab19_task8_gameEnd(0)
    return

# -------------------------------------------
#               Lab 20 - Task 1
# -------------------------------------------

def lab20_task1_polyPerimeter(polygon):
    import math
    perimeter = 0
    vertices = len(polygon)
    for i in range(vertices):
        if i == vertices - 1:
            j = 0
        else:
            j = i + 1
        x1,y1 = polygon[i]
        x2,y2 = polygon[j]
        perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    del math
    return perimeter

def lab20_task1():
    task_header(20,1)
    polygon = []
    vertices = eval(input("Enter the number of vertices: "))
    for i in range(vertices):
        if i == 0:
            postfix = "st"
        elif i == 1:
            postfix = "nd"
        elif i == 2:
            postfix = "rd"
        else:
            postfix = "th"
        point = eval(input(f"Enter the {i + 1}{postfix} point (x,y): "))
        polygon.append(point)
    perimeter = lab20_task1_polyPerimeter(polygon)
    print(f"Perimeter: {perimeter:.2f}")
    return

# -------------------------------------------
#               Lab 20 - Task 2
# -------------------------------------------

def lab20_task2():
    task_header(20,2)
    students = [("Ahmad","Anwar","MCT-UET-01",["CP","LA"]),
                ("Ali","Jamal","MCT-UET-02",["LA"]),
                ("Muneeb","Akhtar","MCT-UET-03",["Phy","CP","LA"]),
                ("Rizwan","Khan","MCT-UET-04",["Statistics","Phy"])]
    cp_students = []
    tc_students = []
    for student in students:
        first_name,last_name,reg_id,courses = student
        if "CP" in courses:
            cp_students.append(reg_id)
        if len(courses) == 3:
            full_name = first_name,last_name
            tc_students.append(full_name)
    print(f"Registration numbers of the students registered in the course CP:")
    for reg_id in cp_students:
        print(reg_id)
    print()
    print(f"Full names of the students registered in exactly 3 courses:")
    for full_name in tc_students:
        first_name,last_name = full_name
        print(f"{first_name} {last_name}")
    return

# -------------------------------------------
#            Auxiliary Functions
# -------------------------------------------

def task_header(lab_number, task_number):
    print()
    print("-------------------------------------------")
    print(f"              Lab {lab_number} - Task {task_number}")
    print("-------------------------------------------")
    print()
    return

def run_all():
    tasks =[
    "lab1_task1","lab1_task2","lab1_task3",
    "lab2_task1","lab2_task2","lab2_task3","lab2_task4","lab2_task5","lab2_task6","lab2_task7"
    "lab3_task1","lab3_task2","lab3_task3",
    "lab4_task1","lab4_task2","lab4_task3","lab4_task4","lab4_task5","lab4_task6",
    "lab5_task1","lab5_task2","lab5_task3","lab5_task4","lab5_task5","lab5_task6","lab5_task7","lab5_task8","lab5_task9","lab5_task10","lab5_task11",
    "lab6_task1","lab6_task2","lab6_task3","lab6_task4","lab6_task5","lab6_task6",
    "lab7_task1","lab7_task2","lab7_task3","lab7_task4","lab7_task5",
    "lab8_task1","lab8_task2","lab8_task3",
    "lab9_task1","lab9_task2","lab9_task3","lab9_task4","lab9_task5","lab9_task6","lab9_task7","lab9_task8","lab9_task9","lab9_task10",
    ]
    for task in tasks:
        globals()[task]()
    return

def run_specific():
    lab_number, task_number = eval(input("\n>> Lab number and task number (lab, task): "))
    globals()[f"lab{lab_number}_task{task_number}"]()
    return

def list_all():
    v_bar = "│"
    h_bar = "─"
    joint = "├"
    elbow = "└"
    
    # TODO: Print a tree like structure
    # that shows all the available tasks for each lab session

def loop():
    prompt = """
--------------------------------------------------------
    [a] - Press A to run all tasks with dummy input
    [n] - Press N to run a specific task
    [h] - List all available tasks
    [q] - Press Q to quit the program
--------------------------------------------------------

    """
    
    while True:
        print(prompt)
        user_input = input(">> ")
        if user_input.lower() == "a":
            run_all()
        elif user_input.lower() == "n":
            run_specific()
        elif user_input.lower() == "h":
            list_all()
        elif user_input.lower() == "q":
            break
        else:
            print("Error: Invalid option")
            return

# -------------------------------------------
#               Program Start
# -------------------------------------------

if __name__ == "__main__":
    loop()