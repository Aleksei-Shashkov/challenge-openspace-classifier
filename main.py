import random
import json
from utils.table import Table

from utils.openspace import Openspace

# import pandas as pd
with open('Members.txt', 'r', encoding='utf-8') as f:
    new_collegues = [line.strip() for line in f if line.strip()] 

if __name__ == "__main__":
        
    tables = [Table(4) for _ in range(6)] # Create 6 tables, each with 4 seats

    workspace = Openspace(tables)
    workspace.organize(new_collegues)
    workspace.display()
    workspace.store("openspace_seating.json")
