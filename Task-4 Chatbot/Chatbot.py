def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created by {0}.".format(birth_year))


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; that's a good time to start programming!".format(age))


def count():
    print('I can count to any number you want, You can test me by entering a number.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


    print(' ')
    print('Completed')
    print(' ')
    print('*')
    print('* *')
    print('* * *')


def end():
    print('Congratulations, have a nice day!')
    print(' ')
    print('* * * *')
    print('* * * * *')
    print('* * * * * *')
    input()
    
greet('Killer ka bot', 'Aniket')
remind_name()
guess_age()
count()
end()
