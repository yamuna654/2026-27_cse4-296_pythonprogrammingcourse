# Manufacturing Cost and Profitability Analysis
quantity = int(input("Enter production quantity: "))

material_per_unit = float(input("Enter material cost per unit (Rs.): "))
wastage_percent = float(input("Enter wastage percentage: "))
labour_per_unit = float(input("Enter labour cost per unit (Rs.): "))
machine_per_unit = float(input("Enter machine cost per unit (Rs.): "))
selling_price = float(input("Enter selling price per unit (Rs.): "))
target_profit = float(input("Enter target profit percentage: "))
if quantity <= 0:
    print("Production quantity must be greater than zero.")

elif (material_per_unit < 0 or wastage_percent < 0
      or labour_per_unit < 0 or machine_per_unit < 0
      or selling_price < 0 or target_profit < 0):

    print("Costs, percentages, and selling price cannot be negative.")

else:
    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0
    print("\n===== MANUFACTURING COST ANALYSIS =====")
    print(f"Material Cost: Rs. {material_cost:.2f}")
    print(f"Wastage Cost: Rs. {wastage_cost:.2f}")
    print(f"Labour Cost: Rs. {labour_cost:.2f}")
    print(f"Machine Cost: Rs. {machine_cost:.2f}")
    print(f"Total Manufacturing Cost: Rs. {total_cost:.2f}")
    print(f"Cost Per Unit: Rs. {cost_per_unit:.2f}")
    print(f"Total Sales Revenue: Rs. {revenue:.2f}")
    print(f"Total Profit: Rs. {profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")
    print(f"Target Profit Percentage: {target_profit:.2f}%")
    print("\n===== PROFITABILITY RESULT =====")

    if profit_percent >= target_profit:
        print("Profit target achieved.")
    else:
        print("Profit target not achieved.")

    if profit < 0:
        print("Warning: Production resulted in a loss.")
    elif profit == 0:
        print("Production reached the break-even point.")
