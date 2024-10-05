import string

print("Password Strength Checker")

password = input("Enter your password: ")

password_length = len(password)

number_included = any(chr.isdigit() for chr in password)

special_character_included = any(c in string.punctuation for c in password)

capital_letter_included = any(c.isupper() for c in password)

small_letter_included = any(c.islower() for c in password)



def check_password_strength(password):
    if password_length <= 7:
        print ("password length: " + str(password_length))
        print("your password should not be less than 8 characters")
    elif not number_included:
        print("Please include a number '0123456789'")
    elif not special_character_included:
        print("Please include a special character !@#$%^&*~")
    elif not capital_letter_included:
        print("Please include at least one capital letter")
    elif not small_letter_included:
        print("please include at least one small letter")
    else:
        print("your password is strong")
check_password_strength(password)


