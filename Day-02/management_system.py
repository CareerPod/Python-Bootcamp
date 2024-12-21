# Complaint Management System

complaints = []


def register_complaint():
    """"Function to register a new complaint"""
    name = input("Enter your name:")
    complaint =input("Enter your complaint: ")
    complaint_id = len(complaints) + 1
    complaints.append({"id":complaint_id,"name":name,"complaint":complaint, "status":"pending"})
    print("Complaint registerd successfully!")


def view_complaint():
    """"Function to view all complaints"""
    if  len(complaints) == 0:
        print("No complaints registered yet.")
    else:
        print("-"* 40)
        for comp in complaints:
            print(f"ID:{comp["id"]}, Name:{comp["name"]}, Complaint:{comp["complaint"]},status:{comp["status"]}")
        print("-"* 40)    


def update_complaint_status():
    """"Function to update Complaint"""
    complaint_id = int(input("Enter the Complaint ID to Update Complaint: "))
    for comp in complaints:
        if comp["id"] == complaint_id:
            print(f"Current status:{comp["status"]}")
            new_status = input("Enter the new status (Resolved/In Progress/Closed): ")
            if new_status in ["Resolved","In Progress","Closed"]:
                comp["status"] = new_status
                print("Complaint status updated successfully!")
            else:
                print("Invalid status. Try again.")
        else:
            print("Complaint ID not found")
                    


def main():
    """"Main menu for the Complaint Management System."""
    while True:
        print("--Complaint Management System--")
        print("1.Register a Complaint")
        print("2.View Complaints")
        print("3.Update Complaint Status")
        print("4.Exit")

        choice = input("Enter your Choice:")

        if choice == "1":
            register_complaint()
        elif choice == "2":
            view_complaint()
        elif choice == "3":
            update_complaint_status()            
        elif choice == "4":
            print("Exiting Complaint Management System. Goodbye!")
            break
        else:
            print("Invalid Choice. Please select a valid option")

main()