import matplotlib.pyplot as plt

time = float(input('Input seconds between each interval: '))
intervals = int(input('Enter the number of intervals: '))

time_list = list()
distance_list = list()

if time <= 0:
    print('Your number is smaller than or equal 0')
    time = float(input('Input seconds between each interval: '))
else:
    for i in range(intervals):
        distance = 0.5 * 0.81 * (time * i) ** 2
        time_list.append(time * i)
        distance_list.append(distance)


plt.plot(time_list, distance_list)
plt.xlabel('Time')
plt.ylabel('Distance')


plt.show()
