#############################################
# Author:       Yahya Mateen                #
# Reg. ID:      2019-R/2018-MC-71           #
# Course:       Computer Programming-II     #
# Teacher:      Mr. Ahsan Naeem             #
#############################################

# -------------------------------------------
#               Module Imports
# -------------------------------------------

import math
import os
import sys
import time
import random
import string
import io
import requests
import json

from functools import lru_cache,reduce,total_ordering

if os.name == "nt":
    import msvcrt
else:
    import select

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
    print("This program calculates the area and volume of a sphere.")
    radius = eval(input("Enter the radius: "))
    print(f"Area of the sphere is A: {4 * math.pi * radius ** 2}")
    print(f"Volume of the sphere is V: {(4 / 3) * math.pi * radius ** 3}")
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
    complex_number = complex(input("Enter a complex number: "))
    magnitude = math.sqrt(complex_number.real ** 2 + complex_number.imag ** 2)
    print(f"The magnitude of the complex number is: {magnitude:.2f}")
    return

# -------------------------------------------
#               Lab 4 - Task 5
# -------------------------------------------

def lab4_task5():
    task_header(4,5)
    complex_number = complex(input("Enter a complex number: "))
    magnitude_squared = complex_number * complex_number.conjugate()
    magnitude = math.sqrt(magnitude_squared.real)
    print(f"The magnitude of the complex number is: {magnitude:.2f}")
    return

# -------------------------------------------
#               Lab 4 - Task 6
# -------------------------------------------

def lab4_task6():
    task_header(4,6)
    vector = complex(input("Enter a vector (as a complex number): "))
    magnitude_squared = vector * vector.conjugate()
    magnitude = math.sqrt(magnitude_squared.real)
    unit_real = vector.real / magnitude
    unit_imag = vector.imag / magnitude
    print(f"The unit vector is: ({unit_real:.2f}{unit_imag:+.2f}j)")
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
    number = eval(input("Enter a number: "))
    if number < 0:
        square_root = complex(0,round(math.sqrt(abs(number)),2))
    else:
        square_root = round(math.sqrt(number),2)
    print(f"The square root of {number} is {square_root}")
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
    number = eval(input("Enter a number: "))
    square_root = math.sqrt(number)
    squared_square_root = square_root * square_root
    if number == squared_square_root:
        print(f"The number {number} is a perfect square")
    else:
        print(f"The number {number} is not a perfect square")
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
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
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
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
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
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return distance

def lab8_task1_triAreaSides(a,b,c):
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
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
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return distance

def lab8_task2_triAreaSides(a,b,c):
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
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
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return distance

def lab8_task3_triAreaSides(a,b,c):
    s = 0.5 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
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
    sqrt_n = math.ceil(math.sqrt(n))
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
    return

# -------------------------------------------
#               Lab 11 - Task 5
# -------------------------------------------

def lab11_task5_isprime(n):
    limit = math.ceil(math.sqrt(n)) + 1
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
    limit = math.ceil(math.sqrt(n)) + 1
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
    limit = math.ceil(math.sqrt(n)) + 1
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
    limit = math.ceil(math.sqrt(n)) + 1
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
    return

# -------------------------------------------
#               Lab 13 - Task 4
# -------------------------------------------

def lab13_task4_clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    return

def lab13_task4_kbhit():
    if os.name == "nt":
        c = msvcrt.kbhit()
        return c
    else:
        dr,dw,de = select.select([sys.stdin],[],[],0)
        return dr != []

def lab13_task4_getch():
    if os.name == "nt":
        c = msvcrt.getch().decode("utf-8")
    else:
        c = sys.stdin.read(1)
    return c

def lab13_task4():
    task_header(13,4)
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
    squareroot = math.floor(math.sqrt(x))
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
    selected_number = random.randint(5,10)
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
    selected_number = random.randint(0,100)
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
    return

# -------------------------------------------
#               Lab 15 - Task 4
# -------------------------------------------

def lab15_task4():
    task_header(15,4)
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
    return

# -------------------------------------------
#               Lab 15 - Task 5
# -------------------------------------------

def lab15_task5():
    task_header(15,5)
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
    return

# -------------------------------------------
#               Lab 15 - Task 6
# -------------------------------------------

def lab15_task6():
    task_header(15,6)
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
    return

# -------------------------------------------
#               Lab 16 - Task 1
# -------------------------------------------

def lab16_task1():
    task_header(16,1)
    n = 10
    my_list = []
    for _ in range(n):
        my_list.append(random.randint(1,20))
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
    for _ in range(n):
        my_list.append(random.randint(-20,20))
    print(f"Initial list:\t{my_list}")
    for i in range(len(my_list)):
        if my_list[i] > 10:
            my_list[i] = 10
        elif my_list[i] < 0:
            my_list[i] = 0
    print(f"Final list:\t{my_list}")
    return

# -------------------------------------------
#               Lab 16 - Task 3
# -------------------------------------------

def lab16_task3():
    task_header(16,3)
    my_list = []
    n = 10
    for _ in range(n):
        my_list.append(random.randint(2,100))
    print(f"List elements:\t\t{my_list}")
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
    return

# -------------------------------------------
#               Lab 16 - Task 4
# -------------------------------------------

def lab16_task4_isprime(n):
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True
        
def lab16_task4():
    task_header(16,4)
    my_list = []
    n = 10
    for _ in range(n):
        my_list.append(random.randint(2,100))
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
    my_list = []
    n = 10
    for _ in range(n):
        my_list.append(random.randint(1,100))
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
    my_list = []
    n = 10
    for _ in range(n):
        my_list.append(random.randint(1,100))
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
    limit = int(math.sqrt(n)) + 1
    for i in range(2,limit):
        if n % i == 0:
            return False
    return True

def lab17_task3():
    task_header(17,3)
    l = []
    n = 20
    for _ in range(n):
        l.append(random.randint(1,50))
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
    for _ in range(20):
        List1.append(random.randint(1,10))
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
    for _ in range(n):
        my_list.append(random.randint(1,50))
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
    for _ in range(n):
        binary_list.append(random.choice([0,1]))
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
    for _ in range(n):
        my_list.append(random.randint(1,50))
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
    for _ in range(size):
        randomList.append(random.randint(low,high))
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
    for _ in range(n):
        l.append(random.randint(lowest,highest))
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
    l = []
    lowest = 0
    highest = 50
    for _ in range(n):
        l.append(random.randint(lowest,highest))
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
    matrix = []
    n = 3
    low = 1
    high = 9
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.randint(low,high))
        matrix.append(row)
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
    matrix = []
    low = 1
    high = 9
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.randint(low,high))
        matrix.append(row)
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
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
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
#               Lab 21 - Task 1
# -------------------------------------------

def lab21_task1():
    task_header(21,1)
    n = eval(input("Enter an integer: "))
    factors = [i for i in range(1,n + 1) if n % i == 0]
    print(f"factors: {factors}")
    return

# -------------------------------------------
#               Lab 21 - Task 2
# -------------------------------------------

def lab21_task2():
    task_header(21,2)
    nums = [i for i in range(15)]
    squared_nums = [i * i for i in nums if i % 2 == 0]
    print(f"nums: {nums}")
    print(f"squared_nums: {squared_nums}")
    return

# -------------------------------------------
#               Lab 21 - Task 3
# -------------------------------------------

def lab21_task3():
    task_header(21,3)
    nested_list = [[4,3,-2,0,1],[6,8,2,9],[5,3,4,-7],[2,9]]
    print(f"nested_list: {nested_list}")
    sum_list = [sum(inner_list) for inner_list in nested_list]
    print(f"sum_list: {sum_list}")
    return

# -------------------------------------------
#               Lab 21 - Task 4
# -------------------------------------------

def lab21_task4():
    task_header(21,4)
    s1 = ('Ahmad','Anwar','MCT-UET-01',['CP','LA'])
    s2 = ('Ali','Jamal','MCT-UET-02',['LA'])
    s3 = ('Muneeb','Akhtar','MCT-UET-03',['Phy','CP','LA'])
    s4 = ('Rizwan','Khan','MCT-UET-04',['Statistics','Phy'])
    s5 = ('Akhtar','Hussain','MCT-UET-05',['Phy','LA'])
    s6 = ('Nasir','Saeed','MCT-UET-06',['Phy','Statistics','LA'])
    s7 = ('Bilal','Akram','MCT-UET-07',['Hist','CP','LA'])
    s8 = ('Hamid','Salman','MCT-UET-08',['CP','Phy'])
    s9 = ('Naveed','Majeed','MCT-UET-09',['CP','LA','Hist'])
    s10 = ('Kashif','Lateef','MCT-UET-10',['LA','Phy','Hist'])
    all_students = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    cp_students = [s[2] for s in all_students if "CP" in s[3]]
    three_courses = [f"{s[0]} {s[1]}" for s in all_students if len(s[3]) == 3]
    courses_count = [len(s[3]) for s in all_students]
    print("-------------------------------------------")
    for student in all_students:
        print(student)
    print("-------------------------------------------")
    print(f"cp_students: {cp_students}")
    print(f"three_courses: {three_courses}")
    print(f"courses_count: {courses_count}")
    return

# -------------------------------------------
#               Lab 21 - Task 5
# -------------------------------------------

def lab21_task5_mag(x,y):
    return math.sqrt(x ** 2 + y ** 2)

def lab21_task5():
    task_header(21,5)
    mag = lab21_task5_mag
    x = [1,-1,5,0,3,10,5,-4]
    y = [2,-1,7,4,10,4,0,-5]
    points = [(i,j) for (i,j) in zip(x,y) if mag(i,j) <= 3]
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"points: {points}")
    return

# -------------------------------------------
#               Lab 21 - Task 6
# -------------------------------------------

def lab21_task6():
    task_header(21,6)
    points = [(1, 2),(-1, -1),(5, 7),(0, 4),(3, 10),(10, 4),(5, 0),(-4, -5)]
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    print(f"points: {points}")
    print(f"x: {x}")
    print(f"y: {y}")
    return

# -------------------------------------------
#               Lab 21 - Task 7
# -------------------------------------------

def lab21_task7():
    task_header(21,7)
    s1 = ('Ahmad','Anwar','MCT-UET-01',['CP','LA'])
    s2 = ('Ali','Jamal','MCT-UET-02',['LA'])
    s3 = ('Muneeb','Akhtar','MCT-UET-03',['Phy','CP','LA'])
    s4 = ('Rizwan','Khan','MCT-UET-04',['Statistics','Phy'])
    s5 = ('Akhtar','Hussain','MCT-UET-05',['Phy','LA'])
    s6 = ('Nasir','Saeed','MCT-UET-06',['Phy','Statistics','LA'])
    s7 = ('Bilal','Akram','MCT-UET-07',['Hist','CP','LA'])
    s8 = ('Hamid','Salman','MCT-UET-08',['CP','Phy'])
    s9 = ('Naveed','Majeed','MCT-UET-09',['CP','LA','Hist'])
    s10 = ('Kashif','Lateef','MCT-UET-10',['LA','Phy','Hist'])
    all_students = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    subjects = [subject for student in all_students for subject in student[3]]
    print("-------------------------------------------")
    for student in all_students:
        print(student)
    print("-------------------------------------------")
    print(f"subjects (with duplicates): {subjects}")
    subjects = list(set(subjects))
    print(f"subjects (no duplicates): {subjects}")    
    return

# -------------------------------------------
#               Lab 21 - Task 8
# -------------------------------------------

