def calc_game(repeat="YES", first_number=None): # DEFAULT VALUES SET FOR EACH ARG

    # Print a welcoming message
    print("Welcome to the standard calculator!\n")

    # Put the calculator in a while loop to cause the calculator to run continuously
    if repeat == "YES":  # CHANGED FROM while TO if, BECAUSE NOW YOU'LL JUST CALL THE FUNCTION AGAIN AT THE BOTTOM

        # Get user input on the numbers and operator and convert the strings to floats
        if first_number is not None:
            print("We are reusing your answer ({}), from last time\n".format(first_number))
            first_number = first_number
        else: # NO NEED FOR elif HERE, JUST FYI...else REQUIRES LESS COMPUTING
            first_number = float(input("Enter a number: "))

        # MOVING EVERYTHING BELOW HERE OUT OF THE if-else...WHY?
        # BECAUSE IT NEEDS TO RUN WHETHER YOU HAVE PASSED IN A first_number OR ARE DEFINING IT DURING THE FUNCTION CALL (USER INPUT PORTION)    
        operator = input(""" Which mathematical operator do you want to use?:
                            + for addition
                            - for subtraction
                            * for multiplication
                            / for division
                            % for modulus
                            ** for power
                            """)
        second_number = float(input("Enter a second number: "))

    # Use an if statement with elif blocks to determine the chosen operator
    # Furthermore, use conditional statments, that if true, apply the chosen operator on the two numbers
    # Then, give user feedback through f-strings to explain the calculations
        if operator == "+":
            answer = first_number + second_number
            print(f"{first_number} + {second_number} = {answer}")
        elif operator == "-":
            answer = first_number - second_number
            print(f"{first_number} - {second_number} = {answer}")
        elif operator == "*":
            answer = first_number * second_number
            print(f"{first_number} * {second_number} = {answer}")
        elif operator == "/":
            answer = first_number / second_number
            print(f"{first_number} / {second_number} = {answer}")
        elif operator == "%":
            answer = first_number % second_number
            print(f"{first_number} % {second_number} = {answer}")
        elif operator == "**":
            answer = first_number ** second_number
            print(f"{first_number} ** {second_number} = {answer}")
    # Add an else statement for invalid input
        else:
            print("You have entered an invalid operator")

    # Make use of the while loop to make the calculator continous
        response = input("Do you want to use the calculator again?\nAnswer YES OR NO: ")
    # Use the .upper() function so both lower and upper-case responses are accepted
        repeat = response.upper()
        #Include a condition to break the while loop if response is negative
        if repeat != "YES":
            print("Thank you for using the calculator, goodbye!")
            exit() # KILL THE PROGRAM
            ## DO THIS BEFORE CHECKING IF THEY WANT TO REUSE THE ANSWER - NO NEED TO ASK THAT IF THEY DON'T WANT TO USE THE CALCULATOR AGAIN
    # Ask them if they want to re-use their previous answer
        reuse = input("Do you want to re-use your answer?\nAnswer YES or NO: ").upper() # JUST DOING THE upper() IN ONE GO - WHATEVER IS EASIEST FOR YOU TO READ
        if reuse == "YES":
            # YOU HAD answer=first_number HERE WHICH DID NOT MAKE SENSE. REMOVED.
            # NOW CALL THE FUNCTION AGAIN
            calc_game(repeat, answer)
        else: # IF reuse IS ANY OTHER STRING APART FROM "YES"
            calc_game(repeat) # NOT PASSING A first_number THIS TIME
    else: # IF repeat IS NOT YES...I DON"T CARE WHAT OTHER STRING IT IS. YOU CAN BE SPECIFIC IF YOU WANT!
        exit()

# WE NEED TO ACTUALLY TELL THE FUNCTION TO RUN. ALL WE HAVE DONE ABOVE IS DEFINE THE FUNCTION
# YOU COULD PASS ARGS/PARAMS INTO THE BELOW FROM THE VERY GET-GO IF YOU WANT
calc_game()


        
