#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sidrah Hashmi # 100915053

############## Q1 ####################

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer greater than 0.")
    elif is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    
################ end ############################

######################### Q2 #######################

try:
    n = int(input("Enter a positive integer n: "))
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        even_sum = 0
        for i in range(2, n + 1, 2):
            even_sum += i
        print(f"The sum of even numbers from 1 to {n} is: {even_sum}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    
######################### end #########################

######################### Q3 ###########################

import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))

        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
        elif user_guess < random_number:
            print("Too low. Try again.")
        elif user_guess > random_number:
            print("Too high. Try again.")
        else:
            print(f"Number: {random_number} guessed correctly.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
########################### end #############################

######################### Q4 #################################

import random

def roll_die():
    return random.randint(1, 6)

def play_game():
    while True:
        player_A_roll = roll_die()
        player_B_roll = roll_die()
        
        print(f"Player A rolled: {player_A_roll}")
        print(f"Player B rolled: {player_B_roll}")
        
        if player_A_roll == 6:
            print("Player A wins!")
            break
        elif player_B_roll == 6:
            print("Player B wins!")
            break

if __name__ == "__main__":
    play_game()
    
######################### end ###########################


# In[ ]:





# In[ ]:




