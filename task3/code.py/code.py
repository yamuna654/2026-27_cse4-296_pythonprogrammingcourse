
# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 5
REBATE_RATE = 10
INCREASE_LIMIT = 30
def calculate_energy_charges(units):
    if units <= 100:
        return units * 2

    elif units <= 200:
        return (100 * 2) + (units - 100) * 3

    elif units <= 300:
        return (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        return (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7
months = int(input("Enter number of months: "))

if months <= 0:
    print("Number of months must be greater than zero.")

else:
    bills = []

    for month in range(1, months + 1):
        print(f"\nMonth {month}")

        units = float(input("Enter electricity consumption (units): "))

        if units < 0:
            print("Consumption cannot be negative.")
            break
        energy_charge = calculate_energy_charges(units)

        fixed_charge = FIXED_CHARGE
        surcharge = energy_charge * SURCHARGE_RATE / 100

        if units <= 100:
            rebate = energy_charge * REBATE_RATE / 100
        else:
            rebate = 0
        total_bill = (
            energy_charge + fixed_charge + surcharge - rebate
        )

        bills.append({
            "month": month,
            "units": units,
            "energy": energy_charge,
            "fixed": fixed_charge,
            "surcharge": surcharge,
            "rebate": rebate,
            "total": total_bill
        })

    if len(bills) == months:
        print("\n===== MONTHLY ELECTRICITY BILLS =====")

        for bill in bills:
            print(f"\nMonth: {bill['month']}")
            print(f"Units Consumed: {bill['units']:.2f}")
            print(f"Energy Charges: Rs. {bill['energy']:.2f}")
            print(f"Fixed Charges: Rs. {bill['fixed']:.2f}")
            print(f"Surcharge: Rs. {bill['surcharge']:.2f}")
            print(f"Rebate: Rs. {bill['rebate']:.2f}")
            print(f"Final Bill: Rs. {bill['total']:.2f}")

        print("\n===== MONTHLY BILL COMPARISON =====")

        for i in range(1, len(bills)):
            previous = bills[i - 1]["total"]
            current = bills[i]["total"]

            print(
                f"\nMonth {i} to Month {i + 1}:"
            )

            if previous > 0:
                increase = ((current - previous) / previous) * 100

                print(f"Percentage Change: {increase:.2f}%")

                if increase > INCREASE_LIMIT:
                    print("Unusual increase detected!")
                else:
                    print("No unusual increase detected.")

            elif current > previous:
                print("Bill increased from zero; unusual increase detected.")

            else:
                print("Percentage increase cannot be calculated.")
        total_expense = sum(bill["total"] for bill in bills)

        print("\n===== SUMMARY =====")
        print(f"Number of Months: {months}")
        print(f"Total Electricity Expense: Rs. {total_expense:.2f}")
        print(
            f"Average Monthly Bill: Rs. {total_expense / months:.2f}"
        )
