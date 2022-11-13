## Call this discount.py ##
import datetime

#Initializing variables.
subtotal = float(input("Please enter the Subtotal: $"))
# instead of .now(tz=none), you can use .today()
day_of_week = datetime.datetime.now(tz=none).weekday()
high_balance_discount = False
discount_day = False

#If statement determines whether to include discount.
if subtotal >= 50 and 0 < day_of_week < 6:
    high_balance_discount = True
    discount_day = True
elif subtotal < 50 and 0 < day_of_week < 6:
    short = 50 - subtotal
    print(f"You are ${short:.2f} short of receiving a 10% discount.")

#Subtotal with discount applied (if applicable).
if high_balance_discount == True and discount_day == True:
    discount_amount = subtotal * .1
    subtotal = subtotal - discount_amount
    print(f"Your discount is: ${discount_amount:.2f}")

#Add sales tax to subtotal.
sales_tax = subtotal * 0.06
final_total = subtotal + sales_tax

#Output information.
print(f"The sales tax amount is: ${sales_tax:.2f}")
print(f"The total amount due is: ${final_total:.2f}")