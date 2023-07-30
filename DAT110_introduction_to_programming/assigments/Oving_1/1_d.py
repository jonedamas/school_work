# This program calculates the velocity and distance an object has traveled
# after a set amount of time and intervals, and checks if the number is smaller than 0.

time = float(input('Input seconds between each interval: '))
intervals = int(input('Enter the number of intervals: '))

if time <= 0:
    print('Your number is smaller than or equal 0')
    time = float(input('Input seconds after fall: '))
else:
    for i in range(intervals):
        velocity = 9.81 * time * (i + 1)
        distance = 0.5 * velocity * time * (i + 1)
        print(f'At {int(time * (i + 1))} seconds, the object has a velocity of {velocity:.2f} m/s,'
              f' and has traveled a distance of {distance:.2f} m.')
