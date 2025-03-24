
def found_p_in_string(str):
    found_p = False

    for letter in str:
        if letter.lower() == 'p':
            return True
    else:
        return False
    

given_string = input("Enter a string:")

print(found_p_in_string(given_string))
