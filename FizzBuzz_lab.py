def fizz_buzz(num):
    try:
        num = int(num)
    except ValueError:
        return 'Input should be of type integer only'
    if num % 3 == 0 and num % 5 == 0: # check whether the number is divisible by both 3 and 5 (should return 'FizzBuzz')
        return 'FizzBuzz'
    elif num % 3 == 0: #check if num is divisible by 3 if yes return 'Fizz'
        return 'Fizz'
    elif num % 5 == 0:#check if num is divisible by 5, if true return 'Buzz'
        return 'Buzz'
    return num

print(fizz_buzz(105))