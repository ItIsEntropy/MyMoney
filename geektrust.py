import sys
from io import FileIO
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
pre_balance_portfolio: Dict[str, np.ndarray] = np.zeros(3)
post_balance_portfolio: Dict[str, np.ndarray] = np.zeros(3)
sip_ammount: np.ndarray = np.zeros(3)
current_month: int = 0;
change_percentages: Dict[str, np.ndarray] = np.zeros(3)
weights: np.ndarray = np.zeros(3)

def perform_rebalance():
    if current_month < 6:
        print('CANNOT_REBALANCE')
        return
    pass

def increment_month():
    if current_month == 12:
        current_month = 0
    else:
        current_month += 1
    if current_month == 6 or current_month == 12:
        perform_rebalance()

def perform_sip(values: List = None):
    if current_month < 2:
        print('ERROR: cannot do a SIP in JANUARY')
        return
    if values is not None:
        sip_ammount = np.array(values)
    pre_balance_portfolio[months[current_month]] = np.sum(sip_ammount, pre_balance_portfolio[months[current_month - 1]])
    increment_month()

def perform_allocate(values: List):
    if current_month > 1:
        print('Error: can only allocate in January')
    pre_balance_portfolio['JANUARY'] = np.array(values)
    increment_month()
    
def perform_change(percentages: np.ndarray, month: str):
    pass

def perform_balance(month: str):
    _ = [print(ammount, end=" ") for ammount in np.floor(post_balance_portfolio[month]).tolist() ]

def process_commands(command_file: str):
    line: str = command_file.readline()
    args = line.split(' ')
    if args[0] == 'ALLOCATE':
        perform_allocate(args[1:])
    elif args[0] == 'SIP':
        perform_sip()
    pass


def read_file(file_path: Path):
    with open(file_path, mode='r') as f:
        return f
        


def main(file_name: str):
    #file_name: str = sys.argv[1]
    file_path: Path = Path(file_name)
    if not file_path.exists():
        print("Error: The file path you've entered does not exist")
        return
    elif not file_path.is_file():
        print("ERROR: Please enter a path to a valid file")
        return
    else:
        command_file: FileIO = read_file(file_path)
        process_commands(command_file)
    

if __name__ == "__main__" :
    file_name: str = sys.argv[1]
    main(file_name=file_name)