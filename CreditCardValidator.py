def sumOfDigitsInNum(num):
    total = 0
    num = str(num)
    for digit in num:
        total+=int(digit)
    return total

def luhn(cardNumber):
    total = 0
    reversedCard = cardNumber[::-1]

    for i in range(len(reversedCard)):
        num = int(reversedCard[i])
        if i % 2 == 1:
            num *= 2
        total += sumOfDigitsInNum(num)
    return total % 10 == 0

def validateType(cardNumber):
    cardLength = len(cardNumber)
    beginning = int(cardNumber[0:2])

    # amex cards
    if(cardLength == 15 and (beginning == 34 or beginning == 37)):
        return True
    # Mastercard
    if (cardLength == 16 and (beginning == 51 or beginning == 52 or beginning == 53 or beginning == 54 or beginning == 55 )):
        return True
    # Visa cards
    if((cardLength == 13 or cardLength == 16) and(int(cardNumber[0]) == 4)):
        return True
    return False


cardNumber = input("Enter your credit card number here: ")

if luhn(cardNumber) and validateType(cardNumber):
    print("The card is valid")
else:
    print("This card is invalid")








