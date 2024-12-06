# Joshua Phillips
# 12/6/24
# While loops practice
import random

# NUMBER GUESSING GAME:

name = input('Helle, please enter your username: ')
number = random.randint(1, 100)
print(f'Welcome {name}! Try to guess my special number. (Somewhere between 1-100)')
guesses_taken = 0

while guesses_taken < 5:
    guess = input('Enter a guess: ')
    guess = int(guess)
    guesses_taken += 1
    if guess < number:
        print('Ar nar, too low!')
    elif guess > number:
        print('Ar nar, Too high!')
    else:
        break
if guess == number:
    print('Congratzzz, YOU WIN A COOKIE.')
else:
    print(f'Too bad no cookie. The number was: {number}')


# TEMPERATURE AVERAGING:
name = input('Helle, please enter your username: ')
print(f'Welcome {name}! Please enter the temperatures below-->')

temps = []
while True:
    temp = int(input('Enter here: '))
    if temp == -9999:
        break
    else:
        temps.append(temp)
        number_of_temps = len(temps)

if number_of_temps >= 0:
    total = sum(temps)
    average = total / number_of_temps
    print(f'Your inputs were: {temps}')
    print(f'The average temperature is: {average}°')

