class Patient: # Create parent class entitled Patient
    def __init__(self, name: str, bill_amount: float): # Initialize the constructor with name and bill_amount as parameters
        self.__name = name # Initialize private attribute __name with the value of name
        self.__bill_amount = bill_amount # Initialize private attribute __bill_amount with the value of bill_amount 

    def get_name(self): # Getter method for the name
        return self.__name # Returns the value of the private attribute __name

    def set_name(self, name: str): # Setter method for the name
        self.__name = name # Sets the value of __name to the provided name

    def get_bill_amount(self): # Getter method for the bill amount
        return self.__bill_amount # Returns the value of the bill amount

    def set_bill_amount(self, bill_amount: float): # Setter method for the bill amount
        self.__bill_amount = bill_amount # Sets the value of __bill_amount to the provided bill_amount

    def calculate_bill(self): # Calculates the final bill amount for a regular patient (no discount)
        return self.__bill_amount # Returns the newly calculated bill amount

    def display_patient_type(self): # Displays the type of patient (Regular Patient)
        print("Patient Type: Regular Patient") # Print "Patient Type: Regular Patient"

# FIRST CHILD CLASS
class Senior_Patient(Patient): # Child class Senior_Patient inherits from the parent class Patient
    def calculate_bill(self): # Calculates the final bill amount for a senior patient with a 20% discount
        return self.get_bill_amount() * 0.8  # Returns bill amount with 20% discount for senior patients

    def display_patient_type(self): # Displays the type of patient (Senior Citizen)
        print("Patient Type: Senior Citizen") # Prints "Patient Type: Senior Citizen"

# SECOND CHILDCLASS
class PhilHealth_Patient(Patient): # Child class PhilHealth_Patient inherits from the parent class Patient
    def calculate_bill(self): # Calculates the final bill amount for a PhilHealth patient with a 15% discount
        return self.get_bill_amount() * 0.85  # Returns bill amount with 15% discount for PhilHealth patients

    def display_patient_type(self): # Displays the type of patient (PhilHealth Patient)
        print("Patient Type: PhilHealth Patient") # Prints "Patient Type: PhilHealth Patient"

# OBJECTS

p1 = Patient("Juan Dela Cruz", 15000.00) # Object of the Patient class, the parent class
p2 = Senior_Patient("Maria Santos", 15000.00) # Object of Senior_Patient class, which is a child class of Patient
p3 = PhilHealth_Patient("Pedro Reyes", 15000.00) # Object of PhilHealth_Patient class, which is a child class of Patient

# OUTPUT
print("Hospital Billing System") # Prints title "Hospital Billing System"
print("-----------------------")

# Prints the details of each patient, including their name, patient type, original bill, and final bill after applying discounts
print("Patient Name:", p1.get_name())
p1.display_patient_type()
print("Original Bill:", f"₱{p1.get_bill_amount():,.2f}")
print("Final Bill:", f"₱{p1.calculate_bill():,.2f}")

print()

print("Patient Name:", p2.get_name())
p2.display_patient_type()
print("Original Bill:", f"₱{p2.get_bill_amount():,.2f}")
print("Final Bill:", f"₱{p2.calculate_bill():,.2f}")

print()

print("Patient Name:", p3.get_name())
p3.display_patient_type()
print("Original Bill:", f"₱{p3.get_bill_amount():,.2f}")
print("Final Bill:", f"₱{p3.calculate_bill():,.2f}")

print()

# End of code. This code demonstrates polymorphism by allowing different patient types to calculate their bills differently while using the same method name calculate_bill().