def lab21_task8_mag(i,j,k):
    return math.sqrt(i ** 2 + j ** 2 + k ** 2)

def lab21_task8():
    task_header(21,8)
    mag = lab21_task8_mag
    x = [round(10 * random.random(),2) for _ in range(10)]
    y = [round(10 * random.random(),2) for _ in range(10)]
    z = [round(10 * random.random(),2) for _ in range(10)]
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    points = [(i,j,k) for (i,j,k) in zip(x,y,z) if j >= 0 and mag(i,j,k) <= 10]
    print(f"points: {points}")
    return

# -------------------------------------------
#               Lab 22 - Task 1
# -------------------------------------------

def lab22_task1():
    task_header(22,1)
    user_string = input("Enter a message: ")
    vowels = "aeiou"
    vowels_count = 0
    for char in user_string:
        if char.lower() in vowels:
            vowels_count += 1
    print(f"There are {vowels_count} vowels in the entered message")
    return

# -------------------------------------------
#               Lab 22 - Task 2
# -------------------------------------------

def lab22_task2():
    task_header(22,2)
    user_string = input("Enter a message: ")
    words_count = 0
    for char in user_string:
        if char.lower().isspace():
            words_count += 1
    print(f"There are {words_count + 1} words in the entered message")
    return

# -------------------------------------------
#               Lab 22 - Task 3
# -------------------------------------------

def lab22_task3():
    task_header(22,3)
    user_string = input("Enter a message: ")
    words = user_string.split(" ")
    count = 0
    for word in words:
        if len(word) == 4:
            count += 1
    print(f"There are {count} words with exactly 4 letters")
    return

# -------------------------------------------
#               Lab 22 - Task 4
# -------------------------------------------

def lab22_task4():
    task_header(22,4)
    word = input("Enter a word: ")
    letters = list(word)
    random.shuffle(letters)
    shuffled_word = "".join(letters)
    print(f"Shuffled word: {shuffled_word}")
    return

# -------------------------------------------
#               Lab 22 - Task 5
# -------------------------------------------

def lab22_task5_prologue(checks):
    print("-------------------------------------------------------------")
    print("            Enter a strong password - [q] to quit            ")
    print("-------------------------------------------------------------")
    print(f"  [{checks[0]}] Password must be between 8 and 32 characters           ")
    print(f"  [{checks[1]}] Password must contain at least one lowercase letter    ")
    print(f"  [{checks[2]}] Password must contain at least one uppercase letter    ")
    print(f"  [{checks[3]}] Password must contain at least one numeric digit       ")
    print(f"  [{checks[4]}] Password must contain at least one special character   ")
    print("-------------------------------------------------------------")

def lab22_task5():
    task_header(22,5)
    password_weak = True
    islong,haslower,hasupper,hasnumeric,hasspecial = False,False,False,False,False
    while password_weak:
        os.system("cls" if os.name == "nt" else "clear")
        checks = [
                "\u2713" if islong else "x",
                "\u2713" if haslower else "x",
                "\u2713" if hasupper else "x",
                "\u2713" if hasnumeric else "x",
                "\u2713" if hasspecial else "x"
        ]
        lab22_task5_prologue(checks)
        password = input("\n>> ")
        if password == "q":
            break
        islong,haslower,hasupper,hasnumeric,hasspecial = False,False,False,False,False
        if len(password) > 8 and len(password) < 32:
            islong = True
        for character in password:
            if character.islower():
                haslower = True
            elif character.isupper():
                hasupper = True
            elif character.isdecimal():
                hasnumeric = True
            elif character in string.punctuation:
                hasspecial = True
        if islong and haslower and hasupper and hasnumeric and hasspecial:
            password_weak = False
        else:
            password_weak = True
    return


# -------------------------------------------
#               Lab 22 - Task 6
# -------------------------------------------

def lab22_task6_extract(player):
    player = player.strip()
    raw = player.split(":")
    name = raw[0].strip()
    score = raw[1].split("-")
    overs = float(score[0].strip())
    maidens = float(score[1].strip())
    runs = float(score[2].strip())
    wickets = float(score[3].strip())
    return name,overs,maidens,runs,wickets

def lab22_task6_reference(players):
    r_player = players[0]
    r_overs = r_player[1]
    r_runs = r_player[3]
    r_economy = r_runs / r_overs
    return r_player[0],r_economy,r_player[2],r_player[4]

def lab22_task6():
    task_header(22,6)
    bowling = """Wasim Akram : 10-0-49-3
                Aaqib Javed: 10- 2-27-2
                Mushtaq Ahmed:10- 1-41-3
                Ijaz Ahmed:3-0-13-0
                Imran Khan:6.2-0-43- 1
                Aamer Sohail : 10-0-49 -0"""
    players = [lab22_task6_extract(player) for player in bowling.split("\n")]
    r_name,r_economy,r_maidens,r_wickets = lab22_task6_reference(players)
    best_economy = [r_economy,r_name]
    most_wickets = [r_wickets,r_name]
    total_maidens = r_maidens
    for index in range(1,len(players)):
        name,overs,maidens,runs,wickets = players[index]
        economy = runs / overs
        if economy < best_economy[0]:
            best_economy = [economy,name]
        total_maidens += maidens
        if wickets > most_wickets[0]:
            most_wickets = [wickets,name]
    print(f"Bowler with the best economy: {best_economy[1]}")
    print(f"Total maiden overs bowled by Pakistan: {total_maidens}")
    print(f"Bowlers who took the best wickets: {most_wickets[1]}")
    return

# -------------------------------------------
#               Lab 22 - Task 7
# -------------------------------------------

def lab22_task7_randomDNA(n):
    dna = []
    nucleotides = ["A","T","C","G"]
    for _ in range(n):
        dna.append(random.choice(nucleotides))
    return dna

def lab22_task7_ATContent(dna):
    a_content = 0
    t_content = 0
    for nucleotide in dna:
        if nucleotide.upper() == "A":
            a_content += 1
        elif nucleotide.upper() == "T":
            t_content += 1
    at_content = a_content / t_content
    return at_content

def lab22_task7_reverseComplement(dna):
    complement = []
    for nucleotide in dna:
        if nucleotide.upper() == "A":
            complement.append("T")
        elif nucleotide.upper() == "T":
            complement.append("A")
        elif nucleotide.upper() == "C":
            complement.append("G")
        elif nucleotide.upper() == "G":
            complement.append("C")
        else:
            print("Error: Unexpected nucleotide detected")
    return complement

def lab22_task7():
    task_header(22,7)
    n = 20
    dna = lab22_task7_randomDNA(n)
    at_content = lab22_task7_ATContent(dna) * 100
    complement = lab22_task7_reverseComplement(dna)
    print(f"DNA sequence:       {dna}")
    print(f"Reverse complement: {complement}")
    print(f"AT content:         {at_content} %")
    return

# -------------------------------------------
#               Lab 23 - Task 1
# -------------------------------------------

def lab23_task1_populate(n,min_v,max_v):
    l = []
    for _ in range(n):
        l.append(random.randint(min_v,max_v))
    return l

def lab23_task1_findMax(l):
    high_v = l[0]
    for i in range(1,len(l)):
        if l[i] > high_v:
            high_v = l[i]
    return high_v

def lab23_task1():
    task_header(23,1)
    n = 20
    min_v = 0
    max_v = 10
    l = lab23_task1_populate(n,min_v,max_v)
    print(f"List with duplicates:    {l}")
    l = list(set(l))
    print(f"List without duplicates: {l}")
    high_v = lab23_task1_findMax(l)
    print(f"Highest value:           {high_v}")
    l.remove(high_v)
    high_v = lab23_task1_findMax(l)
    print(f"Second highest value:    {high_v}")
    return

# -------------------------------------------
#               Lab 23 - Task 2
# -------------------------------------------

def lab23_task2_populate(max_n,max_v):
    l = []
    n = random.randint(5,max_n)
    for _ in range(n):
        l.append(random.randint(0,max_v))
    return l

def lab23_task2():
    task_header(23,2)
    a = lab23_task2_populate(20,20)
    b = lab23_task2_populate(20,20)
    print(f"List A:               {a}")
    print(f"List B:               {b}")
    a.remove(a[0])
    a.remove(a[-1])
    print(f"Special intersection: {set(a).intersection(b)}")
    return

# -------------------------------------------
#               Lab 24 - Task 1
# -------------------------------------------

def lab24_task1_displayDictionary(dictionary,key_name,val_name):
    print()
    print("--------------------------")
    print(f"        {key_name}  |  {val_name}      ")
    print("--------------------------")
    for key,value in dictionary.items():
        print(f"{key:>12}  |  {value:<12}")
    print("--------------------------")
    print()
    return

def lab24_task1():
    task_header(24,1)
    products={'walnuts':1500,'cashew':1800,'almond':2000,'pine nuts':8000}
    while True:
        mode = eval(input("""
-----------------------------------------------
    Select one of the following mode
-----------------------------------------------
    [1] Display the rate of a product
    [2] Add or update a product price
    [3] Generate bill for purchased products
    [4] Quit the program
-----------------------------------------------

>> """))
        if mode == 1:
            product_name = input("\nEnter the product name: ")
            product_price = products.get(product_name)
            if product_price == None:
                print(f"Sorry! There is no record for {product_name}")
            else:
                print(f"The unit price of {product_name} is PKR {product_price}")
        elif mode == 2:
            product_name = input("\nEnter the product name: ")
            product_price = eval(input("Enter the product price: "))
            products.update({product_name:product_price})
            lab24_task1_displayDictionary(products,"Name","Rate")
        elif mode == 3:
            bill = {}
            while True:
                product_name = input("\nEnter the product name - enter [q] to quit: ")
                if product_name.lower() == "q":
                    break
                product_amount = eval(input("Enter the amount purchased: "))
                bill.update({product_name:product_amount})
                print()
            lab24_task1_displayDictionary(bill,"Name","Amount")
            bill_amount = 0
            for name,amount in bill.items():
                rate = products.get(name)
                if rate != None:
                    bill_amount += rate * amount
            print(f"Bill: PKR {bill_amount}")
        elif mode == 4:
            break
        else:
            print("Error: Invalid mode")
    return

# -------------------------------------------
#               Lab 24 - Task 2
# -------------------------------------------

def lab24_task2_displayDictionary(dictionary,key_name,val_name):
    print()
    print("--------------------------")
    print(f"        {key_name}  |  {val_name}      ")
    print("--------------------------")
    for key,value in dictionary.items():
        print(f"{key:>12}  |  {value:<12}")
    print("--------------------------")
    print()
    return

def lab24_task2_mode1(products):
    product_name = input("\nEnter the product name: ")
    product_price = products.get(product_name)
    if product_price == None:
        print(f"Sorry! There is no record for {product_name}")
    else:
        print(f"The unit price of {product_name} is PKR {product_price}")
    return

def lab24_task2_mode2(products):
    product_name = input("\nEnter the product name: ")
    product_price = eval(input("Enter the product price: "))
    products.update({product_name:product_price})
    lab24_task2_displayDictionary(products,"Name","Rate")
    return

def lab24_task2_mode3(products):
    bill = {}
    while True:
        product_name = input("\nEnter the product name - enter [q] to quit: ")
        if product_name.lower() == "q":
            break
        product_amount = eval(input("Enter the amount purchased: "))
        bill.update({product_name:product_amount})
        print()
    lab24_task2_displayDictionary(bill,"Name","Amount")
    bill_amount = 0
    for name,amount in bill.items():
        rate = products.get(name)
        if rate != None:
            bill_amount += rate * amount
    print(f"Bill: PKR {bill_amount}")
    return

