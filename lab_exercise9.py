# shopping cart in functions with price calculation
def add_to_cart(cart, item, price):
    cart.append((item, price))
    print(f"Added {item} to cart with price ${price:.2f}.")
    return cart

def calculate_total(cart):
    total = sum(price for item, price in cart)
    print(f"Total price of items in cart: ${total:.2f}.")
    return total
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, price in cart:
            print(f"- {item}: ${price:.2f}")

def remove_from_cart(cart, item):
    for i, (cart_item, price) in enumerate(cart):
        if cart_item == item:
            del cart[i]
            print(f"Removed {item} from cart.")
            return cart
    print(f"{item} not found in cart.")
    return cart
def main():
    cart = []
    while True:
        print("\nMenu:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Display cart")
        print("4. Calculate total")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            cart = add_to_cart(cart, item, price)
        elif choice == '2':
            item = input("Enter the name of the item to remove: ")
            cart = remove_from_cart(cart, item)
        elif choice == '3':
            display_cart(cart)
        elif choice == '4':
            calculate_total(cart)
        elif choice == '5':
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    
