pin = {4586} #this is the correct pin code that the user needs to enter to gain access
count = 1 #the count of attempts starts at 1
while True:
    enter_pin = int(input("Enter your pin:")); #asks te user to enter their pin as a number (int)
    if (enter_pin) in pin:  #this shows if the entered pin is in the correct pin it will grant access
        print("")
        print("Correct pin")
        print("")
        print("Access granted")
        break #this will stop the process if this part has been acheieved
    print("")
    print("Incorrect pin, please try again")
    count += 1
    if count == 4:  #this will run alongside the original if because of the same indentation and stop at 4
        print("Incorrect pin entered three times, account locked")
        break
#how do i include a message to show how many attempts are left after each one