# shopping cart in functions

def add_to_cart(cart, item):
    cart.append(item)
    print(f"Added '{item}' to the cart.")
def remove_from_cart(cart, item):
    if item in cart:
        cart.remove(item)
        print(f"Removed '{item}' from the cart.")
    else:
        print(f"'{item}' not found in the cart.")

def view_cart(cart):
    if cart:
        print("Your shopping cart contains:")
        for item in cart:
            print(f"- {item}")
    else:
        print("Your shopping cart is empty.")

def main():
    shopping_cart = []
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            item_to_add = input("Enter the name of the item to add: ")
            add_to_cart(shopping_cart, item_to_add)
        elif choice == '2':
            item_to_remove = input("Enter the name of the item to remove: ")
            remove_from_cart(shopping_cart, item_to_remove)
        elif choice == '3':
            view_cart(shopping_cart)
        elif choice == '4':
            print("Thank you for shopping with us! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
    