import math


def area_calc(length, width, angle):
    area = 0.5 * length * width * math.sin(math.radians(angle))
    return area


if __name__ == '__main__':
    length_a = float(input('Length a: '))
    length_b = float(input('Length b: '))
    angle_degrees = float(input('Angle in degrees: '))
    print(f'The area of the triangle is {area_calc(length_a, length_b, angle_degrees):.2f}.')
