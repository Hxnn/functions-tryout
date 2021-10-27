def helloWorld() -> str:
    return 'Hello World!'

def helloWorld3() -> str:
    return 'Hello World!\nHello World!\nHello World!'

def helloWorld7() -> str:
    return 'Hello World!\nHello World!\nHello World!\nHello World!\nHello World!\nHello World!\nHello World!'

message = helloWorld()
message2 = helloWorld3()
message3 = helloWorld7()

vraag = int(input('Hoevaak wil je "Hello World!" zien? Kies uit: 1/3/7 '))
if vraag == 1:
    print(message)
elif vraag == 3:
    print(message2)
else:
    print(message3)

#   Code zonder vraag, input etc.
#   def helloWorld() -> str:
#    return 'Hello World!'

#   message1 = helloWorld()
#   print(message1)

