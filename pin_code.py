# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
# but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


def validate_pin_my(pin):
    if pin.isdigit() == True and (len(pin) == 4 or len(pin) == 6):
        return True
    return False


s = '-125534'
print(validate_pin(s))
