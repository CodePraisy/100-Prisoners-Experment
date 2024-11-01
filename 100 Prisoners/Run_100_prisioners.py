import math

from colorama import Fore, Style
from time import sleep

from functions import build_boxes, clear_print, get_average, get_percentage, build_info
from strategies import strategy_list

clear_print()

approach = 0
prisoners = 0
chances = 0
trials = 0

while True:
    print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}The 100 Prisoners Experiment{Style.RESET_ALL}\n")
    print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Options\n{Style.RESET_ALL}")

    for index, strategy in enumerate(strategy_list):
        print(f"{Fore.LIGHTYELLOW_EX}[{index}]           {strategy.__name__}{Style.RESET_ALL}")
    
    print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
    
    try:
        option = input(f"{Fore.LIGHTCYAN_EX}Which approach to the {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'100 Prisoners'{Style.RESET_ALL}{Fore.LIGHTCYAN_EX} experiment would you like to take?{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}\n:")
        option = int(option)

        if option == abs(option):
            if option < len(strategy_list):
                approach = strategy_list[option]
                print(f"\n{Fore.LIGHTGREEN_EX}Running the {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'100 Prisoners'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} experiment with the {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{approach.__name__}{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} approach.{Style.RESET_ALL}")
                break
        
        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()
    except:
        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()

print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
input(f"{Fore.LIGHTCYAN_EX}Press enter to continue.{Style.RESET_ALL}{Style.BRIGHT}\n:")

clear_print()

while True:
    print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
    
    try:
        prisoners = input(f"{Fore.LIGHTCYAN_EX}How many prisoners would you like?{Style.RESET_ALL}{Style.BRIGHT}\n:")
        prisoners = int(prisoners)

        if prisoners == abs(prisoners):
            print(f"\n{Fore.LIGHTGREEN_EX}There will be {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'{prisoners}'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} prisoners in this experiment.{Style.RESET_ALL}")
            break
        
        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()
    except:
        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()

print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
input(f"{Fore.LIGHTCYAN_EX}Press enter to continue.{Style.RESET_ALL}{Style.BRIGHT}\n:")

clear_print()

while True:
    print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
    print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Choose amount of chances.{Style.RESET_ALL}\n")
    print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Options\n{Style.RESET_ALL}")
    
    options = [round(prisoners / 4), round(prisoners / 2), False]

    print(f"{Fore.LIGHTYELLOW_EX}[1]                Quarter ({options[0]}){Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}[2]                Half ({options[1]}){Style.RESET_ALL}")
    print(f"{Fore.LIGHTYELLOW_EX}[3]                Custom{Style.RESET_ALL}")
    
    print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")

    try:
        chances = input(f"\n{Fore.LIGHTCYAN_EX}Which one would you like to use?{Style.RESET_ALL}{Style.BRIGHT}\n:")
        chances = int(chances)
        chances = chances - 1
        
        if chances == abs(chances):
            if chances < len(options):
                chances = options[chances]
                break

        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()
    except:
        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()    

if chances != False:
    print(f"\n{Fore.LIGHTGREEN_EX}There will be {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'{chances}'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} chances to find their number in {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'{prisoners}'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} different boxes in this experiment.{Style.RESET_ALL}")

