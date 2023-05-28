def is_valid_id(id_number):
    # Check if the ID has exactly 9 characters
    if len(id_number) != 9:
        return False

    digits = list(id_number)
    counter = 0

    # Iterate over the digits of the ID
    for i in range(9):
        digit = int(digits[i])

        # Multiply the digit by 1 or 2 based on its position (odd or even)
        if i % 2 == 0:
            digit *= 1
        else:
            digit *= 2

        # If the resulting value is greater than 9, subtract 9
        if digit > 9:
            digit -= 9

        # Sum up all the modified digits
        counter += digit

    # Check if the sum is divisible by 10
    return counter % 10 == 0

id_num = input('please type id of israel: ')
print(is_valid_id(id_num))


