import flightradar24
fr = flightradar24.Api()

# Getting airports list
airports = fr.get_airports()
fr_api = FlightRadar24API()

# Getting airlines list
airlines = fr.get_airlines()

# Getting flights list
airline = 'THY' # Turkish Airlines
flights = fr.get_flights(airline)

# Getting flight details
flight_id = 'TK1' # Turkish Airlines' Istanbul - New York flight
flight = fr.get_flight(flight_id)