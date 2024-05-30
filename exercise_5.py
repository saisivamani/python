age = input("Please Enter Your Current Age : ")

r_age =  (90 - int(age))

print("The Remaining Year's : ", r_age)

r_days = int(r_age*365)
r_weeks = int(r_age*52)
r_months = int(r_age*12)

print(f"Your Current Age Is {age}. You Have {r_days} Day's, {r_weeks} Week's And {r_months} Month's Left ")