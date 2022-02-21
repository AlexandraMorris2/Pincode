
def password_check(passwd):

    if len(passwd) < 4:
        print('length should be at least 4')
        val = False

    if len(passwd) > 4:
        print('length should be not be greater than 4')
        val = False

    if val:
        return val


# Main method
def main():
    pin = 4563

    if (pin_check(pin)):
        print("Password is valid")
    else:
        print("Invalid Password !!")

#trying to find ways to check that the password is the correct length etc

