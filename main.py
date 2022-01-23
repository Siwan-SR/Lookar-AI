import sys
import turtle
from termcolor import colored
from colorama import Fore, Back, Style
from time import sleep
from datetime import date

print(Fore.BLUE)

options = input (" 1. Input identifier\n 2. Counting to 1000\n 3. Calculator\n 4. Translator \n")

print(Fore.BLUE)

if options == '1':
  name = input("Enter your name:\n")
  if name.isalpha() is False:
    print("Only letters are allowed!")
    sys.exit()


  try:
    birth_date = int(input ("Enter your birth date:\n"))
  except ValueError:
      print("Please enter a number.")
      sys.exit()

  try:
    birth_month = int(input ("Enter your birth month:\n"))
  except ValueError:
      print("Please enter a number.")
      sys.exit()

  try:
    birth_year = int(input ("Enter your birth year:\n"))
    print("\n")
    print("\n")
  except ValueError:
      print("Please enter a number.")
      sys.exit()


  def calculateAge(born):
    today = date.today()
    try:
      birthday = born.replace(year = today.year)

    except ValueError:
      birthday = born.replace(year = today.year,
          month = born.month + 1, day = 1)

    if birthday > today:
      return today.year - born.year - 1
    else:
      return today.year - born.year


  print("You are", name)
  sleep(1.50)
  print("You were born in", birth_date, birth_month, birth_year)
  sleep(1.50)
  print("You are:")
  print(calculateAge(date(birth_year, birth_month, birth_date)), "years old")

  turtle.speed(1)
  turtle.forward(150)
elif options == '2':
  for x in range(1001):
    print(x)
  else:
    print("The counting is finished!")

elif options == '3':
  def add(x, y):
    return x + y

  def subtract(x, y):
    return x - y


  def multiply(x, y):
    return x * y


  def divide(x, y):
    return x / y


  print("Select operation.")
  print("+")
  print("-")
  print("*")
  print("/")

  while True:
    choice = input("Enter Operation(+/-/*//): ")


    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Next? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

