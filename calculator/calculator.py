

### Ask the user for an input and store it in a variable

integer1 = 0
integer2 = 0
op1 = ''

### Main Loop that will run until the user inputs 'q' to quit
while True:
    ### First integer that is being calculated by the application, only integers are valid inputs
    integer1 = int(input("Enter the first number you'd like to calculate, or press q to quit: "))
    ### If this input is 'q', the application will break out of the loop. The same applies for all inputs
    if integer1 == 'q':
        break
    ### If input is an integer and not 'q', the application will store the variable and continue to the next input
    else: 
        integer1 = int(integer1)
    ### Input for the operator that will determine what type of operations are done on the two integers
    op1 = input("Enter the operator that you'd like to use, select from +, -, *, /, or press q to quit: ")
    if op1 == 'q':
        break
    else: 
        op1 = str(op1)
    ### Second integer that is being calculated by the script
    integer2 = int(input("Enter the second number you'd like to calculate, or press q to quit: "))
    if integer2 == 'q':
        break
    else: 
        integer2 = int(integer2)
    ### If statements, if the operator (+, -, *, /) is selected, the appropriate operation will be performed on the two integers.
    if op1 == '+':
        total = integer1 + integer2
    if op1 == '-':
        total = integer1 - integer2
    if op1 == '*':
        total = integer1 * integer2
    if op1 == '/':
        total = integer1 / integer2  # Assign the division operation to the total variable

### Prints the total of the two integers. 
    print("The total of these two integers is:", total)