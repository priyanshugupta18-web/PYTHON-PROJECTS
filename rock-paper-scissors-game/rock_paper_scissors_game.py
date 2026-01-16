from random import choice

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0
tie = 0

n = int(input("ENTER THE NUMBER OF ROUNDS: "))
print("\nINITIALISING THE GAME...\n")
for i in range(0, n):
	computer_choice = choice(choices)

	print(f"\nROUND {i+1}\n")
	user_choice = input("ENTER 'ROCK', 'PAPER' OR 'SCISSOR': ").lower()
	print(f"USER HAS CHOOSEN: {user_choice}")
	print(f"COMPUTER HAS CHOOSEN: {computer_choice}")
	
	if user_choice not in choices:
		print("INVALID INPUT, EXITING THE PROGRAM...")
		break 
	else:
		if (user_choice == computer_choice):
			print("IT'S A TIE...")
			tie += 1
		else:
			if ((user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper")):
				print("YOU WON THIS ROUND")
				user_score += 1
			else:
				print("COMPUTER WON THIS ROUND")
				computer_score += 1
	
	if (i != (n-1)):
		response = input("WOULD YOU LIKE TO CONTINUE(YES/NO): ")
		
		if (response == ("yes")):
			print("PROCESSING YOUR REQUEST...")
		elif (response == ("no")):
			print("EXISTING THE PROGRAM...")
			break
		else:
			print("INVALID INPUT, GET READY FOR THE NEXT ROUND...")
	else:
		print("\nGAME FINISHED, GETTING THE RESULT...")

print(f"\nUSER SCORE = {user_score}")
print(f"COMPUTER SCORE = {computer_score}")
print(f"TIE SCORE = {tie}")

if(user_score > computer_score):
	print("\nCONGRATULATIONS! YOU NAILED IT")
elif(user_score < computer_score):
	print("\nBETTER LUCK NEXT TIME")
else:
	print("\nAAH...IT'S A TIE")




