from io import FileIO
import sys
from typing import Dict, List
from pathlib import Path
import numpy as np

pre_balance_portfolio: Dict[str, np.ndarray] = np.zeros(3)
post_balance_portfolio: Dict[str, np.ndarray] = np.zeros(3)
sip_ammount: np.array = np.zeros(3)

def perform_sip(values: np.ndarray):
    pass

def perform_allocate(values: np.array):
    pre_balance_portfolio['JANUARY'] = np.array()
    pass

def perform_change(percentages: np.ndarray, month: str):
    pass

def perform_balance(month: str):
    pass

def perform_rebalance():
    pass

def process_commands(command_file: str):
    line: str = command_file.readline()
    pass

commands: Dict[str, function] = {''}

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