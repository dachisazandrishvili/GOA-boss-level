import random
user_move = random.randint(1,6)
computer_move = random.randint(1,6)
if user_move > computer_move: 
  print("you win! your number is " + str(user_move) + " and computer's number is  " + str(computer_move) + " congratulations!")
elif user_move == computer_move:
  print("it's Tie! your number is " + str(user_move) + " and computer's number is  " + str(computer_move) + " be stronger next time!")
else:
  print("you lose! your number is " + str(user_move) + " and computer's number is  " + str(computer_move) + " remember all sucsess comes from faliure!")