def lab24_task2():
    task_header(24,2)
    products={'walnuts':1500,'cashew':1800,'almond':2000,'pine nuts':8000}
    while True:
        mode = eval(input("""
-----------------------------------------------
    Select one of the following mode
-----------------------------------------------
    [1] Display the rate of a product
    [2] Add or update a product price
    [3] Generate bill for purchased products
    [4] Quit the program
-----------------------------------------------

>> """))
        if mode == 1:
            lab24_task2_mode1(products)
        elif mode == 2:
            lab24_task2_mode2(products)
        elif mode == 3:
            lab24_task2_mode3(products)
        elif mode == 4:
            break
        else:
            print("Error: Invalid mode")
    return

# -------------------------------------------
#               Lab 24 - Task 3
# -------------------------------------------

def lab24_task3():
    task_header(24,3)
    products={
        'walnuts'   :1500,
        'cashew'    :1800,
        'almond'    :2000,
        'pine nuts' :8000,
        'mangoes'   :600,
        'bananas'   :2100,
        'berries'   :6400,
        'apricots'  :200}
    budget = eval(input("Enter your budget: "))
    affordables = []
    for name,price in products.items():
        if price <= budget:
            affordables.append(name)
    print()
    print("--------------------------")
    print("Affordable products:")
    print("--------------------------")
    for i in range(len(affordables)):
        print(f"[{i + 1}] - {affordables[i]}")
    print("--------------------------")
    return

# -------------------------------------------
#               Lab 24 - Task 4
# -------------------------------------------

def lab24_task4_displayDictionary(words):
    print("--------------------------")
    print("      Word  |  Count      ")
    print("--------------------------")
    for word,count in words.items():
        print(f"{word:>10}  |  {count:<10}")
    return

def lab24_task4():
    task_header(24,4)
    message = input("Enter a message: ")
    for p in string.punctuation:
        message = message.replace(p,"")
    words = {}
    for word in message.lower().split(" "):
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    words = [(count,word) for (word,count) in list(words.items())]
    words.sort(reverse=True)
    words = [(word,count) for (count,word) in words]
    words = dict(words)
    lab24_task4_displayDictionary(words)
    return

# -------------------------------------------
#               Lab 24 - Task 5
# -------------------------------------------

def lab24_task5():
    task_header(24,5)
    logins = {
        "david_bailey"      :"X8@pM!kZ6g#^T2u",
        "emma_collins"      :"L5@dR!tN7h#^B1w",
        "ethan_foster"      :"K9@lH!sJ3m#^P4q",
        "hannah_johnson"    :"F7@yN!zU2v#^G5x",
        "isaac_gonzalez"    :"W2@tK!pV9e#^D3f",
        "jasmine_hall"      :"R3@dZ!wL5s#^U1x",
        "kevin_kim"         :"E4@mB!nH7x#^Q6j",
        "laura_walker"      :"M6@uV!yK8f#^T9s",
        "mason_wright"      :"B8@jT!zN5l#^F1r",
        "olivia_thompson"   :"Y1@sP!wR6k#^G3h",
        "rachel_roberts"    :"S7@tZ!nF2m#^E5x",
        "samuel_smith"      :"C9@vL!pW4s#^T6f",
        "sophia_lee"        :"U2@kM!zX9g#^D8b",
        "tyler_clark"       :"H4@nF!yV5j#^B1p",
        "zoe_taylor"        :"A5@dN!wP3e#^G2q"
    }
    attempts = 5
    while attempts != 0:
        username = input("Username: ")
        if username not in logins.keys():
            print("\nError: The username is not registered")
        else:
            password = input("Password: ")
            if password != logins[username]:
                print("\nError: The password is incorrect")
            else:
                print("\nSuccess: You are logged in to the system")
                break
        attempts -= 1
        print(f"\nYou have {attempts} attempts remaining")
        print("-----------------------------------------")
    else:
        print("Sorry: You failed 5 times, you are locked out")
    return

# -------------------------------------------
#               Lab 24 - Task 6
# -------------------------------------------

def lab24_task6_calculateGPA(credit_hours,letter_grades):
    letters = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
    points = [4,4,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0.0]
    grades = dict(zip(letters,points))
    numerator = 0
    denominator = 0
    for i in range(len(credit_hours)):
        numerator += (grades[letter_grades[i]] * credit_hours[i])
        denominator += credit_hours[i]
    gpa = numerator / denominator
    return gpa

def lab24_task6():
    task_header(24,6)
    ch = [1,3,3,2,1,1,5,2,3,1]
    lg = ["A-","B+","A+","C","A","D","F","C+","B-","A"]
    gpa = lab24_task6_calculateGPA(ch,lg)
    print(f"GPA: {gpa:.2f}")
    return

# -------------------------------------------
#               Lab 24 - Task 7
# -------------------------------------------

def lab24_task7_MorseCodeGenerator(msg):
    mapping = {
        'A': '.-',    'B': '-...',  'C': '-.-.',   'D': '-..',
        'E': '.',     'F': '..-.',  'G': '--.',    'H': '....',
        'I': '..',    'J': '.---',  'K': '-.-',    'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',    'P': '.--.',
        'Q': '--.-',  'R': '.-.',   'S': '...',    'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',    'X': '-..-',
        'Y': '-.--',  'Z': '--..',  '0': '-----',  '1': '.----',
        '2': '..---', '3': '...--', '4': '....-',  '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',  '9': '----.',
    }
    space = " "
    code = ""
    for char in msg.upper():
        if char == space:
            code += space
        else:
            code += mapping[char]
    return code

def lab24_task7():
    task_header(24,7)
    message = input("Enter a message: ")
    code = lab24_task7_MorseCodeGenerator(message)
    print(f"Morse code: {code}")
    return

# -------------------------------------------
#               Lab 25 - Task 1
# -------------------------------------------

def lab25_task1():
    task_header(25,1)
    url = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2018/worldcup.standings.json"
    r = requests.get(url)
    data = r.json()
    teams_count = reduce(lambda c,group: c + len(group["standings"]),data["groups"],0)
    print(f"Number of teams: {teams_count}")
    country_names = [team["team"]["name"] \
        for group in data["groups"] for team in group["standings"] \
        if team["pos"] == 1]
    print(f"Countries with first position: {country_names}")
    country_codes = [team["team"]["code"] \
        for group in data["groups"] for team in group["standings"] \
        if team["goals_for"] > team["goals_against"]]
    print(f"Countries with higher goals for than goals against: {country_codes}")
    goals_for = [reduce(lambda c,team: c + team["goals_for"],group["standings"], 0) \
        for group in data["groups"]]
    goals_against = [reduce(lambda c,team: c + team["goals_against"],group["standings"], 0) \
        for group in data["groups"]]
    group_names = [group["name"] for group in data["groups"]]
    group_scores = {n:{"goals_for":f,"goals_against":a} \
        for (n,f,a) in zip(group_names,goals_for,goals_against)}
    print(f"Group scores:")
    json_str = json.dumps(group_scores,indent=4)
    print(json_str)
    with open("group_scores.json","w") as f:
        json.dump(group_scores,f,indent=4)
        f.close()
    drawn_groups = sorted(data["groups"],
        key=lambda group:reduce(lambda c,team:c + team["drawn"],group["standings"],0),
        reverse=True)
    print(f"Group with most drawn matches: {drawn_groups[0]['name']}")
    return

# -------------------------------------------
#               Lab 26 - Task 1
# -------------------------------------------

def lab26_task1():
    task_header(26,1)
    d = {
        'element1':5,
        'element2':2,
        'element3':0,
        'element4':'Computer',
        'element5':3.2,
        'element6':False,
        'element7':0,
        'element8':9
    }
    for k,v in d.items():
        try:
            reciprocal = 1 / v
        except ZeroDivisionError as e:
            print("Reciprocal of zero is not possible")
            print(f"\tException: {e}")
        except TypeError as e:
            print("Reciprocal of non-integer is not possible")
            print(f"\tException: {e}")
        except Exception as e:
            print(f"\tException: {e}")
        else:
            print(f"Reciprocal of {v} is {1 / v:.2f}")
        finally:
            print()
    return

# -------------------------------------------
#               Lab 26 - Task 2
# -------------------------------------------

def lab26_task2():
    task_header(26,2)
    try:
        f = open("sample.txt","r")
    except FileNotFoundError:
        print("Error: File does not exist")
    else:
        try:
            f.write("Hello, World!")
        except io.UnsupportedOperation:
            print("Error: File is not opened in write mode")
        except Exception as e:
            print(f"Exception: {e}")
    finally:
        if "f" in locals():
            f.close()
    return

# -------------------------------------------
#               Lab 27 - Task 1
# -------------------------------------------

def lab27_task1_pol2cart(r,theta,unit="degree"):
    if unit.lower() == "radian":
        angle = theta
    else:
        angle = theta * 180 / math.pi
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return x,y

def lab27_task1():
    task_header(27,1)
    print("------------------------------------------------------")
    print("This program converts the polar form to cartesian form")
    print("------------------------------------------------------")
    r = eval(input("r: "))
    theta = eval(input("\u03b8: "))
    unit = input("[degree (default) / radian]: ")    
    x,y = lab27_task1_pol2cart(r,theta,unit)
    print(f"\nCartesian form: ({x:.2f} + \u03b9{y:.2f})")
    return

# -------------------------------------------
#               Lab 27 - Task 2
# -------------------------------------------

def lab27_task2_cart2pol(x,y,unit="degree"):
    r = math.sqrt(x ** 2 + y ** 2)
    angle = math.atan2(y,x)
    if unit.lower() == "radian":
        theta = angle
        unit = "rad"
    else:
        theta = angle * 180 / math.pi
        unit = "\u00b0"
    return r,theta,unit

def lab27_task2():
    task_header(27,2)
    print("------------------------------------------------------")
    print("This program converts the cartesian form to polar form")
    print("------------------------------------------------------")
    x = eval(input("x: "))
    y = eval(input("y: "))
    unit = input("[degree (default) / radian]: ")    
    r,theta,unit = lab27_task2_cart2pol(x,y,unit)
    print(f"\nPolar form: ({r:.2f} \u2220 {theta:.2f} {unit})")
    return

# -------------------------------------------
#               Lab 27 - Task 3
# -------------------------------------------

def lab27_task3_addCourses(students,regid,*subjects):
    for subject in subjects:
        students[regid]["courses"].append(subject)
    return

def lab27_task3():
    task_header(27,3)
    students = {
        "MCT-UET-01":{"name":"Ahmad Bradley","courses":[]},
        "MCT-UET-02":{"name":"Misbah Rehman","courses":[]},
        "MCT-UET-03":{"name":"Zainab Khan","courses":[]},
        "MCT-UET-04":{"name":"Hina Xobia","courses":[]}
    }
    while True:
        regid = input("Registration ID - [\"X\" to quit]: ").upper()
        if regid == "X":
            break
        if regid not in students.keys():
            raise KeyError("Invalid registration ID")
        while True:
            print()
            print("----------------------------------------------------------")
            print("  [v] - Enter V to view the currently registered courses")
            print("  [r] - Enter R to register any number of courses")
            print("  [b] - Enter B to go back")
            print("----------------------------------------------------------")
            print()
            option = input(">> ").lower()
            print()
            if option == "v":
                print(students[regid]["courses"])
            elif option == "r":
                subjects = list(eval(input("Courses: ")))
                lab27_task3_addCourses(students,regid,*subjects)
            elif option == "b":
                break
            else:
                print("Error: Invalid option")
    return


