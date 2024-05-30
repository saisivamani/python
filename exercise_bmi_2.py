height = float(input("Enter Your Height In Meter: "))
weight = float(input("Enter Your Weight : "))

bmi = round(weight/height ** 2)
print("The BMI Is " ,bmi)

if(bmi < 18.5):
    print(f"Your BMI is {bmi} You Are In Underweight")
elif(bmi < 25):
    print(f"Your BMI is {bmi} You Are In Normal Range")
elif(bmi < 30):
    print(f"Your BMI is {bmi} You Are In Overweight")
elif(bmi < 35):
    print(f"Your BMI is {bmi} You Are Obese")
else:
    print(f"Your BMI is {bmi} You Are Clinically Obese")


