import random

def main():
    print("Welcome to the game, You have 7 tries to find the number I am guessing")
    Game(10,6)
    print("Time to get a bit harder")
    Game(100, 6)
    

def guess(n):
    if n == 0:
        return input("What is your initial guess? ")
    else:
        return input(f"What will be your {n+1} try! ")

def Game(n,numoftries):
    
    
    print("I am guessing a number from 1 to " , n)
    number = int(random.randint(1,n))
    for i in range(numoftries):
        value = int( guess(i))
        if value > number:
           print("my number is smaller, try again")
        elif value < number:
           print("my number is bigger, try again")
        elif value == number:
            print(f"Congrats! you found my number in your {i+1}th try")
            break
        else:
            print("Bad luck the nmber was:")
    
        
            
        

    
main()