# -------------------------------------------
#               Lab 27 - Task 4
# -------------------------------------------

def lab27_task4_GCD(*args):
    m = min(args)
    for i in range(1,m + 1):
        divides_all = True
        for arg in args:
            if arg % i != 0:
                divides_all = False
        if divides_all:
            gcd = i
    return gcd

def lab27_task4():
    task_header(27,4)
    args = eval(input("Enter a comma-separated list of numbers: "))
    gcd = lab27_task4_GCD(*args)
    print(f"GCD: {gcd}")
    return

# -------------------------------------------
#               Lab 27 - Task 5
# -------------------------------------------

def lab27_task5_dist(v1,v2):
    dist = math.sqrt((v2[1] - v1[1]) ** 2 + (v2[0] - v1[0]) ** 2)
    return dist

def lab27_task5_polyPerimeter(*vertices):
    n = len(vertices)
    perimeter = 0
    for i in range(0,n - 1):
        perimeter += lab27_task5_dist(vertices[i],vertices[i + 1])
    perimeter += lab27_task5_dist(vertices[n - 1],vertices[0])
    return perimeter

def lab27_task5():
    task_header(27,5)
    n = eval(input("Number of sides: "))
    print()
    vertices = []
    for i in range(n):
        vertex = eval(input(f"Vertex {i + 1} - (x,y): "))
        vertices.append(vertex)
    perimeter = lab27_task5_polyPerimeter(*vertices)
    print()
    print(f"Perimeter of the {n}-sided polygon: {perimeter:.2f}")
    return

# -------------------------------------------
#               Lab 28 - Task 1
# -------------------------------------------

def lab28_task1():
    task_header(28,1)
    n = eval(input("n: "))
    @lru_cache(maxsize=1000)
    def lab28_task1_fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return lab28_task1_fibonacci(n - 1) + lab28_task1_fibonacci(n - 2)
    print(f"Fibonacci(n): {lab28_task1_fibonacci(n)}")
    return

# -------------------------------------------
#               Lab 28 - Task 2
# -------------------------------------------

def lab28_task2_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a,b = b,(a + b)
    return a

def lab28_task2():
    task_header(28,2)
    n = eval(input("n: "))
    print(f"Fibonacci(n): {lab28_task2_fibonacci(n)}") 
    return

# -------------------------------------------
#               Lab 28 - Task 3
# -------------------------------------------

def lab28_task3():
    task_header(28,3)
    a,b = eval(input("(a,b): "))
    @lru_cache(maxsize=1000)
    def lab28_task3_gcd(a,b):
        if a < b:
            a,b = b,a
        if b == 0:
            return a
        else:
            return lab28_task3_gcd(a - b, b)
    print(f"GCD: {lab28_task3_gcd(a,b)}")
    return

# -------------------------------------------
#               Lab 28 - Task 4
# -------------------------------------------

def lab28_task4_title():
    print("-------------------------------------------")
    print("              Tower of Hanoi")
    print("-------------------------------------------")
    return

def lab28_task4_render_towers(towers):
    characters = {
        "left"  : "«",
        "right" : "»",
        "disk"  : "=",
        "rod"   : "¦",
        "base"  : "▀",
        "space" : " ",
    }
    n = len(towers[0])
    max_towers = 3
    print()
    for disk_idx in range(n):
        for tower_idx in range(max_towers):
            width = towers[tower_idx][disk_idx]
            print(characters["space"] * (n - width + 1),end="")
            if width != 0:
                print(characters["left"],end="")
                print(characters["disk"] * (width - 1),end="")
            print(characters["rod"],end="")
            if width != 0:
                print(characters["disk"] * (width - 1),end="")
                print(characters["right"],end="")
            print(characters["space"] * (n - width + 5),end="")
        print()
    for tower_idx in range(max_towers):
        print(characters["base"] * (n * 2 + 3),end="")
        print(characters["space"] * 4,end="")
    print()
    for tower_idx in range(max_towers):
        print(characters["space"] * n,end="")
        print(f"[{tower_idx + 1}]",end="")
        print(characters["space"] * (n + 4),end="")
    print()
    print()
    return

def lab28_task4_move_disk(towers,start_tower,end_tower):
    lab28_task4_render_towers(towers)
    if start_tower == end_tower:
        return
    n = len(towers[0])
    disk = 0
    for disk_idx in range(n):
        if towers[start_tower - 1][disk_idx] != 0:
            disk = towers[start_tower - 1][disk_idx]
            towers[start_tower - 1][disk_idx] = 0
            break
    first_non_zero = n
    for disk_idx in range(n):
        if towers[end_tower - 1][disk_idx] != 0:
            first_non_zero = disk_idx
            break
    towers[end_tower - 1][first_non_zero - 1] = disk
    return

def lab28_task4_hanoi(towers,n,source,dest,spare):
    if n == 0:
        lab28_task4_move_disk(towers,source,dest)
    else:
        lab28_task4_hanoi(towers,n - 1,source,spare,dest)
        lab28_task4_move_disk(towers,source,dest)
        lab28_task4_hanoi(towers,n - 1,spare,dest,source)
    return

def lab28_task4_start_towers(n):
    t1 = []
    t2 = []
    t3 = []
    for i in range(1,n + 1):
        t1.append(i)
    for _ in range(n):
        t2.append(0)
        t3.append(0)
    towers = [t1,t2,t3]
    return towers

def lab28_task4():
    task_header(28,4)
    lab28_task4_title()
    n = eval(input("Height of tower: "))
    towers = lab28_task4_start_towers(n)
    if n == 0:
        lab28_task4_render_towers(towers)
        return
    lab28_task4_hanoi(towers,n,source=1,dest=3,spare=2)
    lab28_task4_render_towers(towers)
    return

# -------------------------------------------
#               Lab 29 - Task 1
# -------------------------------------------

def lab29_task1():
    task_header(29,1)
    student1={
        'Reg'       :'2018-MC-01',
        'Name'      :'Muhammad Usman',
        'Sec'       :'A',
        'Courses'   :['CP2','ES']
        }
    student2={
        'Reg'       :'2018-MC-02',
        'Name'      :'Ayesha Xobia',
        'Sec'       :'B',
        'Courses'   :['LS','ES','PD']
        }
    common_courses = lambda s1,s2: list(set(s1["Courses"]).intersection(s2["Courses"]))
    print(f"Common courses: {common_courses(student1,student2)}")
    return

# -------------------------------------------
#               Lab 29 - Task 2
# -------------------------------------------

