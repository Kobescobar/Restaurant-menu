# Creating the menu list 
menu = ["Rice", "Plantains", "Burger", "Sushi", "Potatoe"]

# creating the stock dictionary
stock = {"Rice":15, "Plantains":10, "Burger":20, \
         "Sushi" : 19, "Potatoe" : 12}

# Creating the price dictionary 
price = {"Rice" : 35, "Plantains" : 20, "Burger" : 10, "Sushi" : 22, "Potatoe" : 25}

# Initializing total stock to zero
Total_stock = 0

# Iterate through each menu list item matching with stock and price keys 
for keys in menu: 

    item_value = price[keys] * stock[keys]
    
    Total_stock +=  item_value

# Printing out the value for each menu item 
    print(f" Item value for {keys} is {price[keys]} * {stock[keys]} = \
{item_value}")
    
# Printing out the total worth of stock in the cafe    
print(f" The total worth of stock in the cafe is : {Total_stock} ")
    
