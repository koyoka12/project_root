from enum import Enum  
  
class ReservationPriority(Enum):  
    HIGH = 1  
    MEDIUM = 2  
    LOW = 3  
  
class QueueNode:  
    def __init__(self, group_ID, arrival_time, reservation_priority):  
        self.group_ID = group_ID  
        self.arrival_time = arrival_time  
        self.reservation_priority = reservation_priority  
  
    def __repr__(self):  
        return f"Group ID: {self.group_ID}, Arrival Time: {self.arrival_time}, Priority: {self.reservation_priority.name}"  
  
    def __eq__(self, other):  
        if isinstance(other, QueueNode):  
            return self.group_ID == other.group_ID  
        return False