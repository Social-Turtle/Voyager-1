#matthews_caleb_voyager_1.py

#units of days
time_since_measure = int(input("How many days has it been since 9-25-09 when NASA reported the speed and distance of the Voyager 1 probe? "))
#distance equals rate (miles/day) * days total plus initial position
miles_from_sun = time_since_measure * 9177841 + 16637000000
kilos_from_sun = miles_from_sun * 1.609344
au_from_sun = miles_from_sun/92955887.6
#coefficient of 2 to account for round trip, and 1000 to convert kilometers to meters
radio_time = 2000*kilos_from_sun/299792458

print("It has been", time_since_measure, "days since NASA measured the speed and distance of the Voyager 1 rocket.\n")
print("Travelling at a blistering 38,241 mph, the Voyager 1 rocket is approximately", miles_from_sun, "miles from the sun. \nThat is equivalent to", kilos_from_sun, "kilometers or", au_from_sun , "astronomical units!\n")
print("At this distance, the round trip time for radio communication to the probe is", radio_time, "seconds, or" , radio_time/3600 , "hours! \n")