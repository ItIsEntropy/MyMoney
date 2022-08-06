import sys
from typing import Dict, List
from pathlib import Path
import numpy as np

months: Dict[int, str] = {
    0: 'JANUARY',
    1: 'FEBUARY', 
    2: 'MARCH', 
    3: 'APRIL', 
    4: 'MAY', 
    5: 'JUNE', 
    6: 'JULY', 
    7: 'AUGUST', 
    8: 'SEPTEMBER', 
    9: 'OCTOBER',
    10: 'NOVEMBER',
    11: 'DECEMBER'
}
pre_balance_portfolio: Dict[str, np.ndarray] = {}
post_balance_portfolio: Dict[str, np.ndarray] = {}
sip_ammount: np.ndarray = np.zeros(3)
current_month: int = 0
weights: np.ndarray = {}

def perform_balance(month: str):
    for ammount in np.floor(post_balance_portfolio[month]).tolist():
        print(ammount, end=" ")

def perform_rebalance():
    if current_month < 6:
        print('CANNOT_REBALANCE')
        return
    # TODO: rebalance portfolio using weights
    print('incomplete')
    perform_balance(months[current_month])

def increment_month():
    global current_month
    if current_month == 12:
        current_month = 0
    else:
        current_month += 1
    if current_month == 6 or current_month == 12:
        perform_rebalance()

def perform_sip(sip_values: List = None):
    global sip_ammount
    global pre_balance_portfolio
    if current_month == 0:
        print('ERROR: cannot do a SIP in JANUARY')
        return
    if sip_values is None:
        pre_balance_portfolio[months[current_month]] = np.add(sip_ammount, pre_balance_portfolio[months[current_month - 1]])
    else:
        sip_ammount = np.array(sip_values)
    
def perform_allocate(values: List):
    global pre_balance_portfolio
    global weights
    if current_month > 1:
        print('Error: can only allocate in January')
    pre_balance_portfolio['JANUARY'] = np.array(values)
    total = sum(values)
    weights = np.array([(i/total) * 100 for i in values])
    increment_month()
    
def perform_change(percentages: List, month: str):
    global post_balance_portfolio
    change_percentages: np.ndarray = np.array(percentages)
    print(change_percentages)
    print(np.array([100,100,100]))
    perform_sip()
    # TODO: apply changes
    percentage: np.ndarray = np.divide(change_percentages, np.array([100, 100, 100]))
    change: np.ndarray = np.multiply(pre_balance_portfolio[month], percentage)
    post_balance_portfolio[month] =np.add(change, pre_balance_portfolio[month], percentage)
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

def main(file_name: str):
    #file_name: str = sys.argv[1]
    file_path: Path = Path(file_name)
    if not file_path.exists():
        print("Error: The file path you've entered does not exist")
        return
    if not file_path.is_file():
        print("ERROR: Please enter a path to a valid file")
        return
    with open(file_path, mode='r') as f:
        process_commands(f)
    

if __name__ == "__main__" :
    file_name: str = sys.argv[1]
    main(file_name=file_name)