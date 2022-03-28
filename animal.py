#!/usr/bin/python3

while True:
    print("1. Dog 🐶")
    print("2. Cat 🐈")
    print("3. Turtle 🐢")
    print("0. Exit")
    opcion = int(input("Enter an option: "))
    if opcion == 1:
        print('''
                    __
        (\,--------'()'--o
        (_    ___    /~"
          (_)_)  (_)_)
        ''')
    elif opcion == 2:
        print('''
         _._     _,-'""`-._
        (,-.`._,'(       |\`-/|
            `-.-' \ )-`( , o o)
                 `-    \`_`"'-
        ''')
    elif opcion == 3:
        print('''
          _____     ____
        /      \  |  o | 
        |        |/ ___\| 
        |_________/     
        |_|_| |_|_|
        ''')
    elif opcion == 0:
        break
    else:
        print("Incorrect option")    