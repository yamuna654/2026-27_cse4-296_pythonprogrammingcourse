
# Hospital Billing and Patient Classification System

try:
    patient_name = input("Enter patient name: ")

    consultation = float(input("Enter consultation charges: ₹"))
    diagnostics = float(input("Enter diagnostic charges: ₹"))
    treatment = float(input("Enter treatment charges: ₹"))
    if consultation < 0 or diagnostics < 0 or treatment < 0:
        print("\nError: Charges cannot be negative.")

    else:

        total_bill = consultation + diagnostics + treatment
        if total_bill >= 10000:
            concession_rate = 10
        elif total_bill >= 5000:
            concession_rate = 5
        else:
            concession_rate = 0

        concession = total_bill * concession_rate / 100
        final_amount = total_bill - concession

        if final_amount < 5000:
            classification = "Low Bill"
        elif final_amount < 10000:
            classification = "Medium Bill"
        else:
            classification = "High Bill"
        print("\n====== HOSPITAL BILL ======")
        print("Patient Name:", patient_name)
        print(f"Consultation Charges: ₹{consultation:.2f}")
        print(f"Diagnostic Charges:   ₹{diagnostics:.2f}")
        print(f"Treatment Charges:    ₹{treatment:.2f}")
        print("---------------------------")
        print(f"Total Bill:           ₹{total_bill:.2f}")
        print(f"Concession Rate:      {concession_rate}%")
        print(f"Concession Amount:    ₹{concession:.2f}")
        print(f"Final Payable Amount: ₹{final_amount:.2f}")
        print("Patient Classification:", classification)
        print("===========================")

except ValueError:
    print("Error: Please enter valid numeric charges.")
