print("AWARDS SITE")
position = int(input("Enter athletes position: "))
try:
    if position == 1:
        print("Gold")
    elif position == 2:
        print("Silver")
    elif position == 3:
        print("Bronze")
    elif position <= 0:
        print("Enter number >= 1")
    else:
        print("Thanks for participating")
except Exception:
    print("Enter valid number")
