year = int(input("Enter year to check for leap year:\n"))
print(f"finding if {year} is leap year")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Not Leap Year")
else:
    print("Not leap year")

# Other way of doing
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