def lab29_task2_get_students():
    student1 = {
        'Reg':'2018-MC-01',
        'Name':'Muhammad Usman',
        'Sec':'A',
        'Courses':['CP','EM']
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
    student4 = {
        'Reg':'2018-MC-04',
        'Name':'Ayesha Xobia',
        'Sec':'A',
        'Courses':['LA','PD','CP','ED','EM']
    }
    student5 = {
        'Reg':'2018-MC-05',
        'Name':'Zainab Naeem',
        'Sec':'A',
        'Courses':[]
    }
    student6 = {
        'Reg':'2018-MC-06',
        'Name':'Hira Asif',
        'Sec':'A',
        'Courses':['DLD']
    }
    students = [student1,student2,student3,student4,student5,student6]
    return students

def lab29_task2_print_students(students):
    print("-------------------------------------------------------------------")
    print("    Name       |    Reg     | Sec |    Courses   ")
    print("-------------------------------------------------------------------")
    for student in students:
        name = student["Name"]
        reg = student["Reg"]
        sec = student["Sec"]
        courses = student["Courses"]
        print(f"{name:<14} | ",end="")
        print(f"{reg:<10} | ",end="")
        print(f"{sec:^3} | ",end="")
        print(f"{courses}")
    print("-------------------------------------------------------------------")
    return

def lab29_task2():
    task_header(29,2)
    students = lab29_task2_get_students()
    students.sort(key = lambda student : len(student["Courses"]),reverse=True)
    lab29_task2_print_students(students)    
    return

# -------------------------------------------
#               Lab 29 - Task 3
# -------------------------------------------

def lab29_task3():
    task_header(29,3)
    l = [[4,2,1,3,7],[3,1,7],[8,5,9,11],[9,7]]
    l.sort(key = lambda x:x[1])
    print(l)
    return

# -------------------------------------------
#               Lab 29 - Task 4
# -------------------------------------------

def lab29_task4_prologue():
    print("*" * 60)
    print("  1. Coffee     2. Tea        3. Coke       4.Orange juice")
    print("*" * 60)
    print()
    print("This is a survey for the favorite beverage")
    print()
    print("Choose (1-4) from the above menu or 0 to exit the program")
    print()
    return

def lab29_task4_results(votes):
    participants = 0
    for vote in votes.values():
        participants += vote
    print()
    print(f"The total number of participants: {participants}")
    print()
    print(" Beverage        Votes")
    print("***********************")
    for beverage,vote in votes.items():
        print(f" {beverage:<16} {vote}")
    return

def lab29_task4():
    task_header(29,4)
    lab29_task4_prologue()
    count = 0
    votes = {
        "Coffee"        :0,
        "Tea"           :0,
        "Coke"          :0,
        "Orange juice"  :0
        }
    while True:
        choice = eval(input(f"Please input the favorite beverage of person #{count + 1}: "))
        if choice == 0:
            break
        is_valid = False
        if choice in [1,2,3,4]:
            is_valid = True
        if is_valid:
            count += 1
            if choice == 1:
                votes["Coffee"] += 1
            elif choice == 2:
                votes["Tea"] += 1
            elif choice == 3:
                votes["Coke"] += 1
            else:
                votes["Orange juice"] += 1
        else:
            try:
                raise ValueError("Error: Please enter a number in the range [1-4]")
            except ValueError as e:
                print(e)
    votes = dict(sorted(votes.items(),key=lambda item: item[1],reverse=True))
    lab29_task4_results(votes)
    return

# -------------------------------------------
#               Lab 30 - Task 1
# -------------------------------------------

def lab30_task1_prologue():
    print("*" * 60)
    print("  1. Coffee     2. Tea        3. Coke       4.Orange juice")
    print("*" * 60)
    print()
    print("This is a survey for the favorite beverage")
    print()
    print("Choose (1-4) from the above menu or 0 to exit the program")
    print()
    return

def lab30_task1_results(votes):
    participants = 0
    for _,vote in votes:
        participants += vote
    print()
    print(f"The total number of participants: {participants}")
    print()
    print(" Beverage        Votes")
    print("***********************")
    for beverage,vote in votes:
        print(f" {beverage:<16} {vote}")
    return

def lab30_task1():
    task_header(29,4)
    lab30_task1_prologue()
    count = 0
    beverage_names = ["Coffee","Tea","Coke","Oranga juice"]
    vote_counts = [0,0,0,0]
    while True:
        choice = eval(input(f"Please input the favorite beverage of person #{count + 1}: "))
        if choice == 0:
            break
        is_valid = False
        if choice in [1,2,3,4]:
            is_valid = True
        if is_valid:
            count += 1
            vote_counts[choice - 1] += 1
        else:
            try:
                raise ValueError("Error: Please enter a number in the range [1-4]")
            except ValueError as e:
                print(e)
    votes = list(zip(beverage_names,vote_counts))
    votes.sort(key=lambda x:x[1],reverse=True)
    lab30_task1_results(votes)
    return

# -------------------------------------------
#               Lab 30 - Task 2
# -------------------------------------------

def lab30_task2_gpa1(grade_dict,credit_hours,grades_obtained,/):
    gpa = 0
    total_credits = 0
    for credit_hour,grade_obtained in zip(credit_hours,grades_obtained):
        gpa += grade_dict[grade_obtained] * credit_hour
        total_credits += credit_hour
    gpa /= total_credits
    return gpa

def lab30_task2_gpa2(grade_dict,credit_hours,grades_obtained,/):
    gpa = 0
    total_credits = 0
    grade_points = []
    for credit_hour in credit_hours:
        total_credits += credit_hour
    for grade_obtained in grades_obtained:
        grade_points.append(grade_dict[grade_obtained])
    for i in range(len(credit_hours)):
        gpa += credit_hours[i] * grade_points[i]
    gpa /= total_credits
    return gpa

def lab30_task2():
    task_header(30,2)
    letter_grades = ["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"]
    grade_points = [4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
    grade_dict = dict(zip(letter_grades,grade_points))
    credit_hours = [1,3,2,3,1,1]
    grades_obtained = ["B+","C","A-","A","B+","A+"]
    gpa = lab30_task2_gpa1(grade_dict,credit_hours,grades_obtained)
    print(f"GPA (Approach 1): {gpa:.2f}")
    gpa = lab30_task2_gpa2(grade_dict,credit_hours,grades_obtained)
    print(f"GPA (Approach 2): {gpa:.2f}")
    return

# -------------------------------------------
#               Lab 30 - Task 3
# -------------------------------------------

def lab30_task3_calcAssets1(products,stock,/):
    dry_fruits = zip(products.items(),stock.items())
    assets = 0
    for (product_name,unit_price),(stock_name,available_stock) in dry_fruits:
        if product_name == stock_name:
            assets += (unit_price * available_stock)
        else:
            raise IndexError("different product and stock names")
    return assets

def lab30_task3_calcAssets2(products,stock,/):
    assets = 0
    for product_name,unit_price in products.items():
        if product_name in stock:
            assets += stock[product_name] * unit_price
    return assets

def lab30_task3():
    task_header(30,3)
    products = {'anjeer':2500,'pista':2700,'badaam':2000,'chalghoza':8000}
    stock    = {'anjeer':100, 'pista':240, 'badaam':150, 'chalghoza':80}
    assets1 = lab30_task3_calcAssets1(products,stock)
    print(f"Assets (Approach 1): {assets1}")
    assets2 = lab30_task3_calcAssets2(products,stock)
    print(f"Assets (Approach 2): {assets2}")
    return

# -------------------------------------------
#               Lab 30 - Task 4
# -------------------------------------------

def lab30_task4():
    task_header(30,4)
    points = [(2,1),(-3,0),(4,2),(2,-5)]
    magnitudes = list(map(lambda t:round(math.sqrt(t[0]**2 + t[1]**2),2),points))
    print(f"Points: {points}")
    print(f"Magnitudes: {magnitudes}")
    return

# -------------------------------------------
#               Lab 30 - Task 5
# -------------------------------------------

def lab30_task5_get_students():
    student1 = {
        'Reg'       :'2018-MC-01',
        'Name'      :'Muhammad Usman',
        'Sec'       :'A',
        'Courses'   :['CP2','ES']}
    student2 = {
        'Reg'       :'2018-MC-02',
        'Name'      :'Tahir Mehmood',
        'Sec'       :'A',
        'Courses'   :['ES','LA']}
    student3 = {
        'Reg'       :'2018-MC-51',
        'Name'      :'Danish',
        'Sec'       :'B',
        'Courses'   :['MoM','CP2']}
    student4 = {
        'Reg'       :'2018-MC-52',
        'Name'      :'Hafiz Muhammad Aqib Ali',
        'Sec'       :'B',
        'Courses'   :['LA','ES','MoM']}
    students = [student1,student2,student3,student4]
    return students

def lab30_task5_print_students(students):
    print("-------------------------------------------------------------------")
    print("    Name       |    Reg     | Sec |    Courses   ")
    print("-------------------------------------------------------------------")
    for student in students:
        name = student["Name"]
        reg = student["Reg"]
        sec = student["Sec"]
        courses = student["Courses"]
        print(f"{name:<14} | ",end="")
        print(f"{reg:<10} | ",end="")
        print(f"{sec:^3} | ",end="")
        print(f"{courses}")
    print("-------------------------------------------------------------------")
    return

def lab30_task5():
    task_header(30,5)
    students = lab30_task5_get_students()
    cp_students = list(filter(lambda student: "CP2" in student["Courses"],students))
    lab30_task5_print_students(cp_students)
    return

# -------------------------------------------
#               Lab 30 - Task 6
# -------------------------------------------

def lab30_task6():
    task_header(30,6)
    nums = [5,4,2,1,7,8]
    nums_factorials = list(map(math.factorial,nums))
    even_factorials1 = filter(lambda x: x % 2 == 0,nums)
    even_factorials1 = list(map(math.factorial,even_factorials1))
    even_factorials2 = list(map(math.factorial,filter(lambda x: x % 2 == 0,nums)))
    print(f"Numbers: {nums}")
    print(f"Factorials of numbers: {nums_factorials}")
    print(f"Factorials of even numbers (Approach 1): {even_factorials1}")
    print(f"Factorials of even numbers (Approach 2): {even_factorials2}")
    return

# -------------------------------------------
#               Lab 30 - Task 7
# -------------------------------------------

def lab30_task7_get_students():
    student1 = {
        'Reg'       :'2018-MC-01',
        'Name'      :'Muhammad Usman',
        'Sec'       :'A',
        'Courses'   :['CP2','ES']}
    student2 = {
        'Reg'       :'2018-MC-02',
        'Name'      :'Tahir Mehmood',
        'Sec'       :'A',
        'Courses'   :['ES','LA']}
    student3 = {
        'Reg'       :'2018-MC-51',
        'Name'      :'Danish',
        'Sec'       :'B',
        'Courses'   :['MoM','CP2']}
    student4 = {
        'Reg'       :'2018-MC-52',
        'Name'      :'Hafiz Muhammad Aqib Ali',
        'Sec'       :'B',
        'Courses'   :['LA','ES','MoM']}
    students = [student1,student2,student3,student4]
    return students

def lab30_task7_dispStudent(st):
    print('_____________________________________')
    print(f"Registration No. : {st['Reg']}")
    print(f"Name : {st['Name']}")
    print(f"Section : {st['Sec']}")
    print(f"Courses Registered : {st['Courses']}")
    return

def lab30_task7():
    task_header(30,7)
    students = lab30_task7_get_students()
    cp_students1 = list(filter(lambda student: "CP2" in student["Courses"],students))
    cp_students2 = map(lambda student: None if "CP2" not in student["Courses"] else student,students)
    cp_students2 = list(filter(None,cp_students2))
    print("Students registered in CP-II (Approach 1):")
    for student in cp_students1:
        lab30_task7_dispStudent(student)
    print()
    print("Students registered in CP-II (Approach 2):")
    for student in cp_students2:
        lab30_task7_dispStudent(student)
    return

# -------------------------------------------
#               Lab 30 - Task 8
# -------------------------------------------

def lab30_task8_random_list(size,lowest,highest):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(lowest,highest))
    return random_list

def lab30_task8_print(msg,n_list,factorial_sum,n):
    print(f"{msg}\t: ",end="")
    for i in range(0,n - 1):
        print(f"{n_list[i]}! + ",end="")
    print(f"{n_list[n - 1]}! = {factorial_sum}")
    return

def lab30_task8():
    task_header(30,8)
    n = 10
    n_list = lab30_task8_random_list(size=n,lowest=1,highest=9)
    m_list = map(math.factorial,n_list)
    factorial_sum1 = sum(m_list)
    lab30_task8_print("Using map()",n_list,factorial_sum1,n)
    factorial_sum2 = reduce(lambda x,y: x + factorial(y),n_list,0)
    lab30_task8_print("Using reduce()",n_list,factorial_sum2,n)
    return

# -------------------------------------------
#               Lab 30 - Task 9
# -------------------------------------------

def lab30_task9_get_students():
    student1 = {
        'Reg'       :'2018-MC-01',
        'Name'      :'Muhammad Usman',
        'Sec'       :'A',
        'Courses'   :['CP2','ES']}
    student2 = {
        'Reg'       :'2018-MC-02',
        'Name'      :'Tahir Mehmood',
        'Sec'       :'A',
        'Courses'   :['ES','LA']}
    student3 = {
        'Reg'       :'2018-MC-51',
        'Name'      :'Danish',
        'Sec'       :'B',
        'Courses'   :['MoM','CP2']}
    student4 = {
        'Reg'       :'2018-MC-52',
        'Name'      :'Hafiz Muhammad Aqib Ali',
        'Sec'       :'B',
        'Courses'   :['LA','ES','MoM']}
    students = [student1,student2,student3,student4]
    return students

def lab30_task9():
    task_header(30,9)
    students = lab30_task9_get_students()
    courses = reduce(lambda cummul,s: cummul | set(s["Courses"]),students,set())
    print(courses)
    return

# -------------------------------------------
#               Lab 31 - Task 1
# -------------------------------------------

def lab31_task1_sumAllv1(nested_list):
    item_sum = 0
    for sublist in nested_list:
        for item in sublist:
            item_sum += item
    return item_sum

def lab31_task1_sumAllv2(nested_list):
    flattened_list = [item for sublist in nested_list for item in sublist]
    return sum(flattened_list)

def lab31_task1_sumAllv3(nested_list):
    generator_object = (item for sublist in nested_list for item in sublist)
    return sum(generator_object)

def lab31_task1():
    task_header(31,1)
    nums = [[2,6,2,11,9],[8,9,0,2],[12,6,14,8,24]]
    print(f"Sum (Approach 1): {lab31_task1_sumAllv1(nums)}")
    print(f"Sum (Approach 2): {lab31_task1_sumAllv2(nums)}")
    print(f"Sum (Approach 3): {lab31_task1_sumAllv3(nums)}")
    return

# -------------------------------------------
#               Lab 31 - Task 2
# -------------------------------------------

def lab31_task2_deepAdd(*iterables):
    return reduce(lambda x,y: x + y,(item for iterable in iterables for item in iterable),0)

def lab31_task2():
    task_header(31,2)
    col1 = [3,2,6,1]
    col2 = (5,4)
    col3 = {1,10,20}
    col4 = {'A':200,'B':100}
    print(lab31_task2_deepAdd(col1,col2,col3,col4.values()))
    return

# -------------------------------------------
#               Lab 31 - Task 3
# -------------------------------------------

def lab31_task3_interleave1(itr1,itr2):
    for item1,item2 in zip(itr1,itr2):
        yield item1
        yield item2
    return

def lab31_task3_interleave2(itr1,itr2):
    return (item for pair in zip(itr1,itr2) for item in pair)

def lab31_task3():
    task_header(31,3)
    x = [5,3,"Hello"]
    y = [2,9,20]
    g = lab31_task3_interleave1(x,y)
    print(f"g (Approach 1): {g}")
    print(f"list(g) (Approach 1): {list(g)}")
    g = lab31_task3_interleave2(x,y)
    print(f"g (Approach 2): {g}")
    print(f"list(g) (Approach 2): {list(g)}")
    return

# -------------------------------------------
#               Lab 31 - Task 4
# -------------------------------------------

def lab31_task4_makePairs1(iterable):
    n = len(iterable)
    for i in range(0,n,2):
        yield(iterable[i],iterable[i + 1])

def lab31_task4_makePairs2(iterable):
    n = len(iterable)
    return ((iterable[i],iterable[i + 1]) for i in range(0,n,2))

def lab31_task4():
    task_header(31,4)
    x = [2,9,20,44]
    g = lab31_task4_makePairs1(x)
    print(f"g (Approach 1): {g}")
    print(f"list(g) (Approach 1): {list(g)}")
    g = lab31_task4_makePairs2(x)
    print(f"g (Approach 1): {g}")
    print(f"list(g) (Approach 1): {list(g)}")
    return

# -------------------------------------------
#               Lab 31 - Task 5
# -------------------------------------------

def lab31_task5_fibonacci():
    a = 1
    b = 1
    for _ in range(100):
        yield a
        a,b = b,a + b

def lab31_task5():
    task_header(31,5)
    exhausted = False
    fibonacci = lab31_task5_fibonacci()
    i = 1
    while not exhausted:
        try:
            x = next(fibonacci)
            print(f"[{i}]: {x}")
            i += 1
        except StopIteration:
            exhausted = True
    return

# -------------------------------------------
#               Lab 32 - Task 1
# -------------------------------------------

class lab32_task1_student:
    department = "Mechatronics and Control Engineering"
    offered_courses = ["LA","CP","ES","VCA","PD"]

    def __init__(self,name,reg,sec):
        self.name = name
        self.reg = reg
        self.sec = sec
        self.email = "".join(reg.split("-")).lower() + "@student.uet.edu.pk"
        self.courses = []

    def register_courses(self,*courses):
        for course in courses:
            if course in lab32_task1_student.offered_courses:
                self.courses.append(course)
                self.courses.sort()
            else:
                try:
                    raise ValueError("course must be from the offered courses")
                except ValueError as e:
                    print(f"ValueError: {e}")

def lab32_task1():
    task_header(32,1)
    student = lab32_task1_student("Yahya Mateen","2019-R-2018-MC-71","B")
    courses = ["LA","CP","ES","VCA","PD"]
    student.register_courses(*courses)
    print(f"Courses registered successfully: {student.courses}")
    return

# -------------------------------------------
#               Lab 32 - Task 2
# -------------------------------------------

class lab32_task2_student:
    department = "Mechatronics and Control Engineering"
    offered_courses = ["LA","CP","ES","VCA","PD","MOM","EC","FOTS","ISL","CS"]

    def __init__(self,name,reg,sec):
        self.name = name
        self.reg = reg
        self.sec = sec
        self.email = "".join(reg.split("-")).lower() + "@student.uet.edu.pk"
        self.courses = []

    def register_courses(self,*courses):
        for course in courses:
            if course in lab32_task1_student.offered_courses:
                self.courses.append(course)
                self.courses.sort()
            else:
                try:
                    raise ValueError("course must be from the offered courses")
                except ValueError:
                    pass

def lab32_task2_print_students(students):
    print("-------------------------------------------------------------------")
    print("    Name       |    Reg     | Sec |    Courses   ")
    print("-------------------------------------------------------------------")
    for student in students:
        name = student.name
        reg = student.reg
        sec = student.sec
        courses = student.courses
        print(f"{name:<14} | ",end="")
        print(f"{reg:<10} | ",end="")
        print(f"{sec:^3} | ",end="")
        print(f"{courses}")
    print("-------------------------------------------------------------------")
    return

def lab32_task2():
    task_header(32,2)
    student1 = lab32_task2_student("Yahya Mateen","2019-MC-71","B")
    student2 = lab32_task2_student("Muhammad Ahsan","2019-MC-53","B")
    student3 = lab32_task2_student("Ayesha Xobia","2020-MC-05","A")
    student4 = lab32_task2_student("Hina Ijaz","2019-MC-67","B")
    student5 = lab32_task2_student("Atif Aslam","2021-MC-71","A")
    student1.register_courses("LA","ES")
    student2.register_courses("PD")
    student3.register_courses("CP","ES","PD","LA")
    student4.register_courses("VCA","ES","PD","LA","MOM","ES")
    student5.register_courses("LA","CP","PD")
    students = [student1,student2,student3,student4,student5]
    lab32_task2_print_students(students)
    students.sort(key=lambda student: len(student.courses),reverse=True)
    lab32_task2_print_students(students)
    return

# -------------------------------------------
#               Lab 32 - Task 3
# -------------------------------------------

class lab32_task3_point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)

    def move(self,x,y):
        self.x = x
        self.y = y
    
    def xTranslate(self,xdist):
        self.x += xdist

    def yTranslate(self,ydist):
        self.y += ydist

    def showPoint(self):
        return f"({round(self.x,2)},{round(self.y,2)})"

    def distOrigin(self):
            return round(math.sqrt(self.x ** 2 + self.y ** 2),2)

