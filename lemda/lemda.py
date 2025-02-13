def multiply(num_1: int, num_2: int) -> int:
    return num_1 * num_2


print(multiply(2, 2))


multiplication = lambda num_1, num_2: num_1 * num_2

print(multiplication(2, 7))

answer = (lambda num_1, num_2: num_1 * num_2)(2, 7)
print(answer)

a = 5
b = 7

answer = (lambda num_1, num_2: num_1 * num_2)(a, b)
print(answer)