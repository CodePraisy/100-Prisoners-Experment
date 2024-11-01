# 100-Prisoners-Experiment

This repository simulates the _100 Prisoners Problem_, a famous probability puzzle involving strategy selection. In this puzzle, prisoners attempt to locate their numbered slips from randomly ordered boxes. The goal is to maximize the prisoners' chances of success under varying experimental setups. The program is customizable, allowing the selection of strategies, the number of prisoners, the number of search attempts, and the number of trials.

## Overview

### This project features:

- **Multiple Strategies:** Implements the Random and Loop strategies (see strategies.py) for prisoner attempts.
- **Configurable Setup:** This option allows the user to set the number of prisoners, chances per prisoner, and the number of trials.
- **Simulation:** Runs multiple trials and tracks outcomes, success rates, and average attempts.

## Features

- **Colorized Command Line Interface:** Displays interactive prompts for input and progress.
- **Detailed Statistics:** Calculates total success rate, average tries, win rate, and more.
- **Infinite Trials Mode:** Allows a prolonged or infinite simulation for statistical analysis.

## Installation

-   Clone the repository:
`git clone https://github.com/CodePraisy100-prisoners-experiment.git` then  `100 Prisoners`
- Install the dependencies:
`pip install -r requirements.txt`

## Usage 

Run the simulation:

`python main.py`

The program will guide you through setting up the experiment:

- Choose a strategy.
- Specify the number of prisoners.
- Set the number of chances each prisoner has to find their number.
- Define the number of trials (use "inf" for infinite trials).

### Strategies

- **Random Strategy:** Prisoners open random boxes.
- **Loop Strategy:** Prisoners follow a predefined loop based on the content of each box.

To add new strategies, define a new function in `strategies.py` and add it to `strategy_list`.

### Example Output

After selecting the setup, the program runs trials and outputs:

- Number of correct guesses per trial
- Success rate and win rate
- Average number of attempts per trial
- Cumulative statistics over all trials

## Files

- `main.py`: Main file to run the experiment.
- `functions.py`: Utility functions for calculating statistics, building boxes, etc.
- `strategies.py`: Contains the strategy implementations.
