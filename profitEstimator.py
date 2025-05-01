def estimate_profit(totalWaitingTime, startingWaitingTime):
    # estimate the profit based on the total waiting time and the starting waiting time
    # the profit is based off of time saved multiplied by average money saved on gas per second
    # average money saved on gas per second is 0.02 cents / second, this is found by doing this:
        # Fuel consumption while idling: ~0.2 to 0.5 gallons/hour (typical range for modern cars)
        # Gasoline price: $3.50 per gallon (typical US average)
    
    return totalWaitingTime - startingWaitingTime * 0.0002
