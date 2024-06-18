from ryanair import Ryanair
from datetime import timedelta
from datetime import date


maxPrice = 100
# set the start date of when you want to search for flights
startDate = date(2024, 7, 20)
# set the end date for when you want toi search for flights
endDate = date(2024, 9, 22)
# set the length of your trip
tripLength = 7
# set the airports you want to fly from (Airport ticker symbol)
Airport1 = "MAN"
Airport2 = "LPL"
# set your currency
api = Ryanair("GBP")
flights = api.get_cheapest_flights(Airport1, startDate, endDate)

for i in range(0, len(flights)):

    if flights[i].price < maxPrice and "Ireland" not in flights[i].destinationFull and "United Kingdom" not in flights[i].destinationFull:
        print("Manchester to " + flights[i].destinationFull)
        print("Outbound Price: £" + str(flights[i].price))
        print("Departure Time: " + str(flights[i].departureTime))

        returnFlight = api.get_cheapest_flights(flights[i].destination, flights[i].departureTime+timedelta(days=tripLength), flights[i].departureTime + timedelta(days=tripLength))

        for j in range(0, len(returnFlight)):
            if returnFlight[j].destination == Airport1:
                print("return price:" + str(returnFlight[j].price))
                print("Return Time:" + str(returnFlight[j].departureTime))
                totalPrice = returnFlight[j].price + flights[i].price
                print("Total Price: £" + str(totalPrice))

            elif returnFlight[j].destination == Airport2:
                print("Liverpool return price: £" + str(returnFlight[j].price))
                print("Liverpool Return Time: " + str(returnFlight[j].departureTime))
                totalPrice = returnFlight[j].price + flights[i].price
                print("Liverpool return Total Price: £" + str(totalPrice))
        print("")

flights = api.get_cheapest_flights(Airport2, startDate, endDate)

print("|\n"*10)

for i in range(0, len(flights)):
    if flights[i].price < maxPrice and "Ireland" not in flights[i].destinationFull:
        print("Liverpool to " + flights[i].destinationFull)
        print("Outbound Price: £" + str(flights[i].price))
        print("Departure Time: " + str(flights[i].departureTime))

        returnFlight = api.get_cheapest_flights(flights[i].destination, flights[i].departureTime + timedelta(days= tripLength), flights[i].departureTime + timedelta(days=tripLength))

        for j in range(0, len(returnFlight)):
            if returnFlight[j].destination == Airport2:
                print("Return Price: £" + str(returnFlight[j].price))
                print("Return Time: " + str(returnFlight[j].departureTime))
                totalPrice = returnFlight[j].price + flights[i].price
                print("Total Price: £" + str(totalPrice))

            elif returnFlight[j].destination == Airport1:
                print("Manchester Return Price: £" + str(returnFlight[j].price))
                print("Manchester Return Time: " + str(returnFlight[j].departureTime))
                totalPrice = returnFlight[j].price + flights[i].price
                print("Manchester Return Total Price: £" + str(totalPrice))
        print("")
