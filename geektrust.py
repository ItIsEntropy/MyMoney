import sys
from typing import Dict, List
from pathlib import Path
import math

months: Dict[int, str] = {
    0: 'JANUARY',
    1: 'FEBRUARY', 
    2: 'MARCH', 
    3: 'APRIL', 
    4: 'MAY', 
    5: 'JUNE', 
    6: 'JULY', 
    7: 'AUGUST', 
    8: 'SEPTEMBER', 
    9: 'OCTOBER',
    10: 'NOVEMBER',
    11: 'DECEMBER',
    12: 'JANUARY'
}
pre_balance_portfolio: Dict[str, List] = {}
post_balance_portfolio: Dict[str, List] = {}
sip_ammount: List = []
current_month_number: int = 0
desired_percentages: List = []
already_rebalanced: bool = False

def perform_balance(month: str):
    _ = [print(math.floor(ammount), end=" ") for ammount in post_balance_portfolio[month]]
    print('')
        

def perform_rebalance():
    global already_rebalanced
    if already_rebalanced:
        already_rebalanced = False
        return
    if current_month_number < 5:
        print('CANNOT_REBALANCE')
        return
    current_month: str = months[current_month_number - 1]
    total: int = sum(post_balance_portfolio[current_month])
    desired_ammounts:List = [desired_percentage * total for desired_percentage in desired_percentages]
    post_balance_portfolio[current_month] = [math.floor(desired_ammount / 100) for desired_ammount in desired_ammounts]
    perform_balance(current_month)
    already_rebalanced = True

def increment_month():
    global current_month_number
    if current_month_number == 12:
        current_month_number = 0
    else:
        current_month_number += 1

def perform_sip(sip_values):
    global sip_ammount
    sip_ammount = sip_values
    
def perform_allocate(values: List):
    global pre_balance_portfolio
    global desired_percentages
    if current_month_number > 0:
        print('Error: can only allocate in January')
    pre_balance_portfolio['JANUARY'] = values
    total = sum(values)
    desired_percentages = [(i/total) * 100 for i in values]
    
def perform_change(percentages: List, month: str):
    
    change_percentages: List = percentages

    if month != 'JANUARY':
        pre_balance_portfolio[month] = [
            sip + portfolio_value for sip,portfolio_value  in zip(sip_ammount, post_balance_portfolio[months[current_month_number - 1]])
        ]

    percentages: List = [change_percentage / 100 for change_percentage in change_percentages]
    changes: List = [portfolio_value * percentage for portfolio_value, percentage in zip(pre_balance_portfolio[month], percentages)]

    post_balance_portfolio[month] = [
        math.floor(portfolio_value + change) for change, portfolio_value in zip(changes, pre_balance_portfolio[month])
    ]

    if current_month_number == 6 or current_month_number == 12:
        perform_rebalance()    
    increment_month()

def process_commands(command_file: str):
    for line in command_file:
        line_argumants = line.replace('\n', '').split(' ')
        if line_argumants[0] == 'ALLOCATE':
            clean_args: List = [float(num) for num in line_argumants[1:]]
            perform_allocate(clean_args)
        elif line_argumants[0] == 'SIP':
            clean_args = [float(num) for num in line_argumants[1:]]
            perform_sip(clean_args)
        elif line_argumants[0] == 'BALANCE':
            perform_balance(line_argumants[1])
        elif line_argumants[0] == 'CHANGE':
            perform_change([float(percentage.replace('%', '')) for percentage in line_argumants[1:-1]], line_argumants[-1])
        elif line_argumants[0] == 'REBALANCE':
            perform_rebalance()
        else: 
            print('ERROR: Unknown command')

def main():
    file_name: str = sys.argv[1]
    file_path: Path = Path(file_name)
    if not file_path.exists():
        print("Error: The file path you've entered does not exist")
        sys.exit(-1) 
    if not file_path.is_file():
        print("ERROR: Please enter a path to a valid file")
        sys.exit(-2)
    with open(file_path, mode='r') as f:
        process_commands(f)
    return 0
    
if __name__ == "__main__" :
    main()