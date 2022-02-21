def validate():
    while True:
        supplied_pin = 4865
        pin = input("Enter your pin number:")
        if len(pin) < 4:
            print("Make sure your pin is at lest four numbers")
        elif len(pin) > 4:
            print("Make sure your pin has no more than four numbers")
        elif not pin.isdigit():
            print("Your pin can only include numbers")
        else:
            print("Your pin seems fine")
            break

validate()

#checking different aspects of the pin (length,numbers)