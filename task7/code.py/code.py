
# Railway Fare and Reservation Calculator

CLASSES = {
    "Sleeper": 1.0,
    "AC 3 Tier": 2.0,
    "AC 2 Tier": 3.0,
    "AC First Class": 4.0
}

RESERVATION_FEE = 40
CANCELLATION_RATE = 0.25


def calculate_base_fare(distance):
    if distance <= 100:
        return distance * 1.50
    elif distance <= 300:
        return 100 * 1.50 + (distance - 100) * 1.25
    else:
        return 100 * 1.50 + 200 * 1.25 + (distance - 300)


try:
    distance = float(input("Enter travel distance (km): "))
    count = int(input("Enter number of passengers: "))

    if distance <= 0 or count <= 0:
        raise ValueError("Distance and passenger count must be positive.")

    passengers = []
    total_booking = 0
    total_refund = 0

    for i in range(count):
        print(f"\nPassenger {i + 1}")

        name = input("Enter passenger name: ").strip()
        age = int(input("Enter passenger age: "))

        if not name or age < 0:
            raise ValueError("Invalid passenger name or age.")

        print("Available classes:", ", ".join(CLASSES))
        travel_class = input("Enter travel class: ").strip()

        if travel_class not in CLASSES:
            raise ValueError("Invalid travel class.")
        base_fare = calculate_base_fare(distance)
        class_fare = base_fare * CLASSES[travel_class]
        if age < 5:
            concession_rate = 100
        elif age <= 11:
            concession_rate = 50
        elif age >= 60:
            concession_rate = 40
        else:
            concession_rate = 0

        concession = class_fare * concession_rate / 100
        travel_fare = class_fare - concession
        total_fare = travel_fare + RESERVATION_FEE

        cancel = input("Cancel ticket? (yes/no): ").strip().lower()

        if cancel not in ("yes", "no"):
            raise ValueError("Enter yes or no.")

        if cancel == "yes":
            penalty = travel_fare * CANCELLATION_RATE
            refund = travel_fare - penalty
            status = "Cancelled"
        else:
            penalty = 0
            refund = 0
            status = "Confirmed"

        total_booking += total_fare
        total_refund += refund

        passengers.append({
            "name": name,
            "age": age,
            "class": travel_class,
            "base": base_fare,
            "concession": concession,
            "reservation": RESERVATION_FEE,
            "fare": total_fare,
            "penalty": penalty,
            "refund": refund,
            "status": status
        })
    print("\n" + "=" * 48)
    print("     RAILWAY RESERVATION STATEMENT")
    print("=" * 48)

    for p in passengers:
        print(f"\nPassenger: {p['name']}")
        print(f"Age: {p['age']}")
        print(f"Travel Class: {p['class']}")
        print(f"Base Fare: ₹{p['base']:.2f}")
        print(f"Concession: ₹{p['concession']:.2f}")
        print(f"Reservation Fee: ₹{p['reservation']:.2f}")
        print(f"Total Fare: ₹{p['fare']:.2f}")
        print(f"Status: {p['status']}")
        print(f"Cancellation Penalty: ₹{p['penalty']:.2f}")
        print(f"Refund: ₹{p['refund']:.2f}")
        print("-" * 48)

    print(f"\nTotal Booking Cost: ₹{total_booking:.2f}")
    print(f"Total Refund: ₹{total_refund:.2f}")
    print(f"Net Cost After Refunds: ₹{total_booking - total_refund:.2f}")
    print("=" * 48)

except ValueError as error:
    print("Input Error:", error)
