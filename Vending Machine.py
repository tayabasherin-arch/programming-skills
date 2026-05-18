import time
import random

# Intro banner for the vending machine system
print("""
 ██████╗  █████╗ ████████╗██╗  ██╗    ███████╗██████╗  █████╗ 
 ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ██╔════╝██╔══██╗██╔══██╗
 ██████╔╝███████║   ██║   ███████║    ███████╗██████╔╝███████║
 ██╔══██╗██╔══██║   ██║   ██╔══██║    ╚════██║██╔═══╝ ██╔══██║
 ██████╔╝██║  ██║   ██║   ██║  ██║    ███████║██║     ██║  ██║
 ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝
                      VENDING MACHINE
""")

# Product inventory grouped by category with prices and stock
Inventory = {
    "Chips": { 
        "11": {"item": "Cheetos", "Price": 4.00, "Stock": 5},
        "12": {"item": "Lays Classic", "Price": 4.00, "Stock": 5},
        "13": {"item": "Kurkure Masala", "Price": 4.00, "Stock": 5},
        "14": {"item": "Doritos Nacho", "Price": 4.00, "Stock": 5},
        "15": {"item": "Oman Chips", "Price": 4.00, "Stock": 5},
        "16": {"item": "Takis", "Price": 5.50, "Stock": 13},
        "17": {"item": "Pringles", "Price": 7.00, "Stock": 9},
        "18": {"item": "Doritos Sweet Chili", "Price": 4.00, "Stock": 5},
        "19": {"item": "Sunbites", "Price": 4.00, "Stock": 2} # Added low stock example
    },
    "Candy & Sweets": {
        "21": {"item": "M&Ms", "Price": 2.00, "Stock": 5},
        "22": {"item": "Gumballs", "Price": 2.00, "Stock": 5},
        "23": {"item": "Skittles", "Price": 2.00, "Stock": 5},
        "24": {"item": "Poprocks", "Price": 2.00, "Stock": 5},
        "25": {"item": "Sour Candy", "Price": 2.00, "Stock": 5},
        "26": {"item": "Bubble Gum", "Price": 2.00, "Stock": 5},
        "27": {"item": "Lollipop", "Price": 2.00, "Stock": 5},
        "28": {"item": "Snickers", "Price": 2.00, "Stock": 8},
        "29": {"item": "Twix", "Price": 2.00, "Stock": 5},
        "30": {"item": "Mars Bar", "Price": 2.00, "Stock": 5},
        "31": {"item": "KitKat", "Price": 1.50, "Stock": 13},
        "32": {"item": "Dairy Milk", "Price": 2.00, "Stock": 5}
    },
    "Drinks & Sodas": {
        "41": {"item": "Coca Cola", "Price": 3.00, "Stock": 7},
        "42": {"item": "7up", "Price": 3.00, "Stock": 5},
        "43": {"item": "Fanta", "Price": 3.00, "Stock": 5},
        "44": {"item": "Sprite", "Price": 3.00, "Stock": 5},
        "45": {"item": "Mountain Dew", "Price": 3.00, "Stock": 5},
        "46": {"item": "Kinza Cola", "Price": 3.00, "Stock": 5},
        "47": {"item": "Pepsi", "Price": 2.50, "Stock": 12},
        "48": {"item": "Diet Coke", "Price": 3.00, "Stock": 5},
        "49": {"item": "Mirinda", "Price": 3.00, "Stock": 5},
        "50": {"item": "Red Bull", "Price": 8.00, "Stock": 6},
        "51": {"item": "Water", "Price": 1.00, "Stock": 5},
        "52": {"item": "Apple Juice", "Price": 3.00, "Stock": 1} # Added low stock example
    },
    "Biscuits & Snacks": {
        "61": {"item": "Oreo", "Price": 5.00, "Stock": 5},
        "62": {"item": "Digestive", "Price": 5.00, "Stock": 5},
        "63": {"item": "Belvita", "Price": 5.00, "Stock": 5},
        "64": {"item": "Nutella B-ready", "Price": 5.00, "Stock": 5},
        "65": {"item": "Lotus Biscuits", "Price": 5.00, "Stock": 5},
        "66": {"item": "Nature Valley", "Price": 5.00, "Stock": 12},
        "67": {"item": "Rice Cakes", "Price": 5.00, "Stock": 3}
    }
}