if chances == False:
    while True:
        try:
            clear_print()
            print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
            
            chances = input(f"\n{Fore.LIGHTCYAN_EX}How many chances would you like the prisoners to have? (Max: {prisoners}){Style.RESET_ALL}{Style.BRIGHT}\n:")
            chances = int(chances)

            if chances == abs(chances):
                if chances <= prisoners:
                    if chances != 0:
                        print(f"\n{Fore.LIGHTGREEN_EX}There will be {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'{chances}'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} chances to find their number in {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'{prisoners}'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} different boxes in this experiment.{Style.RESET_ALL}")
                        break
                    else:
                        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input. (Can't be 0.)")
                        sleep(3)
                        clear_print()   
                else:
                    print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input. (Must be less then prisoners. [{prisoners}]){Style.RESET_ALL}")
                    sleep(3)
                    clear_print()
            else:
                print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input. (Must be a positive value.){Style.RESET_ALL}")
                sleep(3)
                clear_print()
        except:
            print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
            sleep(3)
            clear_print()

print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
input(f"{Fore.LIGHTCYAN_EX}Press enter to continue.{Style.RESET_ALL}{Style.BRIGHT}\n:")

while True:
    clear_print()
    print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")

    try:
        trials = input(f"{Fore.LIGHTCYAN_EX}How many trials would you like? (for infinite, say 'inf'.){Style.RESET_ALL}{Style.RESET_ALL}\n:")

        if trials.lower() == "inf":
            trials = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            print(f"\n{Fore.LIGHTGREEN_EX}There will be {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'infinite'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} in this experiment.{Style.RESET_ALL}")
            break

        trials = int(trials)

        if trials == abs(trials):
            print(f"\n{Fore.LIGHTGREEN_EX}There will be {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}'{trials}'{Style.RESET_ALL}{Fore.LIGHTGREEN_EX} in this experiment.{Style.RESET_ALL}")
            break

        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()  
    except:
        print(f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}Invaild input.{Style.RESET_ALL}")
        sleep(3)
        clear_print()  

clear_print()

print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")

print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Overview{Style.RESET_ALL}\n")

print(f"{Fore.LIGHTYELLOW_EX}Approach:           {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{approach.__name__}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Prisoners:          {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{prisoners}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Chances:            {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{chances} ({get_percentage(prisoners, chances)}% of boxes.){Style.RESET_ALL}")
if trials > 9999999999:
    print(f"{Fore.LIGHTYELLOW_EX}Trials:             {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}infinite{Style.RESET_ALL}")
else:
    print(f"{Fore.LIGHTYELLOW_EX}Trials:             {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{trials}{Style.RESET_ALL}")


print(f"\n\n{Style.BRIGHT}If you want to change the settings, please restart this program.{Style.RESET_ALL}")

print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
input(f"{Fore.LIGHTCYAN_EX}Press enter to start.{Style.RESET_ALL}{Style.BRIGHT}\n:")

clear_print()
print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")

total = 0
wins = 0

total_correct = 0

total_average_tries = []
total_success_rate = []

for trial in range(trials):
    boxes = build_boxes(prisoners)
    results = approach(boxes, chances)

    correct, success_rate, average_tries = build_info(results)
    
    total_correct += correct
    
    total_success_rate.append(success_rate)
    total_average_tries.append(average_tries)

    total += 1    

    x_stat = trials
    y_stat = f"{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}everyone was executed.{Style.RESET_ALL}"
    
    if trials > 99999999999999:
        x_stat = "infinite"
    
    if success_rate == 100:
        y_stat = f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{Style.BRIGHT}everyone escaped!{Style.RESET_ALL}"
        wins += 1

    print(f"({trial+1}/{x_stat}) Correct: {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}{correct}{Style.RESET_ALL} || Success Rate: {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{success_rate}%{Style.RESET_ALL} || Average Tries: {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{average_tries}{Style.RESET_ALL} || Win-Rate: {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTCYAN_EX}{get_percentage(total,wins)}%{Style.RESET_ALL} || {y_stat}")

total_success_rate = get_average(total_success_rate)
total_average_tries = get_average(total_average_tries)
total_winrate = get_percentage(total,wins)

print(f"\n{Fore.LIGHTYELLOW_EX}----------------------------------------------------{Style.RESET_ALL}\n")
print(f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Results{Style.RESET_ALL}\n")

print(f"{Fore.LIGHTYELLOW_EX}Approach:            {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{approach.__name__}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Prisoners:           {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{prisoners}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Chances:             {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{chances} ({get_percentage(prisoners, chances)}% of boxes.){Style.RESET_ALL}")
if trials > 9999999999:
    print(f"{Fore.LIGHTYELLOW_EX}Trials:              {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}infinite{Style.RESET_ALL}")
else:
    print(f"{Fore.LIGHTYELLOW_EX}Trials:              {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{trials}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Wins:                {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{wins}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Losses:              {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{total - wins}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Total Winrate:       {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{total_winrate}%{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Total Success Rate:  {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{total_success_rate}%{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Total Average Tries: {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{total_average_tries}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Total Correct:       {Style.RESET_ALL}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{total_correct}/{prisoners*trials}{Style.RESET_ALL}")
