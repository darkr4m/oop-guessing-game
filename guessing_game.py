import random
class GuessingGame():
    """
    Initialized with an integer
    Start game with random number
    Instance methods
        #init
            answer - integer (random number)
        #guess
            input:
                user_guess - integer
            output:
                If user_guess > answer = high (string)
                if user_guess == answer = correct (string)
                If user_guess < answer = low (string)
        #solved
            if most recent user_guess == correct
                output = True (boolean)
            if most recent user_guess !== correct
                output = False (boolean)
    
    """
    # Write your code here
    def __init__(self, answer=random.randint(1,100)):
        self.answer = answer
        self.last_result = None #store result of the last guess
    
    def guess(self, user_guess):
        if user_guess > self.answer:
            self.last_result = 'high'
        elif user_guess == self.answer:
            self.last_result = 'correct'
        else:
            self.last_result = 'low'
        return self.last_result
    def solved(self):
        return self.last_result == 'correct'
        

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_guess = int(last_guess)
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")