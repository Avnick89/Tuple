
# loop through a range of 1, to n - range(1, n) - maybe i'll do n +1 to make sure im including the last number
# check if each number is divisible by 3, 5, or 3 & 5 using the %
# i might have to be careful with the order of my conditionals

def fizzbuzz(n):
    # looping through a range of 1 to n
    for num in range(1, n+1):
        # checking if a number is divisible by 3
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0 :
            print("Fizz")
        else:
            print(num)

# calling my function
fizzbuzz(30)