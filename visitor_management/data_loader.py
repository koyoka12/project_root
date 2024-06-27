import csv  
from tour_queue import TourQueue, ReservationPriority  
  
def load_dataset(filename):  
    queue = TourQueue()  
    with open(filename, mode='r', encoding='utf-8') as file:  
        reader = csv.DictReader(file)  
        for row in reader:  
            arrival_time = row['arrival_time']  # Assuming arrival_time is in a format that can be compared directly  
            reservation_priority = ReservationPriority[row['reservation_priority'].upper()]  
            group_ID = int(row['group_ID'])  
            queue.add_group(group_ID, arrival_time, reservation_priority)  
    return queue  
  
# Example usage:  
queue = load_dataset('cultural_heritage_visitors.csv')