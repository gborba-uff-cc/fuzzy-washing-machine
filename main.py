# imports
import random
import time
from fuzzify import *
from ascii_art import washing_machine_art as art

# washing parameters
def compute_washing_parameters(type_of_dirt, degree_of_dirt, soap_amount, clothes_amount):

    if type_of_dirt < 0.0 or type_of_dirt > 100.0:
        raise Exception("Invalid Type of Dirtiness: %lf" % type_of_dirt)
    if degree_of_dirt < 0.0 or type_of_dirt > 100.0:
        raise Exception("Invalid Degree of Dirtiness: %lf" % degree_of_dirt)
    if 0 > soap_amount < 100:
        raise Exception("Invalid Amount of Soap: %lf" % soap_amount)
    if 0 > clothes_amount < 100:
        raise Exception("Invalid Amount of Clothes: %lf" % clothes_amount)

    type_fuzzy = fuzzify_laundry(type_of_dirt, degree_of_dirt, soap_amount, clothes_amount)

    return type_fuzzy


if __name__ == "__main__":
    try:
        while True:
            type_of_dirt = round(random.randint(0,99) + random.random(),2)
            degree_of_dirt = round(random.randint(0,99) + random.random(), 2)
            soap_amount = round(random.randint(0,99) + random.random(), 2)
            clothes_amount = round(random.randint(0,99) + random.random(), 2)
            print(f'Running with type of dirt {type_of_dirt} and degree of dirt {degree_of_dirt}')

            washing_time = round(compute_washing_parameters(type_of_dirt, degree_of_dirt, soap_amount, clothes_amount), 2)
            print(f"Time required to wash is {washing_time} minutes.\n")

            for i in range(int(washing_time)):
                text = f'time to finish washing {int(washing_time)-i}'
                print(f'{text:<30}', end='')
                time.sleep(1)
                print('\r',end='')
    except KeyboardInterrupt:
        pass
    exit(0)
