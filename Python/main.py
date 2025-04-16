'''
a=10
print ("type of a: " , type(a))
b=10.5
print ("type of b: " , type(b))
c=2+3j
print ("type of c: " , type(c))
d='h'
print ("type of d: " , type(d))

string1 = "Hello"
string2 ="World"
string3 ='''
'''
       it can
       take multiple lines 
       and will still work


print(string1 + string2 + string3)
print("type of string1: " , type(string1))
print("type of string2: " , type(string2))
print("type of string3: " , type(string3))

num = int(input("Enter a number: "))
if num > 0:
   print( num, "is a Positive number")
elif num == 0:
   print(num, "is neither positive or negative it is Zero")
else:
   print(num, "is a Negative number")
print("outside body of if statement") '''

'''num = int(input("Enter a number: "))
if num >= 0:
      print(num, "is neither positive or negative it is Zero")
      if num == 0:
          print("Zero")
      else:
          print("Positive number")
else:
          print("Negative number")'''
'''sum = 0
list = (1,2,3,4,5,6,7,8,9,10)
for i in list:
    sum += i
print("The sum of the list is: ", sum)'''
'''
print(range(10))
alist=list(range(10))
print("print the whole list",alist)
print("print the fourth element of the list:",alist[3])

print(range(0,10,2))
listb=list(range(0,10,2))
print("print the whole list",listb)

for var in range(0,10,2):
    print(var)'''
'''
for char in "string":
    print('in for loop' , char)

    if char == "i":
           print('i found', char)
       
        break
    

print('out of loop' , val)'''
# Fibonacci sequence program with recursion

def fibonacci(n):
    # Base case: Return 0 or 1 for the first two terms
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursively calculate Fibonacci term
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Welcome message
    print("Welcome to the Fibonacci Sequence program!")

    # Get the number of terms the user wants
    while True:
        try:
            n = int(input("How many Fibonacci terms would you like to generate? "))
            if n < 1:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate the Fibonacci sequence up to the nth term
    print("\nFibonacci sequence:")
    for i in range(n):
        print(fibonacci(i), end=" ")

# Call the main function to start the program
    main()
