import csv

contacts = []
def save_contact():
    with open("final.csv", "w", newline="") as file:
        fields = ["Name","Phone","Email","Adress","City"]
        writer = csv.DictWriter(file, fieldnames = fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(contacts)
        


def view_contacts():
    print("Your address book: ")
    for contact in contacts:
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Adress: {contact['Adress']}")
        print(f"City: {contact['City']}")
        print("-"*30)

def add_contact():
        print("Add new contact:") 
        Name = input("Name: ")
        Phone = input("Phone: ")
        Email = input("Address:")
        City = input("City: ")
        if not Phone.isdigit():
            raise ValueError("Only enter digit values")
        if  Name.isdigit():
            raise ValueError("You cannot enter digit values for name")
        contact = {"Name": Name, "Phone": Phone, "Email": Email, "City": City}
        contacts.append(contact)
        save_contact()
        print("Contact saved successfully")
        print("-"*30)

def update_contact():
    name = input("Type in the contact's name:")
    for contact in contacts:
        if contact["Name"] == name:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Adress: {contact['Adress']}")
            print(f"City: {contact['City']}")
            print("-"*30)
            
            New_Name = input("Enter new name (Press enter to keep the old name): ").strip()
            New_Phone = input("Enter new phone (Press enter to keep the old phone): ").strip()
            New_Email = input("Enter new Email (Press enter to keep the old Email): ").strip()
            New_Adress = input("Enter new adress (Press enter to keep the old adress): ").strip()
            New_City = input("Enter new City (Press enter to keep the old City): ").strip()
            if not New_Phone.isdigit() and New_Phone != "":
                raise ValueError("Only enter digit values")
            else:
                if New_Name:
                    contact["Name"] = New_Name
                if New_Phone:
                    contact["Phone"] = New_Phone
                if New_Email:
                    contact["Email"] = New_Email
                if New_Adress:
                    contact["Adress"] = New_Adress
                if New_City:
                    contact["City"] = New_City
            save_contact()
            print("Contacts has been updated")
            return
    print("User not found")
   


def delete_contact():
    name = input("Type in the contact's name:")
    for contact in contacts:
        if contact["Name"] == name:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Adress: {contact['Adress']}")
            print(f"City: {contact['City']}")
            print("-"*30)
            print(f"Do you want to delete {contact['Name']} from your contact?")
            choice =input("yes/no [y/n]: ").upper()
            if choice == "y".upper():
                contacts.remove(contact)
                save_contact()
                print(f"{contact["Name"]}Contact has been deleted")
                return
            elif choice == "n".upper():
                print("Deletion cancelled")
                return
    print("User not found")   
    
def open_file():
    try:
        with open("final.csv", "r") as file:
            lines = csv.DictReader(file)
            for line in lines:
                contacts.append(line)    
    except FileNotFoundError:
        print("File does not exist")
        print("-"*30)

open_file()
while True:
    print("Address book menu:")
    print("1. Add contacts")
    print("2. View contacts")
    print("3. Update contacts")
    print("4. Delete contacts")
    print("5. Exit menu")
    try:
        user_input = int(input("Type the number you wish for the commands above:").strip())
        if user_input == 1:
            add_contact()
        elif user_input == 2:
            view_contacts()
        elif user_input == 3:
            update_contact()
        elif user_input == 4:
            delete_contact()
        elif user_input == 5:
            print("Exited menu")
            exit()
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"Error: {e}")
        
    
