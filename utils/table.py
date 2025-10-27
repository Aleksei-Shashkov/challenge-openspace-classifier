class Seat:
    def __init__(self): # Initialize a Seat object
        self.is_free = True # Indicates whether the seat is available.
        self.occupant = None # Name of the person occupying the seat.

    def set_occupant(self, name:str): # Assign someone to the seat if it is free
                  
        if not self.is_free:
            raise ValueError(f"This seat is occupied by {self.occupant}.") # If the seat is already occupied
        self.occupant = name
        self.is_free = False

    def remove_occupant(self): # Remove the current occupant from the seat
        if self.is_free:
            raise ValueError("This seat is empty.") # If the seat is already free.
        name = self.occupant
        self.occupant = None
        self.is_free = True
        return name
    
class Table:
    def __init__(self, capacity): # Initialize a table with a given number of seats
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)] # list of Seat objects

    def has_free_spot(self): #  returns True if a spot is available
        return any(seat.is_free for seat in self.seats) # 'any' - return True if at least one seat in the list is free

    def assign_seat(self, name): # Assign a person to a free seat at the table
        for seat in self.seats:
            if seat.is_free:
                seat.set_occupant(name)
                return
        raise ValueError("No free seats at this table.")

    def left_capacity(self): # Return the number of remaining free seats
        count = 0
        for seat in self.seats:
            if seat.is_free:
                count += 1
        return count
        # return sum(seat.is_free for seat in self.seats)    