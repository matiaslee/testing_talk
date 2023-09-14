from random import random


class Square():

    def __init__(self):
        self.side_length = int(random() * 10) + 1

    def area(self):
        return self.side_length ** 2


def get_the_area_of_a_random_square():
    square = Square()
    return f"I am a square with area {square.area()}"


if __name__ == '__main__':
    msg = get_the_area_of_a_random_square()
    print(msg)
