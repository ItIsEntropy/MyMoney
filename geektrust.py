import sys
from io import FileIO
from tkinter import E
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
current_month: int = 0;
change_percentages: Dict[str, np.ndarray] = {}
weights: np.ndarray = {}

def perform_rebalance():
    global current_month
    if current_month < 6:
        print('CANNOT_REBALANCE')
        return
    for n in range(current_month):
        pass # TODO: rebal

def increment_month():
    global current_month
    if current_month == 12:
        current_month = 0
    else:
        current_month += 1
    if current_month == 6 or current_month == 12:
        perform_rebalance()

def perform_sip(values: List = None):
    global sip_ammount
    global pre_balance_portfolio
    if current_month < 2:
        print('ERROR: cannot do a SIP in JANUARY')
        return
    if values is not None:
        sip_ammount = np.array(values)
    pre_balance_portfolio[months[current_month]] = np.sum(sip_ammount, pre_balance_portfolio[months[current_month - 1]])
    increment_month()

def perform_allocate(values: List):
    global pre_balance_portfolio
    global weights
    if current_month > 1:
        print('Error: can only allocate in January')
    pre_balance_portfolio['JANUARY'] = np.array(values)
    total = sum(values)
    weights = np.array([(i/total) * 100 for i in values])
    increment_month()
    
def perform_change(percentages: np.ndarray, month: str):
    global change_percentages
    change_percentages[month] = np.array(percentages)

def perform_balance(month: str):
    global post_balance_portfolio
    for ammount in np.floor(post_balance_portfolio[month]).tolist():
        print(ammount, end=" ")

def process_commands(command_file: str):
    line: str = command_file.readline()
    args = line.split(' ')
    if args[0] == 'ALLOCATE':
        perform_allocate(args[1:])
    elif args[0] == 'SIP':
        perform_sip()
    elif args[0] == 'BALANCE':
        perform_balance(args[1])
    elif args[0] == 'CHANGE':
        perform_change(args[1:4])
    elif args[0] == 'REBALANCE':
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