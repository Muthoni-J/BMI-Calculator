print("This program is to calculate the BMI of an individual\n")
name = input("Enter Your Name : ")
weight =float(input("Enter Your Weight : "))
height =float(input("Enter Your height : "))

bmi =weight / (height ** 2)

if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")
else:
        print(f"{name} is overweight by {bmi} BMI")

