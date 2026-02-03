two_digit_number = int(input("Please enter a two-digit number: "))
ones_digit = two_digit_number % 10
tens_digit = two_digit_number // 10
sum_of_digits = ones_digit + tens_digit
reverse = ones_digit * 10 + tens_digit
print("reverse: ",reverse,"\t","sum of digits: ",sum_of_digits)