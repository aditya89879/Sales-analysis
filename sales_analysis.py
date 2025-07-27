def analyze_sales(data):
    total_sales = 0
    max_sale = 0
    best_item = ""

    for item in data:
        name = item['item']
        price = item['price']
        quantity = item['quantity']
        sales = price * quantity
        total_sales += sales

        if sales > max_sale:
            max_sale = sales
            best_item = name

    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Best Selling Item: {best_item} (${max_sale:.2f})")

if __name__ == "__main__":
    sales_data = [
        {'item': 'Notebook', 'price': 5.0, 'quantity': 120},
        {'item': 'Pen', 'price': 1.5, 'quantity': 250},
        {'item': 'Marker', 'price': 3.0, 'quantity': 150},
        {'item': 'Eraser', 'price': 0.75, 'quantity': 300}
    ]
    analyze_sales(sales_data)
