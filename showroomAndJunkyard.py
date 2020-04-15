
# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("Ford GT")
showroom.add("BMW M2")
showroom.add("Porsche 911")
showroom.add("Lotus Elise")


# Print the length of your set.

# print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("Ford GT")

# Print your showroom. Notice how there's still only one instance of that model in there.
# print(showroom)

# Using update(), add two more car models to your showroom with another set.
carsToAdd = {"BMW M Coupe", "1963 Split Window Coupe"}
showroom.update(carsToAdd)
# print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("1963 Split Window Coupe")
# print(showroom)


# Now create another set of cars in a variable junkyard. Someone who owns a junkyard
#  full of old cars has approached you about buying the entire inventory. In the new 
# set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Chevy Sonic", "PT Cruiser"}
junkyard.add("BMW M2")
junkyard.add("Porsche 911")
junkyard.add("Lotus Elise")


# Use the intersection method to see which cars exist in both the junkyard and that junkyard.

existsInBoth = junkyard.intersection(showroom)
# print(existsInBoth)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the 
# junkyard into your showroom.

combinedCars = junkyard.union(showroom)
# print(combinedCars)



# Use the discard() method to remove any cars that you acquired from the junkyard that you
#  do not want in your showroom.

combinedCars.discard("Chevy Sonic")
combinedCars.discard("PT Cruiser")
# print(combinedCars)