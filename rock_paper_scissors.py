import random
cpu = random.randint(1,3)
user = input("Enter rock, paper or scissors: ")
print ()
if user == "rock":
	if cpu == 1: # cpu chose rock
		print("You chose rock")
		print("Cpu chose rock")
		print("Tie game")	
	elif cpu == 2 : #cpu chose paper
		print("You chose rock")
		print("Cpu chose paper")
		print("You lost")	
	else: #cpu choose scissors
		print("you chose rock")
		print("cpu chose scissors")
		print("You win")	

if user == "paper":
	if cpu == 1: # cpu chose rock
		print("You chose paper.")
		print("The cpu chose rock")
		print("You win")
	elif cpu == 2 : #cpu chose paper
		print("You chose paper.")
		print("The cpu chose paper")
		print("Its a tie")	
	else: #cpu choose scissors
		print("You chose paper.")
		print("The cpu chose scissors")
		print("You lost")

if user == "scissors":
	if cpu == 1: # cpu chose rock
		print("You chose scissors")
		print("cpu chose rock")
		print("You lost")
	elif cpu == 2 : #cpu chose paper
		print("You chose scissors")
		print("Cpu chose paper")
		print("You win")
	else: #cpu choose scissors
		print("You chose scissors")
		print("Cpu chose scissors")
		print("Tie game")
print ()