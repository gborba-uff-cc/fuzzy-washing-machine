# imports
import random
import subprocess
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


def ChooseClearCommand():
    for cmd in ('cls','clear'):
        try:
            retcode = subprocess.call(
                cmd,
                shell=True,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)
            if retcode == 0:
                return cmd
        except OSError:
            pass
    return ''


def WriteScreen(
    type_of_dirt,
    degree_of_dirt,
    soap_amount,
    clothes_amount,
    remaining_time
):
    print(f'ctrl + c to stop the program\n')
    print(f'The washing machine is {clothes_amount}% full with an amount of {soap_amount} soap, the clothes are {degree_of_dirt} points on degree of dirtiness and the type of dirt being {type_of_dirt}.\n')
    print(f"Time required to wash all clothes is {washing_time} minutes.\n")
    print(art[remaining_time%2])
    print(end='',flush=True)
    PrintRemainingTime(remaining_time)
    return None

def PrintRemainingTime(seconds):
    text = f'[time until done washing is {seconds}s]'
    print(f'{text:<35}',end='',flush=True)
    return None

if __name__ == "__main__":
    clearCmd = ChooseClearCommand()
    try:
        while True:
            type_of_dirt = round(random.randint(0,99) + random.random(),2)
            degree_of_dirt = round(random.randint(0,99) + random.random(), 2)
            soap_amount = round(random.randint(0,99) + random.random(), 2)
            clothes_amount = round(random.randint(0,99) + random.random(), 2)
            washing_time = round(compute_washing_parameters(type_of_dirt, degree_of_dirt, soap_amount, clothes_amount), 2)

            WriteScreen(type_of_dirt,degree_of_dirt,soap_amount,clothes_amount,0)
            for i in range(int(washing_time)):
                remaining_time=int(washing_time)-i
                if clearCmd:
                    os.system(clearCmd)
                    WriteScreen(type_of_dirt,degree_of_dirt,soap_amount,clothes_amount,remaining_time)
                else:
                    print(end='\r')
                    PrintRemainingTime(remaining_time)
                time.sleep(1)
            if clearCmd:
                os.system(clearCmd)
            else:
                print('','-'*40,sep='\n')
    except KeyboardInterrupt:
        pass
    exit(0)