def display_menu():
    print("\n-*- Vending Machine Menu -*-")
    for category, items in Inventory.items():
        print(f"\nCategory: {category}")
        print(f"{'Code':<6}{'Item':<25}{'Price':<12}{'Stock':<6}")
        print("-" * 50)
        time.sleep(0.2)
        
        for code, details in items.items():
            stock_status = ""
            if details['Stock'] < 3 and details['Stock'] > 0:
                stock_status = " (LOW STOCK)"
            elif details['Stock'] <= 0:
                stock_status = " (OUT OF STOCK)"
                
            print(f"{code:<6}{details['item']:<25}{details['Price']:>5.2f} AED    {details['Stock']}{stock_status}")
        time.sleep(0.2)

def validate_code_inventory(code):
    # Search through every category to find the entered code
    for category, items in Inventory.items():
        if code in items:
            return True, category
    return False, None

def get_product_code():
    while True:
        code = input("\nEnter the Code of the item you want (or type 'Q' to Quit): ").upper()
        if code == "Q": 
            return None, None
        
        valid, category = validate_code_inventory(code)
        if valid:
            return code, category
        else:
            print("Error: That code is not in our system. Please try again.")

def process_stock(code):
    # Reduce stock quantity after successful selection
    for category, items in Inventory.items():
        if code in items:
            if items[code]['Stock'] > 0:
                items[code]['Stock'] -= 1
                return items[code]
    return None

def process_payment(total_price):
    while True:
        money_given = input(f"Please insert money for {total_price:.2f} AED: ")
        
        # Check whether the input format is valid
        if money_given.isalpha():
            print("\n--- VALUE ERROR: You must enter numbers, not letters! ---")
            continue
            
        try:
            amount = float(money_given)
            
            # Prevent zero value payments
            if amount == 0:
                print("\n--- ZERO DIVISION ERROR: You cannot pay with 0! ---")
                continue
                
            if amount >= total_price:
                return amount - total_price
            else:
                print(f"Error: You did not insert enough money. Needs {total_price - amount:.2f} AED more.")
        except ValueError:
            print("Invalid numeric layout. Please look at the balance requirements.")

def suggest_pairing(category):
    pairings = {
        "Chips": "Drinks & Sodas",
        "Candy & Sweets": "Chips",
        "Drinks & Sodas": "Biscuits & Snacks",
        "Biscuits & Snacks": "Drinks & Sodas"
    }
    paired_category = pairings.get(category)
    if not paired_category:
        return {}

    print(f"\nSuggestion: Still hungry? Try pairing it with something from {paired_category}!")
    paired_items = Inventory[paired_category]
    
    # Display 3 random suggestions from the paired category
    available_codes = [c for c, d in paired_items.items() if d['Stock'] > 0]
    sampled_codes = random.sample(available_codes, min(3, len(available_codes)))
    
    for code in sampled_codes:
        print(f"Code {code}: {paired_items[code]['item']} - {paired_items[code]['Price']:.2f} AED")
    return paired_items

def validate_pairing_code(pairings):
    # Keep asking until the user enters a valid pairing code
    while True:
        pairing_code = input("Enter the code of the pairing item: ")
        if pairing_code in pairings and pairings[pairing_code]['Stock'] > 0:
            return pairing_code
        print("Invalid pairing code or out of stock. Try again.")

def print_receipt(items, change):
    print("\n--- Final Receipt ---")
    # Calculate and display the final bill
    total = 0
    for item in items:
        print(f"- {item['item']}: {item['Price']:.2f} AED")
        total += item['Price']
    print("-" * 25)
    print(f"Total Bill: {total:.2f} AED")
    print(f"Your change returned: {change:.2f} AED")
    print("\nThank you for choosing Bath Spa Vending Machine! Have a wonderful day.")

def vending_machine():
    items_purchased = [] 

    while True:
        display_menu()
        code, category = get_product_code()
        if not code:
            print("Exiting machine...Thank you for purchasing, Have a great day!")
            break

        # Check if the selected item is still in stock
        if Inventory[category][code]['Stock'] <= 0:
            print("Out of stock!")
            continue

        item = process_stock(code)
        if item:
            print(f"\nYou selected: {item['item']}")
            print(f"Price: {item['Price']:.2f} AED")
            items_purchased.append(item)
            total_price = item['Price']

            # Suggest related items for additional purchase
            pairings = suggest_pairing(category)
            if pairings:
                buy_more = input("\nDo you want to add a suggested pairing item? (y/n): ").lower()
                if buy_more == 'y':
                    pairing_code = validate_pairing_code(pairings)
                    pairing_item = process_stock(pairing_code)
                    if pairing_item:
                        print(f"{pairing_item['item']} added to your selection.")
                        total_price += pairing_item['Price']
                        items_purchased.append(pairing_item)

            change = process_payment(total_price)
            print(f"\nThank you! Dispensing products...")
            print_receipt(items_purchased, change)
            break

if __name__ == "__main__":
    vending_machine()