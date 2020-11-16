import datetime

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock
    """
      Our constructor class initiate bike rental shop
    """

    def display_stock(self):
        """
        Display currently available bike 
        """
        print(f"We have currently {self.stock} available Bike.")
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        """
        rent Bike on hourly basis and n is number of bike requested
        """
        if n < 0:
            print("Number of bikes should be positive.")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike(s) on hourly basis today at {now.hour} hours.")
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rent_bike_on_daily_basis(self, n):
        """
        rent bike on daily basis
        """
        if n < 0:
            print("Number of bike should be positive integer.")
        elif n > self.stock:
            print(f"Sorry! we have currently {self.stock} bike available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike on day basis today at {now.hour}.")
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock = self.stock - n
            return now
    

    def rent_bike_on_weekly_basis(self, n):
        """
        rent bike on weekly basis
        """
        if n < 0:
            print("Number of bike should be positive integer.")
        elif n > self.stock:
            print(f"Sorry! we have currently {self.stock} bike available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike on weekly basis today at {now.hour}.")
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock = self.stock - n
            return now

    def returnBike(self, request):
        """
        Accept rented bike from customer
        Return a bill
        """
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes:
            self.stock = self.stock + numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.second/3600)*5*numOfBikes

            # daily basis calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days)*20*numOfBikes
            
            # weekly basis calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("You would be ${bill}")
            return bill
        else:
            print("Are you sure you rented a with us?")
            return None


class Customer:
    
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
    
    def requestBike(self):
        """
        Take request from customer for number of bike to rent?
        """
        try:
            bike = int(input("How many bike you want to rent"))
        except:
            print("this is not positive integer number")
            return -1
        
        if bike < 1:
            print("Invalid Input, Number of bike should be positive integer ")
            return -1
        else:
            self.bike = bike

        return bike

    def returnBike(self):
        """
        Return rented bike to owner
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
















