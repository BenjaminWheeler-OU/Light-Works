import unittest

def check_negative(num):
    """Check if a number is non-negative."""
    if num <= 0:
        return False
    return True

class FocusedEmissionEstimate:
    def __init__(self, avg_stop_time, number_of_cars):
        """Initialize with average stop time and number of cars."""
        self.avg_stop_time = avg_stop_time
        self.number_of_cars = number_of_cars

    def valid_avg_stop_time(self):
        """Ensure avg_stop_time is not negative."""
        return check_negative(self.avg_stop_time)

    def valid_car_num(self):
        """Ensure number_of_cars is not negative."""
        return check_negative(self.number_of_cars)
    
if __name__ == "__main__":
    emission_estimate = FocusedEmissionEstimate(avg_stop_time=5.0, number_of_cars=10)
    print("Valid avg_stop_time:", emission_estimate.valid_avg_stop_time())
    print("Valid number_of_cars:", emission_estimate.valid_car_num())
