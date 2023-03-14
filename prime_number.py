MIN_LIMIT = 1
MAX_LIMIT = 100_000

while True:
    number = int(input("Enter any number from 1 to 100_000: "))
    if number < MIN_LIMIT or number > MAX_LIMIT:
        print("You enter incorrect value, try again!")
    else:
        k = 2
        for i in range(2, number // 2 + 1):
            k += 1
            if number % i == 0:
                print(f"Number you entered is not prime, it's multiple in {i}")
                break
        if k == number // 2 + 1:
            print("Number you entered is prime")