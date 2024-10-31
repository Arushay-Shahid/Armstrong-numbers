
def is_armstrong(number):

    num_str = str(number)
    
    power = len(num_str)
 
    total_sum = sum(int(digit) ** power for digit in num_str)
 
    return total_sum == number
number = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")