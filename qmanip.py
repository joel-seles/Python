# Quotation Manipulation , qmanip.py
# Demonstrates string methods
# jseles, 14 July 2014

#Quote from then-IBM Chairman, Thomas Watson, 1943:
quote = "I think there is a world market for maybe 5 computers."

print("original quote")
print(quote)

print("\nIn Uppercase:")
print(quote.upper())

print("\nIn lowercase:")
print(quote.lower())

print("\nAs a title:")
print(quote.title())

print("\nWith a minor replacement:")
print(quote.replace("5", "billions of"))

print("\nOriginal quote is still:")
print(quote)

print("\nsWAPCASE ?:")
print(quote.swapcase())


input("\n\nPress the Enter key to exit.")
