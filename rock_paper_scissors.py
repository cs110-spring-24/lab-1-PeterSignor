import random
cpu = random.randint(1,3)
user = input("Enter rock, paper or scissors: ")
if user == "rock":
	if cpu == 1: # cpu chose rock
		print("Tie game")
	elif cpu == 2 : #cpu chose paper
		print("You lost")	
	else: #cpu choose scissors
		print("You win")	

if user == "paper":
	if cpu == 1: # cpu chose rock
		print("You chose paper.")
		print("The cpu chose rock")
		print("You Win")
	elif cpu == 2 : #cpu chose paper
		print("You chose paper.")
		print("The cpu chose paper")
		print("Its a Tie")	
	else: #cpu choose scissors
		print("You chose paper.")
		print("The cpu chose scissors")
		print("You Lose")

if user == "scissors":
	if cpu == 1: # cpu chose rock
		print("You lost")
	elif cpu == 2 : #cpu chose paper
		print("You win")	
	else: #cpu choose scissors
		print("Tie Game")				
