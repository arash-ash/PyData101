# Yet again, input() is raw_input() for the course and for Python 2
hours = float(input("Enter hours:"))
rate = float(input("Enter rate: "))

if hours > 40:
    normalPay = 40 * rate
    overtimePay = (hours - 40) * (1.5 * rate)
    pay = normalPay + overtimePay
else:
    pay = rate * hours

print(pay)
