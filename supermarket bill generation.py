from datetime import datetime

print("----------------------Welcome--------------------------")
name = input("Enter your name: ")

items = {
    "Rice": 20,
    "sugar": 40,
    "salt": 20,
    "oil": 65,
    "maggi": 10,
    "biscuit": 40,
    "powder": 55,
    "brush": 12
}

option = int(input("For the list of items press 1: "))

if option == 1:
    print("""

Rice        Rs 60/kg
sugar       Rs 40/kg
salt        Rs 20/kg
oil         Rs 65/liter
maggi       Rs 10/each
biscuit     Rs 40/each
powder      Rs 55/each
brush       Rs 12/each

""")

    # Initialize variables to avoid duplicate calculations
    total_price = 0
    gst = 0
    final_amount = 0
    price_list = []

    for i in range(len(items)):
        inp1 = int(input("If you want to buy press 1 or 2 to exit: "))

        if inp1 == 2:
            break

        if inp1 == 1:
            item = input("Enter your item: ").lower()  # Convert to lowercase for case-insensitive matching
            quantity = int(input("Enter quantity: "))

            if item in items.keys():
                price = quantity * items[item]
                total_price += price
                price_list.append((item, quantity, price))
            else:
                print("Your item is not available.")
        else:
            print("You entered a wrong number.")

    inp = input("Can I bill items (yes or no)? ").lower()  # Convert to lowercase for easier comparison

    if inp == 'yes' and total_price != 0:
        gst = (total_price * 5) / 100
        final_amount = gst + total_price

        # Print bill only once
        print(25 * "=", "Shiva Supermarket", 25 * "=")
        print(28 * " ", "Kakinada")
        print("Name:", name, 30 * " ", datetime.now())
        print(75 * "-")
        print("S.No", 8 * '', 'Item', 8 * "", 'Quantity', 3 * " ", 'Price')
        for i in range(len(price_list)):
            item, quantity, price = price_list[i]
            print(i, 8 * '', 5 * '', item, 10 * '', quantity, 10 * " ", price)
        print(75 * "-")
        print(50 * " ", "Total Amount:", "Rs", total_price)
        print("GST Amount", 40 * " ", 'Gst Rs', gst)
        print(75 * "-")
        print(50 * " ", 'Final Amount:', 'Rs', final_amount)
        print(75 * "-")
        print(50 * " ", "Thanks for visiting!")
        print(75 * "-")

print("\n--- Program complete! ---")  # Added confirmation message