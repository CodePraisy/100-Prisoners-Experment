from ast import For
import os
import platform
from secrets import choice

from functions import build_boxes, build_info
from strategies import random_method
from colorama import Fore, Style

os_name = platform.system()

if os_name == "Linux":
    os.system('clear')

prisoners = 2
boxes = build_boxes(prisoners)
chances = round(prisoners / 2)

print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}prisoners: {prisoners} || chances: {chances}{Style.RESET_ALL}")
print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------{Style.RESET_ALL}\n")

results = random_method(boxes, chances)

for result in results:    
    if result[1]:
        print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX} Prisoner {Fore.LIGHTBLUE_EX}{result[0]}{Fore.LIGHTGREEN_EX} found their number in {Fore.LIGHTYELLOW_EX}{result[2]}{Fore.LIGHTGREEN_EX} attempts!{Style.RESET_ALL}")
    else:
        print(f"{Style.DIM}{Fore.LIGHTRED_EX} Prisoner {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{result[0]}{Fore.LIGHTRED_EX}{Style.RESET_ALL}{Style.DIM}{Fore.LIGHTRED_EX} couldn't find their number.{Style.RESET_ALL}")

correct, success_rate, average_tries = build_info(results)

print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------{Style.RESET_ALL}\n")

if prisoners == correct:
    print(f"{Fore.LIGHTYELLOW_EX} Every single prisioner found their box with an average of {average_tries} tries!{Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTGREEN_EX}, all the prisoners has been set free!{Style.RESET_ALL}")
else:
    print(f"{Fore.LIGHTYELLOW_EX}{success_rate}% of all prisoners found their box with an average within the winners of {average_tries} tries. {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTRED_EX}Everyone was executed.{Style.RESET_ALL}")