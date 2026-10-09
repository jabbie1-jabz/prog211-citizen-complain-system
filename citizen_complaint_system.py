"""PROG211 OOP Individual Assignment: Citizen Complaint System."""

class Citizen:
    """Stores basic details for a citizen submitting a complaint."""
    def __init__(self, citizen_id, name, ward):
        self.citizen_id = citizen_id
        self.name = name
        self.ward = ward

    def display(self):
        return f"{self.citizen_id} | {self.name} | Ward: {self.ward}"


class Complaint:
    """Stores complaint details and its current status."""
    total_created = 0

    def __init__(self, complaint_id, citizen, category, description):
        self.complaint_id = complaint_id
        self.citizen = citizen
        self.category = category
        self.description = description
        self.status = "Pending"
        Complaint.total_created += 1

    def update_status(self, new_status):
        if new_status not in ("Pending", "In Progress", "Resolved"):
            return False
        self.status = new_status
        return True

    def display(self):
        return (f"Reference: {self.complaint_id}\nCitizen: {self.citizen.name}\n"
                f"Ward/community: {self.citizen.ward}\nCategory: {self.category}\n"
                f"Description: {self.description}\nStatus: {self.status}")

    @classmethod
    def total_complaints(cls):
        return cls.total_created


# Python list data structure stores Complaint objects.
complaints = []
next_id = 1001


def ask_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def submit_complaint():
    global next_id
    print("\n--- SUBMIT COMPLAINT ---")
    citizen = Citizen(ask_required("Citizen ID: "),
                      ask_required("Citizen name: "),
                      ask_required("Ward/community: "))
    category = ask_required("Category (Roads/Water/Waste/Health/Other): ")
    description = ask_required("Describe the complaint: ")
    item = Complaint(next_id, citizen, category, description)
    complaints.append(item)
    next_id += 1
    print(f"Complaint submitted. Reference number: {item.complaint_id}")


def view_all():
    print("\n--- ALL COMPLAINTS ---")
    if not complaints:
        print("No complaints recorded.")
    for item in complaints:
        print(item.display())
        print("-" * 35)


def find_by_id():
    value = ask_required("Enter complaint reference number: ")
    if not value.isdigit():
        print("Reference number must contain digits only.")
        return None
    for item in complaints:
        if item.complaint_id == int(value):
            return item
    print("Complaint not found.")
    return None


def search_complaint():
    print("\n--- SEARCH COMPLAINT ---")
    item = find_by_id()
    if item:
        print(item.display())


def update_complaint():
    print("\n--- UPDATE STATUS ---")
    item = find_by_id()
    if not item:
        return
    print("1. Pending\n2. In Progress\n3. Resolved")
    choice = ask_required("Choose status: ")
    statuses = {"1": "Pending", "2": "In Progress", "3": "Resolved"}
    if choice not in statuses:
        print("Invalid option.")
        return
    item.update_status(statuses[choice])
    print("Status updated successfully.")


def show_summary():
    print("\n--- SUMMARY ---")
    print(f"Total complaints: {len(complaints)}")
    for status in ("Pending", "In Progress", "Resolved"):
        print(f"{status}: {sum(item.status == status for item in complaints)}")
    print(f"Complaint objects created: {Complaint.total_complaints()}")


def load_demo_data():
    citizen1 = Citizen("C001", "Demo Citizen", "Central")
    citizen2 = Citizen("C002", "Sample Citizen", "East")
    complaints.append(Complaint(1001, citizen1, "Roads", "Pothole on the main road."))
    item = Complaint(1002, citizen2, "Waste", "Waste collection has been missed.")
    item.update_status("In Progress")
    complaints.append(item)


def main():
    load_demo_data()
    while True:
        print("\n=== CITIZEN COMPLAINT SYSTEM ===")
        print("1. Submit complaint")
        print("2. View all complaints")
        print("3. Search complaint")
        print("4. Update complaint status")
        print("5. View summary")
        print("0. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            submit_complaint()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_complaint()
        elif choice == "4":
            update_complaint()
        elif choice == "5":
            show_summary()
        elif choice == "0":
            print("System closed.")
            break
        else:
            print("Invalid option. Choose 0-5.")


if __name__ == "__main__":
    main()
