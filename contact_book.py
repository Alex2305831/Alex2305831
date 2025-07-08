import json

contacts=[]

def add_contact():
    name=input("Onoma: ")
    phone=input("Thlefono: ")
    email=input("Email: ")
    contact={"Onoma":name,"Thlefono":phone,"Email":email}
    contacts.append(contact)
    print("H epathi prostethike.\n")
    
def show_contacts():
    if not contacts:
        print("Kamia epathi den exei katachorithei.\n")
        return
    for i,contact in enumerate(contacts,1):
        print(f"{i}.{contact["name"]}-{contact["phone"]}-{contact["email"]}")
    print()
    
def search_contact():
    keyword=input("Anazhthsh onomatos: ").lower()
    found=False
    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"{contact["name"]}-{contact["phone"]}-{contact["email"]}")
            found=True
    if not found:
        print("Den vrethike epathi me auto to onoma.\n")
        
def delete_contact():
    name=input("Onoma gia diagrafh: ")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("H epathi diagrafthke.\n")
            return
    print("Den vrethike epathi me auto to onoma.\n")
    
def save_contacts():
    with open("contacts.json","w")as file:
        json.dump(contacts,file)
    print("Oi epathes apothikeuthkan sto 'contacts.json'\n")
    
def load_contacts():
    global contacts
    try:
        with open("contacts.json","r")as file:
            contacts=json.load(file)
        print("Oi epathes fortothikan.\n")
    except FileNotFoundError:
        print("To arxeio den uparxei akomh.\n")
        
while True:
    print("1. Prosthiki epathis")
    print("2. Provoli olon")
    print("3. Anazhthsh epathis")
    print("4. Diagrafh epathis")
    print("5. Apothikeush")
    print("6. Fortosh")
    print("7. Exodos")
    
    choice=input("Epilogh: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        save_contacts()
    elif choice == "6":
        load_contacts()
    elif choice == "7":
        print("Exodos apo to programma.\n")
        break
    else:
        print("Mh egkurh epilogh dokimase ksana.\n")