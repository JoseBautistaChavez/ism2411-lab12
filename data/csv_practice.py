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


# --- Exercise 4 ---
print("--- Exercise 4 ---")


# --- Exercise 5 ---
print("--- Exercise 5 ---")


# --- Exercise 6 ---
print("--- Exercise 6 ---")


# --- Exercise 7 ---
print("--- Exercise 7 ---")


# --- Exercise 8 ---
print("--- Exercise 8 ---")
