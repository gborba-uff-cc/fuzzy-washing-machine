# imports
import random
import time
from fuzzify import *
from ascii_art import washing_machine_art as art
import os
import platform

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
        clearCmd = ''
        systemType = platform.system().lower()
        if systemType == 'windows':
            clearCmd = 'clear'
        elif systemType == 'linux':
            clearCmd = 'cls'
        while True:
            type_of_dirt = round(random.randint(0,99) + random.random(),2)
            degree_of_dirt = round(random.randint(0,99) + random.random(), 2)
            soap_amount = round(random.randint(0,99) + random.random(), 2)
            clothes_amount = round(random.randint(0,99) + random.random(), 2)
            washing_time = round(compute_washing_parameters(type_of_dirt, degree_of_dirt, soap_amount, clothes_amount), 2)

            for i in range(int(washing_time)):
                if clearCmd:
                    os.system('cls')
                print(f'The washing machine is {clothes_amount}% full with an amount {soap_amount} of soap, the clothes are {degree_of_dirt} points on degree of dirtiness and the type of dirt being {type_of_dirt}.\n')
                print(f"Time required to wash all clothes is {washing_time} minutes.\n")
                if clearCmd:
                    print(art[i%2])
                text = f'[time until done washing {int(washing_time)-i}s]'
                print(f'{text:<30}',flush=True)
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    exit(0)
