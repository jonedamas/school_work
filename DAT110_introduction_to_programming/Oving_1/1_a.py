# This program calculates the velocity and distance an object has traveled
# after a set amount of time.

time = float(input('Input seconds after fall: '))

velocity = 9.81 * time

distance = 0.5 * velocity * time

print(f'The object has a velocity of {velocity:.2f} m/s, and has traveled a distance of {distance:.2f} m.')
