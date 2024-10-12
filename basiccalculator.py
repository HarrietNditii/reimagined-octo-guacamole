#Function to add two numbers
def add(x, y):
    return x+y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Nditi's Calculator \n" \
      "Select any operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      )

#input from user
select = int(input("Select operations from 1, 2, 3, 4 :"))
x = int(input("Enter 1st number: "))
y = int(input("Enter the 2nd number: "))

if  select == 1:
    print(x, "+", y, "=", 
          add(x, y))
    
elif select == 2:
    print(x, "-", y, "=",
          subtract(x, y))
    
elif select == 3:
    print(x, "*", y, "=",
          multiply(x, y))
    
elif select == 4:
    print(x, "/", y, "=",
          divide(x, y))
    
else:
    print("invalid input!")
          