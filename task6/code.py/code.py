
# Railway Fare and Reservation Calculator

# Travel class multipliers
classes = {
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
        return 100 * 1.50 + 200 * 1.25 + (distance - 300) * 1.00


try:
    distance = float(input("Enter travel distance (km): "))
    passenger_count = int(input("Enter number of passengers: "))

    if distance <= 0 or passenger_count <= 0:
        print("Error: Distance and passenger count must be positive.")

    else:
        passengers = []
        total_booking_cost = 0
        total_refund = 0

        for i in range(passenger_count):
            print(f"\n--- Passenger {i + 1} ---")

            name = input("Enter passenger name: ").strip()
            age = int(input("Enter passenger age: "))

            if not name or age < 0:
                raise ValueError("Name cannot be empty and age cannot be negative.")

            print("Available classes:")
            for travel_class in classes:
                print("-", travel_class)

            travel_class = input("Select travel class: ").strip()

            if travel_class not in classes:
                raise ValueError("Invalid travel class selected.")
            base_fare = calculate_base_fare(distance)
            class_fare = base_fare * classes[travel_class]
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
            cancel = input(
                "Cancel this ticket? (yes/no): "
            ).strip().lower()

            if cancel not in ("yes", "no"):
                raise ValueError("Enter yes or no for cancellation.")

            if cancel == "yes":
                penalty = travel_fare * CANCELLATION_RATE
                refund = total_fare - penalty - RESERVATION_FEE
                refund = max(0, refund)
                status = "Cancelled"
            else:
                penalty = 0
                refund = 0
                status = "Confirmed"

            total_booking_cost += total_fare
            total_refund += refund

            passengers.append({
                "name": name,
                "age": age,
                "class": travel_class,
                "base_fare": base_fare,
                "concession": concession,
                "reservation_fee": RESERVATION_FEE,
                "fare": total_fare,
                "penalty": penalty,
                "refund": refund,
                "status": status
            })
        print("\n" + "=" * 55)
        print("       RAILWAY FARE AND RESERVATION STATEMENT")
        print("=" * 55)

        for p in passengers:
            print(f"\nPassenger Name: {p['name']}")
            print(f"Age: {p['age']}")
            print(f"Travel Class: {p['class']}")
            print(f"Base Fare: ₹{p['base_fare']:.2f}")
            print(f"Age Concession: ₹{p['concession']:.2f}")
            print(f"Reservation Fee: ₹{p['reservation_fee']:.2f}")
            print(f"Total Fare: ₹{p['fare']:.2f}")
            print(f"Status: {p['status']}")
            print(f"Cancellation Penalty: ₹{p['penalty']:.2f}")
            print(f"Refund Amount: ₹{p['refund']:.2f}")
            print("-" * 55)

        print(f"Total Booking Cost: ₹{total_booking_cost:.2f}")
        print(f"Total Refund: ₹{total_refund:.2f}")
        print(
            f"Net Cost After Refunds: "
            f"₹{total_booking_cost - total_refund:.2f}"
        )
        print("=" * 55)

except ValueError as error:
    print("Input Error:", error)
