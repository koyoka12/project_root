import heapq  
from queue_node import QueueNode, ReservationPriority  
import unittest  
  
class TourQueue:  
    def __init__(self):  
        self.queue = []  
        self._index = 0  
  
    def add_group(self, group_ID, arrival_time, reservation_priority):  
        priority = (arrival_time, reservation_priority.value, -self._index)  # Negative index for stable sorting  
        heapq.heappush(self.queue, (priority, QueueNode(group_ID, arrival_time, reservation_priority)))  
        self._index += 1  
  
    def remove_group(self):  
        if not self.is_empty():  
            _, node = heapq.heappop(self.queue)  
            return node  
  
    def peek_next_group(self):  
        if not self.is_empty():  
            _, node = self.queue[0]  
            return node  
  
    def reschedule_group(self, group_ID, new_arrival_time, new_reservation_priority):  
        for i, (priority, node) in enumerate(self.queue):  
            if node.group_ID == group_ID:  
                new_priority = (new_arrival_time, new_reservation_priority.value, -i)  
                heapq.heapreplace(self.queue, (new_priority, node))  
                break  
  
    def is_empty(self):  
        return not bool(self.queue)  
  
    # Additional tests can be added here or in a separate test file  
    class TestTourQueue(unittest.TestCase):  
        # ... add tests here ...  
  
# If running as a script, execute the tests  
if __name__ == "__main__":  
    unittest.main()