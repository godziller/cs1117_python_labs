callTime = int(input('Input time you spent on phone: '))
textsMade = int(input('Input the amount of texts you made: '))
salesTax = 0.05
cost = 0


def calculateBill(cTime, tMade):
    if cTime <= 50 and textsMade <= 50: 
        cost = 15.00
        print(cost)
        return cost 
    
    elif cTime > 50:  
        excessTime = (callTime - 50) * 0.25
        totalCostCall = excessTime + 15.00
        
    if tMade <= 50:
        cost = 15.00
        print(cost)
        return cost 

    elif tMade > 50:
        excessTextTime = (textsMade - 50) * 0.15
        totalCostText = excessTextTime + 15.00

    totalExcessCost = totalCostCall + totalCostText
    cost = totalExcessCost + (totalExcessCost * salesTax)
    print(f"Total cost = {round(cost,2)} euros")
    print(f"Excess Cost = {round(cost - 15.00,2)} euros")
    
calculateBill(callTime, textsMade)