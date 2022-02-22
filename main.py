import sys
import math
import random
import pyqrcode
import png
from pyqrcode import QRCode
from colorama import Fore, Back, Style
from time import sleep
from datetime import date

print(Fore.BLUE)

options = input ("Options: \n\n 1. Input identifier\n 2. Counting to 1000\n 3. Calculator\n 4. Perfect Square\n 5. Square Root\n 6. BMI Calculator\n 7. Games\n 8. PI Converter\n 9. QR Code Creator\n 10. Input Length Identifier \n\nEnter option number: ")

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


elif options == '4':
    try:
      sq = int(input ("Enter number:\n"))
      print("\n")
      print("\n")
    except ValueError:
        print("Please enter a number.")
        sys.exit()
    root = math.sqrt(sq)
    if int(root + 0.5) ** 2 == sq:
      print(sq, 'is a perfect square')
    else:
      print(sq, 'is not a perfect square')  

elif options == '5':
      try:
        sqr = int(input ("Enter number:\n"))
        print("\n")
        print("\n")
      except ValueError:
          print("Please enter a number.")
          sys.exit()
      SquareRoot = math.pow(sqr, 0.5) 
      print("The Square Root of {0} = {1}" .format(sqr, SquareRoot))

elif options == '6':
  def add(x, y):
    return x + y

  def multiply(x, y):
      return x * y

  def divide(x, y):
      return x / y

  try:
      height = float(input ("Enter your height in meters:\n"))
  except ValueError:
        print("Please enter a number.")
        sys.exit()

  try:
      weight = float(input ("Enter your weight in kilograms:\n"))
  except ValueError:
        print("Please enter a number.")
        sys.exit()

  bmiheight = height * height

  print(height, "*", height, "=", multiply(height, height))
  sleep(0.5)
  print(weight, "/", bmiheight, "=", divide(weight, bmiheight))
  print("\n")
  print("\n")
  print("BMI stands for Body Mass Index. If your BMI is less than 18.5, it falls within the underweight range. If your BMI is 18.5 to 24.9, it falls within the normal or Healthy Weight range. If your BMI is 25.0 to 29.9, it falls within the overweight range.")

elif options == '7':
  game_options = input ("1. Number guessing\n")

  if game_options == '1':

      class NumberGuessingGame:

        def __init__(self):

            self.LOWER = 1
            self.HIGHER = 100

        def get_random_number(self):
            return random.randint(self.LOWER, self.HIGHER)

        def start(self):
            random_number = self.get_random_number()

            print(
                f"Guess the number from {self.LOWER} to {self.HIGHER}")

            chances = 0
            while True:
                user_number = int(input("Enter your guessed number: "))
                if user_number == random_number:
                    print(
                        f"-> Hurray! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                    break
                elif user_number < random_number:
                    print("-> Your number is less than the random number")
                else:
                    print("-> Your number is greater than the random number")
                chances += 1

      numberGuessingGame = NumberGuessingGame()
      numberGuessingGame.start()  

  else:
    print("That is not an option!")
    sys.exit()

elif options == '8':
  pi_options = input (" 1. Diameter to Circumference\n 2. Circumference to Diameter\n 3. Diameter to Radius\n 4. Radius to Diameter\n 5. Radius to Area\n\n")

  if pi_options == '1':

    def add(x, y):
      return x + y

    def subtract(x, y):
      return x - y


    def multiply(x, y):
      return x * y


    def divide(x, y):
      return x / y

    try:
      d = float(input ("Enter diameter: "))

    except ValueError:
      print("Only numbers are allowed!")
      sys.exit()
    
    pi = 3.14
    pi_ans1 = d * pi

    print("Circumference: ",multiply(d, pi))

  elif pi_options == '2':
    
    def add(x, y):
      return x + y

    def subtract(x, y):
      return x - y


    def multiply(x, y):
      return x * y


    def divide(x, y):
      return x / y

    try:
      c = float(input ("Enter circumference: "))

    except ValueError:
      print("Only numbers are allowed!")
      sys.exit()

    pi = 3.14
    pi_ans2 = c / pi
    print("Diameter: ",divide(c, pi))

  elif pi_options == '3':
    
    def add(x, y):
      return x + y

    def subtract(x, y):
      return x - y


    def multiply(x, y):
      return x * y


    def divide(x, y):
      return x / y

    try:
      d = float(input ("Enter diameter: "))

    except ValueError:
      print("Only numbers are allowed!")
      sys.exit()

    unit = 2
    pi_ans3 = d / unit
    print("Diameter: ",divide(d, unit))
  
  elif pi_options == '4':
    def add(x, y):
      return x + y

    def subtract(x, y):
      return x - y


    def multiply(x, y):
      return x * y


    def divide(x, y):
      return x / y

    try:
      r = float(input ("Enter radius: "))

    except ValueError:
      print("Only numbers are allowed!")
      sys.exit()

    unit = 2
    pi_ans4 = r * unit
    print("Radius: ",multiply(r, unit))

  elif pi_options == '5':

    def add(x, y):
      return x + y

    def subtract(x, y):
      return x - y


    def multiply(x, y):
      return x * y


    def divide(x, y):
      return x / y

    try:
      r = float(input ("Enter radius: "))

    except ValueError:
      print("Only numbers are allowed!")
      sys.exit()

    unit = 2
    pi = 3.14
    pi_ans5 = r * r
    print("Radius: ",multiply(pi_ans5, pi))

elif options == '9':

  s = input("Enter URL: ")
    
  url = pyqrcode.create(s)
    
  url.svg("myqr.svg", scale = 8)
  
  url.png('myqr.png', scale = 6)
  
  print("Please check myqr.png to see your barcode!")

elif options == '10':
  para = input ("Enter paragraph: ")
  sleep(2.50)
  print("\n")
  print("\n")
  para_len = (len(para))
  print("Characters: ",para_len)

else:
  print("That is not an option!")
  sys.exit()