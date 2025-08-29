import csv
from collections import defaultdict

def read_sales(file_path):
    """Reads sales data from a CSV file and converts 'amount' to float."""
    sales = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    row['amount'] = float(row['amount'])
                    sales.append(row)
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return sales

def generate_report(sales):
    """Generates and prints a sales report."""
    total_sales = sum(s['amount'] for s in sales)
    print(f"\n📊 Total Sales: ${total_sales:.2f}")

    sales_by_product = defaultdict(float)
    for sale in sales:
        sales_by_product[sale['product']] += sale['amount']

    print("\n🛒 Sales by Product:")
    for product, amount in sales_by_product.items():
        print(f"  {product}: ${amount:.2f}")

if __name__ == "__main__":
    sales_data = read_sales("sales.csv")
    if sales_data:
        generate_report(sales_data)
