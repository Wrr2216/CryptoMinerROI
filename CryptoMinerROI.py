# Created by Logan Miller 
# Date: 07/10/2023
# Purpose: Calculate the ROI of a cryptocurrency miner and evalute the profitability of different quantities of miners


minerCost = int(input("Enter the cost of the miner: "))
dailyProfit = float(input("Enter the daily profit: "))
powerCostWatts = int(input("Enter the power consumption in watts: "))
electricityRate = float(input("Enter the cost of electricity in dollars per kilowatt hour: "))
minerQuantity = int(input("Enter the quantity of miners: "))

# Calculate the daily electricity cost
powerCostKilowatt = powerCostWatts / 1000
dailyElectricityCost = powerCostKilowatt * electricityRate

# Calculate the ROI
minerRoi = (dailyProfit - dailyElectricityCost) / minerCost * 100

# Calculate the values for the amount of miners
dailyProfit = dailyProfit * minerQuantity
dailyElectricityCost = dailyElectricityCost * minerQuantity
minerCost = minerCost * minerQuantity

# Store the best ROI and the best number of miners
bestROI = minerRoi  # Initialize the best ROI with the ROI of a single miner
bestMinerQuantity = 1 

# Print the ROI
print("-- Results for {} miners --".format(minerQuantity))
print("ROI: {:.2f}%".format(minerRoi))
print("Time to start making profit: {:.2f} days".format(dailyProfit - dailyElectricityCost))
print("Time to break even: {:.2f} days".format(minerCost / (dailyProfit - dailyElectricityCost)))
print("Cost of {} miners: ${}".format(minerQuantity, minerCost))
print("-----------------------------------------")
print("Daily profit: {:.2f}".format(dailyProfit))
print("Daily electricity cost: {:.2f}".format(dailyElectricityCost))
print("Daily net profit: {:.2f}".format(dailyProfit - dailyElectricityCost))
print("-----------------------------------------")
print("Monthly profit: {:.2f}".format((dailyProfit - dailyElectricityCost) * 30))
print("Monthly electricity cost: {:.2f}".format(dailyElectricityCost * 30))
print("Monthly net profit: {:.2f}".format((dailyProfit - dailyElectricityCost) * 30 - dailyElectricityCost * 30))
print("-----------------------------------------")

# Analyze different quantities of miners for optimal ROI
print("Analyzing different quantities of miners for optimal ROI...")
for minerQuantity in range(2, 1001):  # Loop through different quantities of miners starting from 2
    # Calculate the total daily profit and cost for the given quantity of miners
    totalDailyProfit = dailyProfit * minerQuantity
    totalDailyElectricityCost = dailyElectricityCost * minerQuantity

    # Calculate the ROI for the given quantity of miners
    minerRoi = (totalDailyProfit - totalDailyElectricityCost) / (minerCost * minerQuantity) * 100

    # Check if current ROI is better than the previous best ROI
    if minerRoi > bestROI:
        bestROI = minerRoi
        bestMinerQuantity = minerQuantity

# Print the best ROI and optimal number of miners
print("Best ROI: {:.2f}%".format(bestROI))
print("Optimal number of miners: {}".format(bestMinerQuantity))

print("Completed.")