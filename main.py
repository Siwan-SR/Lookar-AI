import sys
import turtle
from termcolor import colored
from colorama import Fore, Back, Style
from time import sleep
from datetime import date

print(Fore.BLUE)

options = input (" 1. Input identifier\n 2. Counting to 1000\n 3.Calender\n 4. Covid 19 Info \n")

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