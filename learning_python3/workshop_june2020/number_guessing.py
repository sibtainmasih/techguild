from random import randint
print("="*32)
print("Welcome to Number Guessing Game!")
print("="*32)

name=input("Enter your name: ")
number=randint(1,20)
count=1
max_attempts=5
print(f"\nYou will get {max_attempts} chances to guess a number between 1 to 20. Game starts....")

while count<=max_attempts:
	guess = int(input(f"\nAttempt {count} - Enter your guess: "))

	if guess == -1:
		print("\nTerminating...")
		break

	if guess == number:
		print("\nCongratulations! Your guess is correct.")
		break
	else:
		print("Try again")
	count+=1
else:
	print(f"You have exhausted all the attempts. The number was {number}.")

print(f"Thank you {name} for playing with us. Visit Again.")
