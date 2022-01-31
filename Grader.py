
# Welcome to my grade calculator aka Grader -

# input from user for max marks

print('\n--------------Welcome to Grade calculator-------------\n')

def rst():
    choice=input("\nPress enter to restart or press 'x' to exit program ---> ")
    if choice.lower() == 'x':
        print()
        exit()
    elif choice == "":
        main()
    else:
        print("\nPlease Enter a valid choice...")
        rst()

def main():
    def inpt():
        inpt.tm = 0 
        while True:
            try:
                inpt.tm = int(input("\nEnter the total marks possible in single subject out of 5 ---> "))  
            except ValueError:
                print("\nEnter marks (as whole numbers) to calculate...")
                main()
                break
            else:
                break

    inpt()

    mm = (inpt.tm)*5

# input from user for marks scored subjectwise

    mat = int(input("\nEnter your marks in Maths ---> "))
    phy = int(input("\nEnter your marks in Physics ---> "))
    cs = int(input("\nEnter your marks in Computer Science ---> "))
    chem = int(input("\nEnter your marks in Chemistry ---> "))
    eng = int(input("\nEnter your marks in English ---> "))
    
# Total marks

    total = (mat + phy + cs + chem + eng) 

# Percentage

    percentage = total/mm * 100 

    if mm<total:
        print("\nTry again with actual marks scored...")
        rst()
    

# Gradings
    
    if percentage>95:
        grade="Your grade is A  \n                    FEEDBACK : Well done, keep it up!"

    elif percentage<=95 and percentage>75:
        grade="Your grade is B  \n                    FEEDBACK : Only a little more hardwork is required"

    elif percentage<=75 and percentage>60:
       grade ="Your grade is C \n                    FEEDBACK : Hardwork is required!"

    elif percentage<=60:
         grade="Your grade is D  \n                    FEEDBACK : Serious hardwork is required!"
        

# Printing outputs
    
    print("\n Your total marks scored are : ", total, "out of", mm,
          "\n          Your percentage is : ", percentage, "%",
          "\n               Your grade is : ", grade)

    rst()

main()


# The End




