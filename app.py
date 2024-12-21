import random

def computer_guess(x):
    Low = 1
    high = x
    feedback = ''
    
    while feedback != 'c': 
        if Low != high:
            guess = random.randint(Low, high)  
        else:
            guess = Low  
        
       
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == 'h':
            high = guess - 1  
        elif feedback == 'l':
            Low = guess + 1  
        elif feedback == 'c':
            print(f'Yay! The computer guessed your number, {guess}, correctly!')
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")
computer_guess(1000)
