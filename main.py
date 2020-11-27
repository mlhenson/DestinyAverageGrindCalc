# Destiny Average Grind Calculator
# Script to help quickly calculate the maximum average power level the player can grind to using non power sources

# Declaring variables
powerfulcap = 1250
inputgear = [1236, 1240, 1240, 1216, 1215, 1209, 1215, 1214]


# Function that will average a passed gear list, then make a new list with every piece under the average brought up to
# the average and return it
def averagegear(gearlist):
    currentaverage = int((sum(gearlist) / 8))
    modgear = []
    for item in gearlist:
        if item < currentaverage:
            modgear.append(currentaverage)
        else:
            modgear.append(item)
    return modgear


# Check the average of the gear provided by the user, if it's greater or equal to the current powerful cap, let the user
# know that they are at powerful.
if int((sum(inputgear) / 8)) >= powerfulcap:
    print(
        f"The average score of your current gear ({int((sum(inputgear) / 8))}) is equal to or higher than the powerful"
        f" cap of {powerfulcap}")
# If the average power level of the user isn't great or equal to powerful cap, run the averagegear function. Keep going
# through and running the function while the lowest item in the list is under average of the entire list
else:
    updatedgear = averagegear(inputgear)
    while min(updatedgear) != int((sum(updatedgear) / 8)):
        if int((sum(updatedgear) / 8)) == powerfulcap:
            break
        updatedgear = averagegear(updatedgear)
    print(f"The max power you can hit with your current list is {int((sum(updatedgear) / 8))}")
