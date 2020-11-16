from bikeRental import BikeRental, Customer

def main():
    shop = BikeRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)
        choice = int(input("enter choice: "))

        try:
            int(choice)
        except:
            print("this is not integer input")
            continue

        if choice == 1:
            shop.display_stock()
            
        elif choice == 2:
            customer.rentalTime = shop.rent_bike_on_hourly_basis(customer.requestBike())
            customer.rentalBasis = 1
            
        elif choice == 3:
            customer.rentalTime = shop.rent_bike_on_daily_basis(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rent_bike_on_weekly_basis(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0

        elif choice == 6:
            break
        
        else:
            print("Please enter given option which on Screen (1-6) ")
    print("Thank you for using the bike rental system.")

if __name__ == '__main__':
    main()

    