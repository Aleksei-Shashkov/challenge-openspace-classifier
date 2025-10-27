import random
import json

from utils.table import *
# from .table import Table

class Openspace:
    def __init__(self, tables): # Initialize the Openspace with a list of Table objects.
        self.tables = tables
        self.number_of_tables = len(tables)

    def organize(self, names): # Randomly assign people to available seats across all tables
        random.shuffle(names)
        all_seats = []
        for table in self.tables:
            for seat in table.seats:
                all_seats.append(seat)
        # all_seats = [seat for table in self.tables for seat in table.seats]

        if len(names) > len(all_seats):
            raise ValueError("Not enough seats")

        for seat, name in zip(all_seats, names): # creates pairs until it runs out of shorter sequences.
                                                 # That is, extra elements from a longer list are ignored.
            seat.set_occupant(name)

    def display(self): # display tables and their occupants
        print("\n OPENSPACE SEATING PLAN ") # Title
        for i, table in enumerate(self.tables, start=1): # iterates through the elements of a list and gets their ordinal numbers
                                                         # enumerate() turns a regular list into a sequence of (index, element) pairs.
            print(f"\nTable {i} (capacity: {table.capacity})")
            for j, seat in enumerate(table.seats, start=1):
                
                occupant = seat.occupant if seat.occupant else "Empty"
                print(f"  Seat {j}: {occupant}")

    def store(self, filename): # Save result in a JSON file.
        data = {}
        for i, table in enumerate(self.tables, start=1):
            occupants = []
            for seat in table.seats:
                if seat.occupant:
                    occupants.append(seat.occupant)
                else:
                    occupants.append(None)
            data[f"Table {i}"] = occupants
            
            # data[f"Table {i}"] = [seat.occupant if seat.occupant else None for seat in table.seats]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"\nResult saved to '{filename}'!")