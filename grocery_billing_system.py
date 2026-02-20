# --- Item Price Calculator ---

# Accept price input for 3 items
# We use float() to allow for decimal prices
price1 = float(input("Enter the price for item 1: "))
price2 = float(input("Enter the price for item 2: "))
price3 = float(input("Enter the price for item 3: "))

# Calculate the original total cost
original_total = price1 + price2 + price3
discount = 0.0

# Apply 10% discount if total is greater than $50
if original_total > 50:
    discount = original_total * 0.10

# Calculate the final amount after subtracting the discount
final_amount = original_total - discount

# Display the results formatted to 2 decimal places
print("\n--- Receipt Summary ---")
print(f"Original Total: ${original_total:.2f}")

if discount > 0:
    print(f"Discount (10%): -${discount:.2f}")
else:
    print("Discount: $0.00 (Total must be over $50)")

print(f"Final Amount:   ${final_amount:.2f}")