i = 0
while i < 100:

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i += 1
    if i % 3 == 0:
        print("Fizz")
        i += 1
    if i % 5 == 0:
        print("Buzz")
        i += 1
    else:
        print(i)
        i += 1