def lab32_task3():
    task_header(32,3)
    Point = lab32_task3_point
    point = Point(5,6)
    print(f"Point(5,6):           {point.showPoint()}")
    point.reset()
    print(f"reset():              {point.showPoint()}")
    point.move(12,-5)
    print(f"move(12,-5):          {point.showPoint()}")
    point.xTranslate(5.6)
    print(f"xTranslate(5.6):      {point.showPoint()}")
    point.yTranslate(9.11)
    print(f"yTranslate(9.11):     {point.showPoint()}")
    print(f"Distance from origin: {point.distOrigin()}")
    return

# -------------------------------------------
#               Lab 33 - Task 1
# -------------------------------------------

class lab33_task1_student:
    department = "Mechatronics and Control Engineering"
    offered_courses = ["LA","CP","ES","VCA","PD"]

    def __init__(self,name,reg,sec):
        self.name = name
        self.reg = reg
        self.sec = sec
        self.email = "".join(reg.split("-")).lower() + "@student.uet.edu.pk"
        self.courses = []

    def register_courses(self,*courses):
        for course in courses:
            if course in lab33_task1_student.offered_courses:
                self.courses.append(course)
                self.courses.sort()
            else:
                try:
                    raise ValueError("course must be from the offered courses")
                except ValueError as e:
                    print(f"ValueError: {e}")

def lab33_task1():
    task_header(33,1)
    student = lab33_task1_student("Yahya Mateen","2019-R-2018-MC-71","B")
    courses = ["LA","CP","ES","VCA","PD"]
    student.register_courses(*courses)
    print(f"Courses registered successfully: {student.courses}")
    return

# -------------------------------------------
#               Lab 33 - Task 2
# -------------------------------------------

class lab33_task2_student:
    department = "Mechatronics and Control Engineering"
    offered_courses = ["LA","CP","ES","VCA","PD","MOM","EC","FOTS","ISL","CS"]

    def __init__(self,name,reg,sec):
        self.name = name
        self.reg = reg
        self.sec = sec
        self.email = "".join(reg.split("-")).lower() + "@student.uet.edu.pk"
        self.courses = []

    def register_courses(self,*courses):
        for course in courses:
            if course in lab33_task1_student.offered_courses:
                self.courses.append(course)
                self.courses.sort()
            else:
                try:
                    raise ValueError("course must be from the offered courses")
                except ValueError:
                    pass

def lab32_task2_print_students(students):
    print("-------------------------------------------------------------------")
    print("    Name       |    Reg     | Sec |    Courses   ")
    print("-------------------------------------------------------------------")
    for student in students:
        name = student.name
        reg = student.reg
        sec = student.sec
        courses = student.courses
        print(f"{name:<14} | ",end="")
        print(f"{reg:<10} | ",end="")
        print(f"{sec:^3} | ",end="")
        print(f"{courses}")
    print("-------------------------------------------------------------------")
    return

def lab33_task2():
    task_header(33,2)
    student1 = lab33_task2_student("Yahya Mateen","2019-MC-71","B")
    student2 = lab33_task2_student("Muhammad Ahsan","2019-MC-53","B")
    student3 = lab33_task2_student("Ayesha Xobia","2020-MC-05","A")
    student4 = lab33_task2_student("Hina Ijaz","2019-MC-67","B")
    student5 = lab33_task2_student("Atif Aslam","2021-MC-71","A")
    student1.register_courses("LA","ES")
    student2.register_courses("PD")
    student3.register_courses("CP","ES","PD","LA")
    student4.register_courses("VCA","ES","PD","LA","MOM","ES")
    student5.register_courses("LA","CP","PD")
    students = [student1,student2,student3,student4,student5]
    lab32_task2_print_students(students)
    students.sort(key=lambda student: len(student.courses),reverse=True)
    lab32_task2_print_students(students)
    return

# -------------------------------------------
#               Lab 32 - Task 3
# -------------------------------------------

class lab33_task3_point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)

    def move(self,x,y):
        self.x = x
        self.y = y
    
    def xTranslate(self,xdist):
        self.x += xdist

    def yTranslate(self,ydist):
        self.y += ydist

    def showPoint(self):
        return f"({round(self.x,2)},{round(self.y,2)})"

    def distOrigin(self):
            return round(math.sqrt(self.x ** 2 + self.y ** 2),2)

def lab33_task3():
    task_header(33,3)
    Point = lab33_task3_point
    p1 = Point(2,3)
    p2 = Point()
    p3 = Point(5,5)
    print(p2.showPoint())
    print(p3.showPoint())
    p3.reset()
    print(p3.showPoint())
    p2.move(10,10)
    print(p2.showPoint())
    p2.xTranslate(-5)
    print(p2.showPoint())
    p2.yTranslate(5)
    print(p2.showPoint())
    return

# -------------------------------------------
#               Lab 33 - Task 4
# -------------------------------------------

class lab33_task4_point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def move(self,x,y):
        self.x = x
        self.y = y

    @property
    def distOrigin(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2),2)

def lab33_task4():
    task_header(33,4)
    point = lab33_task4_point(5,6)
    print(f"Distance from origin (5,6): {point.distOrigin}")
    point.move(15,41)
    print(f"Distance from origin (15,41): {point.distOrigin}")
    return

# -------------------------------------------
#               Lab 34 - Task 1
# -------------------------------------------

class lab34_task1_point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    @property
    def mag(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2),2)

    def reset(self):
        self.move(0,0)

    def move(self,newx,newy):
        self.x = newx
        self.y = newy

    def movX(self,units):
        self.x = units
    
    def movY(self,units):
        self.y = units
    
    def showPoint(self):
        return f"({self.x},{self.y})"

def lab34_task1_addPoints(p1,p2):
    return lab34_task1_point(p1.x + p2.x, p1.y + p2.y)

def lab34_task1_rand(n,p,q):
    Point = lab34_task1_point
    l = []
    for _ in range(n):
        x = random.randint(p,q)
        y = random.randint(p,q)
        l.append(Point(x,y))
    return l

def lab34_task1_print(l,msg):

    l_str = map(lambda p: p.showPoint(),l)
    l_str = ", ".join(l_str)
    print(f"{msg}: [{l_str}]")

