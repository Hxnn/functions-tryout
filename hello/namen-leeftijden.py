def info():
    print("If you'd like to stop the program, type: stop")
    name = input('What is your name?: ')
    if name == 'stop':
        exit()
    age = input('What is your age?: ')
    if age == 'stop':
        exit()
    print('Hello {}'.format(name) +'.'+ ' Your age is: {}'.format(age))

while True:
    info()