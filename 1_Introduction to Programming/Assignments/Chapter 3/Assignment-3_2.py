# Will keep asking for hours input until hours >= 0
hours = -1
while hours < 0:
    try:
        hours = float(input("Enter hours: "))
    except:
        print("Error, please enter numeric input.")

# Will keep asking for rate input until rate >= 0
rate = -1
while rate < 0:
    try:
        rate = float(input("Enter rate: "))
    except:
        print("Error, please enter numeric input.")

# Solves problem using valid
if hours > 40:
    normalPay = 40 * rate
    overtimePay = (hours - 40) * (1.5 * rate)
    pay = normalPay + overtimePay
else:
    pay = rate * hours

print("Your pay is $" + str(pay))
