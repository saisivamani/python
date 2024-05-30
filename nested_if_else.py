a = input("Please Enter Your College Name : ")
if (a == "SRKR"):
    print("You Are Eligible For Next Step")
    b = input("Please Enter Your Dept Name : ")
    if (b == "CSD"):
        print("Now You Are CSDIAN")
    elif (b != "CSD"):
        print("Join In Our CSD")
    else:
        print("Others Not Allowed")
else:
    print("Sorry This Is Not For You")