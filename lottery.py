import random
def lottery_numbers(quantity):
    number = []
    while True:
        if len(number) == quantity:
            break
        lottery_num = random.randint(1, 39)

        if lottery_num not in number:
            number.append(lottery_num)
    return number

def main():
    print "Welcome to the lottery"

    quantity = int(raw_input("Please enter how many random numbers would you like to have: "))
    user_numbers = []
    while True:
        if len(user_numbers) == quantity:
            break
        lottery_num = int(raw_input("Inser your number: "))

        if lottery_num not in user_numbers:
            user_numbers.append(lottery_num)


    #generate resaults
    numbers = lottery_numbers(quantity)
    print(numbers)

    score = 0
    for user_num in user_numbers:
        if user_num in numbers:
            print("User guesed " + str(user_num))
            score += 1
        else:
            print("User didn't guess " + str(user_num))

    print("User score is: "+ str(score))
    print ("END")

if __name__ == "__main__":
    main()

