print("Fill in the following information: ")
name=input("Name: ")
age=int(input("Age: "))
gpa= float(input("GPA: "))
field_interest = input("Field of interest: ")
print("Answer by 'yes' or 'no':")
graduate = input("Have you graduated?: ")

if age < 25 and gpa >= 3.5 and graduate == "yes":
    print(name,", you are eligible for a scholarship.")
elif age < 30 and gpa >= 2.5:
    print (name, ", you are eligible for an internship.")
else:
    print (name, ", please apply again later.")    
