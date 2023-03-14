from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 1
flag = False

while count <= 10:
    count += 1
    guess_num = int(input("Try to guess the number: "))
    if guess_num == num:
        print(f"You win! Hidden nuber was {num}")
        flag = True
        break
    elif guess_num > num:
        print("Your guess is bigger than our hidden number")
    else:
        print("Your guess is less than our hidden number")

if flag == False:
    print(f"Sorry, you didn't guess! Hidden nuber was {num}")
    