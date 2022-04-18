import datetime
from typing import overload


class Entry:
    def __init__(self, address: str, available: bool, last_used: datetime):
        self.address = address
        self.available = available
        self.last_used = last_used
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        pass
    def __le__(self, other):
        return self.address <= other.address

    def __ge__(self, other):
        return self.address >= other.address

    def __lt__(self, other):
        return self.address < other.address

    def __gt__(self, other):
        return self.address > other.address

    def __eq__(self, other):
        return self.address == other.address

    def __ne__(self, other):
        return self.address != other.address

