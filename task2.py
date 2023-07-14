choice=input("hours to minutes or minutes to hours? ")
    choice == "hours to minutes":
     hours = int(input("enter number of hours: "))
    hours *= 60
    print(hours)
elif choice == "minutes to hours":
    mins = int(input("enter numbers of minute"))
    mins /=60
    print(mins)
