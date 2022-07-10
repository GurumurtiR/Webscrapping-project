# Flipkart-Discount for a price
# google_pay - give 20% off
# else phone_pay - give 10% off
# discount amount : some amount
# take montly emi

mobile_price = 19999
is_google_pay = True
is_phone_pay = False
emi_taken = 9999
print(f"mobile_price:{mobile_price}")
if is_google_pay:
    discount = 0.2 * mobile_price

elif is_phone_pay:
    discount = 0.1 * mobile_price
else:
    print("take emi monthly")
print(f"discount amount:{discount}")
print(f"selling price:{mobile_price-discount}")

take_monthly_emi = [
    {
       "mobile_price": 19999,
       "cash_given": 10000,
       "emi_taken": 9999,
    }

]
print(f"monthly emi:{float(emi_taken/12)}")