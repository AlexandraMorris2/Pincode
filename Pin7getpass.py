import getpass

pin = {4568}
count = 1
while True:
    enter_pin = int(getpass.getpass("Enter your pin:"));
    if (enter_pin) in pin:
        print("")
        print("Correct pin")
        print("")
        print("Access granted")
        break
    print("")
    print("Incorrect pin, please try again")
    count += 1
    if count == 4:
        print("Incorrect pin entered three times, account locked")
        break
