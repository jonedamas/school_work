# This program calculates the velocity and distance an object has traveled
# after a set amount of time, and checks if the number is smaller than 0.
# The user gets another chance if the

time = float(input('Input seconds after fall: '))

velocity = 9.81 * time

distance = 0.5 * velocity * time

if time <= 0:
    print('Your number is smaller than or equal 0')
    time = float(input('Input seconds after fall: '))
else:
    print(f'The object has a velocity of {velocity:.2f} m/s, and has traveled a distance of {distance:.2f} m.')
