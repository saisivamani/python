year = int(input("Enter An Year : "))
print(f"You Have Entered {year}. Computer Is Checking Weather It Is Leap Year Or Not.")
print("Loading...................................................................100%")

if(year % 4 == 0):
    if(year % 100 != 0) and (year % 400 == 0):
        print("The Given Year Is Leap Year.")
else:
    print("The Given Year Is Not An Leap Year")