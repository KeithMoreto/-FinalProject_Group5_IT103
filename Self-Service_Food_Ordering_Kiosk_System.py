'''
Date Finished: December 11, 2024
Programmers: Keith Michael R. Moreto and Xylyn Jriel A. Corpuz
'''

#RESTAURANT'S MENU SECTION: [ "category", [[items], [items],...] ]//  items- [code, name, price]
menu = [ 
    ["burgers", [
        ["B1", "Regular burger", 55.00],
        ["B2", "Cheeseburger", 60.00],
        ["B3", "Veggie burger", 65.00], 
        ["B4", "Hawaiian burger", 75.00]
    ]],
    ["sides", [                     
        ["S1", "Fries", 30.00],
        ["S2", "Onion rings", 35.00],
        ["S3", "Mac and cheese", 40.00],
        ["S4", "Mozzarella sticks", 40.00]
    ]],
    ["drinks", [
        ["DR1", "Sprite", 20.00],
        ["DR2", "Coca-cola", 20.00],   
        ["DR3", "Fanta", 20.00],        
        ["DR4", "Iced tea", 18.00]      
    ]],                                
    ["desserts", [                     
        ["DS1", "Sundae", 25.00],
        ["DS2", "Cheesecake", 35.00],
        ["DS3", "Brownies", 25.00],
        ["DS4", "Apple pie", 25.00]
    ]]
]

#TRANSACTION NUMBERS SECTION:
number_dineIn =[1000] 
number_takeOut = [2000] 

def transaction_number(User_dine):
    if User_dine == "1":
        number_dineIn[0] +=1
        return number_dineIn[0]
    elif User_dine == "2":
        number_takeOut[0] +=1
        return number_takeOut[0]
    
#DISPLAY MENU FUNCTION SECTION:
def display_menu():
    print("\n--- MENU ---")
    for category, items in menu:
        print(f"\n{category.upper()}: ")
        for code, name, price in items:
            print(f"{code} - {name}: ₱{price:.2f}") 

#GET ORDER FUNCTION SECTION:
def get_order():
    order = []  #To summarize the orders and update the cost.
    cost = 0 
    
    print("\nEnter 'x' to cancel your order.") 

    while True:
        menu_choice = input("\nEnter the code of your order (or 'd' if done ordering): ").upper() 

        if menu_choice == 'X':
            print("Order cancelled. Returning to main menu...\n")
            return "cancelled", 0
        elif menu_choice == 'D':
            if order:
                print("Done ordering, proceeding to check-out. \n")
                return order, cost
            else:
                print("Your order basket is empty. Please enter your order first.")
                continue
        #To determine if the entered code is valid:
        item_found = False
        for category, items in menu:
            for code, name, price, in items:
                if menu_choice == code:
                    order.append([name, price])
                    cost += price
                    print(f"{name}: ₱{price: .2f} is added to your order basket.")
                    print(f"Your current total is: ₱{cost:.2f}") 
                    item_found = True
                    break
            if item_found:
                break

        if not item_found:
            print("Invalid input. Make sure to input a code from the menu only. Try again.")

#MAIN MENU SECTION:
while True:
    print("🍔Welcome to Burger Queen!🍔 Fast, Fresh, and Flavor-Packed🍔")
    print("Do you want to order?")                                     
    start = input("Enter '1' to continue or '2' to turn the kiosk off: ") 

    if start not in ["1", "2"]: 
        print("Please enter 1 or 2 only. Try again. \n")
        continue
    elif start == "2":
        print("\nKiosk, turning off...")
        break

    #DINE-IN OR TAKE-OUT SELECTION 
    while True:  
        dining_option = input("Would you like to dine-in (1) or take out (2)? (1 or 2): ").lower() 

        if dining_option in ["1", "2"]: 
            display_menu() 
            order_number= transaction_number(dining_option)
            break
        else:
            print("Please choose between options '1 (dine-in)' and '2 (take-out)' only. Try again.\n")

    #ORDER SUMMARY AND CHECKOUT 
    #Order Summary and total cost
    all_orders = [] 
    total_order_cost = 0

    while True:
        order, cost = get_order()

        if order == "cancelled":
            break
        elif order:
            for item in order:  
                all_orders.append(item)  
                total_order_cost += item[1]  
            break  
    # Checkout the orders:
    if all_orders: 
        print("\n--- Checkout ---")
        print("Order summary:")
        for name, price in all_orders:
            print(f"    {name}: ₱{price:.2f}")

        print(f" Total cost: ₱{total_order_cost:.2f} \n")
        print(f"Your order number is: {order_number}")
        print("Please present your order number to the counter for payment. Thank you for ordering. Enjoy your meal!\n")
        print("Ending the transaction...\n\n")

