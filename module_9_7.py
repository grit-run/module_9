def is_prime(func):
    def wrapper(*args, **kwargs):
        inner_res = func(*args, **kwargs)
        counter = 0
        for i in range(1, inner_res + 1):
            if inner_res % i == 0:
                counter += 1
        print('Простое' if counter == 2 else 'Составное')
        return inner_res
    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    return num1 + num2 + num3


result = sum_three(2, 3, 6)
print(result)