def lab34_task1():
    task_header(34,1)
    Point = lab34_task1_point
    L1 = lab34_task1_rand(5,-10,10)
    lab34_task1_print(L1,"L1")
    L2 = lab34_task1_rand(5,-5,5)
    lab34_task1_print(L2,"L2")
    L3 = list(map(lambda p1,p2: Point(p1.x + p2.x, p1.y + p2.y), L1,L2))
    lab34_task1_print(L3,"L3 (before sort)")
    L3.sort(key=lambda p: p.mag)
    lab34_task1_print(L3,"L3 (after sort)")
    return

# -------------------------------------------
#               Lab 34 - Task 2
# -------------------------------------------

class lab34_task2_student:
    department = "Mechatronics"
    offered_courses = ["Proj","Mech","LA","ES","CP2","MOM","Isl/Pak"]
    all_students = []
    
    def __init__(self,fname,lname, reg):
        self.fname = fname
        self.lname = lname
        self.reg = reg
        self.email = "".join(reg.replace("/","-").split("-")).lower() + "@student.uet.edu.pk"
        self.courses = ["Proj"]
        lab34_task2_student.all_students.append(self)

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    def register_course(self,*courses):
        for course in courses:
            if course in lab34_task2_student.offered_courses:
                if course not in self.courses:
                    self.courses.append(course)
            else:
                try:
                    raise ValueError("course registration must be from offered courses")
                except ValueError:
                    pass
        self.courses.sort()

def lab34_task2():
    task_header(34,2)
    Student = lab34_task2_student
    student1 = Student("Yahya","Mateen","2019-R/2018-MC-71")
    print(f"Email: {student1.email}")
    if "Proj" in student1.courses:
        print("Proj was automatically registered on instantiation")
    else:
        print("Proj was not automatically registered on instantiation")
    print(f"Full name (before fname change): {student1.fullname}")
    student1.fname = "Abdullah"
    print(f"Full name (after fname change): {student1.fullname}")
    print(f"All students: {Student.all_students}")

# -------------------------------------------
#               Lab 34 - Task 3
# -------------------------------------------

class lab34_task3_student:
    department = "Mechatronics and Control Engineering"
    offered_courses = ["Proj","LA","CP","ES","VCA","PD","MOM","EC","FOTS","ISL","CS"]
    all_students = []

    def __init__(self,name,reg,sec):
        self.name = name
        self.reg = reg
        self.sec = sec
        self.courses = ["Proj"]
        lab34_task3_student.all_students.append(self)

    @property
    def email(self):
        return "".join(self.reg.replace("/","-").split("-")).lower() + "@student.uet.edu.pk"

    def register_courses(self,*courses):
        for course in courses:
            if course in lab34_task3_student.offered_courses:
                if course not in self.courses:
                    self.courses.append(course)
                    self.courses.sort()
            else:
                try:
                    raise ValueError(f"{course} is not offered")
                except ValueError:
                    print(f"{course} is not offered")

    def __str__(self):
        return f"{self.name} - {self.reg} - {self.email}"
    
    def __repr__(self):
        return f"Student({self.name},{self.reg},{self.sec})"

def lab34_task3():
    task_header(34,3)
    Student = lab34_task3_student
    student1 = Student("Yahya Mateen","2019-R/2018-MC-71","B")
    student2 = Student("Ali Irfan","2020-R/2019-MC-53","B")
    student3 = Student("Ayesha Xobia","2020-MC-01","A")
    student4 = Student("Hina Ijaz","2019-MC-47","A")
    student1.register_courses("LA","ES")
    student2.register_courses("PD")
    student3.register_courses("CP","ES","PD","LA")
    student4.register_courses("VCA","ES","PD","LA","MOM","ES")
    print("--------------")
    print("Before sorting:")
    print("--------------")
    for student in Student.all_students:
        print(student)
    print(f"\nAll students: {Student.all_students}\n")
    Student.all_students.sort(key=lambda student: len(student.courses),reverse=True)
    print("--------------")
    print("After sorting:")
    print("--------------")
    for student in Student.all_students:
        print(student)
    print(f"\nAll students: {Student.all_students}")
    return

# -------------------------------------------
#               Lab 34 - Task 4
# -------------------------------------------

class lab34_task4_point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    @property
    def mag(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2),2)

    def reset(self):
        self.move(0,0)

    def move(self,newx,newy):
        self.x = newx
        self.y = newy

    def movX(self,units):
        self.x = units
    
    def movY(self,units):
        self.y = units
    
    def showPoint(self):
        return f"({self.x},{self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"

def lab34_task4_addPoints(p1,p2):
    return lab34_task4_point(p1.x + p2.x, p1.y + p2.y)

def lab34_task4_rand(n,p,q):
    Point = lab34_task4_point
    l = []
    for _ in range(n):
        x = random.randint(p,q)
        y = random.randint(p,q)
        l.append(Point(x,y))
    return l

def lab34_task4_print(l,msg):

    l_str = map(lambda p: p.showPoint(),l)
    l_str = ", ".join(l_str)
    print(f"{msg}: [{l_str}]")

def lab34_task4():
    task_header(34,1)
    Point = lab34_task4_point
    L1 = lab34_task4_rand(5,-10,10)
    lab34_task4_print(L1,"L1")
    L2 = lab34_task4_rand(5,-5,5)
    lab34_task4_print(L2,"L2")
    L3 = list(map(lambda p1,p2: Point(p1.x + p2.x, p1.y + p2.y), L1,L2))
    print(f"L3 (before sort): {L3}")
    L3.sort(key=lambda p: p.mag)
    print(f"L3 (after sort): {L3}")
    return

# -------------------------------------------
#               Lab 35 - Task 1
# -------------------------------------------

class lab35_task1_student:
    department = "Mechatronics"
    compulsory_course = "*Project*"
    offered_courses = [compulsory_course,"LA","ES","PD","VCA","CP","EDC","CS","EC"]
    all_students = []
    def __init__(self,fname,lname,reg):
        self.fname = fname
        self.lname = lname
        self.fullname = f"{fname} {lname}"
        self.reg = reg
        self.courses = []
        self.courses.append(type(self).compulsory_course)
        self.__groupmember = None
        type(self).all_students.append(self)

    @property
    def fname(self):
        return self.__fname
    
    @fname.setter
    def fname(self,name):
        if type(self).isvalidname(name):
            self.__fname = name

    @property
    def lname(self):
        return self.__lname
    
    @lname.setter
    def lname(self,name):
        if type(self).isvalidname(name):
            self.__lname = name

    @property
    def reg(self):
        return self.__reg
    
    @reg.setter
    def reg(self,regid):
        if type(self).isvalidreg(regid):
            self.__reg = regid

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self,name):
        first_name,last_name = name.split()
        self.fname = first_name
        self.lname = last_name

    @property
    def email(self):
        return "".join(self.reg.replace("/","-").split("-")).lower() + "@student.uet.edu.pk"

    @property
    def groupmember(self):
        return self.__groupmember
    
    @groupmember.setter
    def groupmember(self,other):
        if self.groupmember == None and other.groupmember == None:
            self.__groupmember = other
            other.__groupmember = self
        else:
            culprit = self if not self.groupmember == None else other 
            try:
                raise ValueError(f"{culprit} already has a group member")    
            except ValueError as e:
                print(e)

    @groupmember.deleter
    def groupmember(self):
        other = self.groupmember
        if other == None:
            return
        if other.groupmember == self:
            self.__groupmember = None
            other.__groupmember = None
        else:
            try:
                raise ValueError(f"{other} is not a group member of {self}")
            except ValueError as e:
                print(e)

    def register_courses(self,*courses):
        for course in courses:
            if course in type(self).offered_courses:
                if course not in self.courses:
                    self.courses.append(course)
            else:
                try:
                    raise ValueError(f"{course} is not an offered course")
                except ValueError as e:
                    print(e)

    @staticmethod
    def isvalidname(name):
        if isinstance(name,str) and name.isalpha():
            return True
        else:
            try:
                raise ValueError("name must be a string of only alphabets")
            except ValueError as e:
                print(e)

    @staticmethod
    def isvalidyear(year):
        try:
            year = int(year)
        except ValueError:
            return False
        except:
            return False
        else:
            return year < 2024 and year > 1950

    @staticmethod
    def isvalidroll(roll):
        try:
            roll = int(roll)
        except ValueError:
            return False
        except:
            return False
        else:
            return roll > 0 and roll < 200
    
    @classmethod
    def isvalidreg(cls,regid):
        if "/" in regid:
            prefix,regid = regid.split("/")
            year,tag = prefix.split("-")
            if not cls.isvalidyear(year) or not tag == "R":
                return False
        year,tag,roll = regid.split("-")
        if cls.isvalidyear(year) and tag == "MC" and cls.isvalidroll(roll):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.fullname} {self.reg}"
    
    def __repr__(self):
        return f"{type(self)}({self.fname},{self.lname},{self.reg})"

def lab35_task1_test(student):
    print(f"__str__(): {student}")
    print(f"__repr__(): {student.__repr__()}")
    print(f"@fname.getter: {student.fname}")
    print(f"@lname.getter: {student.lname}")
    print(f"@fullname.getter: {student.fullname}")
    print(f"@reg.getter: {student.reg}")
    print(f"self.email: {student.email}")
    print(f"self.courses: {student.courses}")
    print(f"@groupmember.getter: {student.groupmember}")
    student.fname = "Mr"
    print(f"@fname.setter: {student.fname}")
    student.lname = "Abdullah"
    print(f"@lname.setter: {student.lname}")
    student.fullname = "Yahya Mateen"
    print(f"@fullname.setter: {student.fullname}")
    print(f"@fname.getter: {student.fname}")
    print(f"@lname.getter: {student.lname}")
    student.reg = "2018-MC-71"
    print(f"@reg.setter: {student.reg}")
    print(f"self.email: {student.email}")
    student.register_courses("LA","PD")
    print(f"self.courses: {student.courses}")
    other = lab35_task1_student("Test","Student","2020-MC-01")
    student.groupmember = other
    print(f"@groupmember.setter: {student.groupmember}")
    del student.groupmember
    print(f"@groupmember.deleter: {student.groupmember}")
    return

def lab35_task1_get_student_lists():
    Student = lab35_task1_student
    girl1 = Student("Hina","Xobia","2020-MC-43")
    girl2 = Student("Zainab","Furqan","2017-MC-88")
    girl3 = Student("Ayesha","Khan","2021-MC-15")
    girl4 = Student("Tania","Itifaq","2018-MC-04")
    boy1 = Student("Yahya","Mateen","2019-R/2018-MC-71")
    boy2 = Student("Atif","Aslam","2019-MC-54")
    boy3 = Student("Mufti","Zubair","2019-MC-78")
    boy4 = Student("Ali","Zulqernain","2018-MC-61")
    girls = [girl1,girl2,girl3,girl4]
    boys = [boy1,boy2,boy3,boy4]
    return girls,boys

def lab35_task1_make_groups(g,b):
    for girl,boy in zip(g,b):
        girl.groupmember = boy

def lab35_task1_print_lists(g,b):
    print("------------------")
    print("      Girls")
    print("------------------")
    for girl in g:
        print(girl)
    print()
    print("------------------")
    print("      Boys")
    print("------------------")
    for boy in b:
        print(boy)
    print()
    print("------------------")
    print("  Group members")
    print("------------------")
    for girl,boy in zip(g,b):
        print(f"{girl} is matched with {girl.groupmember}")

def lab35_task1():
    task_header(35,1)
    girls,boys = lab35_task1_get_student_lists()
    lab35_task1_make_groups(girls,boys)
    lab35_task1_print_lists(girls,boys)
    return

