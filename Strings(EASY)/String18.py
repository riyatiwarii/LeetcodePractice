'''FrizzBuzz'''
def fizzBuzz(n):
    list_of_output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list_of_output.append('FizzBuzz')
        elif i % 3 == 0:
            list_of_output.append('Fizz')
        elif i % 5 == 0:
            list_of_output.append('Buzz')
        else:
            list_of_output.append(str(i))
    return list_of_output
print(fizzBuzz(15))