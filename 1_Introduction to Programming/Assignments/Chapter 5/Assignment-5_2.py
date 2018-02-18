# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    # escapes if num is "done"
    if num == "done" : break

    # then will attempt to parse num as an integer
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    # assigns value if both are none
    if largest is None and smallest is None:
        largest = num
        smallest = num

    # compares to largest and smallest
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# results
print "Maximum is", largest
print "Minimum is", smallest
