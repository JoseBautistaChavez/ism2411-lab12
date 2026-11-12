import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# --- Exercise 1 ---
print("--- Exercise 1 ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

# --- Exercise 2 ---
print("--- Exercise 2 ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --- Exercise 3 ---
print("--- Exercise 3 ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

# --- Exercise 4 ---
print("--- Exercise 4 ---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# --- Exercise 5 ---
high_value = []
rows_read = 0

with open(SALES_FILE, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader, None)
    
    for row in reader:
        if not row or len(row) < 3:
            continue
            
        rows_read += 1
        product, price_str, qty_str = row
        
        try:
            price = float(price_str.strip().replace("$", ""))
            quantity = int(qty_str.strip())
        except ValueError:
            continue
            
        total = price * quantity
        if total > 100:
            high_value.append([product.strip(), f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)

print(f"Wrote {len(high_value)} qualifying rows out of {rows_read} original rows.")

# --- Exercise 6 ---
print("--- Exercise 6 ---")
dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row["product"]}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")

# --- Exercise 7 ---
print("--- Exercise 7 ---")
summary = {}
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# --- Exercise 8 ---
print("--- Exercise 8 ---")
LOG_FILE = "data/run_log.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")
entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())