def recursive_sum(number):
    if number == 1:
        return 1
    if number == 0:
        return 0
    else:
        sum = number
        sum += recursive_sum(number - 1)
        return sum


def run():
    while True:
        number = int(input('Write a number for recursive sum: '))
        result = recursive_sum(number)
        
        print(f'The recursive sum of {number} is {result}')


if __name__ == "__main__":
    run()