# Calculator

import replit


#Add
def add (n1, n2):
  return n1 + n2

#subtract
def subtract (n1, n2):
  return n1 - n2

#multiply
def multiply (n1, n2):
  return n1 * n2

#divide
def divide (n1, n2):
  return n1 / n2


operations = {
  "+":add, 
  "-":subtract, 
  "*":multiply, 
  "/":divide, 
}

# num1 = int(input("Whats the first number?: "))


# for symbol in operations:
#   print(symbol)
  
# operational_symbol = input("Pick an operation from the line above: ")

# num2 = int(input("Whats the second number?: "))

# calculation_function = operations[operational_symbol]

# first_answer = calculation_function(num1, num2)

# print(f"{num1} {operational_symbol} {num2} = {first_answer}")





def calculator():
  firstgo = 1

  keepgoing = "y"
  while keepgoing == "y":
    
    if firstgo == 1:
      num1 = float(input("Whats the first number?: "))
      firstgo =- 1
    else:
      num1 = previous_answer


    for symbol in operations:
      print(symbol)
    
    operational_symbol = input("Pick an operation from the line above: ")


    num2 = float(input("Whats the next number?: "))

    calculation_function = operations[operational_symbol]

    previous_answer = calculation_function(num1, num2)

    print(f"{num1} {operational_symbol} {num2} = {previous_answer}")
    keepgoing = input("Type 'y' to continue calculating, or type 'n' to exit.\n")
  else:
    replit.clear()
    calculator()


calculator()




# operational_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operational_symbol]

# second_answer = calculation_function(calculation_function(num1, num2), num3)

# print(f"{first_answer} {operational_symbol} {num3} = {second_answer}")

