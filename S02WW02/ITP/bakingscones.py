#assuming all are 2 days old?

sconesBought = float(input("How many scones are you buying: "))

def calDiscount(sb):
    discountedPrice = sb * 0.6
    print("Discounted Price: €", discountedPrice, sep='') #Placeholder
    print(f"Discounted price: €{round(discountedPrice,2)}") # Fstring
    

calDiscount(sconesBought)