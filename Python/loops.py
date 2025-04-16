# This is a Fibonacci function using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Main function to run the program
def main():
    # Welcome the user
    print("Welcome to the Fibonacci Sequence program!")

    while True:
        try:
            # It asks the user how many terms they would like to generate
            n = int(input("How many Fibonacci terms would you like to generate? "))

            # Ensures the input is a positive integer
            if n <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    # Generates and print the Fibonacci sequence
    print("Here is the Fibonacci sequence up to the", n, "th term:")
    for i in range(n):
        print(fibonacci(i), end=" ")

# Runs the program
if __name__ == "__main__":
    main()
  
