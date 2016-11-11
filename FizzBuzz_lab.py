def fizz_buzz(num):
    try:
        num = int(num)
    except ValueError:
        return 'Input should be of type integer only'
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return num

#print(fizz_buzz(105))