cars = 100  # Assign Integer Value To Variable
space_in_a_car = 4.0  # Assign Float Value To Variable
drivers = 30  # Assign Integer Value To Variable
passengers = 90  # Assign Integer Value To Variable
cars_not_driven = cars - drivers  # Assign Two Variable Subtraction Result To Third Variable
cars_driven = drivers  # Use Assignment Operator
carpool_capacity = cars_driven * space_in_a_car  # Assign Two Variable Multiplication Result To Third Variable
average_passengers_per_car = passengers / cars_driven  # Assign Two Variable Division Result To Third Variable


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
