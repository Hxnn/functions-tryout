question = input("What do you want to do with the number[s] that you've chosen? Choose: addition/subtraction/multiplication/division/increment/decrement. ")
if question == "addition" or 'subtraction' or "multiplication" or "division":
    number1 = int(input('Choose a number. '))
    number2 = int(input('Choose another number. '))
else:
    number1 = int(input('Choose a number. a'))

if question == "addition":
    def addition(ad):
        print(ad)
    addition(number1 + number2)
    answer = number1 + number2
    print(number1, "+", number2, "=", answer)
elif question == "subtraction":
    def subtraction(sub):
        print(sub)
    subtraction(number1 - number2)
    answer = number1 - number2
    print(number1, "-", number2, "=", answer)
elif question == "multiplication":
    def multiplication(multi):
        print(multi)
    multiplication(number1 * number2)
    answer = number1 * number2
    print(number1, "*", number2, "=", answer)
elif question == "division":
    def division(div):
        print(div)
    division(number1 / number2)
    answer = number1 / number2
    print(number1, ":", number2, "=", answer)
elif question == "increment":
    def increment(increm):
        print(increm)
    increment(number1 + 1)
    answer = number1 + 1
    print(number1, "+", 1, "=", answer)
else:
    def decrement(decrem):
        print(decrem)
    decrement(number1 - 1)
    answer = number1 - number2
    print(number1, "-", 1, "=", answer)


