    # def BiggestRetailChain(someList):
#     max_towns = 0
#     biggest_chains = []

#     for chain, towns in someList.items():
#         town_count = len(towns)
#         if town_count > max_towns:
#             max_towns = town_count
#             biggest_chains = [chain]
#         elif town_count == max_towns:
#             biggest_chains.append(chain)

#     return biggest_chains

# biggest_chains = BiggestRetailChain(d)
# print("Biggest Retail Chains:", biggest_chains)

    
# bestChain = biggestRetailChain(d)

# def CommonTowns(d, rc1, rc2):
#     townsList = []
#     for location in d[rc1]:
#         if location in d[rc2]:
#             townsList.append(location)
#     print(townsList)

# firstLocation = input("Please enter first location: ")
# secondLocation = input("Please enter the second location: ")
# CommonTowns(d, firstLocation, secondLocation)










'''
Question 2
'''
#Part A
# routingKeys = {"A63" : "Greystones", "A98" : "Bray", "P17" : "Kinsale", "A86" : "Dunboyne", "W23" : "Cellbridge", "F45" : "Castlearea",
#                "F35" : "Ballyhaunis", "H14" : "Belturbet", "N39" : "Longford", "F56" : "Ballymote"}

# yourPostCode = input("Please enter your Postal Code: ")
# while yourPostCode not in list(routingKeys.keys()):
#     print("Your Postal Code is incorrect.")
#     yourPostCode = int("Please enter the correct Postal Code")
# print(routingKeys[yourPostCode])

#Part B

# routingKeys = {}
# inFile = open("routingKeys.txt", "r")
# for line in inFile:
#     (key,val) = line.split()
#     routingKeys[key] = val

# print(routingKeys)






#Question 3

'''
Part A
'''

# def load_data(filename):
#     data_dict = {}

#     # Open the file and read its contents
#     inFile =  open(filename, 'r')
#     for line in inFile:
#         parts = line.strip().split(',')
#         location = parts[0].strip(' ')
#         values = [int(value) for value in parts[1:]]
#         data_dict[location] = values
#     inFile.close()

#     return data_dict


# filename = 'Lab7/occurrences.txt'
# result_dict = load_data(filename)
# print(result_dict)


'''
Part B b)
'''
# def load_data(filename):
#     data_dict = {}

#     # Open the file and read its contents
#     inFile =  open(filename, 'r')
#     for line in inFile:
#         parts = line.strip().split(',')
#         location = parts[0].strip(' ')
#         values = [int(value) for value in parts[1:]]
#         data_dict[location] = values
#     inFile.close()

#     return data_dict

# def daily_cases(cumulative):
#     daily_dict = {}
#     for location, cumulative_values in cumulative.items():
#         daily_values = [cumulative_values[i] - cumulative_values[i-1] if i > 0 else cumulative_values[i] for i in range(len(cumulative_values))]
#         daily_dict[location] = daily_values
#     return daily_dict

# cumulative_data = load_data('Lab7/occurrences.txt')
# result_daily = daily_cases(cumulative_data)
# print(result_daily)