try: # the whole script is in a try statement to make keyboard interupt (like ctrl+c) close the program cleanly

    from mpmath import mp # import mpmath to get pi
    import time, sys, msvcrt # import time to do timers, sys to do various system related things, and msvcrt to do the "Press any key to continue..." prompt
    from typePrint import typePrint
    from isValidNum import isNum
    print() # this is to make a like break at start

    typePrint("Welcome to the pi calculator!", 0.03, 2)
    time.sleep(0.4)

    while True:
        typePrint('Please enter how many digits of pi you would like, or type "exit" to quit: ', 0.03, 0)

        digits = input()

        while not isNum(digits) and not digits.lower() == "exit":
            # print() is not needed because input() made a newline.
            typePrint('Please either input a valid number of digits or the word "exit": ', 0.03, 0)
            digits = input()

        if isNum(digits):
            mp.dps = int(digits)

            pi = mp.pi # calculate the pi!

            typePrint(f"\nHere are your {digits} digits of pi:\n{pi}", 0.01, 0)
            time.sleep(0.7) # wait...
            print() # newline for the next typeprint
            typePrint("Press any key to continue...", 0.04, 0)
            msvcrt.getch()
            print(f'\n') # two more new line before the next repeat! (the print does one and the \n does one)
        else:
            typePrint(f"\nBye!! Thank you for using the pi calculator!!", 0.04, 0)
            time.sleep(1)
            print()
            sys.exit(0)

except KeyboardInterrupt:
    print(f"\nKeyboard interupt recieved, exiting...")
    sys.exit(0) # sys.exit(0) closes the application with a successful exit code