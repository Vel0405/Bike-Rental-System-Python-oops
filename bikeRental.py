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
            
            self.stock = self.stock - n
            return now

    def returnbike(self, request):
        """
        Accept rented bike from customer
        Return a bill
        """
        # extract the tuple and initiate bill
        rentaltime, rentalbasis, numofbikes = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentaltime and rentalbasis and numofbikes:
            self.stock = self.stock + numofbikes
            now = datetime.datetime.now()
            rentalperiod = now - rentaltime

            # hourly bill calculation
            if rentalbasis == 1:
                bill = round(rentalperiod.second/3600)*5*numofbikes

            # daily basis calculation
            elif rentalbasis == 2:
                bill = round(rentalperiod.days)*20*numofbikes
            
            # weekly basis calculation
            elif rentalbasis == 3:
                bill = round(rentalperiod.days / 7) * 60 * numofbikes
            
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
        self.rentalbasis = 0
        self.rentaltime = 0
        self.bill = 0
    
    def requestbike(self):
        """
        Take request from customer for number of bike to rent?
        """
        try:
            bike = int(input("How many bike you want to rent"))
        except:
            print("this is not positive integer number")
            return -1
        try:
            bike < 1
        except:
            print("Invalid Input, Number of bike should be positive integer ")
        else:
            self.bike = bike

        return bike

    def returnbike(self):
        """
        Return rented bike to owner
        """
        if self.rentalbasis and self.rentaltime and self.bikes:
            return self.rentaltime, self.rentalbasis, self.bikes  
        else:
            return 0,0,0
















