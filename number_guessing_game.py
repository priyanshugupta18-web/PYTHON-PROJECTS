from random import *

while(True):
    ran_num = randint(1, 100)
    guesses = 0
    while(True):
        inp = int(input("ENTER YOUR GUESS(1-100): "))
        guesses += 1
        if ((inp > ran_num) and (inp < 100)):
            print("YOUR GUESS IS TOO HIGH")
        elif ((inp < ran_num) and (inp > 0)):
            print("YOUR GUESS IS TOO LOW")
        elif (inp == ran_num):
            print(f"CONGRATULATIONS! YOU HAVE GUSSED THE RANDOMLY GENERATED NUMBER IN {guesses} ATTEMPTS")
            break 
        else:
            print("NUMBER ENTERED IS OUT OF RANGE")

        int_response = int(input("DO YOU WANT TO CONTINUE((1 for YES) AND (0 for NO)): "))

        if (int_response == 1):
            print("PROCESSING REQUEST...")
            continue
        elif (int_response == 0):
            print("PROCESSING REQUEST...")
            print("EXITED SUCCESSFULLY")
            break
        elif((int_response != 1) and (int_response != 0)):
            print("INVALID INPUT, PROCESSING NEXT ITERATION...")
    
    ext_response = int(input("DO YOU WANT TO RESTART((1 for YES) AND (0 for NO)): "))

    if (ext_response == 1):
        print("STARTING ANOTHER GAME...")
        continue
    elif (ext_response == 0):
        print("YOU HAVE CHOOSEN TO EXIT, PROCESSING REQUEST...")
        break