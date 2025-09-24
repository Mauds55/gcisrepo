def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def positive_or_negative(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

def square(number):
    print("Square:", number * number)

def cube(number):
    print("Cube:", number * number * number)

def main():
    number = int(input("Enter an integer: "))
    even_or_odd(number)
    positive_or_negative(number)
    square(number)
    cube(number)
main()
 