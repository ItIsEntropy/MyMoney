import sys
from typing import Dict
from pathlib import Path
import numpy as np

def perform_sip(values: np.array):
    pass

def perform_allocate(values: np.array):
    pass

def perform_change(percentages: np.array, month: str):
    pass

def perform_balance(month: str):
    pass

commands: Dict[str, function] = {''}

def read_file(file_path: Path):
    with open(file_path, mode='r') as f:
        pass


def main(file_name: str):
    #file_name: str = sys.argv[0]
    file_path: Path = Path(file_name)
    if not file_path.exists():
        print("Error: The file path entered does not exist")
        return
    elif not file_path.is_file():
        print("ERROR: Please enter a path to a valid file")
        return
    else:
        read_file(file_path)
    

if __name__ == "__main__" :
    file_name: str = sys.argv[0]
    main(file_name=file_name)