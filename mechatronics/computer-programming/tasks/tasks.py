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
    for i in range(2,sqrt_n):
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
#            Auxiliary Function
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
    lab_number = eval(input("\nLab number: "))
    task_number = eval(input("Task number: "))
    globals()[f"lab{lab_number}_task{task_number}"]()
    return

def main():
    print("-------------------------------------------")
    print("   [a] - Press A to run all the tasks")
    print("   [n] - Press N to run a specific task")
    print("   [q] - Press Q to quit the program")
    print("-------------------------------------------")
    user_input = input(">> ")
    if user_input == "q" or user_input == "Q":
        return
    elif user_input == "a" or user_input == "A":
        run_all()
    elif user_input == "n" or user_input == "N":
        run_specific()
    else:
        print("Error: Invalid option")
        return

# -------------------------------------------
#               Program Start
# -------------------------------------------

if __name__ == "__main__":
    main()