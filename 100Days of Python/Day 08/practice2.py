def prime_check(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime == True:
        print(f"{number} is a Prime Number!")
    else:
        print(f"{number} is not a prime number...")

n = int(input("Check this number: "))
prime_check(number=n)