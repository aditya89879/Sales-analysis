# Function to calculate total sales and find the item with the highest sales
def analyze_sales(data):
    total_sales = 0  # keeps track of total revenue
    max_sale = 0     # stores the highest sales amount for any item
    best_item = ""   # name of the item with highest sales

    # going through each item in the sales list
    for item in data:
        name = item['item']
        price = item['price']
        quantity = item['quantity']
        sales = price * quantity  # total sales for this item

        total_sales += sales  # adding to total revenue

        # checking if this item made the highest sales
        if sales > max_sale:
            max_sale = sales
            best_item = name

    # final output
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Best Selling Item: {best_item} (${max_sale:.2f})")


# test data to run the function
if __name__ == "__main__":
    sales_data = [
        {'item': 'Notebook', 'price': 5.0, 'quantity': 120},
        {'item': 'Pen', 'price': 1.5, 'quantity': 250},
        {'item': 'Marker', 'price': 3.0, 'quantity': 150},
        {'item': 'Eraser', 'price': 0.75, 'quantity': 300}
    ]

    analyze_sales(sales_data)  # calling the function
