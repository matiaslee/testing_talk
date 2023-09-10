from random import random


def get_a_random_number_well_formatted():
    now = random()
    message = f"El número exacto es {now:.4f}!!!"
    return message


if __name__ == '__main__':
    msg = get_a_random_number_well_formatted()
    print(msg)