# -------------------------------------------
#               Lab 35 - Task 2
# -------------------------------------------

class lab35_task2_student:
    department = "Mechatronics"
    compulsory_course = "*Project*"
    offered_courses = [compulsory_course,"LA","ES","PD","VCA","CP","EDC","CS","EC"]
    all_students = []
    
    def __init__(self,fname,lname,reg):
        self.fname = fname
        self.lname = lname
        self.fullname = f"{fname} {lname}"
        self.reg = reg
        self.courses = []
        self.courses.append(type(self).compulsory_course)
        self.__groupmember = None
        type(self).all_students.append(self)

    @property
    def fname(self):
        return self.__fname
    
    @fname.setter
    def fname(self,name):
        if type(self).isvalidname(name):
            self.__fname = name

    @property
    def lname(self):
        return self.__lname
    
    @lname.setter
    def lname(self,name):
        if type(self).isvalidname(name):
            self.__lname = name

    @property
    def reg(self):
        return self.__reg
    
    @reg.setter
    def reg(self,regid):
        if type(self).isvalidreg(regid):
            self.__reg = regid

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self,name):
        first_name,last_name = name.split()
        self.fname = first_name
        self.lname = last_name

    @property
    def email(self):
        return "".join(self.reg.replace("/","-").split("-")).lower() + "@student.uet.edu.pk"

    @property
    def groupmember(self):
        return self.__groupmember
    
    @groupmember.setter
    def groupmember(self,other):
        if self.groupmember == None and other.groupmember == None:
            self.__groupmember = other
            other.__groupmember = self
        else:
            culprit = self if not self.groupmember == None else other 
            try:
                raise ValueError(f"{culprit} already has a group member")    
            except ValueError as e:
                print(e)

    @groupmember.deleter
    def groupmember(self):
        other = self.groupmember
        if other == None:
            return
        if other.groupmember == self:
            self.__groupmember = None
            other.__groupmember = None
        else:
            try:
                raise ValueError(f"{other} is not a group member of {self}")
            except ValueError as e:
                print(e)

    def register_courses(self,*courses):
        for course in courses:
            if course in type(self).offered_courses:
                if course not in self.courses:
                    self.courses.append(course)
            else:
                try:
                    raise ValueError(f"{course} is not an offered course")
                except ValueError as e:
                    print(e)

    @staticmethod
    def isvalidname(name):
        if isinstance(name,str) and name.isalpha():
            return True
        else:
            try:
                raise ValueError("name must be a string of only alphabets")
            except ValueError as e:
                print(e)

    @staticmethod
    def isvalidyear(year):
        try:
            year = int(year)
        except ValueError:
            return False
        except:
            return False
        else:
            return year < 2024 and year > 1950

    @staticmethod
    def isvalidroll(roll):
        try:
            roll = int(roll)
        except ValueError:
            return False
        except:
            return False
        else:
            return roll > 0 and roll < 200
    
    @classmethod
    def unregistered_subjects(cls):
        registered_courses = set()
        for student in cls.all_students:
            registered_courses.update(student.courses)
        return list(set(cls.offered_courses).difference(registered_courses))

    @classmethod
    def without_groupmembers(cls):
        return list(filter(lambda student: student.groupmember == None, cls.all_students))

    @classmethod
    def isvalidreg(cls,regid):
        if "/" in regid:
            prefix,regid = regid.split("/")
            year,tag = prefix.split("-")
            if not cls.isvalidyear(year) or not tag == "R":
                return False
        year,tag,roll = regid.split("-")
        if cls.isvalidyear(year) and tag == "MC" and cls.isvalidroll(roll):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.fullname} {self.reg}"
    
    def __repr__(self):
        return f"{type(self)}({self.fname},{self.lname},{self.reg})"

def lab35_task2_initialize():
    Student = lab35_task2_student
    student1 = Student("Yahya","Mateen","2019-R/2018-MC-71")
    student2 = Student("Hina","Xobia","2020-MC-43")
    student3 = Student("Atif","Aslam","2019-MC-54")
    student4 = Student("Zainab","Furqan","2017-MC-88")
    student1.register_courses("PD","CP","ES","EDC")
    student2.register_courses("CP")
    student3.register_courses("PD","CP")
    student4.register_courses("LA","ES","CS")
    return

def lab35_task2():
    task_header(35,2)
    lab35_task2_initialize()
    Student = lab35_task2_student
    print(f"Unregistered courses: {Student.unregistered_subjects()}")
    return

# -------------------------------------------
#               Lab 37 - Task 1
# -------------------------------------------

@total_ordering
class lab37_task1_point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,n_x):
        if type(self).isvalid(n_x):
            self.__x = n_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,n_y):
        if type(self).isvalid(n_y):
            self.__y = n_y

    @staticmethod
    def isvalid(n):
        try:
            int(n)
        except Exception:
            return False
        else:
            return True

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __neg__(self):
        return type(self)(-self.x,-self.y)
    
    def __add__(self,other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __truediv__(self,other):
        return type(self)(self.x / other, self.y / other)

    def __idiv__(self,other):
        self.x /= other
        self.y /= other
        return self

    def __gt__(self,other):
        return abs(self) > abs(other)

    def __eq__(self,other):
        return abs(self) == abs(other)

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"Point({self.x},{self.y})"

def lab37_task1():
    task_header(37,1)
    Point = lab37_task1_point
    p1 = Point(5,7)
    p2 = Point(-13,6)
    n = 2.5
    print("---------------------")
    print("        DATA         ")
    print("---------------------")
    print(f"p1       : {p1}")
    print(f"p2       : {p2}")
    print(f"n        : {n}")
    print(f"add(x)   : {p1.x + p2.x}")
    print(f"sub(x)   : {p1.x - p2.x}")
    print(f"add(y)   : {p1.y + p2.y}")
    print(f"sub(y)   : {p1.y - p2.y}")
    print("---------------------")
    print("       TESTING       ")
    print("---------------------")
    print(f"abs(p1)  : {abs(p1):.2f}")
    print(f"-p1      : {-p1}")
    print(f"p1 + p2  : {p1 + p2}")
    print(f"p1 - p2  : {p1 - p2}")
    p1_dup = Point(p1.x,p1.y)
    p1_dup += p2
    print(f"p1 += p2 : {p1_dup}")
    p1_dup = Point(p1.x,p1.y)
    p1_dup -= p2
    print(f"p1 -= p2 : {p1_dup}")
    print(f"p1 / n   : {p1 / n}")
    p1_dup = Point(p1.x,p1.y)
    p1_dup /= n
    print(f"p1 /= n  : {p1_dup}")
    print(f"p1 < p2  : {p1 < p2}")
    print(f"p1 <= p2 : {p1 <= p2}")
    print(f"p1 > p2  : {p1 > p2}")
    print(f"p1 >= p2 : {p1 >= p2}")
    print(f"p1 == p2 : {p1 == p2}")
    print(f"p1 != p2 : {p1 != p2}")
    for v in p1:
        print(f"__iter__(p1)  : {v}")
    print("---------------------")
    return

# -------------------------------------------
#               Lab 37 - Task 2
# -------------------------------------------

@total_ordering
class lab37_task2_point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,n_x):
        if type(self).isvalid(n_x):
            self.__x = n_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,n_y):
        if type(self).isvalid(n_y):
            self.__y = n_y

    @staticmethod
    def isvalid(n):
        try:
            int(n)
        except Exception:
            return False
        else:
            return True

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __neg__(self):
        return type(self)(-self.x,-self.y)
    
    def __add__(self,other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __truediv__(self,other):
        return type(self)(self.x / other, self.y / other)

    def __idiv__(self,other):
        self.x /= other
        self.y /= other
        return self

    def __gt__(self,other):
        return abs(self) > abs(other)

    def __eq__(self,other):
        return abs(self) == abs(other)

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"Point({self.x},{self.y})"

def lab37_task2_populate(n,low,high):
    Point = lab37_task2_point
    points = []
    for _ in range(n):
        x = random.randint(low,high)
        y = random.randint(low,high)
        points.append(Point(x,y))
    return points

def lab37_task2_print(points,msg):
    idx = 0
    print("-----------------------")
    print(f" {msg}")
    print("-----------------------")
    for point in points:
        print(f"{idx}: {point}\t@ {abs(point):.2f}")
        idx += 1
    print("-----------------------")

def lab37_task2():
    task_header(37,2)
    points = lab37_task2_populate(10,-5,5)
    lab37_task2_print(points,"BEFORE")
    points = filter(lambda p: abs(p) >= 2 and abs(p) <= 3, points)
    lab37_task2_print(points,"AFTER")
    return

# -------------------------------------------
#               Lab 37 - Task 3
# -------------------------------------------

@total_ordering
class lab37_task3_point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,n_x):
        if type(self).isvalid(n_x):
            self.__x = n_x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,n_y):
        if type(self).isvalid(n_y):
            self.__y = n_y

    @staticmethod
    def isvalid(n):
        try:
            int(n)
        except Exception:
            return False
        else:
            return True

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __neg__(self):
        return type(self)(-self.x,-self.y)
    
    def __add__(self,other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return type(self)(self.x - other.x, self.y - other.y)

    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self,other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __truediv__(self,other):
        return type(self)(self.x / other, self.y / other)

    def __idiv__(self,other):
        self.x /= other
        self.y /= other
        return self

    def __mul__(self,other):
        if type(other) == type(self):
            dot_product = 0
            for (a,b) in zip(self,other):
                dot_product += (a * b)
            return dot_product
        return type(self)(self.x * other,self.y * other)
    
    def __rmul__(self,other):
        return type(self)(self.x * other,self.y * other)

    def __gt__(self,other):
        return abs(self) > abs(other)

    def __eq__(self,other):
        return abs(self) == abs(other)

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"Point({self.x},{self.y})"

def lab37_task3_populate(n,low,high):
    Point = lab37_task3_point
    points = []
    for _ in range(n):
        x = random.randint(low,high)
        y = random.randint(low,high)
        points.append(Point(x,y))
    return points

def lab37_task3_print(points,msg):
    idx = 0
    print("---------------")
    print(f" {msg}")
    print("---------------")
    for point in points:
        print(f"{idx}: {point}")
        idx += 1
    print("---------------")

def lab37_task3():
    task_header(37,3)
    points = lab37_task3_populate(10,-5,5)
    lab37_task3_print(points,"LIST")
    points = list(map(lambda p: -(p * 5),points))
    lab37_task3_print(points,"SCALED")
    fix_p = lab37_task3_point(5,10)
    dot_products = list(map(lambda p: (p * fix_p),points))
    lab37_task3_print(dot_products,"DOT PRODUCTS")
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

def run_specific():
    try:
        lab_number, task_number = eval(input("\n>> Lab number and task number (lab, task): "))
    except Exception:
        pass
    try:
        globals()[f"lab{lab_number}_task{task_number}"]()
    except Exception:
        pass
    return

def loop():
    prompt = """
--------------------------------------------------------
    [n] - Press N to run a specific task
    [q] - Press Q to quit the program
--------------------------------------------------------

>> """
    while True:
        option = input(prompt).lower()
        if option == "n":
            run_specific()
        elif option == "q":
            exit()
        else:
            try:
                raise ValueError("invalid option")
            except ValueError:
                pass

# -------------------------------------------
#               Program Start
# -------------------------------------------

if __name__ == "__main__":
    loop()