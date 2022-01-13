
# Welcome to my grade calculator aka Grader --------------------------

# input from user for max marks
tm = int(input("Enter the total marks possible in single subject out of 5 : "))
mm = tm*5

# input from user for marks scored subjectwise
mat = int(input("enter your marks in Maths : "))
phy = int(input("enter your marks in Physics : "))
cs = int(input("enter your marks in Computer Science : "))
chem = int(input("enter your marks in Chemistry : "))
eng = int(input("Enter your marks in English : "))

# Total marks
total = (mat + phy + cs + chem + eng)

# Percentage 
percentage = total/mm * 100 

if mm<total:
    print("invalid input")
    exit()

def Grader():
    
    # Gradings
    if percentage>95:
        grade="Your grade is A, \nFEEDBACK : Well done, keep it up!"

    elif percentage<=95 and percentage>75:
        grade="Your grade is B, \nFEEDBACK : Only a little more hardwork is required"

    elif percentage<=75 and percentage>60:
        grade="Your grade is C, \nFEEDBACK : Hardwork is required!"

    elif percentage<=60:
        grade="Your grade is D, \nFEEDBACK : Serious hardwork is required!"
        exit()

    # Printing outputs
    
    print(" Your total marks scored are : ", total, "out of", mm,
    "\n Your percentage is : ", percentage, "%",
    "\n",grade)
      
Grader()

# The End




