import os
import platform

from random import random, randrange, shuffle

def fasterRandom(max):
    new = randrange(0, max+1)
    
    if new == 0:
        new = 1
    
    return new

def build_boxes(box_count):
    boxes = []
    
    for box in range(box_count):
        boxes.append(box + 1)

    shuffle(boxes)

    return boxes

def isBoxOpen(box, open_boxes):   
    box_open = False

    for open_box in open_boxes:
        if open_box == box:
            box_open = True 

    return box_open

def build_info(results):
    prisoners = len(results)
    
    correct = 0
    average_tries = 0

    for result in results:    
        if result[1]:
            correct += 1
            average_tries = average_tries + result[2]

    success_rate = correct / (prisoners / 100)

    if success_rate == round(success_rate):
        success_rate = int(success_rate)

    if correct != 0:
        average_tries = average_tries / correct

    return correct, success_rate, average_tries

def clear_print():
    os_name = platform.system()
    
    if os_name == "Linux":
        os.system('clear')
    elif os_name == "Windows":
        os.system('cls')

def get_percentage(total, slice):
    return slice / (total / 100)

def get_average(li):
    return_value = 0

    for value in li:
        return_value += value

    return return_value / len(li)