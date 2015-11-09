import numpy as np


def guessgame ():
    secret = np.random.randint (1, 4)
    print ('I have a number between 1 and 4.')
    guess = input ('Guess: ')
    guess = int (guess)
    if guess != secret:
        print ("Wrong, my number is ", secret, '.')
    else:
        print ("Right, my number is", guess, '!\n')


if __name__ == "__main__":
    guessgame ()
