supplied_pin = 4563
a = 0
while a <= 3:
    supplied_pin = int(input("please enter your pin:"))
#counter = 0
#while counter <= 3:
    if supplied_pin == 4563:
        print("correct")

    else:
        print("incorrect")
        supplied_pin = int(input("please enter your pin:"))
        a = a + 1

#how do i make it loop 3 times??
#i tried to use the counter function but it doesnt seem to work